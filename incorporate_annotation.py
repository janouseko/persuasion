# -------------------------------------------------------------------
# extend database with annotation
#
# This script belongs to software collection for persuasion analysis,
# provided by Technology Agency of the Czech Republic TACR TJ02000293
#
# 2019 - 2021, Brno University of Technology, janouseko@vut.cz
# -------------------------------------------------------------------

import pickle
import numpy as np
from constants import *

# open database
with open(DB_FILEPATH+r'\db.pickle', 'rb') as f:
    db = pickle.load(f)

# create database structure using Ps and Rs ID
for i in db['subject'].keys():
    db['subject'][i]['annotation'] = {}
    db['subject'][i]['annotation']['is_persuasion'] = {}
    db['subject'][i]['annotation']['is_persuasion']['value'] = np.empty([EXPERIMENT_LENGTH])
    db['subject'][i]['annotation']['emotion'] = {}
    db['subject'][i]['annotation']['emotion']['value'] = np.empty([EXPERIMENT_LENGTH], dtype="S12")

# add is_persuasion annotation
db['subject']['P1']['annotation']['is_persuasion']['value'][PAUSE1_START:PAUSE1_END] = float('nan')
db['subject']['P1']['annotation']['is_persuasion']['value'][RED_START:RED_END] = 1
db['subject']['P1']['annotation']['is_persuasion']['value'][PAUSE2_START:PAUSE2_END] = 1
db['subject']['P1']['annotation']['is_persuasion']['value'][BLUE_START:BLUE_END] = 1
db['subject']['P1']['annotation']['is_persuasion']['value'][PAUSE3_START:PAUSE3_END] = 1
db['subject']['P1']['annotation']['is_persuasion']['value'][PINK_START:PINK_END] = 1
db['subject']['P1']['annotation']['is_persuasion']['value'][PAUSE4_START:PAUSE4_END] = float('nan')

db['subject']['P2']['annotation']['is_persuasion']['value'][PAUSE1_START:PAUSE1_END] = float('nan')
db['subject']['P2']['annotation']['is_persuasion']['value'][RED_START:RED_END] = 1
db['subject']['P2']['annotation']['is_persuasion']['value'][PAUSE2_START:PAUSE2_END] = 1
db['subject']['P2']['annotation']['is_persuasion']['value'][BLUE_START:BLUE_END] = 1
db['subject']['P2']['annotation']['is_persuasion']['value'][PAUSE3_START:PAUSE3_END] = 1
db['subject']['P2']['annotation']['is_persuasion']['value'][PINK_START:PINK_END] = 1
db['subject']['P2']['annotation']['is_persuasion']['value'][PAUSE4_START:PAUSE4_END] = float('nan')

db['subject']['P3']['annotation']['is_persuasion']['value'][PAUSE1_START:PAUSE1_END] = float('nan')
db['subject']['P3']['annotation']['is_persuasion']['value'][RED_START:RED_END] = 0
db['subject']['P3']['annotation']['is_persuasion']['value'][PAUSE2_START:PAUSE2_END] = 0
db['subject']['P3']['annotation']['is_persuasion']['value'][BLUE_START:BLUE_END] = 0
db['subject']['P3']['annotation']['is_persuasion']['value'][PAUSE3_START:PAUSE3_END] = 0
db['subject']['P3']['annotation']['is_persuasion']['value'][PINK_START:PINK_END] = 0
db['subject']['P3']['annotation']['is_persuasion']['value'][PAUSE4_START:PAUSE4_END] = float('nan')

db['subject']['P4']['annotation']['is_persuasion']['value'][PAUSE1_START:PAUSE1_END] = float('nan')
db['subject']['P4']['annotation']['is_persuasion']['value'][RED_START:RED_END] = 0
db['subject']['P4']['annotation']['is_persuasion']['value'][PAUSE2_START:PAUSE2_END] = 0
db['subject']['P4']['annotation']['is_persuasion']['value'][BLUE_START:BLUE_END] = 0
db['subject']['P4']['annotation']['is_persuasion']['value'][PAUSE3_START:PAUSE3_END] = 0
db['subject']['P4']['annotation']['is_persuasion']['value'][PINK_START:PINK_END] = 0
db['subject']['P4']['annotation']['is_persuasion']['value'][PAUSE4_START:PAUSE4_END] = float('nan')

