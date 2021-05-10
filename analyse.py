# -------------------------------------------------------------------
# analyse data and compute parameters for persusasion asessment
#
# This script belongs to software collection for persuasion analysis,
# provided by Technology Agency of the Czech Republic TACR TJ02000293
#
# 2019 - 2021, Brno University of Technology, janouseko@vut.cz
# -------------------------------------------------------------------

import pickle
import numpy as np
from constants import *
from scipy.stats import pearsonr
from scipy.signal import welch
from scipy.integrate import simps
from statistics import mean
import pandas as pd


# compute absolute power in alpha (8 - 12 Hz) band, fs = 500
def alpha_power(data):
    nperseg = (2 / 8) * 500
    freqs, psd = welch(data, 500, nperseg=nperseg)
    freq_res = freqs[1] - freqs[0]
    idx_band = np.logical_and(freqs >= 8, freqs <= 12)
    return simps(psd[idx_band], dx=freq_res)


# compute absolute power in beta (12 - 40 Hz) band, fs = 500
def beta_power(data):
    nperseg = (2 / 12) * 500
    freqs, psd = welch(data, 500, nperseg=nperseg)
    freq_res = freqs[1] - freqs[0]
    idx_band = np.logical_and(freqs >= 12, freqs <= 40)
    return simps(psd[idx_band], dx=freq_res)


# open database
with open(DB_FILEPATH+r'\db.pickle', 'rb') as f:
    db = pickle.load(f)

# create database structure using Ps and Rs ID
for i in db['subject'].keys():
    db['subject'][i]['analysis'] = {}

    db['subject'][i]['analysis']['arousal_is_start'] = {}
    db['subject'][i]['analysis']['arousal_is_end'] = {}
    db['subject'][i]['analysis']['arousal_is_high'] = {}
    db['subject'][i]['analysis']['arousal_is_low'] = {}
    db['subject'][i]['analysis']['arousal_activity_mean_numeric'] = {}
    db['subject'][i]['analysis']['arousal_activity_mean_verbal'] = {}
    db['subject'][i]['analysis']['arousal_activity_groupmean_numeric'] = {}
    db['subject'][i]['analysis']['arousal_activity_groupmean_verbal'] = {}
    db['subject'][i]['analysis']['valence_activity_mean_numeric'] = {}
    db['subject'][i]['analysis']['valence_activity_mean_verbal'] = {}
    db['subject'][i]['analysis']['valence_activity_groupmean_numeric'] = {}
    db['subject'][i]['analysis']['valence_activity_groupmean_verbal'] = {}
    db['subject'][i]['analysis']['hr_smooth_activity_mean'] = {}
    db['subject'][i]['analysis']['acc_activity_amount'] = {}
    db['subject'][i]['analysis']['acc_total_amount'] = {}
    db['subject'][i]['analysis']['gyro_activity_amount'] = {}
    db['subject'][i]['analysis']['gyro_total_amount'] = {}
    db['subject'][i]['analysis']['hr_activity_correlation'] = {}
    db['subject'][i]['analysis']['hr_total_correlation'] = {}
    db['subject'][i]['analysis']['temp_hand_activity_correlation'] = {}
    db['subject'][i]['analysis']['temp_hand_total_correlation'] = {}
    db['subject'][i]['analysis']['temp_head_activity_correlation'] = {}
    db['subject'][i]['analysis']['temp_head_total_correlation'] = {}
    db['subject'][i]['analysis']['temp_ear_activity_correlation'] = {}
    db['subject'][i]['analysis']['temp_ear_total_correlation'] = {}
    db['subject'][i]['analysis']['eeg_af7_alpha_activity_energy'] = {}
    db['subject'][i]['analysis']['eeg_af8_alpha_activity_energy'] = {}
    db['subject'][i]['analysis']['eeg_tp9_alpha_activity_energy'] = {}
    db['subject'][i]['analysis']['eeg_tp10_alpha_activity_energy'] = {}
    db['subject'][i]['analysis']['eeg_af7_alpha_total_energy'] = {}
    db['subject'][i]['analysis']['eeg_af8_alpha_total_energy'] = {}
    db['subject'][i]['analysis']['eeg_tp9_alpha_total_energy'] = {}
    db['subject'][i]['analysis']['eeg_tp10_alpha_total_energy'] = {}
    db['subject'][i]['analysis']['eeg_af7_beta_activity_energy'] = {}
    db['subject'][i]['analysis']['eeg_af8_beta_activity_energy'] = {}
    db['subject'][i]['analysis']['eeg_tp9_beta_activity_energy'] = {}
    db['subject'][i]['analysis']['eeg_tp10_beta_activity_energy'] = {}
    db['subject'][i]['analysis']['eeg_af7_beta_total_energy'] = {}
    db['subject'][i]['analysis']['eeg_af8_beta_total_energy'] = {}
    db['subject'][i]['analysis']['eeg_tp9_beta_total_energy'] = {}
    db['subject'][i]['analysis']['eeg_tp10_beta_total_energy'] = {}

    db['subject'][i]['analysis']['arousal_is_start']['value'] = np.empty([EXPERIMENT_LENGTH], dtype=bool)
    db['subject'][i]['analysis']['arousal_is_end']['value'] = np.empty([EXPERIMENT_LENGTH], dtype=bool)
    db['subject'][i]['analysis']['arousal_is_high']['value'] = np.empty([EXPERIMENT_LENGTH], dtype=bool)
    db['subject'][i]['analysis']['arousal_is_low']['value'] = np.empty([EXPERIMENT_LENGTH], dtype=bool)
    db['subject'][i]['analysis']['arousal_activity_mean_numeric']['value'] = np.empty([EXPERIMENT_LENGTH],
                                                                                      dtype=float)
    db['subject'][i]['analysis']['arousal_activity_mean_verbal']['value'] = np.empty([EXPERIMENT_LENGTH], dtype="S8")
    db['subject'][i]['analysis']['arousal_activity_groupmean_numeric']['value'] = np.empty([EXPERIMENT_LENGTH],dtype=float)
    db['subject'][i]['analysis']['arousal_activity_groupmean_verbal']['value'] = np.empty([EXPERIMENT_LENGTH],
                                                                                          dtype="S8")
    db['subject'][i]['analysis']['valence_activity_mean_numeric']['value'] = np.empty([EXPERIMENT_LENGTH],dtype=float)
    db['subject'][i]['analysis']['valence_activity_mean_verbal']['value'] = np.empty([EXPERIMENT_LENGTH], dtype="S8")
    db['subject'][i]['analysis']['valence_activity_groupmean_numeric']['value'] = np.empty([EXPERIMENT_LENGTH],dtype=float)
    db['subject'][i]['analysis']['valence_activity_groupmean_verbal']['value'] = np.empty([EXPERIMENT_LENGTH],
                                                                                          dtype="S8")
    db['subject'][i]['analysis']['hr_smooth_activity_mean']['value'] = np.empty([EXPERIMENT_LENGTH],dtype=float)
    db['subject'][i]['analysis']['acc_activity_amount']['value'] = np.empty([EXPERIMENT_LENGTH],dtype=float)
    db['subject'][i]['analysis']['acc_total_amount']['value'] = np.empty([EXPERIMENT_LENGTH],dtype=float)
    db['subject'][i]['analysis']['gyro_activity_amount']['value'] = np.empty([EXPERIMENT_LENGTH],dtype=float)
    db['subject'][i]['analysis']['gyro_total_amount']['value'] = np.empty([EXPERIMENT_LENGTH],dtype=float)
    db['subject'][i]['analysis']['hr_activity_correlation']['value'] = np.empty([EXPERIMENT_LENGTH],dtype=float)
    db['subject'][i]['analysis']['hr_total_correlation']['value'] = np.empty([EXPERIMENT_LENGTH],dtype=float)
    db['subject'][i]['analysis']['temp_hand_activity_correlation']['value'] = np.empty([EXPERIMENT_LENGTH],dtype=float)
    db['subject'][i]['analysis']['temp_hand_total_correlation']['value'] = np.empty([EXPERIMENT_LENGTH],dtype=float)
    db['subject'][i]['analysis']['temp_head_activity_correlation']['value'] = np.empty([EXPERIMENT_LENGTH],dtype=float)
    db['subject'][i]['analysis']['temp_head_total_correlation']['value'] = np.empty([EXPERIMENT_LENGTH],dtype=float)
    db['subject'][i]['analysis']['temp_ear_activity_correlation']['value'] = np.empty([EXPERIMENT_LENGTH],dtype=float)
    db['subject'][i]['analysis']['temp_ear_total_correlation']['value'] = np.empty([EXPERIMENT_LENGTH],dtype=float)
    db['subject'][i]['analysis']['eeg_af7_alpha_activity_energy']['value'] = np.empty([EXPERIMENT_LENGTH],dtype=float)
    db['subject'][i]['analysis']['eeg_af8_alpha_activity_energy']['value'] = np.empty([EXPERIMENT_LENGTH],dtype=float)
    db['subject'][i]['analysis']['eeg_tp9_alpha_activity_energy']['value'] = np.empty([EXPERIMENT_LENGTH],dtype=float)
    db['subject'][i]['analysis']['eeg_tp10_alpha_activity_energy']['value'] = np.empty([EXPERIMENT_LENGTH],dtype=float)
    db['subject'][i]['analysis']['eeg_af7_alpha_total_energy']['value'] = np.empty([EXPERIMENT_LENGTH],dtype=float)
    db['subject'][i]['analysis']['eeg_af8_alpha_total_energy']['value'] = np.empty([EXPERIMENT_LENGTH],dtype=float)
    db['subject'][i]['analysis']['eeg_tp9_alpha_total_energy']['value'] = np.empty([EXPERIMENT_LENGTH],dtype=float)
    db['subject'][i]['analysis']['eeg_tp10_alpha_total_energy']['value'] = np.empty([EXPERIMENT_LENGTH],dtype=float)
    db['subject'][i]['analysis']['eeg_af7_beta_activity_energy']['value'] = np.empty([EXPERIMENT_LENGTH],dtype=float)
    db['subject'][i]['analysis']['eeg_af8_beta_activity_energy']['value'] = np.empty([EXPERIMENT_LENGTH],dtype=float)
    db['subject'][i]['analysis']['eeg_tp9_beta_activity_energy']['value'] = np.empty([EXPERIMENT_LENGTH],dtype=float)
    db['subject'][i]['analysis']['eeg_tp10_beta_activity_energy']['value'] = np.empty([EXPERIMENT_LENGTH],dtype=float)
    db['subject'][i]['analysis']['eeg_af7_beta_total_energy']['value'] = np.empty([EXPERIMENT_LENGTH],dtype=float)
    db['subject'][i]['analysis']['eeg_af8_beta_total_energy']['value'] = np.empty([EXPERIMENT_LENGTH],dtype=float)
    db['subject'][i]['analysis']['eeg_tp9_beta_total_energy']['value'] = np.empty([EXPERIMENT_LENGTH],dtype=float)
    db['subject'][i]['analysis']['eeg_tp10_beta_total_energy']['value'] = np.empty([EXPERIMENT_LENGTH],dtype=float)

