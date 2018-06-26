#!/usr/bin/env python
# coding=utf8
# -*- coding: utf-8 -*-

import os
import sys
import ftplib

os.chdir("/home/tata8661/Work")
filename = sys.argv[1]

myfile = open(filename, 'rb')

ftp = ftplib.FTP("192.168.1.1")
ftp.encoding='utf-8'
ftp.login("id", "passwd")

# file upload 예시
ftp.cwd("/sda1/video/entertain")
ftp.storbinary("STOR %s" % filename, myfile)

ftp.quit()
