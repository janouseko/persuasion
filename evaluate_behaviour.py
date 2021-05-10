# -------------------------------------------------------------------
# evaluate behaviour quantifiers and add it into working database
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
    db['subject'][i]['behaviour'] = {}
    db['subject'][i]['behaviour']['state'] = {}
    db['subject'][i]['behaviour']['state']['value'] = np.empty([EXPERIMENT_LENGTH],dtype="S8")
    db['subject'][i]['behaviour']['performative_capacity_selfevaluation'] = {}
    db['subject'][i]['behaviour']['performative_capacity_selfevaluation']['value'] = np.empty([EXPERIMENT_LENGTH],
                                                                                              dtype="int")
    db['subject'][i]['behaviour']['performation_quality_selfevaluation'] = {}
    db['subject'][i]['behaviour']['performation_quality_selfevaluation']['value'] = np.empty([EXPERIMENT_LENGTH],
                                                                                              dtype="int")
    db['subject'][i]['behaviour']['performation_persuasion_selfevaluation'] = {}
    db['subject'][i]['behaviour']['performation_persuasion_selfevaluation']['value'] = np.empty([EXPERIMENT_LENGTH],
                                                                                             dtype="bool")
    db['subject'][i]['behaviour']['most_persuasion_segment_selfevaluation'] = {}
    db['subject'][i]['behaviour']['most_persuasion_segment_selfevaluation']['value'] = np.zeros([EXPERIMENT_LENGTH],
                                                                                             dtype="int")
    db['subject'][i]['behaviour']['less_persuasion_segment_selfevaluation'] = {}
    db['subject'][i]['behaviour']['less_persuasion_segment_selfevaluation']['value'] = np.zeros([EXPERIMENT_LENGTH],
                                                                                             dtype="int")
    db['subject'][i]['behaviour']['hardest_segment'] = {}
    db['subject'][i]['behaviour']['hardest_segment']['value'] = np.zeros([EXPERIMENT_LENGTH],
                                                                                             dtype="int")
    db['subject'][i]['behaviour']['easiest_segment'] = {}
    db['subject'][i]['behaviour']['easiest_segment']['value'] = np.zeros([EXPERIMENT_LENGTH],
                                                                                             dtype="int")
    db['subject'][i]['behaviour']['pleasant_segment'] = {}
    db['subject'][i]['behaviour']['pleasant_segment']['value'] = np.zeros([EXPERIMENT_LENGTH],
                                                                                             dtype="int")
    db['subject'][i]['behaviour']['unpleasant_segment'] = {}
    db['subject'][i]['behaviour']['unpleasant_segment']['value'] = np.zeros([EXPERIMENT_LENGTH],
                                                                                             dtype="int")
    db['subject'][i]['behaviour']['is_pause_performation_dialoque'] = {}
    db['subject'][i]['behaviour']['is_pause_performation_dialoque']['value'] = np.zeros([EXPERIMENT_LENGTH],
                                                                                             dtype="bool")
    db['subject'][i]['behaviour']['is_recipient_feedback'] = {}
    db['subject'][i]['behaviour']['is_recipient_feedback']['value'] = np.zeros([EXPERIMENT_LENGTH],
                                                                                        dtype="bool")
    db['subject'][i]['behaviour']['is_recipient_respiratory_feedback'] = {}
    db['subject'][i]['behaviour']['is_recipient_respiratory_feedback']['value'] = np.zeros([EXPERIMENT_LENGTH],
                                                                                        dtype="bool")
    db['subject'][i]['behaviour']['is_recipient_eyecontact'] = {}
    db['subject'][i]['behaviour']['is_recipient_eyecontact']['value'] = np.zeros([EXPERIMENT_LENGTH],
                                                                                           dtype="bool")
    db['subject'][i]['behaviour']['is_performer_respiratory'] = {}
    db['subject'][i]['behaviour']['is_performer_respiratory']['value'] = np.zeros([EXPERIMENT_LENGTH],
                                                                                           dtype="bool")
    db['subject'][i]['behaviour']['device_disturbing'] = {}
    db['subject'][i]['behaviour']['device_disturbing']['value'] = np.zeros([EXPERIMENT_LENGTH],
                                                                                           dtype="bool")
    db['subject'][i]['behaviour']['recipient_feedback_form'] = {}
    db['subject'][i]['behaviour']['recipient_feedback_form']['value'] = ''
    db['subject'][i]['behaviour']['pause_performation_form'] = {}
    db['subject'][i]['behaviour']['pause_performation_form']['value'] = ''
    db['subject'][i]['behaviour']['respiratory_feedback_reasoning'] = {}
    db['subject'][i]['behaviour']['respiratory_feedback_reasoning']['value'] = ''
    db['subject'][i]['behaviour']['eye_contact_reasoning'] = {}
    db['subject'][i]['behaviour']['eye_contact_reasoning']['value'] = ''
    db['subject'][i]['behaviour']['persuasion_segment_selfevaluation_reasoning'] = {}
    db['subject'][i]['behaviour']['persuasion_segment_selfevaluation_reasoning']['value'] = ''

