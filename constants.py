# -------------------------------------------------------------------
# constant definition for data processing and timeline definition
#
# This script belongs to software collection for persuasion analysis,
# provided by Technology Agency of the Czech Republic TACR TJ02000293
#
# 2019 - 2021, Brno University of Technology, janouseko@vut.cz
# -------------------------------------------------------------------

# define paths for database and outputs (exported pdf, tables)
import os
DB_FILEPATH = os.path.dirname(__file__)
OUTPUT_FILEPATH = os.path.dirname(__file__)

# set sampling frequency
FS = 500 # sampling frequency for (already resampled) records

# set performer-recipient session parameters and timeline
PAUSE1_START = FS * 60 * (0)
PAUSE1_END = RED_START = FS * 60 * (2)
RED_END = PAUSE2_START = FS * 60 * (2+5)
PAUSE2_END = BLUE_START = FS * 60 * (2+5+2)
BLUE_END = PAUSE3_START = FS * 60 * (2+5+2+5)
PAUSE3_END = PINK_START = FS * 60 * (2+5+2+5+2)
PINK_END = PAUSE4_START = FS * 60 * (2+5+2+5+2+5)
PAUSE4_END = FS * 60 * (2+5+2+5+2+5+2)
EXPERIMENT_LENGTH = FS * 60 * (2+5+2+5+2+5+2)