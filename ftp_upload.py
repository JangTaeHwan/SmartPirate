#!/usr/bin/env python
# coding=utf8
# -*- coding: utf-8 -*-

import os
import sys
import ftplib

os.chdir("/home/tata8661/Work/SmartPirate")
filename = sys.argv[1]


ftp = ftplib.FTP("192.168.1.1")
ftp.encoding='utf-8'
ftp.login("id", "passwd")

#ftp.cwd("/sda1/video/movie")
ftp.cwd("/sda1/video/drama")

def uploadThis(path):
    files = os.listdir(path)
    if os.path.isdir(path):
        ftp.mkd(path)
        os.chdir(path)
        ftp.cwd(path)

    for f in files:
        fh = open(f, 'rb')
        ftp.storbinary('STOR %s' % f, fh)
        fh.close()
        print(f)


if os.path.isdir(filename):
    uploadThis(filename)
else:
    myfile = open(filename, 'rb')
    ftp.storbinary("STOR %s" % filename, myfile)


ftp.quit()
