import os
import sys

def run(program, *args):
    pid = os.fork()
    if not pid:
        os.execvp(program, (program,) +  args)
    return os.wait()[0]

for e in range(5):
    run("python", "hello.py")

print "goodbye"