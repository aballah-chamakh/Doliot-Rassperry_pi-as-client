import requests
import json
import websocket

data = {'email':'abdallah@gmail.com','password':'abdallahchamakh'}
headers = {'Content-Type':'application/json'}
         
res = requests.post('http://192.168.1.28/api/token/',data=json.dumps(data),headers=headers)
token = res.json()['token']
print(token)
headers = {'Content-Type':'application/json'}

def on_message(ws, message):
    msg = json.loads(message)
    print(msg['state'])

def on_error(ws, error):
    print(error)

def on_close(ws):
    print("### closed ###")

def on_open(ws):
    print('connect successfully')

ws = websocket.WebSocketApp("ws://192.168.1.28/ws/bulb/1/?token="+token,
                              on_message = on_message,
                              on_error = on_error,
                              on_close = on_close)
ws.on_open = on_open
ws.run_forever()
