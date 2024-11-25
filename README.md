# **Car Dheko - Used Car Price Prediction Project**

## **Objective**
Develop a robust machine learning model to accurately predict used car prices. Deploy an interactive Streamlit web application enabling customers and sales representatives to input car details and receive instant price estimates.

---

## **Problem Statement**
Enhance customer experience and streamline the pricing process using machine learning to predict used car prices based on features like make, model, year, and fuel type.

---

## **Data and Approach**

### **Data Source**
- Historical dataset of **8,369 used cars** from CarDekho.

### **Steps Involved**
1. **Data Preprocessing**:
   - Imputation for missing values.
   - Encoding categorical variables.
   - Scaling numerical features.
   - Outlier removal.

2. **Exploratory Data Analysis (EDA)**:
   - Derived key insights using:
     - **Scatter Plots**: Visualize relationships (e.g., price vs. mileage).
     - **Histograms**: Understand distributions (e.g., engine size).
     - **Box Plots**: Detect outliers and distribution shapes.
     - **Correlation Heatmaps**: Identify relationships between features.

3. **Feature Selection**:
   - Techniques used:
     - **Correlation Analysis**: Assess linear relationships with target variable.
     - **Feature Importance**: Extract insights from Random Forest and Gradient Boosting models.
     - **Domain Expertise**: Incorporate industry knowledge for logical feature selection.

4. **Model Development**:
   - Algorithms tested:
     - **Linear Regression**
     - **Decision Trees**
     - **Random Forests**
     - **Gradient Boosting**
   - Best-performing model: **Random Forest**.
   - Hyperparameter tuning: **Grid Search** and **Random Search** for optimization.

5. **Optimization**:
   - Feature Engineering:
     - Create or transform features for better patterns.
   - Regularization Techniques:
     - **Lasso Regression** (L1 Regularization) for sparse models.
     - **Ridge Regression** (L2 Regularization) to handle multicollinearity.

---

## **Model Evaluation**
- Metrics used to evaluate performance:
  - **Mean Absolute Error (MAE)**: Average magnitude of errors.
  - **Mean Squared Error (MSE)**: Penalizes large errors more.
  - **Root Mean Squared Error (RMSE)**: Measures accuracy with sensitivity to outliers.
  - **R²**: Proportion of variance explained by the model.

- **Best Model**: Random Forest demonstrated low MAE and RMSE with high R², indicating strong performance and reliability.

---

## **Streamlit Application**

### **Features**
- User-friendly interface with:
  - Dropdowns, sliders, and buttons for easy input of car details.
  - Real-time price predictions using the trained model.

### **Deployment**
- The application can be:
  - Run locally using `streamlit run app.py`.
  - Hosted on platforms like **Streamlit Cloud** or **Heroku**.

---

## **Key Outcomes**

1. **Accurate Model**: Delivered a reliable predictive model with low error metrics.
2. **Comprehensive Analysis**: Insights from EDA improved model efficiency and revealed valuable patterns.
3. **Interactive App**: A Streamlit application accessible to non-technical users for instant predictions.
4. **Thorough Documentation**: Detailed methodology and results ensure transparency and clarity.

---

This project enhances decision-making for used car pricing while providing an intuitive platform for real-time predictions.