#!/usr/bin/env python3
import matplotlib.pyplot as plt
import subprocess
import os,sys

def linplot(f, label, color):
    x = [0, 1350]
    y = [f(x) for x in x]

    axis.plot(x, y, label=label, color=color, linewidth=1, marker='o', markersize=2)

fig = plt.figure(figsize=(10, 10))
axis = fig.add_subplot(1, 1, 1)
axis.set_title('Fakturahonorar')

def ladeklar(x):
	return 79

# https://meshcrafts.com/smartcharge-zaptec/?lang=no
def smartcharge(x):
	return 20 + .1 * x

# https://www.plugpay.no/eiere-av-zaptec-anlegg/
def plugpay(x):
	return .15 * x

linplot(ladeklar, 'ladeklar', 'red')
linplot(smartcharge, 'smartcharge', 'blue')
linplot(plugpay, 'plugpay', 'violet')
axis.set_xlabel('kr')
axis.set_ylabel('kr')
axis.legend()

path = '/tmp/fakturahonorar.png'
fig.savefig(path)
ran = subprocess.run(['kolourpaint', path])
os.remove(path)

sys.exit(ran.returncode)
