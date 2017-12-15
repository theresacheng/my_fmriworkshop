C#!/usr/bin/env python3
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
   for item in glob.glob(os.path.join(basedir,'sub-*','func','sub-*bart*.nii.gz')):
       input= item
       output_path=item.strip('.nii.gz')
       output=output_path+('_brain')
       os.system("/usr/local/fsl/bin/bet %s %s -F" %(input, output))
       # pdb.set_trace() #useful for debugging within a loop; stops BEFORE re-looping, q to exit
    
def main():
    basedir='/Users/theresacheng/Documents/learning/neuroimaging/fmriRepro_UNC2017/data/ds000030_R1.0.5/'
    prepro(basedir)
    
main()

input=glob.glob('/Users/theresacheng/Documents/learning/neuroimaging/fmriRepro_UNC2017/data/ds000030_R1.0.5/sub-*/func/sub-*.nii.gz')
x=input[0]
#print('my path is '+x)
#y=x.split('/')
#print(y)
#sub=y[9]
#print(sub)

# prettier version of getting subjects
sub=input[1].split('/')[9]
print(sub)

subtask=input[1].split('/')[11].split('.')[0]
print(subtask)

output= subtask+'_brain'
print(output)

os.system('bet %s %s -F' %(x, output))

basedir='/Users/theresacheng/Documents/learning/neuroimaging/fmriRepro_UNC2017/data/ds000030_R1.0.5/'
path=os.path.join(basedir,'sub-*','func','sub-*bart*.nii.gz')
print(path)
input=(glob.glob(path))
len(input[1:5])
print(input)
