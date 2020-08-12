#!/usr/bin/env python3

 # import more methods
import shutil
import os

 # set working directory
os.chdir('/home/student/mycode/')

 # move from src to dest, can specify a new file name
shutil.move('raynor.obj', 'ceph_storage/')

 # take user imput
xname = input('What is the new name for kerrigan.obj? ')

 # move from src to dest and renamed kerrigan
shutil.move('ceph_storage/kerrigan.obj', 'ceph_storage/' + xname)

