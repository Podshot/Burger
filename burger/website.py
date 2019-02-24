#!/usr/bin/env python
# -*- coding: utf8 -*-
"""
Copyright (c) 2011 Tyler Kenendy <tk@tkte.ch>

Permission is hereby granted, free of charge, to any person obtaining a copy
of this software and associated documentation files (the "Software"), to deal
in the Software without restriction, including without limitation the rights
to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
copies of the Software, and to permit persons to whom the Software is
furnished to do so, subject to the following conditions:

The above copyright notice and this permission notice shall be included in
all copies or substantial portions of the Software.

THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN
THE SOFTWARE.
"""
import urllib.request as urllib


class Website(object):
    def __init__(self, username, password, version=999999):
        self.username = username
        self.password = password
        self.version = version

    @staticmethod
    def client_jar(path=None, reporthook=None, version="1.9"):
        #url = "http://s3.amazonaws.com/Minecraft.Download/versions/%s/%s.jar" % (version, version)
        # Note: https://launchermeta.mojang.com/mc/game/version_manifest.json
        # Note: https://launchermeta.mojang.com/v1/packages/26ec75fc9a8b990fa976100a211475d18bd97de0/1.13.2.json
        url = "https://launcher.mojang.com/v1/objects/30bfe37a8db404db11c7edf02cb5165817afb4d9/client.jar"
        #url = "http://s3.amazonaws.com/MinecraftDownload/minecraft.jar" # 1.5.2
        r = urllib.urlretrieve(url, filename=path, reporthook=reporthook)
        return r[0]
