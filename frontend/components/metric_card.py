import streamlit as st


def metric_card(
    title: str,
    value,
    icon: str,
    color: str = "#3B82F6",
    subtitle: str = "",
):
    st.markdown(
        f"""
<div class="crm-card">

    <div
        class="crm-card-top"
        style="border-top:4px solid {color};"
    >

        <div class="crm-card-icon">
            {icon}
        </div>

        <div class="crm-card-title">
            {title}
        </div>

    </div>

    <div class="crm-card-value">
        {value}
    </div>

    <div class="crm-card-subtitle">
        {subtitle}
    </div>

</div>
""",
        unsafe_allow_html=True,
    )