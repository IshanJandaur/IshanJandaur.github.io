import streamlit as st
import os
from Pillow import Image

# Set page title
st.set_page_config(page_title="Introduction Page", layout="centered")

# Introduction
st.markdown("<h2 style='text-align: center;'>Hi, I'm Ishan!</h2>", unsafe_allow_html=True)

# Profile picture
st.markdown(
    """
    <div style="display: flex; justify-content: center; padding: 20px;">
        <img src="imnage_path" width="200">
    </div>
    """,
    unsafe_allow_html=True
)

col1, col2 = st.columns([1, 1])  

# Resume Download Button
with col1:
    with open("Ishan_Jandaur_Resume.pdf", "rb") as file:
        st.download_button(label="📄 Download Resume",
                           data=file,
                           file_name="Ishan_Jandaur_Resume.pdf",
                           mime="application/pdf")

# Linkedin URL Link
with col2:
    st.markdown("""
        <a href="https://www.linkedin.com/in/ishanjandaur/" target="_blank">
            <button style="
                background-color: #0077b5; 
                color: white; 
                padding: 10px 20px; 
                border: none; 
                border-radius: 5px;
                font-size: 16px;
                cursor: pointer;">
                🔗 Connect on LinkedIn
            </button>
        </a>
    """, unsafe_allow_html=True)


# Short about me 
st.write("""
    Hi, my name is Ishan Jandaur and I am currently a product design engineer at Lyten. In this role, I design cylindrical battery cells using Li-S chemistry.
         
    I was born and raised in San Jose, CA and have a bachelor's degree from California Polytechnic State University - San Luis Obispo.
    Although my degree is in mechanical engineering, my work experience and interests have varied quite a bit. I have worked in batteries, on medical devices, and even in high volume contract manufacturing environments.
         
    Feel free to reach out to me on Linkedin or by email if you want to chat!
""")

# Initialize session state
if 'counter' not in st.session_state: 
    st.session_state.counter = 0

# Function to show the next photo and cycle through images
def show_photo():
    # Get the current photo path based on the counter
    photo_path = paths_images[st.session_state.counter]
    # Open and display the image using PIL
    photo = Image.open(photo_path)
    col2.image(photo, caption=None)

    # Increment the counter, and wrap around when it reaches the end
    st.session_state.counter = (st.session_state.counter + 1) % len(paths_images)

# Get a list of image file paths in the 'images' folder
folder_with_images = "images"
paths_images = [os.path.join(folder_with_images, f) for f in os.listdir(folder_with_images) if f.lower().endswith(('.png', '.jpg', '.jpeg', '.gif'))]

# List out hobbies
col1, col2 = st.columns(2)
col1.subheader("Hobbies:")
col1.markdown("""
- Training my Dog
- Collecting Vinyl Records
- Playing Basketball
- Traveling/Backpacking
- Cooking New Foods
""")

# Show the button to trigger image change
show_btn = col1.button("Click button to show pictures ⏭️", on_click=show_photo)

# # Optionally show the current photo info or description
# if st.session_state.counter < len(paths_images):
#     st.write(f"Showing image {st.session_state.counter + 1} of {len(paths_images)}")
