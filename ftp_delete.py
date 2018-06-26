#!/usr/bin/env python
# coding=utf8
# -*- coding: utf-8 -*-

import os
import ftplib


ftp = ftplib.FTP("192.168.1.1")
ftp.encoding='utf-8'
ftp.login("id", "passwd")

# file delete 예시
ftp.cwd("/sda1/video/entertain")
filename = u""
ftp.delete(filename)

ftp.quit()
