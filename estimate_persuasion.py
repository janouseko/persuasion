# -------------------------------------------------------------------
# estimate persuasion level
#
# This script belongs to software collection for persuasion analysis,
# provided by Technology Agency of the Czech Republic TACR TJ02000293
#
# 2019 - 2021, Brno University of Technology, janouseko@vut.cz
# -------------------------------------------------------------------

import pickle
from constants import *
from scipy.stats import pearsonr
from tabulate import tabulate

# open database
with open(DB_FILEPATH+r'\db.pickle', 'rb') as f:
    db = pickle.load(f)

    # compute, if there is equality of P's and R's start arousal moments
star_equality = []
for i in [1,2,3,4]:
    star_equality.append(sum(db['subject']['P'+str(i)]['analysis']['arousal_is_start']['value']) \
                         == sum(db['subject']['R'+str(i)]['analysis']['arousal_is_start']['value']))

# compute, if there is equality of P's and R's end arousal moments
enar_equality = []
for i in [1,2,3,4]:
    enar_equality.append(sum(db['subject']['P'+str(i)]['analysis']['arousal_is_end']['value']) \
                         == sum(db['subject']['R'+str(i)]['analysis']['arousal_is_end']['value']))

# compute, where there are decrements of R's valence between pause and subsequent performance
recp_val_diff = []
for i in [1,2,3,4]:
    recp_val_diff.append(
        (db['subject']['R'+str(i)]['analysis']['valence_activity_mean_numeric']['value'][RED_START]\
        -db['subject']['R'+str(i)]['analysis']['valence_activity_mean_numeric']['value'][RED_START-1]+\
        db['subject']['R'+str(i)]['analysis']['valence_activity_mean_numeric']['value'][BLUE_START]\
        -db['subject']['R'+str(i)]['analysis']['valence_activity_mean_numeric']['value'][BLUE_START-1]+\
        db['subject']['R'+str(i)]['analysis']['valence_activity_mean_numeric']['value'][PINK_START]\
        -db['subject']['R'+str(i)]['analysis']['valence_activity_mean_numeric']['value'][PINK_START-1])\
        <0)

# compute, whether there are small difference between P's and R's total amount of linear acceleration
tot_acc_diff = []
for i in [1,2,3,4]:
    tot_acc_diff.append((abs(db['subject']['P'+str(i)]['analysis']['acc_total_amount']['value'][0] \
        -db['subject']['R'+str(i)]['analysis']['acc_total_amount']['value'][0]))<10000)

# compute, where there is a mild correlation between P's and R's smoothed heart rate
hr_corr = []
for i in [1,2,3,4]:
    hr_corr.append(abs(db['subject']['P'+str(i)]['analysis']['hr_total_correlation']['value'][0])>0.2)

# compute, where there is a mild correlation between P's and R's hand temperature
hand_temp_corr = []
for i in [1,2,3,4]:
    hand_temp_corr.append(abs(db['subject']['P'+str(i)]['analysis']['temp_hand_total_correlation']['value'][0])>0.2)

# compute, where there is a strong correlation between P's arousal and inverted R's valence
ars_invval_corr = []
for i in [1,2,3,4]:
    ars_invval_corr.append(pearsonr(db['subject']['P'+str(i)]['record']['arousal']['value'], \
                                    -1*db['subject']['R'+str(i)]['record']['valence']['value'])[0]>0.5)

# compute, where there is a strong correlation between P's and R's arousal
ars_corr = []
for i in [1,2,3,4]:
    ars_corr.append(pearsonr(db['subject']['P'+str(i)]['record']['arousal']['value'], \
                                    db['subject']['R'+str(i)]['record']['arousal']['value'])[0]>0.3)

# compute, where there is a correlation between head temperature of P's and R's
head_temp_corr = []
for i in [1,2,3,4]:
    head_temp_corr.append(pearsonr(db['subject']['P'+str(i)]['record']['temp_head']['value'], \
                                    db['subject']['R'+str(i)]['record']['temp_head']['value'])[0]>0.5)

# compute, where there is a correlation between arousal mean (in every emotion and pause) of P's and R's
ars_act_mean_corr = []
for i in [1,2,3,4]:
    ars_act_mean_corr.append(pearsonr(db['subject']['P'+str(i)]['analysis']['arousal_activity_mean_numeric']['value'], \
                                    db['subject']['R'+str(i)]['analysis']['arousal_activity_mean_numeric']['value'])[
                                 0]>0.5)

# compute, where there is a correlation between amount of rotation (in every emotion and pause) of P's and R's
gyro_tot_act_corr = []
for i in [1,2,3,4]:
    gyro_tot_act_corr.append(pearsonr(db['subject']['P'+str(i)]['analysis']['gyro_activity_amount']['value'], \
                                    db['subject']['R'+str(i)]['analysis']['gyro_activity_amount']['value'])[0]>0.5)

# estimate persuasion level (on the basis of above computed parameters) and print it as a table
total_param = 10 # total number of parameter constituting persuasion level estimation formula
persuasion_level = []
for i in [0,1,2,3]:
    persuasion_level.append([ars_corr[i],ars_act_mean_corr[i],star_equality[i],enar_equality[
             i],recp_val_diff[i],ars_invval_corr[i],tot_acc_diff[i],gyro_tot_act_corr[i],hr_corr[i],hand_temp_corr[i]])
# make a head
head = ['PARAMETER', 'P1-R1', 'P2-R2', 'P3-R3', 'P4-R4']
# make a table
table = [['arousal correlation', ars_corr[0], ars_corr[1], ars_corr[2], ars_corr[3]],
         ['arousal mean in emotions correlation', ars_act_mean_corr[0], ars_act_mean_corr[1], ars_act_mean_corr[2], ars_act_mean_corr[3]],
         ['arousal start equality', star_equality[0], star_equality[1], star_equality[2], star_equality[3]],
         ['arousal end equality', enar_equality[0], enar_equality[1], enar_equality[2], enar_equality[3]],
         ['recipient valence decrement', recp_val_diff[0], recp_val_diff[1], recp_val_diff[2], recp_val_diff[3]],
         ['arousal valence inverse relationship', ars_invval_corr[0], ars_invval_corr[1], ars_invval_corr[2], ars_invval_corr[3]],
         ['amount of acceleration similarity', tot_acc_diff[0], tot_acc_diff[1], tot_acc_diff[2], tot_acc_diff[3]],
         ['amount of rotation similarity', gyro_tot_act_corr[0], gyro_tot_act_corr[1], gyro_tot_act_corr[2], gyro_tot_act_corr[3]],
         ['heart rate correlation', hr_corr[0], hr_corr[1], hr_corr[2], hr_corr[3]],
         ['hand temperature correlation', hand_temp_corr[0], hand_temp_corr[1], hand_temp_corr[2], hand_temp_corr[3]],
         ['PERSUASION LEVEL', str(int(sum(persuasion_level[0])/total_param*100))+'%', \
                              str(int(sum(persuasion_level[1])/total_param*100))+'%', \
                              str(int(sum(persuasion_level[2])/total_param*100))+'%', \
                              str(int(sum(persuasion_level[3])/total_param*100))+'%']]
# display persuasion level table
print(tabulate(table, headers=head, tablefmt="pretty"))

# export table as text file (*.txt)
content_to_export=tabulate(table, headers=head, tablefmt="pretty")
text_file=open("output.txt","w")
text_file.write(content_to_export)
text_file.close()

# export table as HTML file (*.html)
content_to_export=tabulate(table, headers=head, tablefmt="html")
text_file=open("output.html","w")
text_file.write(content_to_export)
text_file.close()