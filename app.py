import streamlit as st
import joblib
from database import create_table,insert_entry,get_entries
import pandas as pd
import matplotlib.pyplot as plt


# load trained model
model = joblib.load("emotion_model.pkl")

# create database table
create_table()
st.title("emotion detection app")

st.write("type how you feel and AI will detect your emotion.")

# user input
text = st.text_area("enter your text here")

if st.button("Analyze Emotion"):
    if text.strip()!="":
        emotion = model.predict([text])[0]
        
        insert_entry(text,emotion)
        st.success(f"Detected Emotion:{emotion}")
    else:
        st.warning("please enter some text")
st.subheader("previous entries")
entries = get_entries()

for entry in entries:
    st.write(f"text: {entry[1]}")
    st.write(f"emotion: {entry[2]} ")
    st.write(f"Time: {entry[3]}")
    st.write("---")
    
# display emotion distribution
entries = get_entries()
df = pd.DataFrame(entries, columns=["id","text","emotion","timestamp"])
emotion_counts = df["emotion"].value_counts()
st.bar_chart(emotion_counts)

# mood trend over time
df["timestamp"] = pd.to_datetime(df["timestamp"])

trend = df.groupby([df["timestamp"].dt.date, "emotion"]).size().unstack()

st.line_chart(trend)