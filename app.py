import streamlit as st
from src.core.analyzer import analyze_resume
from src.utils.file_handler import (save_uploaded_file_to_temp, delete_temp_file)

st.set_page_config(
    page_title = "CareerAi",
    page_icon = "📄",
    layout = "wide"
)

st.title("📄 CareerAi")
st.subheader("AI Powered Resume Analyzer")

st.write(
    "Upload your resume and job description to compare your skills"
)

resume_file = st.file_uploader(
    "Upload Resume (PDF)",
    type = ["pdf"]
)

jd_file = st.file_uploader(
    "Upload Job Description",
    type = ["txt"]
)

analyze_button = st.button(
    "Analyze Resume"
)

if analyze_button:
    if resume_file is None or jd_file is None:
        st.warning("Please upload both files.")
    else:

        temp_resume = save_uploaded_file_to_temp(resume_file)
        temp_jd = save_uploaded_file_to_temp(jd_file)

        try:
            with st.spinner("Analyzing Resume..."):
                result = analyze_resume(temp_resume, temp_jd)
            
            st.success("Analysis Complete!")

            st.divider()

            st.subheader("📊 Match Score")

            st.metric(
                label = "Overall Match",
                value = f"{result['score']}%"
            )

            st.subheader("✅ Matched Skills")

            if result["matched"]:
                for skill in sorted(result["matched"]):
                    st.success(skill)

            else:
                st.info("No matching skills found!")

            st.subheader("❌ Missing Skills")

            if result["missing"]:
                for skill in sorted(result["missing"]):
                    st.error(skill)

            else:
                st.success("No missing skills!")

        finally:
            delete_temp_file(temp_resume)
            delete_temp_file(temp_jd)
