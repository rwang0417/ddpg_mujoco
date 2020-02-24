import argparse
import json
import numpy as np
import matplotlib.pyplot as plt
from scipy import signal
import brewer2mpl
import matplotlib as mpl

with open('.\Swimmer3\exp_0\ddpg_Swimmer3-v2_log.json', 'r') as f:
    data = json.load(f)
time_fraction=1    
episode_reward  = np.array([x for x in data['episode_reward']])
episode_reward_fraction=episode_reward/episode_reward[-1]
episode_reward_1=-episode_reward
#time_fraction=31.067
time = [x*time_fraction for x in data['episode']]

#plot preprocessing
bmap = brewer2mpl.get_map('Set2','qualitative', 7)
colors = bmap.mpl_colors
params = {
    'axes.labelsize': 15,
    'font.size': 20,
    'legend.fontsize': 15,
    'xtick.labelsize': 15,
    'ytick.labelsize': 15,
    'text.usetex': True ,
    'figure.figsize': [8, 6], # instead of 4.5, 4.5
    'font.weight': 'bold',
    'axes.labelweight': 'bold',
    'ps.useafm' : True,
    'pdf.use14corefonts':True,
    'pdf.fonttype': 42,
    'ps.fonttype': 42
}
mpl.rcParams.update(params)

b, a = signal.butter(8  , 0.025)
#%%
plt.figure(1)
plt.plot(time, episode_reward_fraction, color=colors[1], alpha=0.9)
plt.plot(time, signal.filtfilt(b, a, episode_reward_fraction), color=colors[2], linewidth=3)
plt.grid(axis='y', color='.910', linestyle='-', linewidth=1.5)
plt.grid(axis='x', color='.910', linestyle='-', linewidth=1.5)

plt.xlabel('Num of rollouts', fontsize=20)
#plt.xlabel('Training time (seconds)', fontsize=20)
plt.ylabel('Episodic reward fraction', fontsize=20)
plt.legend(['Original','Filtered'])
plt.tight_layout()

plt.figure(2)
plt.plot(time, episode_reward_1, color=colors[1], alpha=0.9)
plt.plot(time, signal.filtfilt(b, a, episode_reward_1), color=colors[2], linewidth=3)
plt.grid(axis='y', color='.910', linestyle='-', linewidth=1.5)
plt.grid(axis='x', color='.910', linestyle='-', linewidth=1.5)

plt.xlabel('Training time (seconds)', fontsize=20)
#plt.xlabel('Num of rollouts', fontsize=20)
plt.ylabel('Episodic cost fraction', fontsize=20)
plt.legend(['Original','Filtered'])
plt.show()
plt.tight_layout()