# add arousal_is_start
for i in db['subject'].keys():
    db['subject'][i]['analysis']['arousal_is_start']['value'] = np.zeros([EXPERIMENT_LENGTH], dtype=bool)
db['subject']['P1']['analysis']['arousal_is_start']['value'][75400] = True
db['subject']['P1']['analysis']['arousal_is_start']['value'][274400] = True
db['subject']['P1']['analysis']['arousal_is_start']['value'][473300] = True
db['subject']['P2']['analysis']['arousal_is_start']['value'][76400] = True
db['subject']['P2']['analysis']['arousal_is_start']['value'][273400] = True
db['subject']['P2']['analysis']['arousal_is_start']['value'][474800] = True
db['subject']['P3']['analysis']['arousal_is_start']['value'][78000] = True
db['subject']['P3']['analysis']['arousal_is_start']['value'][276000] = True
db['subject']['P3']['analysis']['arousal_is_start']['value'][480800] = True
db['subject']['P4']['analysis']['arousal_is_start']['value'][76000] = True
db['subject']['P4']['analysis']['arousal_is_start']['value'][287000] = True
db['subject']['P4']['analysis']['arousal_is_start']['value'][488000] = True
db['subject']['R1']['analysis']['arousal_is_start']['value'][90000] = True
db['subject']['R1']['analysis']['arousal_is_start']['value'][293200] = True
db['subject']['R1']['analysis']['arousal_is_start']['value'][498200] = True
db['subject']['R2']['analysis']['arousal_is_start']['value'][35000] = True
db['subject']['R2']['analysis']['arousal_is_start']['value'][267000] = True
db['subject']['R2']['analysis']['arousal_is_start']['value'][436000] = True
db['subject']['R3']['analysis']['arousal_is_start']['value'][480000] = True
# missing 2x R3 due to recipient absence of arousal start
db['subject']['R4']['analysis']['arousal_is_start']['value'][15400] = True
db['subject']['R4']['analysis']['arousal_is_start']['value'][544000] = True
# missing 1x R4 due to recipient absence of arousal start

# add arousal_is_end
for i in db['subject'].keys():
    db['subject'][i]['analysis']['arousal_is_end']['value'] = np.zeros([EXPERIMENT_LENGTH], dtype=bool)
db['subject']['P1']['analysis']['arousal_is_end']['value'][216000] = True
db['subject']['P1']['analysis']['arousal_is_end']['value'][404040] = True
db['subject']['P1']['analysis']['arousal_is_end']['value'][612000] = True
db['subject']['P2']['analysis']['arousal_is_end']['value'][207300] = True
db['subject']['P2']['analysis']['arousal_is_end']['value'][404000] = True
db['subject']['P2']['analysis']['arousal_is_end']['value'][610000] = True
db['subject']['P3']['analysis']['arousal_is_end']['value'][264000] = True
db['subject']['P3']['analysis']['arousal_is_end']['value'][410000] = True
db['subject']['P3']['analysis']['arousal_is_end']['value'][614600] = True
db['subject']['P4']['analysis']['arousal_is_end']['value'][210000] = True
db['subject']['P4']['analysis']['arousal_is_end']['value'][410000] = True
db['subject']['P4']['analysis']['arousal_is_end']['value'][617000] = True
db['subject']['R1']['analysis']['arousal_is_end']['value'][217500] = True
db['subject']['R1']['analysis']['arousal_is_end']['value'][440000] = True
db['subject']['R1']['analysis']['arousal_is_end']['value'][645000] = True
db['subject']['R2']['analysis']['arousal_is_end']['value'][222000] = True
db['subject']['R2']['analysis']['arousal_is_end']['value'][386000] = True
db['subject']['R2']['analysis']['arousal_is_end']['value'][615000] = True
db['subject']['R3']['analysis']['arousal_is_end']['value'][430000] = True
# missing 2x R3 due to recipient absence of arousal end
db['subject']['R4']['analysis']['arousal_is_end']['value'][194000] = True
db['subject']['R4']['analysis']['arousal_is_end']['value'][414000] = True
db['subject']['R4']['analysis']['arousal_is_end']['value'][640000] = True

# add arousal_is_high
for i in db['subject'].keys():
    db['subject'][i]['analysis']['arousal_is_high']['value'] = db['subject'][i]['record']['arousal'][
                                                                   'value'] > 95  # true or false

# add arousal_is_low
for i in db['subject'].keys():
    db['subject'][i]['analysis']['arousal_is_low']['value'] = db['subject'][i]['record']['arousal'][
                                                                  'value'] < 5  # true or false

