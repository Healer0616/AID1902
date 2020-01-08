

import os 
from time import sleep

pid = os.fork()

if pid < 0:
    print("Error")
elif pid == 0:
    sleep(1)
    print("Child PID",os.getpid())  #子进程
    print("Get parent pid:",os.getppid())
else:
    print("Parent PID:",os.getpid()) #父进程
    print("Get child PID:",pid)