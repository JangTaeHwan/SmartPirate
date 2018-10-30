#!/usr/bin/env python
# coding=utf8
# -*- coding: utf-8 -*-

import os
import ftplib

ftp = ftplib.FTP("192.168.1.1")
ftp.encoding='utf-8'
ftp.login("id", "password")

def list_files(dir):
    print(dir)
    ftp.cwd(dir)
    files = ftp.nlst()
    for file in files:
        print(os.path.basename(file))
    print()

# file list 예시
list_files("/sda1/video/drama")
list_files("/sda1/video/movie")
list_files("/sda1/video/entertain")

ftp.quit()
