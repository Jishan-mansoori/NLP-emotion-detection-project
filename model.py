import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.linear_model import LogisticRegression
from sklearn.pipeline import Pipeline
from sklearn.metrics import accuracy_score, classification_report
import joblib

# load the dataset
df = pd.read_csv("data/emotion_dataset.csv", sep="\t")

#split data
X_train,X_test, y_train,y_test = train_test_split(
    df["text"],df["label"],test_size =0.2,random_state = 42,stratify=df["label"]
)

# create ml pipeline
model = Pipeline([
    ("tfidf", TfidfVectorizer(max_features = 10000,ngram_range =(1,2),stop_words="english")),
    ("clf", LogisticRegression(max_iter = 200))
])

# train model

model.fit(X_train,y_train)

# prediction
y_pred = model.predict(X_test)

# evaluation
print("accuracy:", accuracy_score(y_test, y_pred))
print("classification report:")
print(classification_report(y_test, y_pred))

# save model

joblib.dump(model, "emotion_model.pkl")

print("model saved as emotion_model.pkl")