# add state ( < 10% arousal = active performer)
for i in db['subject'].keys():
    if 'P' in db['subject'][i]['record']['id']:
        for g in range(len(db['subject'][i]['record']['arousal']['value'])):
            if db['subject'][i]['record']['arousal']['value'][g]>10:
                db['subject'][i]['behaviour']['state']['value'][g] = 'active'
            else:
                db['subject'][i]['behaviour']['state']['value'][g] = 'passive'
    elif 'R' in db['subject'][i]['record']['id']:
        for g in range(len(db['subject'][i]['record']['arousal']['value'])):
            db['subject'][i]['behaviour']['state']['value'][g] = 'ready'

# add performative capacity selfevaluation
for g in range(len(db['subject']['P1']['record']['arousal']['value'])):
    db['subject']['P1']['behaviour']['performative_capacity_selfevaluation']['value'][g] = '8'
    db['subject']['P2']['behaviour']['performative_capacity_selfevaluation']['value'][g] = '10'
    db['subject']['P3']['behaviour']['performative_capacity_selfevaluation']['value'][g] = '7'
    db['subject']['P4']['behaviour']['performative_capacity_selfevaluation']['value'][g] = '7'

# add performative quality selfevaluation
for g in range(len(db['subject']['P1']['record']['arousal']['value'])):
    db['subject']['P1']['behaviour']['performation_quality_selfevaluation']['value'][g] = '9'
    db['subject']['P2']['behaviour']['performation_quality_selfevaluation']['value'][g] = '10'
    db['subject']['P3']['behaviour']['performation_quality_selfevaluation']['value'][g] = '8'
    db['subject']['P4']['behaviour']['performation_quality_selfevaluation']['value'][g] = '9'

# add performation persuasion selfevaluation
for g in range(len(db['subject']['P1']['record']['arousal']['value'])):
    db['subject']['P1']['behaviour']['performation_persuasion_selfevaluation']['value'][g] = True
    db['subject']['P2']['behaviour']['performation_persuasion_selfevaluation']['value'][g] = True
    db['subject']['P3']['behaviour']['performation_persuasion_selfevaluation']['value'][g] = True
    db['subject']['P4']['behaviour']['performation_persuasion_selfevaluation']['value'][g] = False

# add most persuasion segment selfevaluation
db['subject']['P1']['behaviour']['most_persuasion_segment_selfevaluation']['value'][BLUE_START:BLUE_END] = 1
db['subject']['P1']['behaviour']['most_persuasion_segment_selfevaluation']['value'][PAUSE4_START:PAUSE4_END] = 1
db['subject']['P2']['behaviour']['most_persuasion_segment_selfevaluation']['value'][PAUSE1_END:PAUSE4_END] = 1
db['subject']['P3']['behaviour']['most_persuasion_segment_selfevaluation']['value'][PINK_START:PINK_END] = 1
# P4 has not phase with most persuasion segment

# add less persuasion segment selfevaluation
db['subject']['P3']['behaviour']['less_persuasion_segment_selfevaluation']['value'][BLUE_START:BLUE_END] = 1

# add subjective evaluation of the hardest persuasion segment
db['subject']['P1']['behaviour']['hardest_segment']['value'][BLUE_START:BLUE_END] = 1
db['subject']['P3']['behaviour']['hardest_segment']['value'][BLUE_START:BLUE_END] = 1
db['subject']['P4']['behaviour']['hardest_segment']['value'][BLUE_START:BLUE_END] = 1

# add subjective evaluation of the easiest persuasion segment
db['subject']['P1']['behaviour']['easiest_segment']['value'][RED_START:RED_END] = 1
db['subject']['P1']['behaviour']['easiest_segment']['value'][RED_START:RED_END] = 1
db['subject']['P3']['behaviour']['easiest_segment']['value'][PINK_START:PINK_END] = 1
db['subject']['P4']['behaviour']['easiest_segment']['value'][PINK_START:PINK_END] = 1

# add subjective evaluation of the most pleasant segment
db['subject']['P1']['behaviour']['pleasant_segment']['value'][PINK_START:PINK_END] = 1
db['subject']['P3']['behaviour']['pleasant_segment']['value'][PINK_START:PINK_END] = 1
db['subject']['P4']['behaviour']['pleasant_segment']['value'][PINK_START:PINK_END] = 1

# add subjective evaluation of the most unpleasant segment
db['subject']['P1']['behaviour']['unpleasant_segment']['value'][BLUE_START:BLUE_END] = 1
db['subject']['P3']['behaviour']['unpleasant_segment']['value'][:] = 1
db['subject']['P4']['behaviour']['unpleasant_segment']['value'][BLUE_START:BLUE_END] = 1

