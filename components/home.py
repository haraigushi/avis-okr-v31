import streamlit as st
from components.org_chart import display as org_chart

def display():
    # First Section: Quote
    st.markdown(
        """
        <div style="border-radius: 15px; padding: 20px; border: 1px solid #ddd; margin-bottom: 20px;">
            <blockquote>
                <p><em>"Diversity in Counsel, Unity in Command."</em></p>
                <p><strong>- Cyrus II</strong></p>
            </blockquote>
        </div>
        """, unsafe_allow_html=True)
    
    # Second Section: AIVS Vision
    st.markdown(
        """
        <div style="border-radius: 15px; padding: 20px; border: 1px solid #ddd; margin-bottom: 20px;">
            <h2>AIVS Vision</h2>
            <h3>The North Star - Where we're going</h3>
            <p><strong>"At AIVS, we move at the speed of innovation and engineer marvels of technology — shaping a world where the next generation has greater access, deeper knowledge, and limitless opportunity."</strong></p>
        </div>
        """, unsafe_allow_html=True)
    
    # Third Section: AIVS Mission Statement
    st.markdown(
        """
        <div style="border-radius: 15px; padding: 20px; border: 1px solid #ddd; margin-bottom: 20px;">
            <h2>AIVS Mission Statement</h2>
            <h3>Daily Actions and Commitments - How we get there</h3>
            <p>At AIVS, our mission is to pioneer a new era of AI venture creation — one defined by extraordinary speed, engineering marvels, and a profound commitment to bridging the global rift in access to technology.</p>
            <p>We exist to accelerate the birth of groundbreaking ventures, turning bold ideas into high-impact realities faster than the world expects — and smarter than the world believes possible.</p>
            <h4>Our mission is anchored on five core concepts:</h4>
            <ul>
                <li><strong>Speed as a Strategic Advantage:</strong> We move decisively, valuing rapid iteration, fast deployment, and operational agility as critical advantages in an age where timing determines victory.</li>
                <li><strong>Engineering at the Level of Marvels:</strong> We engineer not just to solve problems, but to create wonders — building ventures and technologies that endure, inspire, and set new standards for excellence.</li>
                <li><strong>Becoming a Knowledge-Based Organization:</strong> We are committed to growing AIVS into a true learning organization — where knowledge, adaptability, and intellectual capital are systematically cultivated, refined, and scaled through speed and strategic agility.</li>
                <li><strong>Commitment to Scientific Testing and Development:</strong> We approach every venture with scientific rigor — valuing evidence, testing, iteration, and data-driven decision-making as the foundation for sustainable innovation and long-term success.</li>
                <li><strong>Bridging the AI Access Divide:</strong> We are committed to democratizing access to the transformative power of AI, ensuring that the children of tomorrow — wherever they are — inherit the tools to shape their futures with confidence.</li>
            </ul>
            <p>Through the relentless pursuit of speed, marvel, access, learning, and scientific excellence, AIVS is not merely building ventures — we are shaping a future where innovation is swift, enduring, and universally empowering.</p>
        </div>
        """, unsafe_allow_html=True)
    
    # Fourth Section: Org Chart
        # Org chart section with custom style
    with st.container():
        st.markdown(
            """
            <div style="
                background-color: #eaf4fb;
                border-radius: 15px;
                padding: 20px;
                margin-top: 20px;
                border: 1px solid #d1e3f0;
            ">
                <h3 style="margin-bottom: 10px;">Organizational Structure</h3>
            """,
            unsafe_allow_html=True
        )

        org_chart()  # This is your separate component

        st.markdown("</div>", unsafe_allow_html=True)

