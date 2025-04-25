import streamlit as st
from components.executive_summary import display as executive_summary
from components.phase_1_strategy import display as phase_1_strategy
from components.phase_2_market import display as phase_2_market
from components.phase_3_scale import display as phase_3_scale

# Function to display sidebar with radio buttons
def display_sidebar():
    # Set the sidebar width to a smaller value using Streamlit's custom CSS
    st.markdown(
        """
        <style>
            .css-1d391kg {width: 250px;}  /* Adjusts the width of the sidebar */
        </style>
        """, unsafe_allow_html=True)
    
    # Title above the sidebar
    st.sidebar.markdown("# AIVS Co.")
    
    # Define the tab names
    tabs = ["Executive Summary", "Phase 1 (Strategy)", "Phase 2 (Market)", "Phase 3 (Scale)"]
    
    # Use radio buttons for tab selection
    selected_tab = st.sidebar.radio(
        "Select Phase",
        tabs
    )

    # Footer aligned at the bottom (pushed down further)
    st.sidebar.markdown("<div style='margin-top: 250px; text-align: center;'>Powered by AIVS Strategy Labs</div>", unsafe_allow_html=True)
    st.sidebar.markdown("<div style='text-align: center;'>2025 c | All Rights Reserved.</div>", unsafe_allow_html=True)

    return selected_tab

def main():
    st.title("AIVS Strategic Dashboard")

    # Display the custom sidebar with title, radio buttons, and footer
    selected_tab = display_sidebar()

    # Display content based on selected tab
    if selected_tab == "Executive Summary":
        executive_summary()
    elif selected_tab == "Phase 1 (Strategy)":
        phase_1_strategy()
    elif selected_tab == "Phase 2 (Market)":
        phase_2_market()
    elif selected_tab == "Phase 3 (Scale)":
        phase_3_scale()

if __name__ == "__main__":
    main()
