# 🤖 End-to-End Customer Churn Prediction Platform

Welcome to my **Customer Churn Prediction Platform** project! This project demonstrates a complete data science workflow — from raw data ingestion, transformation, and model training to deployment as an interactive web application.

**[➡️ Try the Live App Here!](https://churnpredictionplatform-qzmauwrpwwp7ofsssxx8jp.streamlit.app/)**
---

## 🎯 Project Background & Objectives

*Customer churn* — when users stop subscribing or using a service — is a critical problem for subscription-based businesses. Losing customers not only reduces revenue but also increases the cost of acquiring replacements.

This project aims to build an automated system that can:
1. **Identify** high-risk customers **before** they churn.
2. **Provide** an interactive tool for business teams to perform "what-if" analysis on various customer profiles.

---

## 🏗️ System Architecture

This project is built using a modern data stack, separating each phase of the data lifecycle. The workflow is as follows:

![Architecture Diagram](![WhatsApp Image 2025-08-07 at 01 56 56_bfefedfe](https://github.com/user-attachments/assets/d4eb8cd3-5c8c-49a5-8d5f-561657dd2785)
) 

1. **Ingestion:** Raw data is uploaded to **Google Cloud Storage (GCS)**, acting as the data lake.
2. **Warehousing:** Data is loaded into **Google BigQuery** for structured storage and querying.
3. **Transformation:** **dbt (data build tool)** is used to clean, transform, and shape the raw data into analytics-ready models.
4. **Modeling:** A **Jupyter notebook** pulls the transformed data from BigQuery, trains a classification model using **Scikit-learn**, and saves it as a model artifact.
5. **Deployment:** An interactive web app is built using **Streamlit**, loading the trained model and serving predictions to end-users.

---

## 🛠️ Tech Stack

- **Cloud Provider:** Google Cloud Platform (GCP)  
- **Data Storage:** Google Cloud Storage, Google BigQuery  
- **Data Transformation:** dbt (data build tool)  
- **Machine Learning:** Python, Pandas, Scikit-learn  
- **Web Application:** Streamlit  
- **Orchestration & Automation (Local):** Python Scripts, Jupyter Notebook  

---

## 🚀 How to Run the Project Locally

Follow these steps to run the project on your local machine:

1. **Clone the Repository**
    ```bash
    git clone https://github.com/YOUR_USERNAME/ChurnPredictionPlatform.git
    cd ChurnPredictionPlatform
    ```

2. **Install Dependencies**  
   Ensure Python 3.8+ and pip are installed.
    ```bash
    pip install -r requirements.txt
    ```

3. **Set Up Google Cloud Authentication**
    ```bash
    gcloud auth application-default login
    ```

4. **Run dbt Transformations**
    ```bash
    cd churn_analytics
    dbt run
    cd ..
    ```

5. **Launch the Streamlit App**
    ```bash
    streamlit run app.py
    ```
    The app will be available at `http://localhost:8501`.

---

## 📈 Results & Learnings

- The model achieved around **80% accuracy** in predicting churn on the test dataset.
- **Biggest Challenge:** Handling data type inconsistencies between BigQuery, Pandas, and Scikit-learn — highlighting the importance of explicit and consistent data validation.
- This project reinforced the value of modular data architecture and using the right tool for the right task (e.g., dbt for transformations, Streamlit for interactivity).

---

Feel free to fork this project, open an issue, or contribute! 🚀
