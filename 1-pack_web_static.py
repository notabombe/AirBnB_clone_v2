#!/usr/bin/python3
from fabric.api import local
import datetime
"""generates a .tgz archive from the contents of the web_static folder
"""


def do_pack():
    date = datetime.datetime.now().strftime("%Y%m%d%H%M%S")
    file = f"versions/web_static_{date}.tgz"
    print(f"Packing web_static to {file}")
    try:
        local("mkdir -p versions")
        local(f"tar -cvzf {file} web_static")
        return f"{file}"
    except:
        return None
