import streamlit as st

# Set page configuration
st.set_page_config(page_title="Projects", layout="centered")

# Barker Bird Project Description
st.markdown(
    """
    <div style="text-align: left;">
        <h1>Barker Bird Animatronic</h1>
        <p style="font-size: 18px;">
            My senior design project consisted of developing a robotic bird based on Disneyland’s Barker Bird.
            I worked with three other engineers to design a 3D-printed skeleton that sang, flapped and extended 
            its wings, and rotated on a base. The project consisted of multiple electromechanical components and 
            customizable code that will be used as a teaching tool for students who want to learn about animatronics.
        </p>
    </div>
    """,
    unsafe_allow_html=True
)

col1, col2, col3 = st.columns([1, 2, 1])

# Display image in the center column
with col2:
    st.image("barkerbird.jpg", width=300) 

# # Display original barker bird
# st.image("barkerbird.png", width=300)

# Embed video of Barker Bird prototype working
video_url = "https://www.youtube.com/watch?v=TDqJGbDxhho" 
st.video(video_url)

# Caption for video
st.markdown(
    """
    <div style="text-align: center; font-size: 18px; color: gray;">
        Here’s a demo of the Barker Bird Animatronic!
    </div>
    """,
    unsafe_allow_html=True
)

import streamlit as st

# Description for MEDITEC Project 
st.markdown(
    """
    <div style="text-align: left;">
        <h1>Medical Device NDA Project - MEDITEC</h1>
        <p style="font-size: 18px;">
            We determined an accurate method of monitoring the force required to dissect human tissue. 
            We designed and 3D-printed a fixture to simulate the surgical procedure. Additionally, 
            off-the-shelf sensors were calibrated and used to measure the pressure from the users’ hands. 
            Prototyping was done using an Arduino Mega, a breadboard, and various electrical/wiring components.
        </p>
    </div>
    """,
    unsafe_allow_html=True
)

# Pictures for MEDITEC Project 
col1, col2 = st.columns(2)

with col1:
        st.image("fixture.jpg", use_container_width=True)
        st.write("*3D Printed fixture to test surgical tool*")

with col2:
        st.image("breadboard.jpg", use_container_width=True)
        st.write("*Setup to process force readings*")