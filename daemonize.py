#!/usr/bin/env python
# coding=utf8

import time
import daemon
from daemon.pidfile import PIDLockFile
import logging
from logging import handlers

logger = logging.getLogger("mylogger")
logger.setLevel(logging.INFO)

file_handler = handlers.RotatingFileHandler(
    "log/daemon.log",
    maxBytes= (1024 * 1024 * 512),
    backupCount=3
)
logger.addHandler(file_handler)


pidLockfile = PIDLockFile('.pid')
if pidLockfile.is_locked():
    print("running already (pid: %d)" % pidLockfile.read_pid())
    exit(1) 

context = daemon.DaemonContext(pidfile=pidLockfile)
logfile_fileno = file_handler.stream.fileno()
context.files_preserve = [logfile_fileno]


def main():
    while True:
        time.sleep(0.5)

with context:
   main_program()
