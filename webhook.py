from flask import Flask, request
import logging
import requests
import urllib
import pycurl


app = Flask(__name__)
logging.basicConfig(filename='record.log', level=logging.DEBUG)
@app.route('/')
def hello():
    return "Hello World!"




@app.route('/join-accept', methods=['POST'])
def webhook3():
    print("hello")
    app.logger.info('Info level log')
    if(request.method == 'POST'):
        print(request.json)
    return 'success', 200

@app.route('/uplinks', methods=['POST'])
def webhook1():
    if(request.method == 'POST'):
        print(request.json)
        url = 'https://lorala.nam1.cloud.thethings.industries/api/v3/as/applications/my-application/webhooks/test-webhook/devices/my-device/down/push'
        headers = {'Authorization': "Bearer NNSXS.QYNVIPCESUULZ73YK2CGM2KRBGSTIGVJXCZMRSY.CVA4L4P47W7PPYUTACCDOTR5DGKN3QGJMN2HFJ6AYNOPILY7KI4A",
       'Content-Type': "application/json",
       'User-Agent': "my-integration/my-integration-version"}
        data = {"downlinks":[{
      "frm_payload":"vu8=",
      "f_port":2,
      "priority":"NORMAL"
    }]
  }
        res = requests.post(url, json=data, headers=headers)
        print (res.status_code)
        print (res.raise_for_status())
        return 'success', 200

#for downlink    
@app.route('/', methods=['POST'])
def webhook2():
    if(request.method == 'POST'):
        print(request.json)
        return 'success', 200

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=80)
