#!/usr/bin/python3
"""
Script that generates a .tgz archive from the contents of
the web_static folder of your AirBnB Clone repo, using the function do_pack
"""
from fabric.api import local
from datetime import datetime


def do_pack():
    local('mkdir -p versions')
    time = datetime.now().strftime('%Y%m%d%H%M%S')
    name_path = 'versions/web_static_' + time
    file = local('sudo tar -czvf {}.tgz web_static'.format(name_path))
    if file.failed:
        return None
    else:
        return file
