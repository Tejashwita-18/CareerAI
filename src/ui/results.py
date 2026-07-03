import streamlit as st

def render_results(result):
    """
    Display analysis result.
    """

    st.success("Analysis Complete!")

    st.divider()

    score_col, summary_col = st.columns(2)

    with score_col:
        st.subheader("📊 Match Score")

        st.metric(
            label = "Overall Match",
            value = f"{result['score']}%"
        )

    with summary_col:
        st.subheader("📋 Summary")

        st.write(f"✅ Matched Skills: {len(result['matched'])}")

        st.write(f"❌ Missing Skills: {len(result['missing'])}")

    st.write("")

    matched_col, missing_col = st.columns(2)

    with matched_col:
        st.subheader("✅ Matched Skills")

        if result["matched"]:
            for skill in sorted(result["matched"]):
                st.success(skill)

        else:
            st.info("No matching skills found!")

    with missing_col:
        st.subheader("❌ Missing Skills")

        if result["missing"]:
            for skill in sorted(result["missing"]):
                st.error(skill)

        else:
            st.success("No missing skills!")
