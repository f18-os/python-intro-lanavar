#!/usr/bin/env python3
#Importing necessary
import sys, re, os, subprocess, time

# Initial prompt
function = input(">>$ ")
done = False
class ExitClause(Exception):
    pass

# Loop for the prompt
while(not done):
    try:
        #handling exit typed in
        if function == "exit()":
            raise ExitClause("Exiting bye")
        pid = os.getpid()        
        print("Function entered is " + function)
        os.write(1, ("About to fork (pid:%d)\n" % pid).encode())
        rc = os.fork()
        
        if rc < 0:
            os.write(2, ("fork failed, returning %d\n" % rc).encode())
            sys.exit(1)
        elif rc == 0:
            os.write(1, ("I am child. My pid==%d. Parent's pid=%d. Function is %s\n" % (os.getpid(), pid, function)).encode())
            args = function.split()
            # handle event that exit is entered
            for dir in re.split(":", os.environ['PATH']):
                program = "%s/%s" % (dir, args[0])
                os.write(1, ("Child:  ...trying to exec %s\n" % program).encode())
                try:
                    os.execve(program, args, os.environ)
                except FileNotFoundError:
                    pass

            os.write(2, ("Child:  Could not exec %s\n" % args[0]).encode())
            sys.exit(1)
        else:
            os.write(1, ("Parent: my pid=%d. Child's pid=%d\n" % (pid, rc)).encode())
            childPidcode = os.wait()
            os.write(1, ("Parent: Child %d terminated with exit code %d\n" % (childPidcode)).encode())
            function = input(">>$ ")
    except EOFError:
        print("")
        print("Done")
        break

    except ExitClause:
        print("Exiting ... Bye")
        break

