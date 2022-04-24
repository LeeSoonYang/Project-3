# -*- coding: utf-8 -*-
"""
Created on Mon Oct 12 18:13:24 2020

@author: keroy
"""
import matplotlib.pyplot as plt
import math
import nympy as np

try:
    total = 0
    student = 0
    marks = open('CourseMark.txt','r')
    for i in marks:
        total += int(i)
        student += 1
    avg = total/student
    std = np.std()
except:
    pass