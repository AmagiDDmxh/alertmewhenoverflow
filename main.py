import psutil
import time
import subprocess
import os
from osax import *
from beepy import beep

AMA_TEXT = 'Hey, u should clean my memory now. Can\'t take it anymore'
OK_TEXT = 'Im fine, take care of youself, love ya'
sa = OSAX()

threshold = 90

i = 0
try:
  while True:
    now = time.asctime(time.localtime(time.time()))
    time.sleep(1)
    usage = psutil.virtual_memory().percent
    if usage >= threshold:
      sa.set_volume(100)
      # Wait till the 'awa' finished
      print(now)
      print(AMA_TEXT)
      subprocess.Popen(["say", AMA_TEXT])
      for i in range(10):
        beep(sound=7)
        time.sleep(0.1)
      time.sleep(1)
    
    os.system('clear')
    divider = '='*int(len(OK_TEXT)*1.5)
    print(divider)
    print('[Current usage]: ', usage, '--', now)
    print('Everything is fine, do ur work')
    print(OK_TEXT)
    print(divider)
except KeyboardInterrupt:
  print('we should stop now')
