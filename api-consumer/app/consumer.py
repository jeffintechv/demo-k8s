import os
import time
import requests
import json

# CONSUMER_DELAY = os.environ.get('CONSUMER_DELAY')
# CONSUMER_TOKEN = os.environ.get('CONSUMER_TOKEN')
#
# API_HOST = os.environ.get('FLASK_API_SERVICE_HOST')
# API_PORT = os.environ.get('FLASK_API_SERVICE_PORT')
#
# API_ENDPOINT = "http://%s:%s" % (API_HOST,API_PORT)

# to get error if env key is not present
CONSUMER_DELAY = os.environ['CONSUMER_DELAY']
CONSUMER_TOKEN = os.environ['CONSUMER_TOKEN']

# # not feasible to change env key based on service name
# API_HOST = os.environ['FLASK_API_SERVICE_HOST']
# API_PORT = os.environ['FLASK_API_SERVICE_PORT']

API_ENDPOINT = os.environ['API_ENDPOINT']

# infinite loop
while True:
    #Checking for pending load test request
    loadtest = requests.get("%s/consumer?token=%s"%(API_ENDPOINT,CONSUMER_TOKEN))
    if loadtest.status_code != 200:
        print("API failed with status_code",loadtest.status_code)
        break
    if loadtest.text == "ERROR":
        print("API TOKEN error")
        break

    loadtest_count = loadtest.json()

    if loadtest_count['count'] != 0:
        data = {'id': loadtest_count['id'], 'success': 0, 'failed': 0}
        for c in range(loadtest_count['count']):
            try:
                response = requests.get(API_ENDPOINT)
                if response.status_code == 200:
                    data['success'] += 1
                else:
                    data['failed'] += 1
            except:
                data['failed'] += 1
        print("Completed %d requests"%loadtest_count['count'])
        print(data)
        url = "%s/consumer/completed"%API_ENDPOINT
        headers = {'Content-type': 'application/json', 'Accept': 'text/plain'}
        r = requests.post(url, data=json.dumps(data), headers=headers)
        if r.text == "ERROR":
            print("consumer/completed API ERROR")
    else:
        print("No pending loadtest remaining. Waiting for the next..")

    print("############")
    time.sleep(int(CONSUMER_DELAY))
