Car Dheko - Used Car Price Prediction Project
Objective
The project aims to develop a robust machine learning model for accurately predicting the prices of used cars. An interactive Streamlit web application is deployed to allow customers and sales representatives to input car details and receive instant price estimates.

Problem Statement
The goal is to enhance customer experience and streamline the pricing process by leveraging machine learning to predict used car prices based on various features such as make, model, year, and fuel type.

Data and Approach
Data Source: Historical data of 8,369 cars from CarDekho.
Steps Involved:
Data Preprocessing:
Imputation for missing values, encoding categorical variables, scaling numerical features, and outlier removal.
Exploratory Data Analysis (EDA):
Key insights derived through visualizations like scatter plots, histograms, box plots, and correlation heatmaps.
Feature Selection:
Techniques include correlation analysis, feature importance from models, and domain expertise.
Model Development:
Algorithms tested include Linear Regression, Decision Trees, Random Forests, and Gradient Boosting. Random Forest performed best.
Hyperparameter tuning using Grid Search and Random Search.
Optimization:
Feature engineering and regularization techniques (Lasso and Ridge Regression) to improve model performance.
Model Evaluation
The model was evaluated using metrics like MAE, MSE, RMSE, and R². Random Forest demonstrated the best performance with low error rates and high accuracy.

Streamlit Application
Features:
User-friendly interface with dropdowns, sliders, and buttons to input car details.
Real-time price prediction using the trained model.
Deployment:
The app can be run locally or hosted on platforms like Streamlit Cloud or Heroku.
Key Outcomes
Accurate Model: Delivered a reliable predictive model with low error metrics.
Comprehensive Analysis: Insights from EDA revealed valuable patterns, improving model efficiency.
Interactive App: Developed a Streamlit application that makes the tool accessible to non-technical users.
Thorough Documentation: Detailed methodology and results ensure transparency and ease of understanding.
This project enhances decision-making for used car pricing while offering an intuitive platform for instant predictions.