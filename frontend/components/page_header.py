from textwrap import dedent

import streamlit as st


def page_header(title, subtitle, icon=""):

    st.markdown(
        dedent(
            f"""
            <div class="page-header">
                <div class="page-title">
                    <span class="page-icon">{icon}</span>
                    <span>{title}</span>
                </div>

                <div class="page-subtitle">
                    {subtitle}
                </div>
            </div>
            """
        ),
        unsafe_allow_html=True,
    )