# Resale HDB Pricing
## Introduction
This repository contains the resale HDB pricing exploratory data analysis, resale housing prediction modelling and resale pricing. All data is taken from https://data.gov.sg/dataset/resale-flat-prices. I have also written a two part blog post on medium (https://medium.com/p/94ab708cccf8). However, since those were done previously, i have decided to make this repo usable for others. 

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
- [![Flask][Flask]][flask-url]
- [![Turborepo][Turborepo]][Turborepo-url]
- [![FastAPI][FastAPI]][fastapi-url]
- [![Open_In_Colab][Open_In_Colab]][Open_In_Colab-url]



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

<!-- MARKDOWN LINKS & IMAGES -->
<!-- https://www.markdownguide.org/basic-syntax/#reference-style-links -->

[Next.js]: https://img.shields.io/badge/next.js-000000?style=for-the-badge&logo=nextdotjs&logoColor=white
[Next-url]: https://nextjs.org/
[React.js]: https://img.shields.io/badge/React-20232A?style=for-the-badge&logo=react&logoColor=61DAFB
[React-url]: https://reactjs.org/
[flask]: https://img.shields.io/badge/Flask-000000?style=for-the-badge&logo=flask&logoColor=white
[flask-url]: https://flask.palletsprojects.com/en/2.2.x/quickstart/
[Turborepo]: https://camo.githubusercontent.com/a7d3629f30574e4176766e5ced5b0497083dfbbc4b8c2799840bacba7f935cbc/68747470733a2f2f696d672e736869656c64732e696f2f7374617469632f76313f7374796c653d666f722d7468652d6261646765266d6573736167653d547572626f7265706f26636f6c6f723d454634343434266c6f676f3d547572626f7265706f266c6f676f436f6c6f723d464646464646266c6162656c3d
[Turborepo-url]: https://turbo.build/
[FastAPI]: https://camo.githubusercontent.com/81b1b79330b1154fc0743b25327cbfd6282a7bf37e8d0b48278dc57528b2517c/68747470733a2f2f696d672e736869656c64732e696f2f7374617469632f76313f7374796c653d666f722d7468652d6261646765266d6573736167653d4661737441504926636f6c6f723d303039363838266c6f676f3d46617374415049266c6f676f436f6c6f723d464646464646266c6162656c3d
[fastapi-url]: https://fastapi.tiangolo.com/
[Open_In_Colab]: https://colab.research.google.com/assets/colab-badge.svg
[Open_In_Colab-url]: https://colab.research.google.com/drive/1aeDdsbgU66_Nx3wUURgXcjgX3s-1Qfyb?authuser=1#scrollTo=qRA0dBU_odU3
