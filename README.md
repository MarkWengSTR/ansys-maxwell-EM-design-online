# Ansys Maxwell Automation Script

## Goal
Using python control ansys maxwell software to draw a surface PM motor

## Requirements
1. Windows 7 or above
2. Legal Ansys Maxwell Electromagnetic Suite
3. Required Ansys material
 - 35CS250_20190702.amat
 - ZH_N44SH_20deg_20190702.amat
4. Python 3
 - python 3.7.6
5. Python library
 - pywin32==227
 - ramda==0.5.5
 - six==1.13.0
 - functional-pipeline==0.3.1
 - ipdb==0.12.3
 - Flask==1.1.2
 - Flask-Cors==3.0.8
 - pandas==1.0.1
 - numpy==1.18.1
 - requests==2.24.0
## Environment Install Guide (Verified)
1. Install Python 3.7.6
2. (optional) Install virutal env
 - pip install virtualenv
3. optional) create virutal env
 - virutalenv venv
4. (optional) activate virutal env
 - ./venv/Scripts/activate
5. Installed needed library using the following command
 - pip install -r requirements.txt
## SPM Motor params
all setting are in params/

## Execute Guide
1. active virtual env
 - ./venv/Scripts/activate
2. execute run.py
 - python run.py
