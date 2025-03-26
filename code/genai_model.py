import pandas as pd
from transformers import pipeline
import joblib

data = pd.read_csv("data/tickets.csv")
feedback = pd.read_csv("data/feedback.csv")

corpus = data['description'].tolist() + feedback['comments'].tolist()

recommendation_pipeline = pipeline("text-generation", model="gpt2")

def generate_recommendations(prompt):
    result = recommendation_pipeline(prompt, max_length=200, num_return_sequences=1)
    return result[0]['generated_text']

prompt = "Recommend a solution for a slow internet connection"
recommendation = generate_recommendations(prompt)
print("Recommendation:", recommendation)

joblib.dump(recommendation_pipeline, "models/genai_model.pkl")
