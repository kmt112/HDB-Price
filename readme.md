# Resale HDB Pricing
## Introduction
This repository contains the resale HDB pricing exploratory data analysis, resale housing prediction modelling and resale pricing. All data is taken from https://data.gov.sg/dataset/resale-flat-prices. I have also written a two part blog post on medium (https://medium.com/p/94ab708cccf8). However, since those were done previously, i have decided to make this repo usable for others. Current Work in progress


## Data Cleaning
This notebook creates new coordinates for all addresses (utilizing onemap API). The new coordinates are then used to calculate the closest distance between the HDB to closest MRT, Primary school and CDB area.

```
├── drive
│   ├── MyDrive
│   │   ├── Projects
│   │       ├── HDB
                ├── models
                ├── resale-flat-prices-based-on-approval-date-2000-feb-2012.csv
                ├── List_of_primary_schools_in_Singapore_1.csv
                ├── mrt_lrt_data.csv
```

- [![Open_In_Colab][Open_In_Colab]][Open_In_Colab-url]

## Modelling
This notebook generates the final model used. to be updated with insights, local explaination and Local Interpretable Model-agnostics Explainations
- [![Open_In_Colab][Open_In_Colab]][Open_In_Colab-url_modelling]

## Setup
Do create a new virtual environment using the supplied requirements.txt to ensure that you have the required packages.

Once the virtual environment is set up, the folder structure is as such:
```
├── HDB-Price
│   ├── Main.py
│   ├── readme.md
│   ├── Xformer.py
│   ├── dataPackage
│   │   ├── final_mrt_list.csv
│   │   ├── primary_hdb.pickle
│   │   ├── final_columns.pickle
│   │   ├── hdb_model.bst
```

### Built With


- [![React][React.js]][React-url]
- [![Flask][Flask]][flask-url]
- [![Turborepo][Turborepo]][Turborepo-url]
- [![FastAPI][FastAPI]][fastapi-url]



### Steps
#### Generating ensembled probabilities

#### Training models to generate probabilities from evaluation dataset



## Results


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
[Open_In_Colab-url_modelling]: https://colab.research.google.com/drive/1ZYWHqRLk3fK2UIPVykvlfYOMJgCEju_2?authuser=1
