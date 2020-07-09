# Electrical Machines Design Automation by Ansys Maxwell Script

## Goal
Setup a python api server, accept motor spec(stator Outer Diameter, DC bus voltage, max toruqe, max speed), 
auto design, draw and run ansys analysis,
finally response result data(BEMF, cogging torque, max torque, torque ripple, induce voltage, efficiency)
(Now just 10p12s Surface PM design, It still working on...)

## Requirements
1. Windows 7 or above
2. Legal Ansys Maxwell Electromagnetic Suite
3. Python 3
 - python 3.7.6
4. Python library
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
2. execute
 - just run analysis(params set at spec_params in run.py) - python run.py
 - run flask api server and call ansys run and return result as response (POST method, json data sample in example/, url = http://localhost:5000/run_simu) - python server.py
 - run flask api server, call but run ansys asyc in backgroud and return result use request to another url (POST method, json data sample in example/, url = http://localhost:5000/run_simu) - python server_run_back.py
