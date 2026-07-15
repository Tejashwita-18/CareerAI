import streamlit as st

def load_theme():

    st.markdown(
        """
<style>

/* ----------- Main App ----------- */

.block-container{
    padding-top: 2rem;
    padding_bottom: 2rem;
}

/* ----------- Hero ----------- */

.hero{
    background: #111827;
    border: 1px solid #374151;
    border-radius: 20px;
    padding: 28px 40px;
    margin-bottom: 35px;
}

/* ----------- Upload Card ----------- */

.upload-card{
    background: #1F2937;
    border-radius: 20px;
    padding: 30px;
    margin-top: 15px;
    margin-bottom: 25px;
}

/* File Upload */

section[data-testid="stFileUploader"] {
    border-radius: 14px;
}

/* ----------- Analyze button ----------- */

div.stButton > button{
    width: 100% !important;
    height: 58px !important;
    background: linear-gradient(135deg, #4F46E5, #7C3AED) !important;
    color: #F8FAFC !important;
    font-size: 18px !important;
    font-weight: 700 !important;
    border-radius: 14px !important;
    border: 2px solid #3B82F6 !important;
    padding: 18px 30px !important;
    transition: .25s;
    box-shadow: 0px 0px 18px rgba(59, 130, 246, .25);
}

/* Button Text */

div.stButton button p{
    font-size: 22px !important;
    font-weight: 700 !important;
    margin: 0 !important;
    line-height: 1.2 !important;
}

/* Hover */

div.stButton > button:hover{
    background: linear-gradient(135deg, #6366F1, #8B5CF6) !important;
    border-color: #60A5FA !important;
    transform: translateY(-2px);
    box-shadow: 0px 0px 25px rgba(59, 130, 246, 0.45);
}

/* Click */

div.stButton > button:active{
    transform: scale(0.98)
}

/* ----------- Result Card ----------- */

.result-card{
    background: #1F2937;
    border-radius: 18px;
    padding: 20px;
}

/* ----------- Footer ----------- */

.footer{
    text-align: center;
    color: #9CA3AF;
    padding-top: 30px;
}

</style>
""",
        unsafe_allow_html = True
    )
