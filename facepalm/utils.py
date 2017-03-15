#!/usr/bin/env python

'''
utils.py: part of oscookie package

'''

import collections
import os
import re
import requests

import shutil
import simplejson
import oscookie.__init__ as hello
from facepalm.logman import bot
import sys

from subprocess import (
    Popen,
    PIPE,
    STDOUT
)

import subprocess

import tempfile
import zipfile


######################################################################################
# Local commands and requests
######################################################################################


def get_installdir():
    '''get_installdir returns the installation directory of the application
    '''
    return os.path.abspath(os.path.dirname(hello.__file__))


def check_installed(software):
    '''check_installed will check if a software is installed
    :param software: the name of the software
    '''
    testing_command = ["which", software]
    return run_command(testing_command)


def run_command(command):
    '''run_command will run a command (a list)
    :param command: the command to run
    '''
    if not isinstance(command,list):
        command = [command]
    output = Popen(command,stderr=STDOUT,stdout=PIPE)
    t = output.communicate()[0],output.returncode
    result = {'message':t[0],
              'return_code':t[1]}
    return result



############################################################################
## FILE OPERATIONS #########################################################
############################################################################

def write_file(filename,content,mode="w"):
    '''write_file will open a file, "filename" and write content, "content"
    and properly close the file
    '''
    with open(filename,mode) as filey:
        filey.writelines(content)
    return filename


def write_json(json_obj,filename,mode="w",print_pretty=True):
    '''write_json will (optionally,pretty print) a json object to file
    :param json_obj: the dict to print to json
    :param filename: the output file to write to
    :param pretty_print: if True, will use nicer formatting   
    '''
    with open(filename,mode) as filey:
        if print_pretty == True:
            filey.writelines(simplejson.dumps(json_obj, indent=4, separators=(',', ': ')))
        else:
            filey.writelines(simplejson.dumps(json_obj))
    return filename


def read_file(filename,mode="r"):
    '''write_file will open a file, "filename" and write content, "content"
    and properly close the file
    '''
    with open(filename,mode) as filey:
        content = filey.readlines()
    return content
