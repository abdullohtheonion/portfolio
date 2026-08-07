import streamlit as st
import pandas

st.set_page_config(layout="wide")

col1, col2 = st.columns(2)

with col1:
    st.image("images/photo.jpg")

with col2:
    st.title("Abdulloh Abduvaliyev")
    content = """
        Hi, I am Abdulloh! I am a Python programmer, student, and future founder of snowblind company. I graduated in 2026 with perfect GPA & SAT Math score from Rahimov School.
    I haven't yet worked with companies, but I'm to cook the industry. Let's go!!
    """
    st.info(content)

st.text("This is the end! Hold your breath, and count to ten! Feel the earth move, and then. Hear my heart burst agaaiin. For this is the end! I've drowned and dreamt this moment.")

col3, empty_col, col4 = st.columns([1.5, .5, 1.5])

df = pandas.read_csv("data.csv", sep=";")

with col3:
    for index, row in df[:10].iterrows():
        st.header(row["title"])
        st.write(row["description"])
        st.image("images/" + row["image"])
        st.write("[Source code](https://youtu.be/dQw4w9WgXcQ?si=i8oH61ZEi7IvvEpk)")

with col4:
    for index, row in df[10:].iterrows():
        st.header(row["title"])
        st.write(row["description"])
        st.image("images/" + row["image"])
        st.write("[Source code](https://youtu.be/dQw4w9WgXcQ?si=i8oH61ZEi7IvvEpk)")
