from parse_rest.connection import register

import json, httplib, urllib

'''
Increments radio_id field and returns success key. 
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
    return json.loads(connection.getresponse().read())


'''
Add a new suggested song to the requests list. 
Default values initialized as follows:
    played: False
    num_likes: 0
    num_dislikes: 0
All other values are passed in.
Returns success message.
'''
def add_song(radio_id, song_url):
    connection = httplib.HTTPSConnection('api.parse.com', 443)
    connection.connect()
    connection.request('POST', '/1/batch', json.dumps({
       "requests": [
         {
           "method": "POST",
           "path": "/1/classes/Songs",
           "body": {
             "url": unicode(song_url),
             "played": False,
             "num_likes": 0,
             "num_dislikes": 0,
             "radio_id": unicode(radio_id)
           }
         }
       ]
     }), {
       "X-Parse-Application-Id": "4bpR62fiuRaP4Fo3YYPL0dWzYr88dEci81nRNOOa",
       "X-Parse-REST-API-Key": "SDx9W7JT95o2Z9wK1qdZ5YvrOfxExKboTRaP9qKb",
       "Content-Type": "application/json"
     })
    return json.loads(connection.getresponse().read())


def like_song(song_id):
    connection = httplib.HTTPSConnection('api.parse.com', 443)
    connection.connect()
    connection.request('PUT', '/1/classes/Songs/%s' % song_id, json.dumps({
       "num_likes": {
         "__op": "Increment",
         "amount": 1
       }
     }), {
       "X-Parse-Application-Id": "4bpR62fiuRaP4Fo3YYPL0dWzYr88dEci81nRNOOa",
       "X-Parse-REST-API-Key": "SDx9W7JT95o2Z9wK1qdZ5YvrOfxExKboTRaP9qKb",
       "Content-Type": "application/json"
     })
    return json.loads(connection.getresponse().read())


def dislike_song(song_id):
    connection = httplib.HTTPSConnection('api.parse.com', 443)
    connection.connect()
    connection.request('PUT', '/1/classes/Songs/%s' % song_id, json.dumps({
       "num_dislikes": {
         "__op": "Increment",
         "amount": 1
       }
     }), {
       "X-Parse-Application-Id": "4bpR62fiuRaP4Fo3YYPL0dWzYr88dEci81nRNOOa",
       "X-Parse-REST-API-Key": "SDx9W7JT95o2Z9wK1qdZ5YvrOfxExKboTRaP9qKb",
       "Content-Type": "application/json"
     })
    return json.loads(connection.getresponse().read())


if __name__ == '__main__':
    app.run()