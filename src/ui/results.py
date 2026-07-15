import streamlit as st

def render_results(result):
    """
    Display analysis result.
    """

    st.markdown("## 📊 Resume Analysis")

    st.write("")

    metric1, metric2, metric3 = st.columns(3)

    with metric1:

        st.metric(
            "🎯 Match Score",
            f"{result['score']}%"
        )

        st.progress(result["score"]/100)

        if result['score'] >= 80:
            st.success("Excellent Match")
        elif result['score'] >= 60:
            st.info("Good Match")
        elif result['score'] >= 40:
            st.warning("Average Match")
        else:
            st.error("Low Match")

    with metric2:

        st.metric(
            "✅ Matched Skills",
            len(result['matched'])
        )

        st.caption("Skills found in both your resume and job description.")

    with metric3:

        st.metric(
            "❌ Missing Skills",
            len(result['missing'])
        )

        st.caption("Skills required by the job but missing from your resume.")

    st.write("")
    st.write("")

    left, right = st.columns(2, gap="large")

    with left:

        with st.expander(
            f"✅ Matched Skills ({len(result['matched'])})",
            expanded = True
        ):

            for skill in sorted(result["matched"]):
                st.markdown(f"""
                    - ✅ **{skill.title()}**
                """)

    with right:

        with st.expander(
            f"❌ Missing Skills ({len(result['missing'])})",
            expanded = True
        ):

            for skill in sorted(result["missing"]):
                st.markdown(f"""
                    - ❌ **{skill.title()}**
                """)

    # AI Insight

    st.write("")
    st.divider()

    st.subheader("🤖 AI Career Insight")

    st.info(
    """
    🚧 Coming Soon

    Gemini AI will provide:

    • Resume improvement suggestions

    • ATS optimization

    • Skill gap analysis

    • Learning roadmap

    • Interview preparation
    """
    )

    # FOOTER

    st.divider()

    st.caption(
        "Built with ❤️ using Python • Streamlit • Pdfplumber"
    )
