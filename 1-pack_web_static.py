#!/usr/bin/env python3
""" A module to package web_static files """

import os
from datetime import datetime
from fabric.api import local


def do_pack():
    """ Generates a .tgz archive from the contents of the web_static folder """

    try:
        local("mkdir -p versions")
        now = datetime.now()
        filename = "web_static_" + now.strftime("%Y%m%d%H%M%S") + ".tgz"
        path = "versions/" + filename
        local("tar -cvzf {} web_static".format(path))
        return path
    except Exception as e:
        print("An error occurred while creating the archive: {}".format(e))
        return None
