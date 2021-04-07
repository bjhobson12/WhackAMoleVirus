# File: main.py
# Created: Tue Apr 06 2021
#
# Copyright © 2021 Foxbat

import os, sys
from game import WhackAMole
from subprocess import Popen, PIPE

"""
This file was primarily written by Benjamin Hobson to bridge the c virus and pygame
"""
class PolymorphicAttack():

    def __init__(self):
        self.gcc_path = None
        

def run_weak_process(cmd, blocking=False):
    # This is a non-blocking call
    p = Popen(cmd, stdout=PIPE, stderr=PIPE)
    # This is a blocking call to wait for the process
    output, error = p.communicate()

    if p.returncode != 0: 
        raise Exception(error.decode('utf-8').strip())
    else:
        return output.decode('utf-8').strip()


if __name__ == '__main__':

    # Check python version at runtime https://stackoverflow.com/questions/9079036/how-do-i-detect-the-python-version-at-runtime
    if sys.version_info[0] < 3:
        raise Exception("Must be using Python 3")

    PolyAttack = PolymorphicAttack()

    # python docs https://docs.python.org/3/library/sys.html#sys.platform
    try:
        
        if sys.platform.startswith('darwin') or sys.platform.startswith('linux'):
            # Mac OS or Linux
            PolyAttack.gcc_path = run_weak_process(["which", "gcc"])
        elif sys.platform.startswith('win32'):
            # Windows (true)
            pass
        elif sys.platform.startswith('cygwin'):
            # Windows ('cygwin')
            pass
        else:
            raise Exception("The environment was not recognized")
    
    except Exception as e:
        print(e)
        print("Sorry we cannot run Whack a Mole on your OS")
        sys.exit()

    run_weak_process([PolyAttack.gcc_path, os.path.join(os.getcwd(), "main.c"), "-o", "main"])
    run_weak_process(['chmod', '+x', './main'])
    
    #Popen(['./main'], shell=True)
    Popen(['./main'], stderr=PIPE, stdout=PIPE, shell=True)
    # 

    ppp = WhackAMole()
    ppp.main()

    
