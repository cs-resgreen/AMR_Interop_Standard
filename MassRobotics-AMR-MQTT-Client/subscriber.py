#!/usr/bin/env python
# -*- coding: utf-8 -*-

import paho.mqtt.client as mqtt
import json
from jsonschema import validate, ValidationError

host = "localhost"
port = 1883
keepalive = 60

with open('../AMR_Interop_Standard.json') as file_obj:
    json_schema = json.load(file_obj)

def on_message(mqttc, obj, msg):
    print(msg.topic)
    print(msg.topic[len(msg.topic) - 12:len(msg.topic)])
    json_dict = json.loads(msg.payload)
    try:
        validate(json_dict, json_schema)
        print(json_dict)
        if msg.topic == "identityReport":
            print("new client device online: " + str(json_dict["uuid"]))
            mqtt_client.subscribe(str(json_dict["uuid"]) + "/#")
        elif msg.topic[len(msg.topic) - 12:len(msg.topic)] == "statusReport":
            print("UUID: " + str(json_dict["uuid"]))
            print("Battery: " + str(json_dict["batteryPercentage"]))
    except ValidationError as e:
        print(e.message)

mqtt_client = mqtt.Client()
mqtt_client.on_message = on_message
mqtt_client.connect(host, port, keepalive)

mqtt_client.subscribe("identityReport")
while True:
    mqtt_client.loop()