# add information whether dialoque exist during pause segment?
db['subject']['P1']['behaviour']['is_pause_performation_dialoque']['value'][:] = True
db['subject']['P2']['behaviour']['is_pause_performation_dialoque']['value'][:] = True
db['subject']['P3']['behaviour']['is_pause_performation_dialoque']['value'][:] = True
db['subject']['P4']['behaviour']['is_pause_performation_dialoque']['value'][:] = True

# add information whether performer react on recipient somehow?
db['subject']['P1']['behaviour']['is_recipient_feedback']['value'][:] = True
db['subject']['P2']['behaviour']['is_recipient_feedback']['value'][:] = False
db['subject']['P3']['behaviour']['is_recipient_feedback']['value'][:] = True
db['subject']['P3']['behaviour']['is_recipient_feedback']['value'][:] = False

# add information whether performer react on recipient's breathing somehow?
db['subject']['P1']['behaviour']['is_recipient_respiratory_feedback']['value'][:] = False
db['subject']['P2']['behaviour']['is_recipient_respiratory_feedback']['value'][:] = False
db['subject']['P3']['behaviour']['is_recipient_respiratory_feedback']['value'][:] = False
db['subject']['P3']['behaviour']['is_recipient_respiratory_feedback']['value'][:] = False

# add information whether performer keep eye contact with recipient
db['subject']['P1']['behaviour']['is_recipient_eyecontact']['value'][:] = True
db['subject']['P2']['behaviour']['is_recipient_eyecontact']['value'][:] = False
db['subject']['P3']['behaviour']['is_recipient_eyecontact']['value'][:] = True
db['subject']['P3']['behaviour']['is_recipient_eyecontact']['value'][:] = True

# add information: does performer focus on its own breathing?
db['subject']['P1']['behaviour']['is_performer_respiratory']['value'][:] = False
db['subject']['P2']['behaviour']['is_performer_respiratory']['value'][:] = False
db['subject']['P3']['behaviour']['is_performer_respiratory']['value'][:] = False
db['subject']['P3']['behaviour']['is_performer_respiratory']['value'][:] = True

# add information: does A-V device manipulation distrupt performer?
db['subject']['P1']['behaviour']['device_disturbing']['value'][:] = True
db['subject']['P2']['behaviour']['device_disturbing']['value'][:] = False
db['subject']['P3']['behaviour']['device_disturbing']['value'][:] = True
db['subject']['P3']['behaviour']['device_disturbing']['value'][:] = False

# add information: reasoning the way performer feels recipient feedback
db['subject']['P1']['behaviour']['recipient_feedback_form']['value'] = 'Mirroring.'
db['subject']['P2']['behaviour']['recipient_feedback_form']['value'] = '---'
db['subject']['P3']['behaviour']['recipient_feedback_form']['value'] = 'Physiology, eyes.'
db['subject']['P3']['behaviour']['recipient_feedback_form']['value'] = 'Eyes.'

# add information: the way performer observes recipient respiratory changes
db['subject']['P1']['behaviour']['respiratory_feedback_reasoning']['value'] = '---'
db['subject']['P2']['behaviour']['respiratory_feedback_reasoning']['value'] = '---'
db['subject']['P3']['behaviour']['respiratory_feedback_reasoning']['value'] = '---'
db['subject']['P3']['behaviour']['respiratory_feedback_reasoning']['value'] = '---'

# add information: the way performer keep eye contact with recipient
db['subject']['P1']['behaviour']['eye_contact_reasoning']['value'] = 'Strong eye contact - recipients cried.'
db['subject']['P2']['behaviour']['eye_contact_reasoning']['value'] = '---'
db['subject']['P3']['behaviour']['eye_contact_reasoning']['value'] = 'Continous eye contact with several eye bends.'
db['subject']['P3']['behaviour']['eye_contact_reasoning']['value'] = 'Shy but continous eye contact. ' \

# add information: reasoning of maximal/minimal persuasion segment
db['subject']['P1']['behaviour']['persuasion_segment_selfevaluation_reasoning']['value'] = 'Red is native to me. Blue makes me sick.'
db['subject']['P2']['behaviour']['persuasion_segment_selfevaluation_reasoning']['value'] = 'Red influences recipient, ' \
                                                                                  'which is satisfacting.'
db['subject']['P3']['behaviour']['persuasion_segment_selfevaluation_reasoning']['value'] = 'Pink makes me ňuňu. Blue makes me ' \
                                                                                  'sick. '
db['subject']['P3']['behaviour']['persuasion_segment_selfevaluation_reasoning']['value'] = 'Pink reflect my character.' \


# save database on local drive
with open('db.pickle', 'wb') as handle:
    pickle.dump(db, handle)