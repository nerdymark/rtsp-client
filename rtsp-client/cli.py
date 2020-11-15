# -*- coding: utf-8 -*-

"""Console script for rtsp-client."""
import logging
import os
import sys
import rtsp
import time as t

rtspUser = os.environ['RTSP_USER']
rtspPass = os.environ['RTSP_PASS']
previewLength = 15

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
        with rtsp.Client(url) as client:
            previewEnd = t.time() + previewLength
            while True:
                try:
                    print('Trying ' + url + ' from ' + str(t.time()) + ' until ' + str(previewEnd))
                    client.preview()
                except Exception as e:
                    print(e)
                    pass
                if t.time() < previewEnd:
                    break
                    client.close()