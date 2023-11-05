# Diabetes Prediction from CDC survey

I am usimng Diabetes Health Indicators Dataset which has 253,680 survey responses from cleaned BRFSS 2015 + balanced dataset provided here https://www.kaggle.com/datasets/alexteboul/diabetes-health-indicators-dataset/data

## Context

The Behavioral Risk Factor Surveillance System (BRFSS) is a health-related telephone survey that is collected annually by the CDC. Each year, the survey collects responses from over 400,000 Americans on health-related risk behaviors, chronic health conditions, and the use of preventative services. It has been conducted every year since 1984. For this project, a csv of the dataset available on Kaggle for the year 2015 was used. This original dataset contains responses from 441,455 individuals and has 330 features. These features are either questions directly asked of participants, or calculated variables based on individual participant responses.

This dataset contains 3 files:

1) diabetes _ 012 _ health _ indicators _ BRFSS2015.csv is a clean dataset of 253,680 survey responses to the CDC's BRFSS2015. The target variable Diabetes_012 has 3 classes. 0 is for no diabetes or only during pregnancy, 1 is for prediabetes, and 2 is for diabetes. There is class imbalance in this dataset. This dataset has 21 feature variables

2) diabetes _ binary _ 5050split _ health _ indicators _ BRFSS2015.csv is a clean dataset of 70,692 survey responses to the CDC's BRFSS2015. It has an equal 50-50 split of respondents with no diabetes and with either prediabetes or diabetes. The target variable Diabetes_binary has 2 classes. 0 is for no diabetes, and 1 is for prediabetes or diabetes. This dataset has 21 feature variables and is balanced.

3) diabetes _ binary _ health _ indicators _ BRFSS2015.csv is a clean dataset of 253,680 survey responses to the CDC's BRFSS2015. The target variable Diabetes_binary has 2 classes. 0 is for no diabetes, and 1 is for prediabetes or diabetes. This dataset has 21 feature variables and is not balanced.

## Purpose of this work
I indented to build a web service which can provide probabaility and prediction of whether a person has diabetes or not by using same question as they were asked in BRFSS is a health-related telephone survey.

I will be using third file `diabetes _ binary _ health _ indicators _ BRFSS2015.csv ` which is what you get pull data from UCI repository.


## How to review this work

- All the notebook are in the main directory of this repository:
    
    - `01_EDA.ipynb` located inside `01_EDA.ipynb` contains the exploratory data analysis. **I had to zip this file as it is more than 100MB in size and GitHub wouldn't let me updaload it**
    
    - `02_build_multiple_models.ipynb` shows my work on training and comparing multiple models. Then I chosoe one model and perform hyper parameter tuning.
    
    - `03_fit_tuned_random_forest.ipynb` contains code for building my final model
    
    - `04_flask_app.ipynb` contains code to run the application as flask web app. To test the prediction either use a tool like HTTPie or PostMan or use the notebook `05_flask_diabetes_check.ipynb`
    
    - `docker` folder has my code building and running the diabetes prediction app via docker. To test the predictions via docker either use the notebook `06_docker_diabetes_check.ipynb` use a tool like HTTPie or PostMan 
    
    - lastly, I deployed the docker version of my web app to to render.com. To test the predictions via docker either use the notebook `07_cloudapp_diabetes_check.ipynb` use a tool like HTTPie or PostMan 

- My Webapp on render platform can be reached using https://diabetesprediction-l5y1.onrender.com. It is a headless app and there is no GUI. If you want to test it then following instruction provided in 1.f. As per render website **Free instance types will spin down with inactivity. Upgrade to a paid instance type to prevent this behavior. Learn more.** So I request you to please use the screenshots and exiting notebook `07_cloudapp_diabetes_check.ipynb` to verfy that it was working the time of creating this GitHub Repo

- Screenshots of predictions as provided in folder named `screenshots of predictions`. This is will allow you test what I done without the need to run the code.

- `examples.txt` has some example patient  survey data which you can use to make predictions. I have already extracted three examples for each of prediction type into their folders amd notebooks 

- **IMPORTANT Due to warnings from gitHub I have to zip my pickled files. Please extract them in the same folder where they are located.**
