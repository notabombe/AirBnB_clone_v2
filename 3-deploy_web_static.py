#!/usr/bin/python3
from fabric.api import local, run, put, env
import datetime
import os.path
"""creates and distributes an archive to the web servers
"""

env.hosts = ['66.70.184.235', '34.229.113.91']


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


def do_deploy(archive_path):
    if not os.path.exists(archive_path):
        return False
    ws_rs = "web_static/releases"
    ws = "web_static"
    try:
        filename = archive_path.split('/')[1]
        put(f"versions/{filename}", f"/tmp/{filename}")
        run(f"mkdir -p /data/{ws_rs}/{filename[:-4]}")
        run(f"tar -xzf /tmp/{filename} -C /data/{ws_rs}/{filename[:-4]}/")
        run(f"rm /tmp/{filename}")
        run(f"mv /data/{ws_rs}/{filename[:-4]}/{ws}/* /data/{ws_rs}/{filename[:-4]}")
        run(f"rm -rf /data/{ws_rs}/{filename[:-4]}/{ws}")
        run("rm -rf /data/web_static/current")
        run(f"ln -s /data/{ws_rs}/{filename[:-4]} /data/{ws}/current")
    except:
        return False


def deploy():
    archive_path = do_pack()
    return False if archive_path is None else do_deploy(archive_path)
