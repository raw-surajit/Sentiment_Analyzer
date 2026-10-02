import streamlit as st
import joblib
import string
import nltk
from nltk.corpus import stopwords

# Download stopwords quietly
nltk.download('stopwords', quiet=True)
stop_words = set(stopwords.words('english'))

# 1. Load the serialized Colab models
vectorizer = joblib.load('tfidf_vectorizer.pkl')
model = joblib.load('sentiment_model.pkl')

# 2. Define the exact preprocessing function used in your training
def preprocess_text(text):
    # 1. Convert to lowercase
    text = text.lower()
    
    # 2. Strip all punctuation from the string using the translation table method
    text = text.translate(str.maketrans('', '', string.punctuation))
    
    # 3. Tokenize and remove stopwords
    words = text.split()
    cleaned_words = [word for word in words if word not in stop_words]
    
    # 4. Remove standalone numbers (as done in the tutorial)
    cleaned_words = [word for word in cleaned_words if not word.isdigit()]
    
    return " ".join(cleaned_words)

# 3. Streamlit UI
st.title("Emotion & Sentiment Analysis")
st.write("Enter a sentence below to predict the underlying emotion.")

user_input = st.text_area("Text Input:", "I am feeling very happy today!")

if st.button("Predict Emotion"):
    if user_input.strip():
        # Apply preprocessing
        cleaned_text = preprocess_text(user_input)
        
        # Vectorize (must be passed as a list)
        vectorized_input = vectorizer.transform([cleaned_text])
        
        # Predict
        prediction = model.predict(vectorized_input)[0]
        
        # Map numeric predictions to text labels based on your Colab mapping
        emotion_mapping = {0: 'Sadness', 1: 'Anger', 2: 'Love', 3: 'Surprise', 4: 'Fear', 5: 'Joy'}
        predicted_emotion = emotion_mapping.get(prediction, "Unknown")
        
        st.success(f"Predicted Emotion: **{predicted_emotion}**")
    else:
        st.warning("Please enter text to analyze.")