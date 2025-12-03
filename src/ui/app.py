import streamlit as st

from settings import settings
from utilities.api_functions import *

st.title("Inspect AI App Example")

st.header("Evaluation Datasets")

datasets = available_datasets()
dataset_name = st.selectbox("Select an evaluation dataset", datasets)

dataset_cached = is_dataset_cached(dataset_name)
st.markdown(f"**Dataset cached:** {str(dataset_cached).lower()}")

st.header("Run Evalutation")