from parse_rest.connection import register

import json, httplib, urllib

'''
Increments radio_id field and returns unique key for url. 
'''
def create_radio():
    connection = httplib.HTTPSConnection('api.parse.com', 443)
    connection.connect()
    params = urllib.urlencode({"order":"-radio_id"})
    connection.request('GET', '/1/classes/Radios?%s' % params, '', {
       "X-Parse-Application-Id": "4bpR62fiuRaP4Fo3YYPL0dWzYr88dEci81nRNOOa",
       "X-Parse-REST-API-Key": "SDx9W7JT95o2Z9wK1qdZ5YvrOfxExKboTRaP9qKb"
     })
    results = json.loads(connection.getresponse().read())
    max_id = results[unicode('results')][0][unicode('radio_id')]
    
    connection.request('POST', '/1/batch', json.dumps({
       "requests": [
         {
           "method": "POST",
           "path": "/1/classes/Radios",
           "body": {
             "radio_id": (max_id + 1)
           }
         }
       ]
     }), {
       "X-Parse-Application-Id": "4bpR62fiuRaP4Fo3YYPL0dWzYr88dEci81nRNOOa",
       "X-Parse-REST-API-Key": "SDx9W7JT95o2Z9wK1qdZ5YvrOfxExKboTRaP9qKb",
       "Content-Type": "application/json"
     })
    radio_id = json.loads(connection.getresponse().read())[0][unicode('success')][unicode('objectId')]
    print 'radio id: %s' % radio_id



if __name__ == '__main__':
    app.run()