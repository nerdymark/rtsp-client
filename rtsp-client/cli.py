# -*- coding: utf-8 -*-

"""Console script for rtsp-client."""
import logging
import os
import sys
import rtsp
import time
from interruptingcow import timeout


rtspUser = os.environ['RTSP_USER']
rtspPass = os.environ['RTSP_PASS']

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
        try:
            with rtsp.Client(url) as client:
                with timeout(15, exception=RuntimeError):
                    client.preview()
        except RuntimeError:
            client.close()
            pass