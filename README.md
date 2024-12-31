# **Insurance Data Analysis and Modeling**

## **Project Overview**
This project is focused on exploring and modeling insurance data with the goal of predicting key metrics like **TotalPremium** and **TotalClaims**. The project incorporates data exploration, hypothesis testing, version control, and statistical modeling techniques.

---

## **Git and GitHub Setup**

### **Overview**
The initial setup involves using **Git** and **GitHub** for tracking and collaborating on the project. The repository hosts all the code for data analysis and model building.

### **Key Actions:**
- Created a GitHub repository for the project.
- Used version control for managing and collaborating on the codebase.
- Implemented CI/CD pipelines with GitHub Actions for automatic testing and deployment.

### **Key Metrics:**
- GitHub repository management.
- Git commits with descriptive messages.
- Integration of CI/CD workflows.

---

## **Data Version Control (DVC)**

### **Overview**
This section involves incorporating **Data Version Control (DVC)** to manage and track the datasets throughout the project. DVC ensures that the datasets are consistently versioned, making it easier to reproduce results and share data between team members.

### **Key Actions:**
- Installed and initialized DVC for the project.
- Configured local remote storage for storing dataset versions.
- Added and committed data files to DVC for version control.
- Pushed data to the local remote storage.

### **Key Metrics:**
- Data versioning with DVC.
- Local remote storage setup and configuration.

---

## **A/B Hypothesis Testing**

### **Overview**
In this phase, **A/B Hypothesis Testing** was conducted to test several null hypotheses about the data. The goal was to assess whether there were statistically significant differences across certain factors like gender, province, and zip code.

### **Key Actions:**
- Selected Key Performance Indicators (KPIs) to measure the impact of the features.
- Segmented the data into two groups: Control (Group A) and Test (Group B).
- Conducted statistical tests (Chi-squared, t-test, or z-test) to evaluate differences.
- Analyzed p-values to determine whether to accept or reject the null hypotheses.

### **Hypotheses Tested:**
1. There are no risk differences across provinces.
2. There are no risk differences between zip codes.
3. There are no significant margin (profit) differences between zip codes.
4. There are no significant risk differences between women and men.

### **Key Metrics:**
- Hypothesis testing results (accept or reject null hypotheses).
- p-values analysis to determine statistical significance.

---

## **Statistical Modeling**

### **Overview**
In this phase, predictive models were built to estimate **TotalPremium** and **TotalClaims**. This includes data preparation, model implementation, and evaluation using various machine learning techniques.

### **Key Actions:**
- **Data Preparation**: 
  - Handled missing data (imputation/removal).
  - Engineered new features.
  - Encoded categorical data using one-hot encoding.
  - Split data into training and test sets.
  
- **Model Building**:
  - Built models using **Linear Regression**, **Random Forest**, and **XGBoost** algorithms.

- **Model Evaluation**:
  - Evaluated models using **Mean Absolute Error (MAE)**, **Mean Squared Error (MSE)**, and **R²**.
  
- **Feature Importance Analysis**:
  - Used Random Forest and XGBoost to assess feature importance.
  - Implemented SHAP for model interpretability.

### **Key Metrics:**
- Model performance: **MAE**, **MSE**, **R²**.
- Feature importance analysis.
- SHAP values for model interpretability.