# add arousal_activity_mean_numeric
for i in db['subject'].keys():
    db['subject'][i]['analysis']['arousal_activity_mean_numeric']['value'][PAUSE1_START:PAUSE1_END] = \
        mean(db['subject'][i]['record']['arousal']['value'][PAUSE1_START:PAUSE1_END])
    db['subject'][i]['analysis']['arousal_activity_mean_numeric']['value'][RED_START:RED_END] = \
        mean(db['subject'][i]['record']['arousal']['value'][RED_START:RED_END])
    db['subject'][i]['analysis']['arousal_activity_mean_numeric']['value'][PAUSE2_START:PAUSE2_END] = \
        mean(db['subject'][i]['record']['arousal']['value'][PAUSE2_START:PAUSE2_END])
    db['subject'][i]['analysis']['arousal_activity_mean_numeric']['value'][BLUE_START:BLUE_END] = \
        mean(db['subject'][i]['record']['arousal']['value'][BLUE_START:BLUE_END])
    db['subject'][i]['analysis']['arousal_activity_mean_numeric']['value'][PAUSE3_START:PAUSE3_END] = \
        mean(db['subject'][i]['record']['arousal']['value'][PAUSE3_START:PAUSE3_END])
    db['subject'][i]['analysis']['arousal_activity_mean_numeric']['value'][PINK_START:PINK_END] = \
        mean(db['subject'][i]['record']['arousal']['value'][PINK_START:PINK_END])
    db['subject'][i]['analysis']['arousal_activity_mean_numeric']['value'][PAUSE4_START:PAUSE4_END] = \
        mean(db['subject'][i]['record']['arousal']['value'][PAUSE4_START:PAUSE4_END])

# add arousal_activity_mean_verbal
for i in db['subject'].keys():
    for g in range(len(db['subject'][i]['analysis']['arousal_activity_mean_numeric']['value'])):
        db['subject'][i]['analysis']['arousal_activity_mean_verbal']['value'][g] = \
            'strong' if db['subject'][i]['analysis']['arousal_activity_mean_numeric']['value'][g] > 50 else 'weak'

# add arousal_activity_groupmean_numeric
db['subject']['P1']['analysis']['arousal_activity_groupmean_numeric']['value'] = \
    db['subject']['P2']['analysis']['arousal_activity_groupmean_numeric']['value'] = \
    db['subject']['P3']['analysis']['arousal_activity_groupmean_numeric']['value'] = \
    db['subject']['P4']['analysis']['arousal_activity_groupmean_numeric']['value'] = np.mean(
    [db['subject']['P1']['analysis']['arousal_activity_mean_numeric']['value'],
     db['subject']['P2']['analysis']['arousal_activity_mean_numeric']['value'],
     db['subject']['P3']['analysis']['arousal_activity_mean_numeric']['value'],
     db['subject']['P4']['analysis']['arousal_activity_mean_numeric']['value']], axis=0)

db['subject']['R1']['analysis']['arousal_activity_groupmean_numeric']['value'] = \
    db['subject']['R2']['analysis']['arousal_activity_groupmean_numeric']['value'] = \
    db['subject']['R3']['analysis']['arousal_activity_groupmean_numeric']['value'] = \
    db['subject']['R4']['analysis']['arousal_activity_groupmean_numeric']['value'] = np.mean(
    [db['subject']['R1']['analysis']['arousal_activity_mean_numeric']['value'],
     db['subject']['R2']['analysis']['arousal_activity_mean_numeric']['value'],
     db['subject']['R3']['analysis']['arousal_activity_mean_numeric']['value'],
     db['subject']['R4']['analysis']['arousal_activity_mean_numeric']['value']], axis=0)

# add arousal_activity_groupmean_verbal
for i in db['subject'].keys():
    for g in range(len(db['subject'][i]['analysis']['arousal_activity_groupmean_numeric']['value'])):
        db['subject'][i]['analysis']['arousal_activity_groupmean_verbal']['value'][g] = \
            'strong' if db['subject'][i]['analysis']['arousal_activity_groupmean_numeric']['value'][g] > 50 else 'weak'

# add valence_activity_mean_numeric
for i in db['subject'].keys():
    db['subject'][i]['analysis']['valence_activity_mean_numeric']['value'][PAUSE1_START:PAUSE1_END] = \
        mean(db['subject'][i]['record']['valence']['value'][PAUSE1_START:PAUSE1_END])
    db['subject'][i]['analysis']['valence_activity_mean_numeric']['value'][RED_START:RED_END] = \
        mean(db['subject'][i]['record']['valence']['value'][RED_START:RED_END])
    db['subject'][i]['analysis']['valence_activity_mean_numeric']['value'][PAUSE2_START:PAUSE2_END] = \
        mean(db['subject'][i]['record']['valence']['value'][PAUSE2_START:PAUSE2_END])
    db['subject'][i]['analysis']['valence_activity_mean_numeric']['value'][BLUE_START:BLUE_END] = \
        mean(db['subject'][i]['record']['valence']['value'][BLUE_START:BLUE_END])
    db['subject'][i]['analysis']['valence_activity_mean_numeric']['value'][PAUSE3_START:PAUSE3_END] = \
        mean(db['subject'][i]['record']['valence']['value'][PAUSE3_START:PAUSE3_END])
    db['subject'][i]['analysis']['valence_activity_mean_numeric']['value'][PINK_START:PINK_END] = \
        mean(db['subject'][i]['record']['valence']['value'][PINK_START:PINK_END])
    db['subject'][i]['analysis']['valence_activity_mean_numeric']['value'][PAUSE4_START:PAUSE4_END] = \
        mean(db['subject'][i]['record']['valence']['value'][PAUSE4_START:PAUSE4_END])

# add valence_activity_mean_verbal
for i in db['subject'].keys():
    for g in range(len(db['subject'][i]['analysis']['valence_activity_mean_numeric']['value'])):
        db['subject'][i]['analysis']['valence_activity_mean_verbal']['value'][g] = \
            'strong' if db['subject'][i]['analysis']['valence_activity_mean_numeric']['value'][g] > 50 else 'weak'

# add valence_activity_groupmean_numeric
db['subject']['P1']['analysis']['valence_activity_groupmean_numeric']['value'] = \
    db['subject']['P2']['analysis']['valence_activity_groupmean_numeric']['value'] = \
    db['subject']['P3']['analysis']['valence_activity_groupmean_numeric']['value'] = \
    db['subject']['P4']['analysis']['valence_activity_groupmean_numeric']['value'] = np.mean(
    [db['subject']['P1']['analysis']['valence_activity_mean_numeric']['value'],
     db['subject']['P2']['analysis']['valence_activity_mean_numeric']['value'],
     db['subject']['P3']['analysis']['valence_activity_mean_numeric']['value'],
     db['subject']['P4']['analysis']['valence_activity_mean_numeric']['value']], axis=0)
db['subject']['R1']['analysis']['valence_activity_groupmean_numeric']['value'] = \
    db['subject']['R2']['analysis']['valence_activity_groupmean_numeric']['value'] = \
    db['subject']['R3']['analysis']['valence_activity_groupmean_numeric']['value'] = \
    db['subject']['R4']['analysis']['valence_activity_groupmean_numeric']['value'] = np.mean(
    [db['subject']['R1']['analysis']['valence_activity_mean_numeric']['value'],
     db['subject']['R2']['analysis']['valence_activity_mean_numeric']['value'],
     db['subject']['R3']['analysis']['valence_activity_mean_numeric']['value'],
     db['subject']['R4']['analysis']['valence_activity_mean_numeric']['value']], axis=0)

# add valence_activity_groupmean_verbal
for i in db['subject'].keys():
    for g in range(len(db['subject'][i]['analysis']['valence_activity_groupmean_numeric']['value'])):
        db['subject'][i]['analysis']['valence_activity_groupmean_verbal']['value'][g] = \
            'strong' if db['subject'][i]['analysis']['valence_activity_groupmean_numeric']['value'][g] > 50 else 'weak'

