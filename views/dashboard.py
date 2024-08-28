import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt

st.title("📊 Data Dashboard")
st.write("In questa pagina potrai analizzare i tuoi dati ricavandone tabelle e grafici! Ti basterà inserire un file in formato CSV ed il gioco è fatto!")
st.write("---")

uploaded_file = st.file_uploader("Seleziona un file CSV", type="csv")

if uploaded_file is not None:
    df = pd.read_csv(uploaded_file)

    st.subheader("Data Preview")
    st.write(df.head())

    st.subheader("Data Summary")
    st.write(df.describe())

    st.subheader("Filter Data")
    columns = df.columns.tolist()
    selected_column = st.selectbox("Select column to filter by", columns)
    unique_values = df[selected_column].unique()
    selected_value = st.selectbox("Select value", unique_values)

    filtered_df = df[df[selected_column] == selected_value]
    st.write(filtered_df)

    st.subheader("Plot Data")
    x_column = st.selectbox("Select the X axis column", columns)
    y_column = st.selectbox("Select the Y axis column", columns)

    if st.button("Generate PLot"):
        st.line_chart(filtered_df.set_index(x_column)[y_column])
    else:
        st.write("Waiting on file upload...")