# -*- coding: utf-8 -*-

"""Console script for rtsp-client."""
import logging
import os
import sys
import rtsp
import time as t

rtspUser = os.environ['RTSP_USER']
rtspPass = os.environ['RTSP_PASS']

def previewLength(max_seconds, *, interval=1):
    interval = int(interval)
    start_time = time.time()
    end_time = start_time + max_seconds
    yield 0
    while time.time() < end_time:
        if interval > 0:
            next_time = start_time
            while next_time < time.time():
                next_time += interval
            time.sleep(int(round(next_time - time.time())))
        yield int(round(time.time() - start_time))
        if int(round(time.time() + interval)) > int(round(end_time)): 
            return


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
        for sec in previewLength(15):
            with rtsp.Client(url) as client:
                previewEnd = t.time() + previewLength
                print('Trying ' + url + ' from ' + str(t.time()) + ' until ' + str(previewEnd))
                client.preview()
            client.close()