# add hr_smooth_activity_mean
for i in db['subject'].keys():
    db['subject'][i]['analysis']['hr_smooth_activity_mean']['value'][PAUSE1_START:PAUSE1_END] = \
        mean(db['subject'][i]['signal']['hr_smooth']['value'][PAUSE1_START:PAUSE1_END])
    db['subject'][i]['analysis']['hr_smooth_activity_mean']['value'][RED_START:RED_END] = \
        mean(db['subject'][i]['signal']['hr_smooth']['value'][RED_START:RED_END])
    db['subject'][i]['analysis']['hr_smooth_activity_mean']['value'][PAUSE2_START:PAUSE2_END] = \
        mean(db['subject'][i]['signal']['hr_smooth']['value'][PAUSE2_START:PAUSE2_END])
    db['subject'][i]['analysis']['hr_smooth_activity_mean']['value'][BLUE_START:BLUE_END] = \
        mean(db['subject'][i]['signal']['hr_smooth']['value'][BLUE_START:BLUE_END])
    db['subject'][i]['analysis']['hr_smooth_activity_mean']['value'][PAUSE3_START:PAUSE3_END] = \
        mean(db['subject'][i]['signal']['hr_smooth']['value'][PAUSE3_START:PAUSE3_END])
    db['subject'][i]['analysis']['hr_smooth_activity_mean']['value'][PINK_START:PINK_END] = \
        mean(db['subject'][i]['signal']['hr_smooth']['value'][PINK_START:PINK_END])
    db['subject'][i]['analysis']['hr_smooth_activity_mean']['value'][PAUSE4_START:PAUSE4_END] = \
        mean(db['subject'][i]['signal']['hr_smooth']['value'][PAUSE4_START:PAUSE4_END])

# add acc_activity_amount
for i in db['subject'].keys():
    db['subject'][i]['analysis']['acc_activity_amount']['value'][PAUSE1_START:PAUSE1_END] = \
        np.sum(db['subject'][i]['signal']['acc_mag']['value'][PAUSE1_START:PAUSE1_END])
    db['subject'][i]['analysis']['acc_activity_amount']['value'][RED_START:RED_END] = \
        np.sum(db['subject'][i]['signal']['acc_mag']['value'][RED_START:RED_END])
    db['subject'][i]['analysis']['acc_activity_amount']['value'][PAUSE2_START:PAUSE2_END] = \
        np.sum(db['subject'][i]['signal']['acc_mag']['value'][PAUSE2_START:PAUSE2_END])
    db['subject'][i]['analysis']['acc_activity_amount']['value'][BLUE_START:BLUE_END] = \
        np.sum(db['subject'][i]['signal']['acc_mag']['value'][BLUE_START:BLUE_END])
    db['subject'][i]['analysis']['acc_activity_amount']['value'][PAUSE3_START:PAUSE3_END] = \
        np.sum(db['subject'][i]['signal']['acc_mag']['value'][PAUSE3_START:PAUSE3_END])
    db['subject'][i]['analysis']['acc_activity_amount']['value'][PINK_START:PINK_END] = \
        np.sum(db['subject'][i]['signal']['acc_mag']['value'][PINK_START:PINK_END])
    db['subject'][i]['analysis']['acc_activity_amount']['value'][PAUSE4_START:PAUSE4_END] = \
        np.sum(db['subject'][i]['signal']['acc_mag']['value'][PAUSE4_START:PAUSE4_END])

# add acc_total_amount
for i in db['subject'].keys():
    db['subject'][i]['analysis']['acc_total_amount']['value'][:] = np.sum(
        db['subject'][i]['signal']['acc_mag']['value'])

# add gyro_activity_amount
for i in db['subject'].keys():
    db['subject'][i]['analysis']['gyro_activity_amount']['value'][PAUSE1_START:PAUSE1_END] = \
        np.sum(db['subject'][i]['signal']['gyro_mag']['value'][PAUSE1_START:PAUSE1_END])
    db['subject'][i]['analysis']['gyro_activity_amount']['value'][RED_START:RED_END] = \
        np.sum(db['subject'][i]['signal']['gyro_mag']['value'][RED_START:RED_END])
    db['subject'][i]['analysis']['gyro_activity_amount']['value'][PAUSE2_START:PAUSE2_END] = \
        np.sum(db['subject'][i]['signal']['gyro_mag']['value'][PAUSE2_START:PAUSE2_END])
    db['subject'][i]['analysis']['gyro_activity_amount']['value'][BLUE_START:BLUE_END] = \
        np.sum(db['subject'][i]['signal']['gyro_mag']['value'][BLUE_START:BLUE_END])
    db['subject'][i]['analysis']['gyro_activity_amount']['value'][PAUSE3_START:PAUSE3_END] = \
        np.sum(db['subject'][i]['signal']['gyro_mag']['value'][PAUSE3_START:PAUSE3_END])
    db['subject'][i]['analysis']['gyro_activity_amount']['value'][PINK_START:PINK_END] = \
        np.sum(db['subject'][i]['signal']['gyro_mag']['value'][PINK_START:PINK_END])
    db['subject'][i]['analysis']['gyro_activity_amount']['value'][PAUSE4_START:PAUSE4_END] = \
        np.sum(db['subject'][i]['signal']['gyro_mag']['value'][PAUSE4_START:PAUSE4_END])

# add gyro_total_amount
for i in db['subject'].keys():
    db['subject'][i]['analysis']['gyro_total_amount']['value'][:] = \
        np.sum(np.ma.masked_invalid(db['subject'][i]['signal']['gyro_mag']['value']))

# add hr_activity_correlation
for i in range(4):
    db['subject'][list(db['subject'].keys())[i]]['analysis']['hr_activity_correlation']['value'][
    PAUSE1_START:PAUSE1_END], _ = \
        pearsonr(db['subject'][list(db['subject'].keys())[i]]['signal']['hr_smooth']['value'][PAUSE1_START:PAUSE1_END], \
                 db['subject'][list(db['subject'].keys())[i + 4]]['signal']['hr_smooth']['value'][
                 PAUSE1_START:PAUSE1_END])
    db['subject'][list(db['subject'].keys())[i]]['analysis']['hr_activity_correlation']['value'][RED_START:RED_END], _ = \
        pearsonr(db['subject'][list(db['subject'].keys())[i]]['signal']['hr_smooth']['value'][RED_START:RED_END], \
                 db['subject'][list(db['subject'].keys())[i + 4]]['signal']['hr_smooth']['value'][RED_START:RED_END])
    db['subject'][list(db['subject'].keys())[i]]['analysis']['hr_activity_correlation']['value'][
    PAUSE2_START:PAUSE2_END], _ = \
        pearsonr(db['subject'][list(db['subject'].keys())[i]]['signal']['hr_smooth']['value'][PAUSE2_START:PAUSE2_END], \
                 db['subject'][list(db['subject'].keys())[i + 4]]['signal']['hr_smooth']['value'][
                 PAUSE2_START:PAUSE2_END])
    db['subject'][list(db['subject'].keys())[i]]['analysis']['hr_activity_correlation']['value'][
    BLUE_START:BLUE_END], _ = \
        pearsonr(db['subject'][list(db['subject'].keys())[i]]['signal']['hr_smooth']['value'][BLUE_START:BLUE_END], \
                 db['subject'][list(db['subject'].keys())[i + 4]]['signal']['hr_smooth']['value'][BLUE_START:BLUE_END])
    db['subject'][list(db['subject'].keys())[i]]['analysis']['hr_activity_correlation']['value'][
    PAUSE3_START:PAUSE3_END], _ = \
        pearsonr(db['subject'][list(db['subject'].keys())[i]]['signal']['hr_smooth']['value'][PAUSE3_START:PAUSE3_END], \
                 db['subject'][list(db['subject'].keys())[i + 4]]['signal']['hr_smooth']['value'][
                 PAUSE3_START:PAUSE3_END])
    db['subject'][list(db['subject'].keys())[i]]['analysis']['hr_activity_correlation']['value'][
    PAUSE3_START:PAUSE3_END], _ = \
        pearsonr(db['subject'][list(db['subject'].keys())[i]]['signal']['hr_smooth']['value'][PAUSE3_START:PAUSE3_END], \
                 db['subject'][list(db['subject'].keys())[i + 4]]['signal']['hr_smooth']['value'][
                 PAUSE3_START:PAUSE3_END])
    db['subject'][list(db['subject'].keys())[i]]['analysis']['hr_activity_correlation']['value'][
    PINK_START:PINK_END], _ = \
        pearsonr(db['subject'][list(db['subject'].keys())[i]]['signal']['hr_smooth']['value'][PINK_START:PINK_END], \
                 db['subject'][list(db['subject'].keys())[i + 4]]['signal']['hr_smooth']['value'][PINK_START:PINK_END])
    db['subject'][list(db['subject'].keys())[i]]['analysis']['hr_activity_correlation']['value'][
    PINK_START:PINK_END], _ = \
        pearsonr(db['subject'][list(db['subject'].keys())[i]]['signal']['hr_smooth']['value'][PAUSE4_START:PAUSE4_END], \
                 db['subject'][list(db['subject'].keys())[i + 4]]['signal']['hr_smooth']['value'][
                 PAUSE4_START:PAUSE4_END])

