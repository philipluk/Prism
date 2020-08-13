# -*- coding: utf-8 -*-
#
####################################################
#
# PRISM - Pipeline for animation and VFX projects
#
# www.prism-pipeline.com
#
# contact: contact@prism-pipeline.com
#
####################################################
#
#
# Copyright (C) 2016-2020 Richard Frangenberg
#
# Licensed under GNU GPL-3.0-or-later
#
# This file is part of Prism.
#
# Prism is free software: you can redistribute it and/or modify
# it under the terms of the GNU General Public License as published by
# the Free Software Foundation, either version 3 of the License, or
# (at your option) any later version.
#
# Prism is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
# GNU General Public License for more details.
#
# You should have received a copy of the GNU General Public License
# along with Prism.  If not, see <https://www.gnu.org/licenses/>.


import os
import time
import errno


class LockfileException(Exception):
    pass


class Lockfile(object):
    def __init__(self, core, fileName, timeout=10, delay=0.05):
        self.core = core
        self.isLocked = False
        self.lockPath = fileName + ".lock"
        self.fileName = fileName
        self.timeout = timeout
        self.delay = delay

    def acquire(self):
        startTime = time.time()
        while True:
            try:
                self.lockFile = os.open(self.lockPath, os.O_CREAT|os.O_EXCL|os.O_RDWR)
                self.isLocked = True
                break
            except OSError as e:
                if e.errno != errno.EEXIST:
                    raise
                elif time.time() - startTime >= self.timeout:
                    msg = "This config seems to be in use by another process:\n\n%s\n\nForcing to write to this file while another process is writing to it could result in data loss.\n\nDo you want to force writing to this file?" % self.fileName
                    result = self.core.popupQuestion(msg)
                    if result == "Yes":
                        os.remove(self.lockPath)
                    else:
                        raise LockfileException("Timeout occurred while writing to file: %s" % self.fileName)

                time.sleep(self.delay)

    def release(self):
        if self.isLocked:
            os.close(self.lockFile)
            os.remove(self.lockPath)
            self.isLocked = False

    def __enter__(self):
        if not self.isLocked:
            self.acquire()
        return self

    def __exit__(self, type, value, traceback):
        if self.isLocked:
            self.release()

    def __del__(self):
        self.release()