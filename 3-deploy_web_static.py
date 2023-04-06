#!/usr/bin/python3
""" a module to pack and deploy a package to servers """
from fabric.operations import put, run
from datetime import datetime
from os.path import isfile
from fabric.api import put, env, run, local


env.hosts = ["35.231.213.145", "34.234.65.186"]

env.user = "ubuntu"


def do_pack():
    """ Generates a .tgz archive from the contents of the web_static folder """
    try:
        current_time = datetime.utcnow().strftime('%Y%m%d%H%M%S')
        local("mkdir -p versions")
        filename = "web_static_{}.tgz".format(current_time)
        local("tar -czvf versions/{} web_static".format(filename))
        return "versions/{}".format(filename)
    except:
        return None

def do_deploy(archive_path):
    """ deploys archive to web servers """
    if not isfile(archive_path):
        return False

    try:
        # Upload archive to the server
        put(archive_path, "/tmp/")

        # Create folder to extract files to
        file_name = archive_path.split("/")[-1]
        folder_name = file_name.split(".")[0]
        run("sudo mkdir -p /data/web_static/releases/{}".format(folder_name))

        # Extract archive contents into folder
        run("sudo tar -xzf /tmp/{} -C /data/web_static/releases/{}/"
            .format(file_name, folder_name))

        # Remove archive
        run("sudo rm /tmp/{}".format(file_name))

        # Move files into correct folder
        run("sudo mv /data/web_static/releases/{}/web_static/* "
            "/data/web_static/releases/{}/"
            .format(folder_name, folder_name))

        # Remove unneeded folder
        run("sudo rm -rf /data/web_static/releases/{}/web_static"
            .format(folder_name))

        # Remove old symbolic link
        run("sudo rm -rf /data/web_static/current")

        # Create new symbolic link
        run("sudo ln -s /data/web_static/releases/{}/ /data/web_static/current"
            .format(folder_name))

        return True
    except Exception:
        return False

def deploy():
    """ packs and deploys an archive to the web servers """
    archive_path = do_pack()
    if archive_path is None:
        return False
    return do_deploy(archive_path)