# add hr_total_correlation
for i in range(4):
    db['subject'][list(db['subject'].keys())[i]]['analysis']['hr_total_correlation']['value'][:], _ = \
        db['subject'][list(db['subject'].keys())[i + 4]]['analysis']['hr_total_correlation']['value'][:], _ = \
        pearsonr(db['subject'][list(db['subject'].keys())[i]]['signal']['hr_smooth']['value'], \
                 db['subject'][list(db['subject'].keys())[i + 4]]['signal']['hr_smooth']['value'])

# add temp_hand_activity_correlation
for i in range(4):
    db['subject'][list(db['subject'].keys())[i]]['analysis']['temp_hand_activity_correlation']['value'][
    PAUSE1_START:PAUSE1_END], _ = \
        pearsonr(db['subject'][list(db['subject'].keys())[i]]['record']['temp_hand']['value'][PAUSE1_START:PAUSE1_END], \
                 db['subject'][list(db['subject'].keys())[i + 4]]['record']['temp_hand']['value'][
                 PAUSE1_START:PAUSE1_END])
    db['subject'][list(db['subject'].keys())[i]]['analysis']['temp_hand_activity_correlation']['value'][
    RED_START:RED_END], _ = \
        pearsonr(db['subject'][list(db['subject'].keys())[i]]['record']['temp_hand']['value'][RED_START:RED_END], \
                 db['subject'][list(db['subject'].keys())[i + 4]]['record']['temp_hand']['value'][RED_START:RED_END])
    db['subject'][list(db['subject'].keys())[i]]['analysis']['temp_hand_activity_correlation']['value'][
    PAUSE2_START:PAUSE2_END], _ = \
        pearsonr(db['subject'][list(db['subject'].keys())[i]]['record']['temp_hand']['value'][PAUSE2_START:PAUSE2_END], \
                 db['subject'][list(db['subject'].keys())[i + 4]]['record']['temp_hand']['value'][
                 PAUSE2_START:PAUSE2_END])
    db['subject'][list(db['subject'].keys())[i]]['analysis']['temp_hand_activity_correlation']['value'][
    BLUE_START:BLUE_END], _ = \
        pearsonr(db['subject'][list(db['subject'].keys())[i]]['record']['temp_hand']['value'][BLUE_START:BLUE_END], \
                 db['subject'][list(db['subject'].keys())[i + 4]]['record']['temp_hand']['value'][BLUE_START:BLUE_END])
    db['subject'][list(db['subject'].keys())[i]]['analysis']['temp_hand_activity_correlation']['value'][
    PAUSE3_START:PAUSE3_END], _ = \
        pearsonr(db['subject'][list(db['subject'].keys())[i]]['record']['temp_hand']['value'][PAUSE3_START:PAUSE3_END], \
                 db['subject'][list(db['subject'].keys())[i + 4]]['record']['temp_hand']['value'][
                 PAUSE3_START:PAUSE3_END])
    db['subject'][list(db['subject'].keys())[i]]['analysis']['temp_hand_activity_correlation']['value'][
    PAUSE3_START:PAUSE3_END], _ = \
        pearsonr(db['subject'][list(db['subject'].keys())[i]]['record']['temp_hand']['value'][PAUSE3_START:PAUSE3_END], \
                 db['subject'][list(db['subject'].keys())[i + 4]]['record']['temp_hand']['value'][
                 PAUSE3_START:PAUSE3_END])
    db['subject'][list(db['subject'].keys())[i]]['analysis']['temp_hand_activity_correlation']['value'][
    PINK_START:PINK_END], _ = \
        pearsonr(db['subject'][list(db['subject'].keys())[i]]['record']['temp_hand']['value'][PINK_START:PINK_END], \
                 db['subject'][list(db['subject'].keys())[i + 4]]['record']['temp_hand']['value'][PINK_START:PINK_END])
    db['subject'][list(db['subject'].keys())[i]]['analysis']['temp_hand_activity_correlation']['value'][
    PINK_START:PINK_END], _ = \
        pearsonr(db['subject'][list(db['subject'].keys())[i]]['record']['temp_hand']['value'][PAUSE4_START:PAUSE4_END], \
                 db['subject'][list(db['subject'].keys())[i + 4]]['record']['temp_hand']['value'][
                 PAUSE4_START:PAUSE4_END])

# add temp_hand_total_correlation
for i in range(4):
    db['subject'][list(db['subject'].keys())[i]]['analysis']['temp_hand_total_correlation']['value'][:], _ = \
        db['subject'][list(db['subject'].keys())[i + 4]]['analysis']['temp_hand_total_correlation']['value'][:], _ = \
        pearsonr(db['subject'][list(db['subject'].keys())[i]]['record']['temp_hand']['value'], \
                 db['subject'][list(db['subject'].keys())[i + 4]]['record']['temp_hand']['value'])

