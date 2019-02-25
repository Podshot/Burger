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
from urllib.request import urlopen
import json


class VersionNotFoundException(Exception):
    pass


class Website(object):
    def __init__(self, username, password, version=999999):
        self.username = username
        self.password = password
        self.version = version

    @staticmethod
    def client_jar(path: str = None, reporthook=None, version: str = "latest"):
        versions_manifest = urlopen("https://launchermeta.mojang.com/mc/game/version_manifest.json", timeout=10)
        manifest = json.loads(versions_manifest.read())
        version_url = None

        if version == "latest":
            version = manifest["latest"]["release"]

        for m_version in manifest["versions"]:
            if m_version["id"] == version:
                version_url = m_version["url"]
                break
        if not version_url:
            raise VersionNotFoundException(f"Version \"{version}\" doesn't exist in the Minecraft version manifest")
        specific_manifest = urlopen(version_url, timeout=10)
        manifest = json.loads(specific_manifest.read())

        jar_url = manifest["downloads"]["client"]["url"]
        jar_response = urlopen(jar_url, timeout=40)

        if not path:
            path = f"{version}.jar"

        with open(path, "wb") as fp:
            fp.write(jar_response.read())

        return path


if __name__ == "__main__":
    print(Website.client_jar(version="1.13.2"))
    print(Website.client_jar(version="1.14.2"))