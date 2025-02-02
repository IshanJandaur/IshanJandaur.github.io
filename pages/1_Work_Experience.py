import streamlit as st

st.set_page_config(page_title="Work Experience")

# Put resume on top of page for download
st.markdown(
    """
    <div style="text-align: center;">
        <h3>Please download my resume to view in greater detail!</h3>
    </div>
    """,
    unsafe_allow_html=True,
)

# Button for resume download
with open("Ishan_Jandaur_Resume.pdf", "rb") as file:
    st.markdown(
        """
        <div style="display: flex; justify-content: center;">
    """,
        unsafe_allow_html=True,
    )
    st.download_button(
        label="📄 Download Resume",
        data=file,
        file_name="Ishan_Jandaur_Resume.pdf",
        mime="application/pdf",
    )
    st.markdown("</div>", unsafe_allow_html=True)

# Experience at Lyten 
st.markdown("### **January 2022 – Present**")
col1, col2 = st.columns([2, 4])

with col1:
    st.image("lyten.jpg", use_container_width=True)  
    st.markdown("**Location:** San Jose, CA")  
    st.markdown('<p style="text-align: center;"><a href="https://lyten.com" target="_blank">Visit Website</a></p>', unsafe_allow_html=True)

with col2:
    st.markdown("#### **Product Design Engineer** | Lyten")  
    st.write("• Spearheaded roadmap for **first 250 Wh/kg 21700 Li-S battery**")  
    st.write("• Developed MES process flow to optimize material tracking")  
    st.write("• Defined equipment specifications for **multi-GWh factory**")  
    st.write("• Designed and sourced materials meeting performance & weight targets")  
    st.write("• Led conversion of tooling & material for various battery formats")  
    st.write("• Engineered fixtures and test methods to validate new cell designs")  

    st.markdown("#### **Associate Product Design Engineer**")  
    st.write("• Owned first 18650 & 21700 Li-S cylindrical cell designs")  
    st.write("• Conducted **DFM, PFMEA, and DFA** on all components & assemblies")  
    st.write("• Performed **DOEs & data analysis** for electrochemical improvements")  
    st.write("• Scaled pilot line from **0 to 100 finished cells/shift** with **80% yield**")  
    st.write("• Developed QC metrics & testing methods")  
    st.write("• Led Site Acceptance Testing (**SAT**) on 3 assembly machines")  

#Picture of cylindrical cells
col1, col2, col3 = st.columns([1, 2, 1])

with col2:
    st.image("lyten-1.jpg", width=700) 

#Divider
st.markdown("""<div style="height: 5px; background-color: #69ADFF; margin: 20px 0;"></div>""", unsafe_allow_html=True)

# Flex Experience
st.markdown("### **June 2022 - August 2022**")
col1, col2 = st.columns([2, 4])

with col1:
    st.image("flex-logo.png", width=500)  
    st.markdown("**Location:** Milpitas, CA")  
    st.markdown('<p style="text-align: center;"><a href="https://flex.com" target="_blank">Visit Website</a></p>', unsafe_allow_html=True)

with col2:
    st.markdown("#### **Project Engineer Intern** | Flex Inc")  
    st.write("• Structured and scrubbed **800-line BOM** for production release")  
    st.write("• Trained operators on complex subassembly processes")  
    st.write("• Created & managed **in-house MES system** for inventory tracking")  
    st.write("• Assisted PCB fabrication line by troubleshooting defects")  

#Picture of Serve Robotics robot
col1, col2, col3 = st.columns([1, 2, 1])

with col2:
    st.image("serve-robotics.jpeg", width=300) 

st.markdown("""<div style="height: 5px; background-color: #69ADFF; margin: 20px 0;"></div>""", unsafe_allow_html=True)

# Enovix Experience
st.markdown("### **June 2021 - September 2021**")
col1, col2 = st.columns([2, 4])

with col1:
    st.image("enovix-logo.png", width=500)  
    st.markdown("**Location:** Fremont, CA")  
    st.markdown('<p style="text-align: center;"><a href="https://enovix.com" target="_blank">Visit Website</a></p>', unsafe_allow_html=True)

with col2:
    st.markdown("#### **Product Engineering Intern** | Enovix Corporation")  
    st.write("• Developed and tested next-gen lithium-ion battery with **5% energy increase**")  
    st.write("• Led installation & qualification of Instron machine for weld pull testing")  
    st.write("• Designed experiments to establish max allowable clamp force on cells")  
    st.write("• Created work instructions & fixtures to streamline testing")  

st.markdown("""<div style="height: 5px; background-color: #69ADFF; margin: 20px 0;"></div>""", unsafe_allow_html=True)

# Toray Experience
st.markdown("### **October 2020 - January 2021**")
col1, col2 = st.columns([2, 4])

with col1:
    st.image("toray-logo.png", width=500)  
    st.markdown("**Location:** Fairfield, CA")  
    st.markdown('<p style="text-align: center;"><a href="https://toray-tac.com" target="_blank">Visit Website</a></p>', unsafe_allow_html=True)

with col2:
    st.markdown("#### **Expert/Technical Services Intern** | Toray Advanced Composites")  
    st.write("• Communicated directly with customers on test results & specifications")  
    st.write("• Authored technical summary reports & work instructions")  
    st.write("• Collaborated with Quality Assurance to resolve testing discrepancies on a new DMA machine")  

st.markdown("""<div style="height: 5px; background-color: #69ADFF; margin: 20px 0;"></div>""", unsafe_allow_html=True)
