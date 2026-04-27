# Spotify User Review Sentiment Analysis

Streamlit:
https://nbspotifypridiction-l6ea8e8fdqq2rvuyknfmei.streamlit.app/

Hugging Face:
https://huggingface.co/spaces/VTharun616/nb_spotify?logs=container

## 1. Project Overview
This project focuses on sentiment analysis of Spotify user reviews using Machine Learning techniques. 
The goal is to classify user reviews into positive or negative sentiments based on the text content.
The project includes full data preprocessing, feature engineering using TF-IDF, model training with multiple 
ML algorithms, evaluation, and deployment using Streamlit + Hugging Face Spaces.

## 2. Workflow

1. Data Preprocessing
Lowercasing text
Removing special characters using regex
Removing stopwords (NLTK)
Handling missing values
Removing duplicates
2. Feature Engineering
Converted text into numerical format using TF-IDF Vectorization
Split dataset into training (80%) and testing (20%)
3. Machine Learning Models Used
Naive Bayes (Best Model)
Multinomial Naive Bayes
Other Models Tested
K-Nearest Neighbors (KNN)
Decision Tree Classifier
Logistic Regression
Support Vector Machine (SVM)
Ensemble Models
Random Forest (Bagging)
AdaBoost (Boosting)
Voting Classifier
Stacking Classifier

## 3. Evaluation Metrics
Accuracy Score
Precision, Recall, F1-score
Confusion Matrix
ROC-AUC Curve

## 4. Best Model
Multinomial Naive Bayes
Chosen because:
Simple and fast
Works best for text classification
Good accuracy

## 5. Model Saving
nb_model.pkl
vectorizer.pkl

## 6. Tech Stack
Python
Pandas, NumPy
NLTK
Scikit-learn
Matplotlib, Seaborn
Streamlit
TF-IDF

## 7. Key Learnings
NLP preprocessing
TF-IDF vectorization
ML model comparison
Evaluation techniques
Deployment basics

## Author
Tharun Kumar Vadde

