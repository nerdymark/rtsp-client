# -*- coding: utf-8 -*-

"""Console script for rtsp-client."""
import logging
import os
import sys
import rtsp
import time
import multiprocessing


rtspUser = os.environ['RTSP_USER']
rtspPass = os.environ['RTSP_PASS']
os.environ['DISPLAY'] = ":0"
timeout = 15

def showStream(url):
    with rtsp.Client(url) as client:
        client.preview()

cameraList = [
    'rtsp://'+rtspUser+':'+rtspPass+'@10.0.1.150:554/ch01/1',
    'rtsp://'+rtspUser+':'+rtspPass+'@10.0.1.150:554/ch02/1',
    'rtsp://'+rtspUser+':'+rtspPass+'@10.0.1.150:554/ch03/1',
    'rtsp://'+rtspUser+':'+rtspPass+'@10.0.1.150:554/ch04/1',
    'rtsp://'+rtspUser+':'+rtspPass+'@10.0.1.152:554/ch01/1',
    'rtsp://'+rtspUser+':'+rtspPass+'@10.0.1.152:554/ch02/1'
]

while True:
    for url in cameraList:
        p = multiprocessing.Process(target=showStream(url), name="Stream")
        p.start()
        p.join(timeout)
        if p.is_alive()
            print('function terminated')
            p.terminate()
            p.join()
            client.close()