# add temp_head_activity_correlation
for i in range(4):
    db['subject'][list(db['subject'].keys())[i]]['analysis']['temp_head_activity_correlation']['value'][
    PAUSE1_START:PAUSE1_END], _ = \
        pearsonr(db['subject'][list(db['subject'].keys())[i]]['record']['temp_head']['value'][PAUSE1_START:PAUSE1_END], \
                 db['subject'][list(db['subject'].keys())[i + 4]]['record']['temp_head']['value'][
                 PAUSE1_START:PAUSE1_END])
    db['subject'][list(db['subject'].keys())[i]]['analysis']['temp_head_activity_correlation']['value'][
    RED_START:RED_END], _ = \
        pearsonr(db['subject'][list(db['subject'].keys())[i]]['record']['temp_head']['value'][RED_START:RED_END], \
                 db['subject'][list(db['subject'].keys())[i + 4]]['record']['temp_head']['value'][RED_START:RED_END])
    db['subject'][list(db['subject'].keys())[i]]['analysis']['temp_head_activity_correlation']['value'][
    PAUSE2_START:PAUSE2_END], _ = \
        pearsonr(db['subject'][list(db['subject'].keys())[i]]['record']['temp_head']['value'][PAUSE2_START:PAUSE2_END], \
                 db['subject'][list(db['subject'].keys())[i + 4]]['record']['temp_head']['value'][
                 PAUSE2_START:PAUSE2_END])
    db['subject'][list(db['subject'].keys())[i]]['analysis']['temp_head_activity_correlation']['value'][
    BLUE_START:BLUE_END], _ = \
        pearsonr(db['subject'][list(db['subject'].keys())[i]]['record']['temp_head']['value'][BLUE_START:BLUE_END], \
                 db['subject'][list(db['subject'].keys())[i + 4]]['record']['temp_head']['value'][BLUE_START:BLUE_END])
    db['subject'][list(db['subject'].keys())[i]]['analysis']['temp_head_activity_correlation']['value'][
    PAUSE3_START:PAUSE3_END], _ = \
        pearsonr(db['subject'][list(db['subject'].keys())[i]]['record']['temp_head']['value'][PAUSE3_START:PAUSE3_END], \
                 db['subject'][list(db['subject'].keys())[i + 4]]['record']['temp_head']['value'][
                 PAUSE3_START:PAUSE3_END])
    db['subject'][list(db['subject'].keys())[i]]['analysis']['temp_head_activity_correlation']['value'][
    PAUSE3_START:PAUSE3_END], _ = \
        pearsonr(db['subject'][list(db['subject'].keys())[i]]['record']['temp_head']['value'][PAUSE3_START:PAUSE3_END], \
                 db['subject'][list(db['subject'].keys())[i + 4]]['record']['temp_head']['value'][
                 PAUSE3_START:PAUSE3_END])
    db['subject'][list(db['subject'].keys())[i]]['analysis']['temp_head_activity_correlation']['value'][
    PINK_START:PINK_END], _ = \
        pearsonr(db['subject'][list(db['subject'].keys())[i]]['record']['temp_head']['value'][PINK_START:PINK_END], \
                 db['subject'][list(db['subject'].keys())[i + 4]]['record']['temp_head']['value'][PINK_START:PINK_END])
    db['subject'][list(db['subject'].keys())[i]]['analysis']['temp_head_activity_correlation']['value'][
    PINK_START:PINK_END], _ = \
        pearsonr(db['subject'][list(db['subject'].keys())[i]]['record']['temp_head']['value'][PAUSE4_START:PAUSE4_END], \
                 db['subject'][list(db['subject'].keys())[i + 4]]['record']['temp_head']['value'][
                 PAUSE4_START:PAUSE4_END])

# add temp_head_total_correlation
for i in range(4):
    db['subject'][list(db['subject'].keys())[i]]['analysis']['temp_head_total_correlation']['value'][:], _ = \
        db['subject'][list(db['subject'].keys())[i + 4]]['analysis']['temp_head_total_correlation']['value'][:], _ = \
        pearsonr(db['subject'][list(db['subject'].keys())[i]]['record']['temp_head']['value'], \
                 db['subject'][list(db['subject'].keys())[i + 4]]['record']['temp_head']['value'])

# add temp_ear_activity_correlation
for i in range(4):
    db['subject'][list(db['subject'].keys())[i]]['analysis']['temp_ear_activity_correlation']['value'][
    PAUSE1_START:PAUSE1_END], _ = \
        pearsonr(db['subject'][list(db['subject'].keys())[i]]['record']['temp_ear']['value'][PAUSE1_START:PAUSE1_END], \
                 db['subject'][list(db['subject'].keys())[i + 4]]['record']['temp_ear']['value'][
                 PAUSE1_START:PAUSE1_END])
    db['subject'][list(db['subject'].keys())[i]]['analysis']['temp_ear_activity_correlation']['value'][
    RED_START:RED_END], _ = \
        pearsonr(db['subject'][list(db['subject'].keys())[i]]['record']['temp_ear']['value'][RED_START:RED_END], \
                 db['subject'][list(db['subject'].keys())[i + 4]]['record']['temp_ear']['value'][RED_START:RED_END])
    db['subject'][list(db['subject'].keys())[i]]['analysis']['temp_ear_activity_correlation']['value'][
    PAUSE2_START:PAUSE2_END], _ = \
        pearsonr(db['subject'][list(db['subject'].keys())[i]]['record']['temp_ear']['value'][PAUSE2_START:PAUSE2_END], \
                 db['subject'][list(db['subject'].keys())[i + 4]]['record']['temp_ear']['value'][
                 PAUSE2_START:PAUSE2_END])
    db['subject'][list(db['subject'].keys())[i]]['analysis']['temp_ear_activity_correlation']['value'][
    BLUE_START:BLUE_END], _ = \
        pearsonr(db['subject'][list(db['subject'].keys())[i]]['record']['temp_ear']['value'][BLUE_START:BLUE_END], \
                 db['subject'][list(db['subject'].keys())[i + 4]]['record']['temp_ear']['value'][BLUE_START:BLUE_END])
    db['subject'][list(db['subject'].keys())[i]]['analysis']['temp_ear_activity_correlation']['value'][
    PAUSE3_START:PAUSE3_END], _ = \
        pearsonr(db['subject'][list(db['subject'].keys())[i]]['record']['temp_ear']['value'][PAUSE3_START:PAUSE3_END], \
                 db['subject'][list(db['subject'].keys())[i + 4]]['record']['temp_ear']['value'][
                 PAUSE3_START:PAUSE3_END])
    db['subject'][list(db['subject'].keys())[i]]['analysis']['temp_ear_activity_correlation']['value'][
    PAUSE3_START:PAUSE3_END], _ = \
        pearsonr(db['subject'][list(db['subject'].keys())[i]]['record']['temp_ear']['value'][PAUSE3_START:PAUSE3_END], \
                 db['subject'][list(db['subject'].keys())[i + 4]]['record']['temp_ear']['value'][
                 PAUSE3_START:PAUSE3_END])
    db['subject'][list(db['subject'].keys())[i]]['analysis']['temp_ear_activity_correlation']['value'][
    PINK_START:PINK_END], _ = \
        pearsonr(db['subject'][list(db['subject'].keys())[i]]['record']['temp_ear']['value'][PINK_START:PINK_END], \
                 db['subject'][list(db['subject'].keys())[i + 4]]['record']['temp_ear']['value'][PINK_START:PINK_END])
    db['subject'][list(db['subject'].keys())[i]]['analysis']['temp_ear_activity_correlation']['value'][
    PINK_START:PINK_END], _ = \
        pearsonr(db['subject'][list(db['subject'].keys())[i]]['record']['temp_ear']['value'][PAUSE4_START:PAUSE4_END], \
                 db['subject'][list(db['subject'].keys())[i + 4]]['record']['temp_ear']['value'][
                 PAUSE4_START:PAUSE4_END])

# add temp_ear_total_correlation
for i in range(4):
    db['subject'][list(db['subject'].keys())[i]]['analysis']['temp_ear_total_correlation']['value'][:], _ = \
        db['subject'][list(db['subject'].keys())[i + 4]]['analysis']['temp_ear_total_correlation']['value'][:], _ = \
        pearsonr(db['subject'][list(db['subject'].keys())[i]]['record']['temp_ear']['value'], \
                 db['subject'][list(db['subject'].keys())[i + 4]]['record']['temp_ear']['value'])

# add eeg_af7_alpha_activity_energy
for i in db['subject'].keys():
    db['subject'][i]['analysis']['eeg_af7_alpha_activity_energy']['value'][PAUSE1_START:PAUSE1_END] = \
        alpha_power(db['subject'][i]['record']['eeg_af7']['value'][PAUSE1_START:PAUSE1_END])
    db['subject'][i]['analysis']['eeg_af7_alpha_activity_energy']['value'][RED_START:RED_END] = \
        alpha_power(db['subject'][i]['record']['eeg_af7']['value'][RED_START:RED_END])
    db['subject'][i]['analysis']['eeg_af7_alpha_activity_energy']['value'][PAUSE2_START:PAUSE2_END] = \
        alpha_power(db['subject'][i]['record']['eeg_af7']['value'][PAUSE2_START:PAUSE2_END])
    db['subject'][i]['analysis']['eeg_af7_alpha_activity_energy']['value'][BLUE_START:BLUE_END] = \
        alpha_power(db['subject'][i]['record']['eeg_af7']['value'][BLUE_START:BLUE_END])
    db['subject'][i]['analysis']['eeg_af7_alpha_activity_energy']['value'][PAUSE3_START:PAUSE3_END] = \
        alpha_power(db['subject'][i]['record']['eeg_af7']['value'][PAUSE3_START:PAUSE3_END])
    db['subject'][i]['analysis']['eeg_af7_alpha_activity_energy']['value'][PINK_START:PINK_END] = \
        alpha_power(db['subject'][i]['record']['eeg_af7']['value'][PINK_START:PINK_END])
    db['subject'][i]['analysis']['eeg_af7_alpha_activity_energy']['value'][PAUSE4_START:PAUSE4_END] = \
        alpha_power(db['subject'][i]['record']['eeg_af7']['value'][PAUSE4_START:PAUSE4_END])

