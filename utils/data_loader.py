import pandas as pd
import streamlit as st

DATA_PATH = "data/"

@st.cache_data
def load_mesh_location():
    return pd.read_csv(DATA_PATH + "mesh_location.csv")

@st.cache_data
def load_mesh_hospital_matrix():
    return pd.read_csv(DATA_PATH + "mesh_hospital_case_matrix.csv")

@st.cache_data
def load_hospital_stress():
    return pd.read_csv(DATA_PATH + "hospital_stress_scores.csv")

@st.cache_data
def load_hospital_groups():
    return pd.read_csv(DATA_PATH + "hospital_stress_with_groups.csv")
