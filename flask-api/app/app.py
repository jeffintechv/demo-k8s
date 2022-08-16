from flask import Flask, request, jsonify
from flask_mysqldb import MySQL
import MySQLdb.cursors

import socket
import os

app = Flask(__name__)

# app.config['MYSQL_HOST'] = os.environ.get('DB_HOST')
# app.config['MYSQL_USER'] = os.environ.get('DB_USER')
# app.config['MYSQL_PASSWORD'] = os.environ.get('DB_PASSWORD')
# app.config['MYSQL_DB'] = os.environ.get('DB_NAME')
#
# CONSUMER_TOKEN = os.environ.get('CONSUMER_TOKEN')


# to get error if env key is not present
app.config['MYSQL_HOST'] = os.environ['DB_HOST']
app.config['MYSQL_USER'] = os.environ['DB_USER']
app.config['MYSQL_PASSWORD'] = os.environ['DB_PASSWORD']
app.config['MYSQL_DB'] = os.environ['DB_NAME']

CONSUMER_TOKEN = os.environ['CONSUMER_TOKEN']

mysql = MySQL(app)



@app.route('/')
def index():
    hostname = socket.gethostname()
    cursor = mysql.connection.cursor()
    sql = "INSERT INTO api_hits (hostname) VALUES ('%s')" % hostname
    cursor.execute(sql)
    mysql.connection.commit()
    return "request served from {}".format(socket.gethostname())

@app.route('/clear')
def clear():
    try:
        cursor = mysql.connection.cursor()
        sql = "truncate table api_hits"
        cursor.execute(sql)
        sql = "truncate table loadtest"
        cursor.execute(sql)
        mysql.connection.commit()
    except:
        return jsonify({"status":"error"})

    return jsonify({"status":"success","message":"tables cleared"})

@app.route('/loadtest')
def loadtest():
    try:
        count = int(request.args.get('count',0))
    except:
        # return "ERROR : provide integer as count parameter"
        return jsonify({"status":"error","message":"provide interger value"})

    if count == 0:
        cursor = mysql.connection.cursor(MySQLdb.cursors.DictCursor)
        cursor.execute("SELECT * from loadtest;")
        loadtest = list(cursor.fetchall())
        return jsonify(loadtest)
    else:
        cursor = mysql.connection.cursor()
        sql = "INSERT INTO loadtest (count) VALUES ('%d')" % count
        cursor.execute(sql)
        mysql.connection.commit()
        # return "added new load test entry with count %d" % count
        return jsonify({"status":"success","message":"new loadtest added","count":count})


@app.route('/consumer')
def consumer():
    token = request.args.get('token','')
    if token != CONSUMER_TOKEN:
        print("TOKEN Mismatch")
        return "ERROR"
    cursor = mysql.connection.cursor(MySQLdb.cursors.DictCursor)
    cursor.execute("SELECT id,count FROM loadtest where status='pending'")
    pending = cursor.fetchone()
    # print(pending)
    if pending:
        cursor.execute("update loadtest set start_ts=NOW(),status='processing' where id='%d'" % pending['id'])
        mysql.connection.commit()
        return pending
    else:
        return {"count":0}

@app.route('/consumer/completed',methods=['POST'])
def consumer_completed():
    data = request.json
    # print(data)
    cursor = mysql.connection.cursor(MySQLdb.cursors.DictCursor)
    try:
        cursor.execute("update loadtest set completed_ts=NOW(),status='completed',success='%d',failed='%d' where id='%d'" % (data['success'],data['failed'],data['id']))
        mysql.connection.commit()
    except:
        print("ERRORR")
        return "ERROR"

    return "OK"

@app.route('/hits')
def hits():
    cursor = mysql.connection.cursor(MySQLdb.cursors.DictCursor)
    cursor.execute('SELECT hostname,COUNT(hostname) AS total_hits from api_hits GROUP BY hostname ORDER BY total_hits DESC;')
    hits = list(cursor.fetchall())

    return jsonify(hits)

    # out = "<h3>Total requests servered by each back end node</h3><p>"
    # for i in hits:
    #     out += "%s <b>( %d )</b><br>" %(i['hostname'],i['total_hits'])
    # out += "</p>"
    #
    # return out

# main driver function
if __name__ == '__main__':
    app.run(debug=True)
