import streamlit as st

def render_upload_section():
    """
    Render the upload section.

    Returns:
        tuple: resume_file, jd_file, analyze_button
    """

    col1, col2 = st.columns(2)

    with col1:
        resume_file = st.file_uploader(
            "📄 Upload Resume",
            type = ["pdf"]
        )

    with col2:
        jd_file = st.file_uploader(
            "💼 Upload Job Description",
            type = ["txt"]
        )

    left, center, right = st.columns([3,1,3])

    with center:
        analyze_button = st.button(
            "🚀 Analyze Resume",
            use_container_width = True
        )

    return resume_file, jd_file, analyze_button
