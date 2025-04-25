import streamlit as st
import plotly.graph_objects as go

def display():
    # --- Summary Block ---
    st.markdown("""
        <style>
            .exec-summary {
                background-color: #333333;
                color: #ffffff;
                padding: 2rem;
                margin-bottom: 2rem;
                border-radius: 1rem;
                box-shadow: 0 4px 12px rgba(0, 0, 0, 0.3);
            }
            .exec-summary h3 {
                font-size: 1.8rem;
                margin-bottom: 0.5rem;
            }
            .exec-summary p {
                font-size: 1.1rem;
            }
        </style>
        <div class="exec-summary">
            <h3>Executive Summary</h3>
            <p>
                This section provides an overview of core strategic KPIs during the Foundation phase. Each KPI reflects a critical milestone in building internal capacity, auditing products, and preparing for pilot launches.
            </p>
        </div>
    """, unsafe_allow_html=True)

    # --- KPI Definitions ---
    kpis = {
        "Assemble Strategy Unit": {
            "desc": "Hire 6 additional members to help develop AIVS business and operationalize execution.",
            "subkpi": "# VP, PMO, Financial Director, Legal Director, AIVS Internal Market Researcher, AIVS International Market Researcher",
            "value": 1,
            "total": 6,
            "color": "#1f77b4",
            "textcolor": "#0d3d66",
            "criticality": "red",
            "icon": "👥"
        },
        "Product Audit": {
            "desc": "Evaluate readiness, differentiation, and market alignment of 6 internal products.",
            "subkpi": "# Expert Finder Product, Customer Engagement and Capability Matcher (CECM) Product, Lead Generator, etc.",
            "value": 0,
            "total": 6,
            "color": "#2ca02c",
            "textcolor": "#1a661a",
            "criticality": "red",
            "icon": "🧪"
        },
        "Directory Development": {
            "desc": "Populate an internal directory of 10 AIVS venture teams.",
            "subkpi": "# Employee Profiles:  Skills, Resumes, and Capabilities.",
            "value": 0,
            "total": 10,
            "color": "#ff7f0e",
            "textcolor": "#c25e00",
            "criticality": "red",
            "icon": "📇"
        },
        "Pilot Launch": {
            "desc": "Launch 1–3 most viable projects in Iran.",
            "subkpi": "# Steel and Petrochemical CECM Product launched AIVS. Expert Finder Product launched within CECM Product. Lead Generator Product launched within CECM Product",
            "value": 0,
            "total": 3,
            "color": "#9467bd",
            "textcolor": "#5c3b82",
            "criticality": "yellow",
            "icon": "🚀"
        },
        "Brand Positioning": {
            "desc": "Define AIVS's core brand messaging and value proposition in a differentiated branding package.",
            "subkpi": "# Develop Company Name, Company Logo, Vision, Mission Statement",
            "value": 0,
            "total": 4,
            "color": "#e377c2",
            "textcolor": "#9c3d84",
            "criticality": "yellow",
            "icon": "🎯"
        },
        "VC Funnel Prioritization": {
            "desc": "Categorize 240 venture proposals into kill, incubate, or fast-track.",
            "subkpi": "# Proposals Triaged/Incubated Killed.",
            "value": 1,
            "total": 240,
            "color": "#d62728",
            "textcolor": "#8a1a1a",
            "criticality": "green",
            "icon": "📊"
        }
    }

    criticality_colors = {
        "red": "🔴 Critical",
        "yellow": "🟡 Moderate",
        "green": "🟢 Healthy"
    }

    # --- KPI Layout ---
    for i, (kpi_name, kpi) in enumerate(kpis.items(), start=1):
        st.markdown(" ")  # white space
        col1, col2 = st.columns([2, 1])

        with col1:
            st.markdown(f"""
                <div style="font-size: 1.6rem; font-weight: bold; color: {kpi['textcolor']};">
                    {kpi['icon']} {kpi_name} <span style="font-size: 1rem; float: right;">({i}/{len(kpis)})</span>
                </div>
                <div style="font-size: 1rem; font-weight: bold; margin-bottom: 0.5rem; color: {kpi['textcolor']};">
                    {criticality_colors[kpi['criticality']]}
                </div>
                <div style="font-size: 1.05rem; color: {kpi['textcolor']};">
                    <b>Description:</b> {kpi['desc']}<br>
                    <b>Sub-KPI:</b> {kpi['subkpi']}<br>
                </div>
            """, unsafe_allow_html=True)

            # Progress label and bar
            st.markdown(f"<div style='font-weight: bold; margin-top: 0.5rem;'>Progress:</div>", unsafe_allow_html=True)
            st.progress(kpi["value"] / kpi["total"])

        with col2:
            fig = go.Figure(go.Pie(
                labels=["Progress", "Remaining"],
                values=[kpi['value'], kpi['total'] - kpi['value']],
                marker=dict(
                    colors=[kpi['color'], "#d3d3d3"],
                    line=dict(color='#FFFFFF', width=2)
                ),
                hole=0.5,
                textinfo="none"
            ))
            fig.update_layout(
                margin=dict(t=0, b=0, l=0, r=0),
                showlegend=False,
                height=200,
                width=200,
                paper_bgcolor='rgba(0,0,0,0)',
            )
            st.plotly_chart(fig, use_container_width=True)

        st.markdown(" ")  # white space
        st.markdown("---")  # separator
