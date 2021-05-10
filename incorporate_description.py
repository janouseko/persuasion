# -------------------------------------------------------------------
# extend working database with description (explanation) of experiments
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
db['description'] = {}

db['description']['aim'] = 'persuasion assessment in anger, peace and waggishness'
db['description']['date'] = 'summer session 2020'
db['description']['place'] = 'laboratory adapted on multi-stage scene, temperature stabilized, noise-free'
db['description']['setup'] = 'design of experiment: neutral (2m) vs emotions (5m): 2N-5A-2N-5P-2N-5W-2N, \'' \
                             'person: 4x duo performer + recipient, devices: elektroencephalography, temperature of ' \
                             'head, hand and ear, heart rhythm, accelaration and rotation of head, respiration.'
db['description']['note'] = 'biosignals preprocessed and resampled at 500 Hz'

# save database on local drive
with open('db.pickle', 'wb') as handle:
    pickle.dump(db, handle)