#!/usr/bin/env python3
#Importing necessary
import sys, re, os, subprocess



# Loop for the prompt
while(True):
    try:
        pid = os.getpid()
        function = input(">>$ ")
        print("Function entered is " + function)
        os.write(1, ("About to fork (pid:%d)\n" % pid).encode())
        rc = os.fork()
        
        if rc < 0:
            os.write(2, ("fork failed, returning %d\n" % rc).encode())
            sys.exit(1)
        elif rc == 0:
            os.write(1, ("I am child. My pid==%d. Parent's pid=%d. Function is %s\n" % (os.getpid(), pid, function)).encode())
        else:
            os.write(1, ("I am parent. My pid=%d. Child's pid=%d. Function is %s\n" % (pid, rc, function)).encode())
    except EOFError:
        print("")
        print("Done")
        break

