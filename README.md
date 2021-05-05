# Persuasion
Persuasion assessment in performer-recipient session based on biosignal analysis. 

Software collection for persuasion analysis, provided by Technology Agency of the Czech Republic TACR TJ02000293. 
Brno University of Technology, Masaryk University and The Janáček Academy of Music and Performing Arts Brno, 2019 - 2021.

# Install
1. install requirements  `$ pip install -r requirements.txt`
2. download [biosignal record database](https://drive.google.com/file/d/1bvtsGG7NHU1nbTTuAJb6lsSn_bU1p1j8/view?usp=sharing) into working dir.

# Run
Run `run_all.py`. See *output.pdf* and *output.txt* in working dir. 

or

Run individual scripts sequentially:
1. `load_biosignals_record.py`
2. `evaluate_signals.py`
3. `evaluate_behaviour.py`
4. `incorporate_annotation.py`,
