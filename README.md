# Emotion & Sentiment Analysis Web App 🧠💬

![Python](https://img.shields.io/badge/Python-3.8%2B-blue)
![Streamlit](https://img.shields.io/badge/Streamlit-Framework-red)
![Scikit-Learn](https://img.shields.io/badge/Scikit--Learn-Machine%20Learning-orange)
![NLTK](https://img.shields.io/badge/NLTK-NLP-green)

A Natural Language Processing (NLP) end-to-end machine learning project that classifies text into six distinct emotional categories: **Sadness, Anger, Love, Surprise, Fear, and Joy**. 

The model was trained on text data using TF-IDF vectorization and Logistic Regression. It is deployed as an interactive web application using Streamlit, allowing users to type in any sentence and instantly see the predicted underlying emotion.

## 🌟 Features
* **Custom Text Preprocessing:** Automatically removes punctuation and stop words using `nltk` to ensure high prediction accuracy.
* **Trained ML Model:** Utilizes a highly efficient Logistic Regression model built with `scikit-learn`.
* **Interactive UI:** A clean, user-friendly frontend powered by Streamlit.
* **Instant Predictions:** Real-time inference through serialized `.pkl` models (`joblib`).

## 🛠️ Technology Stack
* **Language:** Python
* **Machine Learning:** Scikit-Learn, Pandas, NumPy
* **NLP:** NLTK (Natural Language Toolkit)
* **Frontend:** Streamlit
* **Model Serialization:** Joblib

## 📂 Project Structure
```text
Sentiment Analysis/
│
├── app.py                   # Main Streamlit application script
├── sentiment_model.pkl      # Serialized Logistic Regression model
├── tfidf_vectorizer.pkl     # Serialized TF-IDF text vectorizer
├── requirements.txt         # Python dependencies
├── .gitignore               # Files ignored by git (e.g., venv/)
└── README.md                # Project documentation
```

## 🚀 How to Run the Project Locally

Follow these instructions to get a copy of the project up and running on your local machine.

### 1. Prerequisites
Make sure you have Python installed on your system (Python 3.8 or higher is recommended). You can download it from [python.org](https://www.python.org/).

### 2. Clone the Repository
```bash
git clone https://github.com/raw-surajit/Sentiment_Analyzer.git
cd "Sentiment Analysis"
```
*(Note: If you haven't uploaded this to GitHub yet, simply open your terminal and navigate to the project folder).*

### 3. Create a Virtual Environment
It is highly recommended to use a virtual environment to avoid conflicts with other projects.

**For Windows:**
```bash
python -m venv venv
venv\Scripts\activate
```

**For macOS / Linux:**
```bash
python3 -m venv venv
source venv/bin/activate
```

### 4. Install Dependencies
Install all required libraries using the `requirements.txt` file:
```bash
pip install -r requirements.txt
```

### 5. Launch the Application
Run the Streamlit server:
```bash
streamlit run app.py
```

### 6. Usage
1. After running the command above, your default web browser will automatically open a new tab to `http://localhost:8501`.
2. Type or paste a sentence into the text box (e.g., *"I am absolutely thrilled about my new job!"*).
3. Click the **Predict Emotion** button.
4. The app will preprocess your text, pass it through the trained model, and display the predicted emotion.

## 💡 Notes on NLTK Data
The application automatically downloads the necessary `stopwords` corpus from NLTK quietly in the background when the script runs. No manual NLTK downloads are required by the user!

## 🤝 Contributing
Contributions, issues, and feature requests are welcome! Feel free to check the issues page if you want to contribute.

## 📝 License
This project is open-source and available under the [MIT License](LICENSE).