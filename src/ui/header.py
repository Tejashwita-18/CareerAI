import streamlit as st

def render_header():
    """
    Render the application header
    """

    st.markdown(
        """
<div class="hero">

<h1 align="center">
🎯 CareerAi
</h1>

<h2 align="center">
Your Intelligent Career Assistant
</h2>

<p align="center">
Compare your resume with any job description
and instantly discover your strengths,
missing skills and career opportunities.
</p>

</div>
""",
        unsafe_allow_html = True
    )

    st.markdown("<br>", unsafe_allow_html = True)
