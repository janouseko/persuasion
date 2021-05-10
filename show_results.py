# -------------------------------------------------------------------
# show results
#
# This script belongs to software collection for persuasion analysis,
# provided by Technology Agency of the Czech Republic TACR TJ02000293
#
# 2019 - 2021, Brno University of Technology, janouseko@vut.cz
# -------------------------------------------------------------------
# -*- coding: utf-8 -*-
import pickle
import numpy as np
from constants import *
import matplotlib.pyplot as plt
import matplotlib.backends.backend_pdf

# open database
with open(DB_FILEPATH+r'\db.pickle', 'rb') as f:
    db = pickle.load(f)

# setup pdf file
pdf = matplotlib.backends.backend_pdf.PdfPages('output.pdf')

# show parameters - part record
parameter_dict = db['subject']['P1']['record']
parameter_dict.pop('id')
parameter_list = parameter_dict.keys()
for p in parameter_list:
    plt.figure(figsize=(14, 8), dpi=80)
    plt.suptitle(db['subject']['P1']['record'][p]['description'])
    g = 0
    for s in db['subject'].keys():
        g = g + 1
        plt.subplot(2, 4, g)
        plt.plot(db['subject'][s]['record']['timestamp']['value'] / 60, db['subject'][s]['record'][p]['value'],
                 color='black')
        plt.title(s)
        plt.xlabel('time [m]')
        plt.ylabel(db['subject'][s]['record'][p]['name'] + ' ' + db['subject'][s]['record'][p]['unit'])
        xposition = [2, 2 + 5, 2 + 5 + 2, 2 + 5 + 2 + 5, 2 + 5 + 2 + 5 + 2, 2 + 5 + 2 + 5 + 2 + 5]
        for xc in xposition:
            plt.axvline(x=xc, color='gray', linestyle='--')
    plt.tight_layout()
    pdf.savefig(plt.gcf().number)
    plt.close()

# show parameters - part signal
parameter_dict = db['subject']['P1']['signal']
parameter_list = parameter_dict.keys()
for p in parameter_list:
    plt.figure(figsize=(14, 8), dpi=80)
    plt.suptitle(db['subject']['P1']['signal'][p]['description'])
    g = 0
    for s in db['subject'].keys():
        g = g + 1
        plt.subplot(2, 4, g)
        plt.plot(db['subject'][s]['record']['timestamp']['value'] / 60, db['subject'][s]['signal'][p]['value'],
                 color='black')
        plt.title(s)
        plt.xlabel('time [m]')
        plt.ylabel(db['subject'][s]['signal'][p]['name'] + ' ' + db['subject'][s]['signal'][p]['unit'])
        xposition = [2, 2 + 5, 2 + 5 + 2, 2 + 5 + 2 + 5, 2 + 5 + 2 + 5 + 2, 2 + 5 + 2 + 5 + 2 + 5]
        for xc in xposition:
            plt.axvline(x=xc, color='gray', linestyle='--')
    plt.tight_layout()
    pdf.savefig(plt.gcf().number)
    plt.close()

# show parameters - part behaviour
parameter_dict = db['subject']['P1']['behaviour']
parameter_dict.pop('recipient_feedback_form')
parameter_dict.pop('respiratory_feedback_reasoning')
parameter_dict.pop('eye_contact_reasoning')
parameter_dict.pop('persuasion_segment_selfevaluation_reasoning')
parameter_list = parameter_dict.keys()
# plot only the first 16 behaviour parameters, because others has
# strings only on position [0], therefore not applicable for plotting time series with timeline on x axis.
for p in parameter_list:
    plt.figure(figsize=(14, 8), dpi=80)
    plt.suptitle(db['subject']['P1']['behaviour'][p]['description'])
    g = 0
    for s in db['subject'].keys():
        g = g + 1
        plt.subplot(2, 4, g)
        plt.plot(db['subject'][s]['record']['timestamp']['value'] / 60, db['subject'][s]['behaviour'][p]['value'],
                 color='black')
        plt.title(s)
        plt.xlabel('time [m]')
        plt.ylabel(db['subject'][s]['behaviour'][p]['name'] + ' ' + db['subject'][s]['behaviour'][p]['unit'])
        xposition = [2, 2 + 5, 2 + 5 + 2, 2 + 5 + 2 + 5, 2 + 5 + 2 + 5 + 2, 2 + 5 + 2 + 5 + 2 + 5]
        for xc in xposition:
            plt.axvline(x=xc, color='gray', linestyle='--')
    plt.tight_layout()
    pdf.savefig(plt.gcf().number)
    plt.close()

# show parameters - part annotation
parameter_dict = db['subject']['P1']['annotation']
parameter_list = parameter_dict.keys()
for p in parameter_list:
    plt.figure(figsize=(14, 8), dpi=80)
    plt.suptitle(db['subject']['P1']['annotation'][p]['description'])
    g = 0
    for s in db['subject'].keys():
        g = g + 1
        plt.subplot(2, 4, g)
        plt.plot(db['subject'][s]['record']['timestamp']['value'] / 60, db['subject'][s]['annotation'][p]['value'],
                 color='black')
        plt.title(s)
        plt.xlabel('time [m]')
        plt.ylabel(db['subject'][s]['annotation'][p]['name'] + ' ' + db['subject'][s]['annotation'][p]['unit'])
        xposition = [2, 2 + 5, 2 + 5 + 2, 2 + 5 + 2 + 5, 2 + 5 + 2 + 5 + 2, 2 + 5 + 2 + 5 + 2 + 5]
        for xc in xposition:
            plt.axvline(x=xc, color='gray', linestyle='--')
    plt.tight_layout()
    pdf.savefig(plt.gcf().number)
    plt.close()

# show parameters - part analysis
parameter_dict = db['subject']['P1']['analysis']
parameter_list = parameter_dict.keys()
for p in parameter_list:
    plt.figure(figsize=(14, 8), dpi=80)
    plt.suptitle(db['subject']['P1']['analysis'][p]['description'])
    g = 0
    for s in db['subject'].keys():
        g = g + 1
        plt.subplot(2, 4, g)
        plt.plot(db['subject'][s]['record']['timestamp']['value'] / 60, db['subject'][s]['analysis'][p]['value'],
                 color='black')
        plt.title(s)
        plt.xlabel('time [m]')
        plt.ylabel(db['subject'][s]['analysis'][p]['name'] + ' ' + db['subject'][s]['analysis'][p]['unit'])
        xposition = [2, 2 + 5, 2 + 5 + 2, 2 + 5 + 2 + 5, 2 + 5 + 2 + 5 + 2, 2 + 5 + 2 + 5 + 2 + 5]
        for xc in xposition:
            plt.axvline(x=xc, color='gray', linestyle='--')
    plt.tight_layout()
    pdf.savefig(plt.gcf().number)
    plt.close()

pdf.close()