# add eeg_af8_alpha_activity_energy
for i in db['subject'].keys():
    db['subject'][i]['analysis']['eeg_af8_alpha_activity_energy']['value'][PAUSE1_START:PAUSE1_END] = \
        alpha_power(db['subject'][i]['record']['eeg_af8']['value'][PAUSE1_START:PAUSE1_END])
    db['subject'][i]['analysis']['eeg_af8_alpha_activity_energy']['value'][RED_START:RED_END] = \
        alpha_power(db['subject'][i]['record']['eeg_af8']['value'][RED_START:RED_END])
    db['subject'][i]['analysis']['eeg_af8_alpha_activity_energy']['value'][PAUSE2_START:PAUSE2_END] = \
        alpha_power(db['subject'][i]['record']['eeg_af8']['value'][PAUSE2_START:PAUSE2_END])
    db['subject'][i]['analysis']['eeg_af8_alpha_activity_energy']['value'][BLUE_START:BLUE_END] = \
        alpha_power(db['subject'][i]['record']['eeg_af8']['value'][BLUE_START:BLUE_END])
    db['subject'][i]['analysis']['eeg_af8_alpha_activity_energy']['value'][PAUSE3_START:PAUSE3_END] = \
        alpha_power(db['subject'][i]['record']['eeg_af8']['value'][PAUSE3_START:PAUSE3_END])
    db['subject'][i]['analysis']['eeg_af8_alpha_activity_energy']['value'][PINK_START:PINK_END] = \
        alpha_power(db['subject'][i]['record']['eeg_af8']['value'][PINK_START:PINK_END])
    db['subject'][i]['analysis']['eeg_af8_alpha_activity_energy']['value'][PAUSE4_START:PAUSE4_END] = \
        alpha_power(db['subject'][i]['record']['eeg_af8']['value'][PAUSE4_START:PAUSE4_END])

# add eeg_tp9_alpha_activity_energy
for i in db['subject'].keys():
    db['subject'][i]['analysis']['eeg_tp9_alpha_activity_energy']['value'][PAUSE1_START:PAUSE1_END] = \
        alpha_power(db['subject'][i]['record']['eeg_tp9']['value'][PAUSE1_START:PAUSE1_END])
    db['subject'][i]['analysis']['eeg_tp9_alpha_activity_energy']['value'][RED_START:RED_END] = \
        alpha_power(db['subject'][i]['record']['eeg_tp9']['value'][RED_START:RED_END])
    db['subject'][i]['analysis']['eeg_tp9_alpha_activity_energy']['value'][PAUSE2_START:PAUSE2_END] = \
        alpha_power(db['subject'][i]['record']['eeg_tp9']['value'][PAUSE2_START:PAUSE2_END])
    db['subject'][i]['analysis']['eeg_tp9_alpha_activity_energy']['value'][BLUE_START:BLUE_END] = \
        alpha_power(db['subject'][i]['record']['eeg_tp9']['value'][BLUE_START:BLUE_END])
    db['subject'][i]['analysis']['eeg_tp9_alpha_activity_energy']['value'][PAUSE3_START:PAUSE3_END] = \
        alpha_power(db['subject'][i]['record']['eeg_tp9']['value'][PAUSE3_START:PAUSE3_END])
    db['subject'][i]['analysis']['eeg_tp9_alpha_activity_energy']['value'][PINK_START:PINK_END] = \
        alpha_power(db['subject'][i]['record']['eeg_tp9']['value'][PINK_START:PINK_END])
    db['subject'][i]['analysis']['eeg_tp9_alpha_activity_energy']['value'][PAUSE4_START:PAUSE4_END] = \
        alpha_power(db['subject'][i]['record']['eeg_tp9']['value'][PAUSE4_START:PAUSE4_END])

# add eeg_tp10_alpha_activity_energy
for i in db['subject'].keys():
    db['subject'][i]['analysis']['eeg_tp10_alpha_activity_energy']['value'][PAUSE1_START:PAUSE1_END] = \
        alpha_power(db['subject'][i]['record']['eeg_tp10']['value'][PAUSE1_START:PAUSE1_END])
    db['subject'][i]['analysis']['eeg_tp10_alpha_activity_energy']['value'][RED_START:RED_END] = \
        alpha_power(db['subject'][i]['record']['eeg_tp10']['value'][RED_START:RED_END])
    db['subject'][i]['analysis']['eeg_tp10_alpha_activity_energy']['value'][PAUSE2_START:PAUSE2_END] = \
        alpha_power(db['subject'][i]['record']['eeg_tp10']['value'][PAUSE2_START:PAUSE2_END])
    db['subject'][i]['analysis']['eeg_tp10_alpha_activity_energy']['value'][BLUE_START:BLUE_END] = \
        alpha_power(db['subject'][i]['record']['eeg_tp10']['value'][BLUE_START:BLUE_END])
    db['subject'][i]['analysis']['eeg_tp10_alpha_activity_energy']['value'][PAUSE3_START:PAUSE3_END] = \
        alpha_power(db['subject'][i]['record']['eeg_tp10']['value'][PAUSE3_START:PAUSE3_END])
    db['subject'][i]['analysis']['eeg_tp10_alpha_activity_energy']['value'][PINK_START:PINK_END] = \
        alpha_power(db['subject'][i]['record']['eeg_tp10']['value'][PINK_START:PINK_END])
    db['subject'][i]['analysis']['eeg_tp10_alpha_activity_energy']['value'][PAUSE4_START:PAUSE4_END] = \
        alpha_power(db['subject'][i]['record']['eeg_tp10']['value'][PAUSE4_START:PAUSE4_END])

# add eeg_af7_alpha_total_energy
for i in db['subject'].keys():
    db['subject'][i]['analysis']['eeg_af7_alpha_total_energy']['value'][:] = \
        alpha_power(db['subject'][i]['record']['eeg_af7']['value'][:])

# add eeg_af8_alpha_total_energy
for i in db['subject'].keys():
    db['subject'][i]['analysis']['eeg_af8_alpha_total_energy']['value'][:] = \
        alpha_power(db['subject'][i]['record']['eeg_af8']['value'][:])

# add eeg_tp9_alpha_total_energy
for i in db['subject'].keys():
    db['subject'][i]['analysis']['eeg_tp9_alpha_total_energy']['value'][:] = \
        alpha_power(db['subject'][i]['record']['eeg_tp9']['value'][:])

# add eeg_tp10_alpha_total_energy
for i in db['subject'].keys():
    db['subject'][i]['analysis']['eeg_tp10_alpha_total_energy']['value'][:] = \
        alpha_power(db['subject'][i]['record']['eeg_tp10']['value'][:])

