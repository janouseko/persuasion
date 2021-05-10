# -------------------------------------------------------------------
# evaluate signals (such as derivates of raw biosignals)
#
# This script belongs to software collection for persuasion analysis,
# provided by Technology Agency of the Czech Republic TACR TJ02000293
#
# 2019 - 2021, Brno University of Technology, janouseko@vut.cz
# -------------------------------------------------------------------

import pickle
from scipy.signal import savgol_filter
import numpy as np
from constants import *
from statistics import mean

# open database
with open(DB_FILEPATH+r'\db.pickle', 'rb') as f:
    db = pickle.load(f)


# create database structure using Ps and Rs ID
for i in db['subject'].keys():
    db['subject'][i]['signal'] = {}

for i in db['subject'].keys():
    db['subject'][i]['signal']['hr_smooth'] = {}
    db['subject'][i]['signal']['hr_smooth_derivation'] = {}
    db['subject'][i]['signal']['res_volume'] = {}
    db['subject'][i]['signal']['acc_mag'] = {}
    db['subject'][i]['signal']['gyro_mag'] = {}
    db['subject'][i]['signal']['impression'] = {}

# add smooth heart rate
smoothing_window_length = 50001 #samples
for i in db['subject'].keys():
    db['subject'][i]['signal']['hr_smooth']['value'] = \
        savgol_filter(db['subject'][i]['record']['hr']['value'],smoothing_window_length, 2)

# add speed of change of smoothed heart rate
for i in db['subject'].keys():
    db['subject'][i]['signal']['hr_smooth_derivation']['value'] = \
        np.concatenate((np.diff(db['subject'][i]['signal']['hr_smooth']['value']),
                         np.diff(db['subject'][i]['signal']['hr_smooth']['value'])[-1]), axis=None)

# add respiratory volume (computed as res_amp * res_freq)
for i in db['subject'].keys():
    db['subject'][i]['signal']['res_volume']['value'] = \
        np.multiply(db['subject'][i]['record']['res_amp']['value'],
                    db['subject'][i]['record']['res_freq']['value'])

# add total amount of linear acceleration
for i in db['subject'].keys():
    db['subject'][i]['signal']['acc_mag']['value'] = \
        np.sqrt(((db['subject'][i]['record']['acc_x']['value'] -
                  mean(db['subject'][i]['record']['acc_x']['value']))**2 +
                 (db['subject'][i]['record']['acc_y']['value'] -
                  mean(db['subject'][i]['record']['acc_y']['value']))**2 +
                 (db['subject'][i]['record']['acc_z']['value'] -
                  mean(db['subject'][i]['record']['acc_z']['value']))**2))

# add total amount of rotation acceleration
for i in db['subject'].keys():
    db['subject'][i]['signal']['gyro_mag']['value'] = \
        np.sqrt(((db['subject'][i]['record']['gyro_x']['value'] -
                  mean(db['subject'][i]['record']['gyro_x']['value'])) ** 2 +
                 (db['subject'][i]['record']['gyro_y']['value'] -
                  mean(db['subject'][i]['record']['gyro_y']['value'])) ** 2 +
                 (db['subject'][i]['record']['gyro_z']['value'] -
                  mean(db['subject'][i]['record']['gyro_z']['value'])) ** 2))

# add impression (computed as arousal * valence)
for i in db['subject'].keys():
    db['subject'][i]['signal']['impression']['value'] = \
        np.multiply(db['subject'][i]['record']['arousal']['value'],
                    db['subject'][i]['record']['valence']['value'])

# save database on local drive
with open('db.pickle', 'wb') as handle:
    pickle.dump(db, handle)