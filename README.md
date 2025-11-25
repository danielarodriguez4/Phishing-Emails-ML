# Phishing-Emails-ML

## Developed by:
- Daniela Rodríguez Chacón
- Estiven Ospina González

# Description
This work presents a machine learning approach for detecting phishing emails using the Phishing and Legitimate Emails Dataset, a synthetically generated corpus of 10,000 email samples. The study focuses on binary classification to distinguish phishing from legitimate messages, leveraging logistic regression as a baseline model. Unlike traditional datasets, this collection includes enriched metadata such as phishing type, severity, and confidence levels, allowing for enhanced feature exploration. Experimental results demonstrate the effectiveness of logistic regression in capturing key linguistic and structural cues within email text, highlighting its potential as a lightweight yet reliable method for phishing detection in email security systems.

# How to run locally

## Clone the repository
```bash
git clone https://github.com/danielarodriguez4/Phishing-Emails-ML.git
```

## Install Miniconda based on your OS

### MacOS
```bash
curl -O https://repo.anaconda.com/miniconda/Miniconda3-latest-MacOSX-arm64.sh
```
### Windows
```bash
curl https://repo.anaconda.com/miniconda/Miniconda3-latest-Windows-x86_64.exe --output .\Downloads\Miniconda3-latest-Windows-x86_64.exe
```
## Access the folder
```bash
cd Phishing-Emails-ML
```

## Create and activite the Conda environment
```bash
conda create -n phishing-env python=3.9 -y

conda activate phishing-env
```

## Install requirements.txt
```bash
pip install -r requirements.txt
```

## Initiate the notebook
```bash
jupyter notebook
```
