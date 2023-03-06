# Resale HDB Pricing
## Introduction
This repository contains the resale HDB pricing exploratory data analysis, resale housing prediction modelling and resale pricing. All data is taken from https://data.gov.sg/dataset/resale-flat-prices. I have also written a two part blog post on medium (https://medium.com/p/94ab708cccf8). However, since those were done previously, i have decided to make this repo usable for others who wish to have an API. 

## Performance Metrics
HDB pricing model is evaluated based on 

## Setup
Do create a new virtual environment using the supplied requirements.txt to ensure that you have the required packages.

Once the virtual environment is set up, the folder structure is as such:
```
├── Main
│   ├── Code
│   │   ├── Submission.ipynb
│   │   ├── helperfunction.py
│   ├── dataPackage
│   │   ├── HDB_Data.CSV
│   ├── dataPackageEval
│   │   ├── EvalSet_StartEndTimes.csv
```

### Built With


- [![React][React.js]][React-url]
- [![Chakraui][Chakraui]][chakraui-url]
- [![Turborepo][Turborepo]][Turborepo-url]
- [![FastAPI][FastAPI]][fastapi-url]



### Steps
#### Generating ensembled probabilities
Utilising the time series classification APIs available in sktime, we methodically trained the APIs on each physiological signal and tested the models against 20% holdout data across 5 folds. (Certain datasets were too large to feasibly train on local machines. For these we only conducted 1 fold testing as each fold require up to 10 hours to run)

Through this process, we optimised the hyperparameters and selected the best classifier for that particular physiological signal.

Following this, the classifier with optimised parameters were used to generate the prediction probabilities for each physiological signal. The predictions of the five holdout sets of data was combined to one table. Here is an example generated for the ECG signal:

![pred_proba](https://github.com/skulu/cogpilotdatachallenge/blob/main/readme_pics/prediction_probabilities.png)

This was repeated for all the signals. The probabilities were joined on the `subject`, `difficulty` and `run` columns to form a large ensembled table.

#### Training models to generate probabilities from evaluation dataset
With the optimised classifiers and hyperparameters found in the previous section, we trained the classifiers on the entire physiological signal training set for each signal. These models were then used on the evaluation datasets to generate the probabilities like the above picture and once again ensembled across all physiological signals.

With these probabilities we now have a training set of ensembled probabilities and an evaluation set of ensembled probabilities with all physiological signals included.


## Results
The fully trained model on the 4 important signals was applied to the evaluation data set and we are now pending the results of the competition.

## Team Members (alphabetical order)
1. Jie Yong <ins>Er</ins> - [LinkedIn](https://www.linkedin.com/in/erjieyong/)
2. Kah Ming <ins>Tan</ins> - [LinkedIn](https://www.linkedin.com/in/tankahming/) | [GitHub](https://github.com/kmt112)
3. Skyler <ins>Tan</ins> - [LinkedIn](https://www.linkedin.com/in/skyler-tan/) | [GitHub](https://github.com/skulu)
4. Xue Yang
