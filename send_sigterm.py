import signal
import os
from subprocess import Popen
import time

p = Popen("python run_forever.py".split())
print('process:', p.pid, 'started!')
time.sleep(2)
print('Kill the process in send_sigterm.py')
os.kill(p.pid, signal.SIGTERM)
print('process cannot be gracefully shutdown~!')