# add eeg_af7_beta_activity_energy
for i in db['subject'].keys():
    db['subject'][i]['analysis']['eeg_af7_beta_activity_energy']['value'][PAUSE1_START:PAUSE1_END] = \
        beta_power(db['subject'][i]['record']['eeg_af7']['value'][PAUSE1_START:PAUSE1_END])
    db['subject'][i]['analysis']['eeg_af7_beta_activity_energy']['value'][RED_START:RED_END] = \
        beta_power(db['subject'][i]['record']['eeg_af7']['value'][RED_START:RED_END])
    db['subject'][i]['analysis']['eeg_af7_beta_activity_energy']['value'][PAUSE2_START:PAUSE2_END] = \
        beta_power(db['subject'][i]['record']['eeg_af7']['value'][PAUSE2_START:PAUSE2_END])
    db['subject'][i]['analysis']['eeg_af7_beta_activity_energy']['value'][BLUE_START:BLUE_END] = \
        beta_power(db['subject'][i]['record']['eeg_af7']['value'][BLUE_START:BLUE_END])
    db['subject'][i]['analysis']['eeg_af7_beta_activity_energy']['value'][PAUSE3_START:PAUSE3_END] = \
        beta_power(db['subject'][i]['record']['eeg_af7']['value'][PAUSE3_START:PAUSE3_END])
    db['subject'][i]['analysis']['eeg_af7_beta_activity_energy']['value'][PINK_START:PINK_END] = \
        beta_power(db['subject'][i]['record']['eeg_af7']['value'][PINK_START:PINK_END])
    db['subject'][i]['analysis']['eeg_af7_beta_activity_energy']['value'][PAUSE4_START:PAUSE4_END] = \
        beta_power(db['subject'][i]['record']['eeg_af7']['value'][PAUSE4_START:PAUSE4_END])

# add eeg_af8_beta_activity_energy
for i in db['subject'].keys():
    db['subject'][i]['analysis']['eeg_af8_beta_activity_energy']['value'][PAUSE1_START:PAUSE1_END] = \
        beta_power(db['subject'][i]['record']['eeg_af8']['value'][PAUSE1_START:PAUSE1_END])
    db['subject'][i]['analysis']['eeg_af8_beta_activity_energy']['value'][RED_START:RED_END] = \
        beta_power(db['subject'][i]['record']['eeg_af8']['value'][RED_START:RED_END])
    db['subject'][i]['analysis']['eeg_af8_beta_activity_energy']['value'][PAUSE2_START:PAUSE2_END] = \
        beta_power(db['subject'][i]['record']['eeg_af8']['value'][PAUSE2_START:PAUSE2_END])
    db['subject'][i]['analysis']['eeg_af8_beta_activity_energy']['value'][BLUE_START:BLUE_END] = \
        beta_power(db['subject'][i]['record']['eeg_af8']['value'][BLUE_START:BLUE_END])
    db['subject'][i]['analysis']['eeg_af8_beta_activity_energy']['value'][PAUSE3_START:PAUSE3_END] = \
        beta_power(db['subject'][i]['record']['eeg_af8']['value'][PAUSE3_START:PAUSE3_END])
    db['subject'][i]['analysis']['eeg_af8_beta_activity_energy']['value'][PINK_START:PINK_END] = \
        beta_power(db['subject'][i]['record']['eeg_af8']['value'][PINK_START:PINK_END])
    db['subject'][i]['analysis']['eeg_af8_beta_activity_energy']['value'][PAUSE4_START:PAUSE4_END] = \
        beta_power(db['subject'][i]['record']['eeg_af8']['value'][PAUSE4_START:PAUSE4_END])

# add eeg_tp9_beta_activity_energy
for i in db['subject'].keys():
    db['subject'][i]['analysis']['eeg_tp9_beta_activity_energy']['value'][PAUSE1_START:PAUSE1_END] = \
        beta_power(db['subject'][i]['record']['eeg_tp9']['value'][PAUSE1_START:PAUSE1_END])
    db['subject'][i]['analysis']['eeg_tp9_beta_activity_energy']['value'][RED_START:RED_END] = \
        beta_power(db['subject'][i]['record']['eeg_tp9']['value'][RED_START:RED_END])
    db['subject'][i]['analysis']['eeg_tp9_beta_activity_energy']['value'][PAUSE2_START:PAUSE2_END] = \
        beta_power(db['subject'][i]['record']['eeg_tp9']['value'][PAUSE2_START:PAUSE2_END])
    db['subject'][i]['analysis']['eeg_tp9_beta_activity_energy']['value'][BLUE_START:BLUE_END] = \
        beta_power(db['subject'][i]['record']['eeg_tp9']['value'][BLUE_START:BLUE_END])
    db['subject'][i]['analysis']['eeg_tp9_beta_activity_energy']['value'][PAUSE3_START:PAUSE3_END] = \
        beta_power(db['subject'][i]['record']['eeg_tp9']['value'][PAUSE3_START:PAUSE3_END])
    db['subject'][i]['analysis']['eeg_tp9_beta_activity_energy']['value'][PINK_START:PINK_END] = \
        beta_power(db['subject'][i]['record']['eeg_tp9']['value'][PINK_START:PINK_END])
    db['subject'][i]['analysis']['eeg_tp9_beta_activity_energy']['value'][PAUSE4_START:PAUSE4_END] = \
        beta_power(db['subject'][i]['record']['eeg_tp9']['value'][PAUSE4_START:PAUSE4_END])

# add eeg_tp10_beta_activity_energy
for i in db['subject'].keys():
    db['subject'][i]['analysis']['eeg_tp10_beta_activity_energy']['value'][PAUSE1_START:PAUSE1_END] = \
        beta_power(db['subject'][i]['record']['eeg_tp10']['value'][PAUSE1_START:PAUSE1_END])
    db['subject'][i]['analysis']['eeg_tp10_beta_activity_energy']['value'][RED_START:RED_END] = \
        beta_power(db['subject'][i]['record']['eeg_tp10']['value'][RED_START:RED_END])
    db['subject'][i]['analysis']['eeg_tp10_beta_activity_energy']['value'][PAUSE2_START:PAUSE2_END] = \
        beta_power(db['subject'][i]['record']['eeg_tp10']['value'][PAUSE2_START:PAUSE2_END])
    db['subject'][i]['analysis']['eeg_tp10_beta_activity_energy']['value'][BLUE_START:BLUE_END] = \
        beta_power(db['subject'][i]['record']['eeg_tp10']['value'][BLUE_START:BLUE_END])
    db['subject'][i]['analysis']['eeg_tp10_beta_activity_energy']['value'][PAUSE3_START:PAUSE3_END] = \
        beta_power(db['subject'][i]['record']['eeg_tp10']['value'][PAUSE3_START:PAUSE3_END])
    db['subject'][i]['analysis']['eeg_tp10_beta_activity_energy']['value'][PINK_START:PINK_END] = \
        beta_power(db['subject'][i]['record']['eeg_tp10']['value'][PINK_START:PINK_END])
    db['subject'][i]['analysis']['eeg_tp10_beta_activity_energy']['value'][PAUSE4_START:PAUSE4_END] = \
        beta_power(db['subject'][i]['record']['eeg_tp10']['value'][PAUSE4_START:PAUSE4_END])

# add eeg_af7_beta_total_energy
for i in db['subject'].keys():
    db['subject'][i]['analysis']['eeg_af7_beta_total_energy']['value'][:] = \
        beta_power(db['subject'][i]['record']['eeg_af7']['value'][:])

# add eeg_af8_beta_total_energy
for i in db['subject'].keys():
    db['subject'][i]['analysis']['eeg_af8_beta_total_energy']['value'][:] = \
        beta_power(db['subject'][i]['record']['eeg_af8']['value'][:])

# add eeg_tp9_beta_total_energy
for i in db['subject'].keys():
    db['subject'][i]['analysis']['eeg_tp9_beta_total_energy']['value'][:] = \
        beta_power(db['subject'][i]['record']['eeg_tp9']['value'][:])

# add eeg_tp10_beta_total_energy
for i in db['subject'].keys():
    db['subject'][i]['analysis']['eeg_tp10_beta_total_energy']['value'][:] = \
        beta_power(db['subject'][i]['record']['eeg_tp10']['value'][:])

# save database on local drive
with open('db.pickle', 'wb') as handle:
    pickle.dump(db, handle)