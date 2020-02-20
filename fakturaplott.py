#!/usr/bin/env python3
import matplotlib.pyplot as plt
import subprocess
import os,sys

def plutteplott(x, f, label, color):
	y = [f(x) for x in x]
	axis.plot(x, y, label=label, color=color, linewidth=1, marker='o', markersize=2)

def linplot(f, label, color):
	plutteplott([0, 1350], f, label, color)

fig = plt.figure(figsize=(10, 10))
axis = fig.add_subplot(1, 1, 1)
axis.set_title('Fakturahonorar')

def ladeklar(x):
	return 69

# https://meshcrafts.com/smartcharge-zaptec/?lang=no
def smartcharge(x):
	return 20 + .1 * x

# https://www.plugpay.no/eiere-av-zaptec-anlegg/
def plugpay(x):
	return .15 * x

# https://borettslad.no/
def borettslad(x):
	if x < 50:
		return x * 29/50
	else:
		return 29

linplot(ladeklar, 'ladeklar alt2', 'red')
linplot(smartcharge, 'smartcharge', 'blue')
linplot(plugpay, 'plugpay', 'violet')
plutteplott([0, 50, 1350], borettslad, 'borettslad', '#28b800')
axis.set_xlabel('kr')
axis.set_ylabel('kr')
axis.legend()

path = '/tmp/fakturahonorar.png'
fig.savefig(path)
ran = subprocess.run(['kolourpaint', path])
os.remove(path)

sys.exit(ran.returncode)
