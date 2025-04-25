import streamlit as st
from .utils import build_dial

def display():
    # --- Summary Block ---
    st.markdown("""
        <style>
            .phase3-summary {
                background-color: #C5CAE9;  /* Darker Purple Background */
                color: #512DA8;  /* Dark Purple Text */
                padding: 2rem;
                margin-bottom: 2rem;
                border-radius: 1rem;
                box-shadow: 0 4px 12px rgba(0, 0, 0, 0.1);
            }
            .phase3-summary h3 {
                font-size: 1.8rem;
                margin-bottom: 0.5rem;
            }
            .phase3-summary p {
                font-size: 1.1rem;
            }
        </style>
        <div class="phase3-summary">
            <h3>Phase 3 (Scale) Overview</h3>
            <p>
                This section highlights KPIs for Phase 3 (Scale). The gauges below represent progress toward scaling the company's operations and market reach.
            </p>
        </div>
    """, unsafe_allow_html=True)

    # --- KPI Definitions ---
    kpis = {
        "Domestic Expansion": {
            "desc": "Broaden client base across Iran’s industrial and public sectors.",
            "example": "E.g. 2 new clients from public sector.",
            "value": 0,
            "total": 4,
            "icon": "🌍"
        },
        "International Soft Launches": {
            "desc": "Test-market in 1–2 other MENA countries.",
            "example": "E.g. Soft launch in UAE and Qatar.",
            "value": 0,
            "total": 2,
            "icon": "🌐"
        },
        "Partner Ecosystem": {
            "desc": "Build a partner/reseller network for non-Iranian markets.",
            "example": "E.g. 1 new partnership in the GCC region.",
            "value": 0,
            "total": 2,
            "icon": "🤝"
        },
        "Revenue Growth": {
            "desc": "Achieve 10x revenue growth from initial pilots.",
            "example": "E.g. Increase revenue by 3x.",
            "value": 0,
            "total": 10,
            "icon": "📈"
        }
    }

    # --- KPI Layout ---
    for i, (kpi_name, kpi) in enumerate(kpis.items(), start=1):
        st.markdown(" ")  # white space
        col1, col2 = st.columns([2, 1])

        with col1:
            st.markdown(f"""
                <div style='font-size: 1.4rem; font-weight: bold; color: #512DA8; margin-bottom: 0.5rem;'>
                    {kpi['icon']} {kpi_name} <span style='font-size: 0.9rem;'>({i} / {len(kpis)})</span>
                </div>
                <div style='font-size: 1.05rem; color: #512DA8; line-height: 1.5;'>
                    <b>Description:</b> {kpi['desc']}<br>
                    <b>Example:</b> <i>{kpi['example']}</i><br>
                    <b>Progress:</b> {kpi['value']} / {kpi['total']}
                </div>
            """, unsafe_allow_html=True)

        with col2:
            build_dial(kpi_name, kpi['value'], kpi['total'], "#512DA8", key_prefix="phase3")

        st.markdown(" ")  # white space
        st.markdown("---")  # horizontal separator
