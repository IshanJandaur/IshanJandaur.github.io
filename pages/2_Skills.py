import streamlit as st

st.set_page_config(page_title="Skills")

st.header("Skill Proficiency")

# List of coding skills with their proficiency levels
skills_coding = [
    ("Python", 60),  
    ("RStudio", 60),  
    ("Jupyter Notebook", 50),  
    ("MATLAB", 30),  
]

# Sort the skills by proficiency in descending order
skills_coding = sorted(skills_coding, key=lambda x: x[1], reverse=True)

# Header for the Coding Languages Section
st.subheader("Coding Languages")

# Loop through each skill and display the progress with percentages
for skill, proficiency in skills_coding:
    col1, col2, col3 = st.columns([5, 1, 1])  
    with col1:
        st.write(f"**{skill}**")  
    with col2:
        st.progress(proficiency)  
    with col3:
        st.write(f"{proficiency}%")  


# List of CAD skills with their proficiency levels
skills_CAD = [
    ("SolidWorks", 70),  
    ("Autodesk Fusion 360", 70),  
    ("GD&T", 50),  
    ("PDM", 50),  
    ("Engineering Drawings", 70), 
]

# Sort the skills by proficiency in descending order
skills_CAD = sorted(skills_CAD, key=lambda x: x[1], reverse=True)

# Header for the CAD section
st.subheader("Computer-Aided Drafting")

# Loop through each skill and display the progress with percentages
for skill, proficiency in skills_CAD:
    col1, col2, col3 = st.columns([5, 1, 1]) 
    with col1:
        st.write(f"**{skill}**")  
    with col2:
        st.progress(proficiency) 
    with col3:
        st.write(f"{proficiency}%") 

# List of manufacturing skills
skills_manu = [
    ("DFM/DFA", 70),  
    ("P/D FMEA", 80),  
    ("Quality Control", 70),  
    ("Machining", 30),  
    ("Welding", 30),  
    ("Hand Tools", 90),  
    ("3D Printing", 70),  
    ("Root Cause Analysis", 80),  
    ("Tolerance Stack Analysis", 60),  
    ("Engineering Change Control", 90),  
    ("MES/ERP", 30),  
    ("Design of Experiments", 60), 
]

# Sort the skills by proficiency in descending order
skills_manu = sorted(skills_manu, key=lambda x: x[1], reverse=True)

# Header for the Manufacturing section
st.header("Manufacturing Knowledge")

# Loop through each skill and display the progress with percentages
for skill, proficiency in skills_manu:
    col1, col2, col3 = st.columns([5, 1, 1])  
    with col1:
        st.write(f"**{skill}**") 
    with col2:
        st.progress(proficiency)  
    with col3:
        st.write(f"{proficiency}%")

# List of soft skills 
skills_soft = [
    ("Microsoft Project", 60), 
    ("Conflict Resolution", 90),  
    ("Powerpoint", 60), 
    ("Excel", 60),  
    ("Technical Report Writing", 30), 
    ("Think-cell", 80),  
    ("Project Management", 80), 
]

# Sort the skills by proficiency in descending order
skills_soft = sorted(skills_soft, key=lambda x: x[1], reverse=True)

# Header for the Soft Skills section
st.subheader("Soft Skills")

# Loop through each skill and display the progress with percentages
for skill, proficiency in skills_soft:
    col1, col2, col3 = st.columns([5, 1, 1])  
    with col1:
        st.write(f"**{skill}**")  
    with col2:
        st.progress(proficiency)  
    with col3:
        st.write(f"{proficiency}%")  