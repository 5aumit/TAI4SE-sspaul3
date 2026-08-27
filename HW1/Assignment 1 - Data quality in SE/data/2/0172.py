#!/usr/bin/python
# -*- coding: utf-8 -*-

import os
import sys
import paramiko
import commands


def ip_check():
    """
    Parses attributes for given hosts,
    then checks if hosts are up
    and then calls path_check function with working hosts.
    """
    hosts = []
    valid_hosts = []
    for item in sys.argv:
        if '@' in item:
            hosts.append(item)
    for i in hosts:
        host = i.split('@')[1].split(':')[0]
        command = os.system('ping -c 1 '+host+' > /dev/null')
        if command == 0:
            valid_hosts.append(i)
    if valid_hosts:
        path_check(valid_hosts)


def path_check(hosts):
    """
    Parses username, port, host and local and remote path,
    finds all local and remote files, using find_local_files and find_remote_files functions,
    and then opens ssh session using paramiko for each given host.
    """
    local_files = []
    local_path = ''
    for item in sys.argv:
        if '–pass' in item:
            secret = item.split('=')[1].strip("'")
            break
        else:
            secret = ''
    for item in sys.argv:
        if '/' in item and '@' not in item:
            local_path = item
        if '.' in item and '/' not in item:
            local_files.append(item)
    if local_path:
        local_files.append(find_local_files(local_path, 'f'))
    for i in hosts:
        user_port, host_remote_path = i.split('@')
        if ':' in i:
            host, remote_path = host_remote_path.split(':')
        else:
            host = host_remote_path
            remote_path = ''
        for separator in ',.:':
            if separator in user_port:
                user, port = user_port.split(separator)
                break
            else:
                user = user_port
                port = 0
        ssh = open_sshclient(host, user, port, secret)
        if not remote_path:
            remote_path = local_path
        ssh.exec_command('mkdir -p '+remote_path)
        remote_files = find_remote_files(remote_path, 'f', ssh)
        ssh.close()
    copy_file(hosts)


def open_sshclient(host, user, port, secret):
    """
    Opens ssh session using paramiko.
    """
    ssh_client = paramiko.SSHClient()
    ssh_client.set_missing_host_key_policy(paramiko.AutoAddPolicy())
    ssh_client.load_system_host_keys()
    if secret and port:
        ssh_client.connect(hostname=host, username=user, password=secret, port=port)
    elif secret and port==0:
        ssh_client.connect(hostname=host, username=user, password=secret)
    elif not secret and port:
        ssh_client.connect(hostname=host, username=user, port=port)
    else:
        ssh_client.connect(hostname=host, username=user)
    return ssh_client


def copy_file(hosts):
    """
    Makes all needed operations according to given attributes with rsync.
    """
    arguments = []
    for item in sys.argv[1:]:
        if '@' not in item and '–pass' not in item:
            arguments.append(item)
    for item in hosts:
        # plz use .format for test strings concatenation
        os.system('rsync '+' '.join(arguments)+' '+item)


def find_remote_files(remote_path, type, ssh):
    """
    Finds all files or directories on remote machine, according to given attributes.
    """
    (ssh_in, ssh_out, ssh_err) = ssh.exec_command("find %s -name \"*\" -type %s" % (remote_path, type))
    files = []
    for file in ssh_out.readlines():
        files.append(file.rstrip())
    return files


def find_local_files(local_path, type):
    """
    Finds all files or directories on local machine, according to given attributes.
    """
    local_out = commands.getoutput("find %s -name \"*\" -type %s" % (local_path, type))
    files = []
    for file in local_out.split("\n"):
        files.append(file)
    return files

ip_check()

