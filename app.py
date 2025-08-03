import streamlit as st
from utils import extract_text_from_pdf
from granite_api import generate_profile

st.set_page_config(page_title="Faculty Profile Builder", layout="wide")
st.title("📄 Faculty Profile Builder (RAG + Granite)")

uploaded_file = st.file_uploader("Upload Resume (PDF)", type="pdf")

if uploaded_file:
    text = extract_text_from_pdf(uploaded_file)
    if st.button("🚀 Generate Faculty Profile"):
        with st.spinner("Generating profile using IBM Granite..."):
            try:
                profile = generate_profile(text)
                st.success("✅ Profile Generated")
                for key, value in profile.items():
                    st.subheader(key.capitalize())
                    st.write(value)
            except Exception as e:
                st.error(f"❌ Failed to generate profile: {e}")