db['subject']['R1']['annotation']['is_persuasion']['value'][PAUSE1_START:PAUSE1_END] = float('nan')
db['subject']['R1']['annotation']['is_persuasion']['value'][RED_START:RED_END] = 1
db['subject']['R1']['annotation']['is_persuasion']['value'][PAUSE2_START:PAUSE2_END] = 1
db['subject']['R1']['annotation']['is_persuasion']['value'][BLUE_START:BLUE_END] = 1
db['subject']['R1']['annotation']['is_persuasion']['value'][PAUSE3_START:PAUSE3_END] = 1
db['subject']['R1']['annotation']['is_persuasion']['value'][PINK_START:PINK_END] = 1
db['subject']['R1']['annotation']['is_persuasion']['value'][PAUSE4_START:PAUSE4_END] = float('nan')

db['subject']['R2']['annotation']['is_persuasion']['value'][PAUSE1_START:PAUSE1_END] = float('nan')
db['subject']['R2']['annotation']['is_persuasion']['value'][RED_START:RED_END] = 1
db['subject']['R2']['annotation']['is_persuasion']['value'][PAUSE2_START:PAUSE2_END] = 1
db['subject']['R2']['annotation']['is_persuasion']['value'][BLUE_START:BLUE_END] = 1
db['subject']['R2']['annotation']['is_persuasion']['value'][PAUSE3_START:PAUSE3_END] = 1
db['subject']['R2']['annotation']['is_persuasion']['value'][PINK_START:PINK_END] = 1
db['subject']['R2']['annotation']['is_persuasion']['value'][PAUSE4_START:PAUSE4_END] = float('nan')

db['subject']['R3']['annotation']['is_persuasion']['value'][PAUSE1_START:PAUSE1_END] = float('nan')
db['subject']['R3']['annotation']['is_persuasion']['value'][RED_START:RED_END] = 0
db['subject']['R3']['annotation']['is_persuasion']['value'][PAUSE2_START:PAUSE2_END] = 0
db['subject']['R3']['annotation']['is_persuasion']['value'][BLUE_START:BLUE_END] = 0
db['subject']['R3']['annotation']['is_persuasion']['value'][PAUSE3_START:PAUSE3_END] = 0
db['subject']['R3']['annotation']['is_persuasion']['value'][PINK_START:PINK_END] = 0
db['subject']['R3']['annotation']['is_persuasion']['value'][PAUSE4_START:PAUSE4_END] = float('nan')

db['subject']['R4']['annotation']['is_persuasion']['value'][PAUSE1_START:PAUSE1_END] = float('nan')
db['subject']['R4']['annotation']['is_persuasion']['value'][RED_START:RED_END] = 0
db['subject']['R4']['annotation']['is_persuasion']['value'][PAUSE2_START:PAUSE2_END] = 0
db['subject']['R4']['annotation']['is_persuasion']['value'][BLUE_START:BLUE_END] = 0
db['subject']['R4']['annotation']['is_persuasion']['value'][PAUSE3_START:PAUSE3_END] = 0
db['subject']['R4']['annotation']['is_persuasion']['value'][PINK_START:PINK_END] = 0
db['subject']['R4']['annotation']['is_persuasion']['value'][PAUSE4_START:PAUSE4_END] = float('nan')

# add activity
for i in db['subject'].keys():
    db['subject'][i]['annotation']['emotion']['value'][PAUSE1_START:PAUSE1_END] = 'neutral'
    db['subject'][i]['annotation']['emotion']['value'][RED_START:RED_END] = 'anger'
    db['subject'][i]['annotation']['emotion']['value'][PAUSE2_START:PAUSE2_END] = 'neutral'
    db['subject'][i]['annotation']['emotion']['value'][BLUE_START:BLUE_END] = 'peace'
    db['subject'][i]['annotation']['emotion']['value'][PAUSE3_START:PAUSE3_END] = 'neutral'
    db['subject'][i]['annotation']['emotion']['value'][PINK_START:PINK_END] = 'waggishness'
    db['subject'][i]['annotation']['emotion']['value'][PAUSE4_START:PAUSE4_END] = 'neutral'

# save database on local drive
with open('db.pickle', 'wb') as handle:
    pickle.dump(db, handle)