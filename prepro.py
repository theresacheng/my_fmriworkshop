#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Dec 12 10:54:31 2017

@author: theresacheng
"""

import glob
import os
import pdb
import subprocess
import argparse
import datetime
import shutil


def prepro(basedir):
   print('Hello data in the path'+basedir) 
    
    
def main():
    basedir='/Users/theresacheng/Documents/learning/neuroimaging/fmriRepro_UNC2017/my_fmriworkshop/fmri_workshop/'
    prepro(basedir)
    

main()

