#!/usr/bin/python3
"""
fabric file to compress all web_static folder
"""


from fabric.api import local, settings
from datetime import datetime as dt


def do_pack():
    """
    pack web_static files to tar
    """
    with settings(warn_only=True):
        res = local("mkdir -p versions")
        date = dt.now()
        pathname = "versions/web_static_"
        pathname += str(date.year)
        pathname += str(date.month)
        pathname += str(date.day)
        pathname += str(date.hour)
        pathname += str(date.minute)
        pathname += str(date.second)
        pathname += ".tgz"
        res2 = local("tar -cvzf " + pathname + " web_static")
        if res2.return_code == 0:
            return pathname
