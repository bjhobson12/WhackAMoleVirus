# File: utility.py
# Created: Tue Apr 06 2021
#
# Copyright © 2021 Foxbat

import math

def easeInBounce(x):
    return (1-x)*math.sin(9*x)/1.5+1

def easeOutBound(x):
    return -x*math.sin(9*x - 1)/1.5+1 if x < 0.7624 else -5*(x-.87)+0.67

