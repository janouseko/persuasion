# -------------------------------------------------------------------
# add acquisition devices list and properties
#
# This script belongs to software collection for persuasion analysis,
# provided by Technology Agency of the Czech Republic TACR TJ02000293
#
# 2019 - 2021, Brno University of Technology, janouseko@vut.cz
# -------------------------------------------------------------------

import pickle
from constants import *

# open database
with open(DB_FILEPATH+r'\db.pickle', 'rb') as f:
    db = pickle.load(f)

# create database structure
db['device'] = {}
db['device']['fs'] = {}
db['device']['resolution'] = {}

db['device']['fs']['fs_eeg'] = FS
db['device']['fs']['fs_res'] = FS
db['device']['fs']['fs_hr'] = FS
db['device']['fs']['fs_temp_head'] = FS
db['device']['fs']['fs_temp_hand'] = FS
db['device']['fs']['fs_temp_ear'] = FS
db['device']['fs']['fs_acc'] = FS
db['device']['fs']['fs_gyro'] = FS
db['device']['fs']['fs_arousal'] = FS
db['device']['fs']['fs_valence'] = FS
db['device']['fs']['fs_marker'] = FS


db['device']['resolution']['eeg_resolution'] = '2 uV'
db['device']['resolution']['res_resolution'] = '-'
db['device']['resolution']['hr_resolution'] = '1 BPM'
db['device']['resolution']['temp_head_resolution'] = '0.1 °C'
db['device']['resolution']['temp_hand_resolution'] = '0.1 °C'
db['device']['resolution']['temp_ear_resolution'] = '1 °C'
db['device']['resolution']['acc_resolution'] = '4G, 2^16 bits'
db['device']['resolution']['gyro_resolution'] = '1000°/s, 2^16 bits'
db['device']['resolution']['arousal_resolution'] = '1 %'
db['device']['resolution']['valence_resolution'] = '1 %'
db['device']['resolution']['marker_resolution'] = '1 %'

# save database on local drive
with open('db.pickle', 'wb') as handle:
    pickle.dump(db, handle)