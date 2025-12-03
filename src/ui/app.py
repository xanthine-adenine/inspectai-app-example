import streamlit as st

from utilities.api_functions import *

st.title("Inspect AI App Example")

st.header("Evaluation Datasets")

datasets = available_datasets()
dataset_name = st.selectbox("Select an evaluation dataset", datasets)
dataset_loaded = is_dataset_loaded(dataset_name)

st.button("Load Dataset", on_click=load_dataset, args=(dataset_name,))

st.markdown(f"**Dataset loaded:** {str(dataset_loaded).lower()}")

st.header("Run Evalutation")