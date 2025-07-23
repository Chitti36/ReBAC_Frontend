import streamlit as st
import pandas as pd
import requests

import streamlit as st
API_URL = st.secrets["API_URL"]


st.set_page_config(page_title="ReBAC Policy ML App", layout="wide")
st.title("🔐 ReBAC Policy Rule Extractor")

uploaded_file = st.file_uploader("📤 Upload a CSV file (ReBAC format)", type=["csv"])

if uploaded_file:
    st.success("✅ File uploaded! Click below to train model.")
    
    if st.button("🚀 Train & Extract Policies"):
        with st.spinner("Training model..."):
            response = requests.post(
                f"{API_URL}/train",
                files={"file": (uploaded_file.name, uploaded_file, "text/csv")},
            )
        if response.status_code == 200:
            auc = response.json().get("roc_auc", "N/A")
            st.success(f"🎯 Model trained successfully! ROC-AUC: {auc}")
        else:
            try:
                error_msg = response.json().get("error", "Unknown error")
            except Exception:
                error_msg = response.text  # fallback for non-JSON error
            st.error(f"❌ Training failed: {error_msg}")

if st.button("📜 Show Extracted Rules"):
    with st.spinner("Loading rules..."):
        response = requests.get(f"{API_URL}/rules")
    if response.status_code == 200:
        rules = response.json()["rules"]
        for i, rule in enumerate(rules):
            st.markdown(f"**{i+1}.** {rule}")
    else:
        st.error("❌ Failed to load rules.")

if st.button("🚨 Show False Positives"):
    with st.spinner("Detecting false positives..."):
        response = requests.get(f"{API_URL}/false_positives")
    if response.status_code == 200:
        fps = response.json()["false_positives"]
        if fps:
            df_fps = pd.DataFrame(fps)
            st.write("🔎 False Positives Found:")
            st.dataframe(df_fps)
        else:
            st.success("✅ No false positives detected!")
    else:
        st.error("❌ Could not retrieve false positives.")
