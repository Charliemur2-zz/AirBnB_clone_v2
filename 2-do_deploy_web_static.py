#!/usr/bin/python3
"""
script (based on the file 1-pack_web_static.py) that distributes an
archive to your web servers, using the function do_deploy
"""
from fabric.api import *
from datetime import datetime
import os
env.hosts = ['35.237.123.97', '35.231.114.243']


def do_pack():
    """
    Function to create a dist folder compressed
    Returns: False if the file at the path archive_path doesn’t exist
    """
    local('mkdir -p versions')
    time = datetime.now().strftime('%Y%m%d%H%M%S')
    name_path = 'versions/web_static_' + time
    file = local('sudo tar -czvf {}.tgz web_static'.format(name_path))
    if file.failed:
        return None
    else:
        return file


def do_deploy(archive_path):
    """
    Function to deploy in 2 web servers
    Args: archive_path
    Returns False if the file at the path archive_path doesn’t exist
    """
    if os.path.exists(archive_path):
        name = archive_path.split('/')[-1]
        data_path = '/data/web_static/releases/' + name[:-4]
        tmp_path = '/tmp/' + name
        put(archive_path, '/tmp/')
        run('mkdir -p {}'.format(data_path))
        run('tar -xzf {} -C {}'.format(tmp_path, data_path))
        run('rm {}'.format(tmp_path))
        run('mv {}/web_static/* {}'.format(data_path, data_path))
        run('rm -rf {}/web_static'.format(data_path))
        run('rm -rf /data/web_static/current')
        run('ln -s {} /data/web_static/current'.format(data_path))
        print('New version deployed!')
        return True
    else:
        return False
