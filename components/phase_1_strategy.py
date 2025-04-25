import streamlit as st
from .utils import build_dial

def display():
    # --- Summary Block ---
    st.markdown("""
        <style>
            .phase1-summary {
                background-color: #e3f2fd;
                color: #0d3d66;
                padding: 2rem;
                margin-bottom: 2rem;
                border-radius: 1rem;
                box-shadow: 0 4px 12px rgba(0, 0, 0, 0.1);
            }
            .phase1-summary h3 {
                font-size: 1.8rem;
                margin-bottom: 0.5rem;
            }
            .phase1-summary p {
                font-size: 1.1rem;
            }
        </style>
        <div class="phase1-summary">
            <h3>Phase 1 (Strategy) Overview</h3>
            <p>
                This section highlights strategic KPIs for Phase 1 execution. The gauges below represent progress toward critical foundational goals for the company’s strategic positioning.
            </p>
        </div>
    """, unsafe_allow_html=True)

    # --- KPI Definitions ---
    kpis = {
        "Assemble Strategy Unit": {
            "desc": "Hire 2–4 additional members including a COO to help operationalize execution.",
            "example": "E.g. 3 new hires including a COO.",
            "value": 1,
            "total": 4,
            "icon": "👥"
        },
        "Product Audit": {
            "desc": "Evaluate readiness, differentiation, and market alignment of 6 internal projects.",
            "example": "E.g. 2 projects evaluated for market readiness.",
            "value": 1,
            "total": 6,
            "icon": "🧪"
        },
        "Directory Development": {
            "desc": "Populate an internal directory of employee skills, resumes, and capabilities.",
            "example": "E.g. 3 employee profiles completed.",
            "value": 1,
            "total": 4,
            "icon": "📇"
        },
        "Pilot Launch": {
            "desc": "Launch 2–3 most viable projects in Iran.",
            "example": "E.g. 2 pilot products launched in Iran.",
            "value": 1,
            "total": 3,
            "icon": "🚀"
        },
        "VC Funnel Prioritization": {
            "desc": "Categorize 240 venture proposals into kill, incubate, or fast-track.",
            "example": "E.g. 80 proposals processed.",
            "value": 1,
            "total": 240,
            "icon": "📊"
        }
    }

    # --- KPI Layout ---
    for i, (kpi_name, kpi) in enumerate(kpis.items(), start=1):
        st.markdown(" ")  # white space
        col1, col2 = st.columns([2, 1])

        with col1:
            st.markdown(f"""
                <div style='font-size: 1.4rem; font-weight: bold; color: #1565c0; margin-bottom: 0.5rem;'>
                    {kpi['icon']} {kpi_name} <span style='font-size: 0.9rem;'>({i} / {len(kpis)})</span>
                </div>
                <div style='font-size: 1.05rem; color: #0d47a1; line-height: 1.5;'>
                    <b>Description:</b> {kpi['desc']}<br>
                    <b>Example:</b> <i>{kpi['example']}</i><br>
                    <b>Progress:</b> {kpi['value']} / {kpi['total']}
                </div>
            """, unsafe_allow_html=True)

        with col2:
            build_dial(kpi_name, kpi['value'], kpi['total'], "#4fc3f7", key_prefix="phase1")

        st.markdown(" ")  # white space
        st.markdown("---")  # horizontal separator
