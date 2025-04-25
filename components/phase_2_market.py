import streamlit as st
from .utils import build_dial

def display():
    # --- Summary Block ---
    st.markdown("""
        <style>
            .phase2-summary {
                background-color: #FFF3E0;  /* Light Peach Background */
                color: #FF7043;  /* Vibrant Orange Text */
                padding: 2rem;
                margin-bottom: 2rem;
                border-radius: 1rem;
                box-shadow: 0 4px 12px rgba(0, 0, 0, 0.1);
            }
            .phase2-summary h3 {
                font-size: 1.8rem;
                margin-bottom: 0.5rem;
            }
            .phase2-summary p {
                font-size: 1.1rem;
            }
        </style>
        <div class="phase2-summary">
            <h3>Phase 2 (Market) Overview</h3>
            <p>
                This section focuses on KPIs for Phase 2 (Market) execution. The gauges below represent progress toward critical market positioning and growth goals.
            </p>
        </div>
    """, unsafe_allow_html=True)

    # --- KPI Definitions ---
    kpis = {
        "Industry Partnerships": {
            "desc": "Secure 3–5 pilot clients (B2B) in petrochemical, steel, education sectors.",
            "example": "E.g. 2 pilot clients secured.",
            "value": 0,
            "total": 5,
            "icon": "🏭"
        },
        "Product Refinement": {
            "desc": "Use feedback loops from pilots to iterate rapidly.",
            "example": "E.g. 2 product iterations completed.",
            "value": 0,
            "total": 4,
            "icon": "🔧"
        },
        "Marketing Foundation": {
            "desc": "Build scalable marketing assets (case studies, whitepapers, landing pages).",
            "example": "E.g. 1 whitepaper and 2 landing pages built.",
            "value": 0,
            "total": 3,
            "icon": "📈"
        },
        "Revenue Model Design": {
            "desc": "Define monetization strategies per product type.",
            "example": "E.g. 1 monetization strategy designed for AI products.",
            "value": 0,
            "total": 2,
            "icon": "💰"
        }
    }

    # --- KPI Layout ---
    for i, (kpi_name, kpi) in enumerate(kpis.items(), start=1):
        st.markdown(" ")  # white space
        col1, col2 = st.columns([2, 1])

        with col1:
            st.markdown(f"""
                <div style='font-size: 1.4rem; font-weight: bold; color: #D35400; margin-bottom: 0.5rem;'>
                    {kpi['icon']} {kpi_name} <span style='font-size: 0.9rem;'>({i} / {len(kpis)})</span>
                </div>
                <div style='font-size: 1.05rem; color: #D35400; line-height: 1.5;'>
                    <b>Description:</b> {kpi['desc']}<br>
                    <b>Example:</b> <i>{kpi['example']}</i><br>
                    <b>Progress:</b> {kpi['value']} / {kpi['total']}
                </div>
            """, unsafe_allow_html=True)

        with col2:
            build_dial(kpi_name, kpi['value'], kpi['total'], "#FF7043", key_prefix="phase2")

        st.markdown(" ")  # white space
        st.markdown("---")  # horizontal separator
