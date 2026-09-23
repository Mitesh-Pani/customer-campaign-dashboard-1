import streamlit as st
import pandas as pd
import os

st.set_page_config(
    page_title="Customer Campaign Response Dashboard",
    page_icon="📊",
    layout="wide"
)

st.title("📊 Customer Campaign Response Prediction Dashboard")
st.write("Customer campaign analysis and machine learning dashboard")

# Load dataset
data_path = "data/cleaned_customer_data.csv"

if os.path.exists(data_path):
    df = pd.read_csv(data_path)

    st.success("Dataset loaded successfully!")

    # Overview
    st.header("🏠 Executive Overview")

    col1, col2, col3, col4 = st.columns(4)

    with col1:
        st.metric("Total Customers", len(df))

    with col2:
        st.metric("Total Columns", len(df.columns))

    with col3:
        st.metric(
            "Missing Values",
            int(df.isnull().sum().sum())
        )

    with col4:
        st.metric(
            "Duplicate Rows",
            int(df.duplicated().sum())
        )

    st.divider()

    # Dataset preview
    st.header("👥 Customer Data")

    st.dataframe(
        df,
        use_container_width=True
    )

    # Basic statistics
    st.header("📊 Dataset Statistics")

    st.dataframe(
        df.describe(include="all").transpose(),
        use_container_width=True
    )

else:
    st.error("Dataset not found!")

    st.write("Expected file:")
    st.code("data/cleaned_customer_data.csv")
