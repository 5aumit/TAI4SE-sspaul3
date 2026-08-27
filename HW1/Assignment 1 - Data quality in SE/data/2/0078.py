import time
import random
import datetime

from sentidos.som import FREQUENCIA, doppler

print(FREQUENCIA)
doppler()

exit()
#import subprocess

#Importando mudulos específicos
from subprocess import run, PIPE

#r = subprocess.run(['free', '-h'], stdout=subprocess.PIPE)

r = run(['apt-get', '-install','-y','sl'], stdout=PIPE, stderr=PIPE)

if not r.returncode != 0:
	print('Deu merda.......')


print(r.stdout)
exit()

#Ou import time, ramdom, datetime


letras = ['A', 'B', 'C ', 'D']

print(random.randint(100, 999))

time.sleep(5)

print(random.choice(letras))

print(datetime.datetime.now())

hoje = datetime.datetime.now()

print(hoje.strftime('%d/%m/%Y'))