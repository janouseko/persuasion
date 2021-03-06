# Persuasion
Persuasion assessment in performer-recipient session based on biosignal analysis. 

# Description
Software collection for persuasion analysis, provided by Technology Agency of the Czech Republic TACR TJ02000293. 
Brno University of Technology, Masaryk University and The Janáček Academy of Music and Performing Arts Brno, 2019 - 2021.

See project [wiki](https://github.com/janouseko/persuasion/wiki) (in Czech language) for detail description of persuasion assessment and biosignal being recorded in performer-recipient session.

# Install
1. install requirements  `$ pip install -r requirements.txt`
2. download [biosignal record database](https://drive.google.com/file/d/1bvtsGG7NHU1nbTTuAJb6lsSn_bU1p1j8/view?usp=sharing) into working dir.

# Usage
Run `run_all.py`. See *output.pdf* and *output.txt* in working dir. 

**or**

Run individual scripts sequentially:
1. `load_biosignals.py`
2. `incorporate_annotation.py`
3. `incorporate_device.py`
4. `incorporate_description.py`
5. `evaluate_signals.py`
6. `evaluate_behaviour.py`
7. `analyse.py`
8. `add_units_and_explanation.py`
9. `estimate_persuasion.py`
10. `show_results.py`

See *output.pdf* and *output.txt* in working dir. 

# Miscellaneous
Free space >3 GB required, due to result database file (db.pickle) being saved on local drive.
