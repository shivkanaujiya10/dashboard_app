import streamlit as st
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
import plotly.express as px

st.set_page_config(layout="wide",page_icon="🎉",page_title="Pokemon Dashboard",)

@st.cache_data
def load_data():
    file = "Pokemon.csv"
    data = pd.read_csv(file)
    return data

def main():
    st.markdown()
    st.image("hero_image.jpg", use_column_width=True)
    st.title("Pokemon Dashboard")
    with st.spinner("Loading Pokemon..."):
        df = load_data()
    # st.snow()
    rows, columns = df.shape
    col_names = df.columns.tolist()

    c1,c2,c3 = st.columns(3)
    c1.subheader(f"Total Rows: {rows}")
    c2.subheader(f"Total Columns: {columns}")
    c3.subheader(f"Columns: {", ".join(col_names)}")

# yaha double underscore h 4 baar
if __name__ == "__main__":
    main()
