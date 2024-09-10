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
    st.markdown("")
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

    c1.metric("Total Power", df.Total.sum(), delta=df.Total.mean())

    count = df['Type 1'].value_counts()
    fig, ax = plt.subplots(figsize=(10,5))
    sns.barplot(x=count.index, y=count, ax=ax)
    plt.xticks(rotation=90)
    c3.pyplot(fig)

    count2 = df['Type 2'].value_counts()
    fig2 = px.bar(count2, count2.index, count2.values)
    c2.plotly_chart(fig2)

    cols = ['Attack','Defense','Sp. Atk','Sp. Def','Speed','HP']
    c1.subheader("Pokemon Stats")
    selections = c1.multiselect("Select Stats", cols, default=['HP','Attack'])

    if selections:
        fig3 = px.scatter_matrix(df, dimensions=selections, color='Generation', height=800)
        st.plotly_chart(fig3, use_container_width=True)
        fig4 = px.histogram(df, x=selections, height=600)
        st.plotly_chart(fig4, use_container_width=True)

    c1, c2, c3, c4 = st.columns(4)
    num_cols = df.select_dtypes(include=[np.number]).columns.tolist()
    cat_cols = df.select_dtypes(exclude=[np.number]).columns.tolist()[1:]
    x = c1.selectbox("Select X-axis", num_cols, index=0)
    y = c2.selectbox("Select Y-axis", num_cols, index=1)
    z = c3.selectbox("Select Hue", num_cols, index=2)
    face = c4.selectbox("Select Face", cat_cols)
 
    fig5 = px.scatter(df, x=x, y=y, color=z, size='Total', hover_name='Name', facet_col=face, height=1000, facet_col_wrap=3)
    st.plotly_chart(fig5, use_container_width=True)

    fig6 = px.scatter_3d(df, x=x, y=y, z=z, color='Generation', size='Total', hover_name='Name', height=800)
    st.plotly_chart(fig6, use_container_width=True)

# yaha double underscore h 4 baar
if __name__ == "__main__":
    main()
