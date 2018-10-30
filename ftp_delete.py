#!/usr/bin/env python
# coding=utf8
# -*- coding: utf-8 -*-

import os
import sys
import ftplib


ftp = ftplib.FTP("192.168.1.1")
ftp.encoding='utf-8'
ftp.login("id", "password")

# file delete 예시
ftp.cwd("/sda1/video/drama")
filename = sys.argv[1]
ftp.delete(filename)

ftp.quit()
