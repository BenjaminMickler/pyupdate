import os
import sys
import time

def spawn_daemon(func):
    try: 
        pid = os.fork() 
        if pid > 0:
            return
    except OSError as e:
        print(sys.stderr, "fork #1 failed: %d (%s)" % (e.errno, e.strerror))
        sys.exit(1)
    os.setsid()
    try: 
        pid = os.fork()
        if pid > 0:
            sys.exit(0) 
    except OSError as e: 
        print(sys.stderr, "fork #2 failed: %d (%s)" % (e.errno, e.strerror))
        sys.exit(1)
    func()