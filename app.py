import streamlit as st
from src.core.analyzer import analyze_resume
from src.utils.file_handler import (save_uploaded_file_to_temp, delete_temp_file)

from src.ui.header import render_header
from src.ui.upload_section import render_upload_section
from src.ui.results import render_results

# -----------------------------------------
# PAGE CONFIGURATION
# -----------------------------------------

st.set_page_config(
    page_title = "CareerAi",
    page_icon = "📄",
    layout = "wide"
)

# -----------------------------------------
# HEADER
# -----------------------------------------

render_header()

# -----------------------------------------
# UPLOAD SECTION
# -----------------------------------------

resume_file, jd_file, analyze_button = render_upload_section()

# -----------------------------------------
# ANALYSIS
# -----------------------------------------

if analyze_button:
    if resume_file is None or jd_file is None:
        st.warning("Please upload both files.")
    else:

        temp_resume = save_uploaded_file_to_temp(resume_file)
        temp_jd = save_uploaded_file_to_temp(jd_file)

        try:
            with st.spinner("Analyzing Resume..."):
                result = analyze_resume(temp_resume, temp_jd)
            
            render_results(result)

        finally:
            delete_temp_file(temp_resume)
            delete_temp_file(temp_jd)
