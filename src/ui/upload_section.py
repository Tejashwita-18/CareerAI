import streamlit as st

def render_upload_section():
    """
    Render the upload section.

    Returns:
        tuple: resume_file, jd_file, analyze_button
    """

    col1, col2 = st.columns(2, gap="large")

    with col1:

        st.markdown("### 📄 Resume")

        resume_file = st.file_uploader(
            "Upload your Resume",
            type = ["pdf"],
            label_visibility = "collapsed"
        )

    with col2:

        st.markdown("### 💼 Job Description")

        jd_file = st.file_uploader(
            "Upload your Job Description",
            type = ["txt"],
            label_visibility = "collapsed"
        )

    st.write("")

    col1,col2,col3 = st.columns([2.5,1,2.5])

    with col2:

        analyze_button = st.button(
            "🚀 Analyze Resume",
            use_container_width = True
        )

    return resume_file, jd_file, analyze_button
