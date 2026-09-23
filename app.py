import streamlit as st
import pandas as pd
import os

# --------------------------------------------------
# PAGE CONFIGURATION
# --------------------------------------------------

st.set_page_config(
    page_title="Customer Campaign Analytics",
    page_icon="📊",
    layout="wide"
)

# --------------------------------------------------
# TITLE
# --------------------------------------------------

st.title("📊 Customer Campaign Response Prediction")
st.caption("Interactive Customer Analytics & Machine Learning Dashboard")

# --------------------------------------------------
# LOAD DATA
# --------------------------------------------------

data_path = "data/cleaned_customer_data.csv"

if not os.path.exists(data_path):

    st.error("❌ Dataset not found.")
    st.stop()

df = pd.read_csv(data_path)

st.success("✅ Dataset loaded successfully!")

# --------------------------------------------------
# SIDEBAR
# --------------------------------------------------

st.sidebar.title("🔎 Dashboard Controls")

st.sidebar.info(
    "Use the controls below to explore the customer dataset."
)

# --------------------------------------------------
# EXECUTIVE OVERVIEW
# --------------------------------------------------

st.header("🏠 Executive Overview")

col1, col2, col3, col4 = st.columns(4)

with col1:
    st.metric(
        "👥 Total Customers",
        f"{len(df):,}"
    )

with col2:
    st.metric(
        "📋 Total Features",
        len(df.columns)
    )

with col3:
    st.metric(
        "⚠️ Missing Values",
        int(df.isnull().sum().sum())
    )

with col4:
    st.metric(
        "🔁 Duplicate Rows",
        int(df.duplicated().sum())
    )

st.divider()

# --------------------------------------------------
# DATASET INFORMATION
# --------------------------------------------------

st.header("📊 Dataset Overview")

col1, col2 = st.columns(2)

with col1:

    st.subheader("Dataset Shape")

    st.write(
        f"**Rows:** {df.shape[0]:,}"
    )

    st.write(
        f"**Columns:** {df.shape[1]}"
    )

with col2:

    st.subheader("Data Quality")

    missing = int(df.isnull().sum().sum())
    duplicates = int(df.duplicated().sum())

    if missing == 0:
        st.success("✅ No missing values")

    else:
        st.warning(
            f"⚠️ {missing:,} missing values found"
        )

    if duplicates == 0:
        st.success("✅ No duplicate rows")

    else:
        st.warning(
            f"⚠️ {duplicates:,} duplicate rows found"
        )

# --------------------------------------------------
# CUSTOMER DATA
# --------------------------------------------------

st.header("👥 Customer Data")

st.write(
    "Use the table below to explore the customer dataset."
)

st.dataframe(
    df,
    use_container_width=True,
    height=450
)

# --------------------------------------------------
# STATISTICS
# --------------------------------------------------

st.header("📈 Dataset Statistics")

numeric_columns = df.select_dtypes(
    include="number"
).columns

if len(numeric_columns) > 0:

    st.dataframe(
        df[numeric_columns].describe().T,
        use_container_width=True
    )

else:

    st.info(
        "No numeric columns available for statistical analysis."
    )

# --------------------------------------------------
# COLUMN INFORMATION
# --------------------------------------------------

st.header("🧾 Column Information")

column_info = pd.DataFrame({
    "Column": df.columns,
    "Data Type": df.dtypes.astype(str),
    "Missing Values": df.isnull().sum().values,
    "Unique Values": [
        df[column].nunique()
        for column in df.columns
    ]
})

st.dataframe(
    column_info,
    use_container_width=True
)

# --------------------------------------------------
# AVAILABLE DATASET COLUMNS
# --------------------------------------------------

st.header("🔍 Available Dataset Columns")

st.write(
    "The following columns are available in the cleaned dataset:"
)

st.write(df.columns.tolist())

# --------------------------------------------------
# FOOTER
# --------------------------------------------------

st.divider()

st.caption(
    "Customer Campaign Response Prediction Dashboard | "
    "Built with Python, Pandas and Streamlit"
)
