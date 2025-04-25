import streamlit as st
import plotly.graph_objects as go

# --- Reusable pie chart builder ---
def build_pie(title, value, total, color, desc, subkpi, key_prefix):
    fig = go.Figure(go.Pie(
        labels=["Completed", "Remaining"],
        values=[value, total - value],
        hole=0.5,
        marker_colors=[color, "#e0e0e0"]
    ))

    # Title, description, and example text color match pie chart color
    st.markdown(f"<h3 style='color: {color};'>{title}</h3>", unsafe_allow_html=True)
    st.markdown(f"<p style='color: {color};'>{desc}</p>", unsafe_allow_html=True)
    st.markdown(f"<p style='color: {color};'><i>Sub-KPIs: {subkpi}</i></p>", unsafe_allow_html=True)
    st.plotly_chart(fig, use_container_width=True, key=f"{key_prefix}_{title}_pie")

# --- Reusable dial builder ---
def build_dial(kpi_name, value, total, color, key_prefix):
    fig = go.Figure(go.Indicator(
        mode="gauge+number",
        value=value,
        domain={'x': [0, 1], 'y': [0, 1]},
        title={'text': ""},
        gauge={
            'axis': {'range': [0, total]},
            'bar': {'color': color},
            'bgcolor': "white",
            'borderwidth': 1,
            'bordercolor': "gray"
        }
    ))
    fig.update_layout(margin=dict(t=10, b=0, l=0, r=0), height=200)
    st.plotly_chart(fig, use_container_width=True, key=f"{key_prefix}_{kpi_name}_dial")