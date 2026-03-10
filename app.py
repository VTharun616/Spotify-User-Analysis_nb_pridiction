import streamlit as st
import pickle
import pandas as pd
import numpy as np

st.title("SPOTIFY USER REVIEW ANALYSIS 🎵")

with open("nb_model.pkl", "rb") as f:
    model = pickle.load(f)

with open("vectorizer.pkl", "rb") as f:
    vectorizer = pickle.load(f)


user_review = st.text_area("Enter your Spotify user review here:")

if st.button("Analyze Review"):
    if not user_review.strip():
        st.warning("Please enter a review first.")
    else:
        
        vector_input = vectorizer.transform([user_review])
        
        
        prediction = model.predict(vector_input)[0]
        
        
        if prediction == "positive":
            st.success(f"Predicted sentiment: 👍 Positive")
        else:
            st.error(f"Predicted sentiment: 👎 Negative")