import RPi.GPIO as GPIO
import json
import requests
import time

GPIO.setmode(GPIO.BCM)
GPIO.setup(21,GPIO.OUT)
bulb_id = 12
# Doliot api endpoints
base_end_point = 'http://192.168.1.10/api/'
token_end_point = base_end_point+'token'
end_point_thing = base_end_point+'/thing/'+str(bulb_id)+'/'
# Authentication
credential = {'email':'example@gmail.com',
               'password':'exampleexample'}
headers = {'Content-Type':'application/json'}
r1 = requests.post(token_end_point,data=json.dumps(credential),headers=headers)
print(r1.json())
token = r1.json()['access']
headers = {'Content-Type':'application/json',
           'Authorization':'Bearer '+token}
# infinite loop to get the current state of the bulb and sync it with the gpio pin state which in our case 21 pin
while True :
    r2 = requests.get(end_point_thing,headers=headers_token)
    state = r2.json()['state']
    if state :
        GPIO.output(21,GPIO.HIGH)
        print('bulb on')
    else :
        GPIO.output(21,GPIO.LOW)
        print('bulb off')
    time.sleep(0.3)
