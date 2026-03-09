# NLP Emotion Detection Journal

## Overview

This project is a **Natural Language Processing (NLP) based Emotion Detection System** that analyzes text and predicts the user's emotional state.
The system also allows users to store journal entries and track emotions over time.

The project combines machine learning, NLP techniques, and a web interface for interactive emotion analysis.

---

## Features

* Detect emotions from text input
* Store journal entries with detected emotions
* Interactive web interface
* Emotion prediction using a trained machine learning model
* Local database storage for journal history

---

## Tech Stack

* Python
* Scikit-learn
* Streamlit
* Pandas
* SQLite

---

## Project Structure

```
NLP-emotion-detection-project
│
├── data/
│   └── emotion_dataset.csv
│
├── app.py
├── model.py
├── database.py
├── utils.py
├── emotion_model.pkl
├── journal.db
└── README.md
```

---

## How to Run the Project

1. Clone the repository

```
git clone https://github.com/Jishan-mansoori/NLP-emotion-detection-project.git
```

2. Navigate to the project folder

```
cd NLP-emotion-detection-project
```

3. Install dependencies

```
pip install -r requirements.txt
```

4. Run the Streamlit app

```
streamlit run app.py
```

---

## Example

User Input:

```
I feel very happy today because I finished my project.
```

Prediction:

```
Emotion: Joy
```

---

## Future Improvements

* Add emotion visualization charts
* Deploy the application online
* Improve model accuracy using deep learning
* Add emotion history tracking dashboard

---

## Author

**Jishan Mansoori**

GitHub:
https://github.com/Jishan-mansoori
