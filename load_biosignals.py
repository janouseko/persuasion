# -------------------------------------------------------------------
# load biosignal records from performer's and recipients's session
#
# This script belongs to software collection for persuasion analysis,
# provided by Technology Agency of the Czech Republic TACR TJ02000293
#
# 2019 - 2021, Brno University of Technology, janouseko@vut.cz
# -------------------------------------------------------------------

import pickle
import numpy as np
from constants import *

# open a data-table of preprocessed (filtered, resampled)
with open(DB_FILEPATH+r'\biosignal_records.pickle', 'rb') as f:

    P1_pre,R1_pre,P2_pre,R2_pre,P3_pre,R3_pre,P4_pre,R4_pre = pickle.load(f)
    dataset = {'P1':P1_pre,'P2':P2_pre,'P3':P3_pre,'P4':P4_pre,'R1':R1_pre,'R2':R2_pre,'R3':R3_pre,'R4':R4_pre}

# create timeline covering the duration of experiment
timeline = np.arange(0,23*60,1/FS)

# CREATE STRUCTURE OF WORKING DATABASE
# create database structure using Ps and Rs ID
db = {'subject':{'P1': {'record': {'id': 'P1'}},
                 'P2': {'record': {'id': 'P2'}},
                 'P3': {'record': {'id': 'P3'}},
                 'P4': {'record': {'id': 'P4'}},
                 'R1': {'record': {'id': 'R1'}},
                 'R2': {'record': {'id': 'R2'}},
                 'R3': {'record': {'id': 'R3'}},
                 'R4': {'record': {'id': 'R4'}},
                 }
      }

for i in db['subject'].keys():
    db['subject'][i]['record']['timestamp'] = {}
    db['subject'][i]['record']['res'] = {}
    db['subject'][i]['record']['res_amp'] = {}
    db['subject'][i]['record']['res_freq'] = {}
    db['subject'][i]['record']['temp_head'] = {}
    db['subject'][i]['record']['temp_hand'] = {}
    db['subject'][i]['record']['temp_ear'] = {}
    db['subject'][i]['record']['hr'] = {}
    db['subject'][i]['record']['eeg_tp9'] = {}
    db['subject'][i]['record']['eeg_af7'] = {}
    db['subject'][i]['record']['eeg_af8'] = {}
    db['subject'][i]['record']['eeg_tp10'] = {}
    db['subject'][i]['record']['acc_x'] = {}
    db['subject'][i]['record']['acc_y'] = {}
    db['subject'][i]['record']['acc_z'] = {}
    db['subject'][i]['record']['gyro_x'] = {}
    db['subject'][i]['record']['gyro_y'] = {}
    db['subject'][i]['record']['gyro_z'] = {}
    db['subject'][i]['record']['arousal'] = {}
    db['subject'][i]['record']['valence'] = {}
    db['subject'][i]['record']['marker'] = {}

# FILL WORKING DATABASE WITH BIOSIGNALS
# add timeline in Ps and Rs
for i in db['subject'].keys():
    db['subject'][i]['record']['timestamp']['value'] = timeline

# add respiration in Ps and Rs
for i in db['subject'].keys():
    db['subject'][i]['record']['res']['value'] = dataset[i].res

# add respiration amplitude in Ps and Rs
for i in db['subject'].keys():
    db['subject'][i]['record']['res_amp']['value'] = dataset[i].res_amp

# add respiration frequency in Ps and Rs
for i in db['subject'].keys():
    db['subject'][i]['record']['res_freq']['value'] = dataset[i].res_freq

# add head temperature in Ps and Rs
for i in db['subject'].keys():
    db['subject'][i]['record']['temp_head']['value'] = dataset[i].th

# add hand temperature in Ps and Rs
for i in db['subject'].keys():
    db['subject'][i]['record']['temp_hand']['value'] = dataset[i].tr

# add ear temperature in Ps and Rs
for i in db['subject'].keys():
    db['subject'][i]['record']['temp_ear']['value']= dataset[i].tu

# add heart rate in Ps and Rs
for i in db['subject'].keys():
    db['subject'][i]['record']['hr']['value'] = dataset[i].tf

# add eeg TP9 in Ps and Rs
for i in db['subject'].keys():
    db['subject'][i]['record']['eeg_tp9']['value'] = dataset[i].eeg_tp9

# add eeg_af7 in Ps and Rs
for i in db['subject'].keys():
    db['subject'][i]['record']['eeg_af7']['value'] = dataset[i].eeg_af7

# add eeg_af8 in Ps and Rs
for i in db['subject'].keys():
    db['subject'][i]['record']['eeg_af8']['value'] = dataset[i].eeg_af8

# add eeg_tp10 in Ps and Rs
for i in db['subject'].keys():
    db['subject'][i]['record']['eeg_tp10']['value'] = dataset[i].eeg_tp10

# add linear acceleration in X axis in Ps and Rs
for i in db['subject'].keys():
    db['subject'][i]['record']['acc_x']['value'] = dataset[i].acc_x
    db['subject'][i]['record']['acc_x']['value'] = db['subject'][i]['record']['acc_x']['value'] .astype('float64')

# add linear acceleration in Y axis in Ps and Rs
for i in db['subject'].keys():
    db['subject'][i]['record']['acc_y']['value'] = dataset[i].acc_y
    db['subject'][i]['record']['acc_y']['value']  = db['subject'][i]['record']['acc_y']['value'] .astype('float64')

# add linear acceleration in Z axis in Ps and Rs
for i in db['subject'].keys():
    db['subject'][i]['record']['acc_z']['value'] = dataset[i].acc_z
    db['subject'][i]['record']['acc_z']['value']  = db['subject'][i]['record']['acc_z']['value'] .astype('float64')

# add gyroscopic acceleration in roll axis in Ps and Rs
for i in db['subject'].keys():
    db['subject'][i]['record']['gyro_x']['value'] = dataset[i].gyro_x
    db['subject'][i]['record']['gyro_x']['value'] = db['subject'][i]['record']['gyro_x']['value'].astype('float64')

# add gyroscopic acceleration in pitch axis in Ps and Rs
for i in db['subject'].keys():
    db['subject'][i]['record']['gyro_y']['value'] = dataset[i].gyro_y
    db['subject'][i]['record']['gyro_y']['value'] = db['subject'][i]['record']['gyro_y']['value'].astype('float64')

# add gyroscopic acceleration in yaw axis in Ps and Rs
for i in db['subject'].keys():
    db['subject'][i]['record']['gyro_z']['value'] = dataset[i].gyro_z
    db['subject'][i]['record']['gyro_z']['value'] = db['subject'][i]['record']['gyro_z']['value'].astype('float64')

# add arousal in Ps and Rs
for i in db['subject'].keys():
    db['subject'][i]['record']['arousal']['value'] = dataset[i].arousal

# add arousal in Ps and Rs
for i in db['subject'].keys():
    db['subject'][i]['record']['valence']['value'] = dataset[i].valence

# add marker in Ps and Rs
for i in db['subject'].keys():
    db['subject'][i]['record']['marker']['value'] = dataset[i].marker

# save working database on local drive
with open('db.pickle', 'wb') as handle:
    pickle.dump(db, handle)