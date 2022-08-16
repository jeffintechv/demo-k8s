from flask import Flask,render_template,request
import os
import requests

app = Flask(__name__)

API_HOST = os.environ['API_HOST']

@app.route('/')
def index():
    hit_count = requests.get("%s/hits" % API_HOST).json()
    total = sum([x['total_hits'] for x in hit_count ])
    return render_template('index.html',hit_count=hit_count,total=total)


@app.route('/loadtest')
def loadtest():
    loadtest = requests.get("%s/loadtest" % API_HOST).json()
    # print(loadtest)
    # result = sum([x['total_hits'] for x in hit_count ])
    return render_template('loadtest.html',loadtest=loadtest)

@app.route('/loadtest/add',methods=['POST'])
def loadtest_add():
    try:
        count = request.form['inputcount']
    except:
        count = 1
    message = requests.get("%s/loadtest?count=%s" % (API_HOST,count)).json()
    # result = sum([x['total_hits'] for x in hit_count ])
    return render_template('loadtest_add.html',message=message)

@app.route('/loadtest/clear')
def loadtest_clear():
    clear = requests.get("%s/clear" % API_HOST).json()
    # print(clear)
    # result = sum([x['total_hits'] for x in hit_count ])
    return render_template('clear.html',clear=clear)

# main driver function
if __name__ == '__main__':
    app.run(debug=True)
