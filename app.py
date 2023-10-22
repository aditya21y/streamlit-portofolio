import streamlit as st
from streamlit_option_menu import option_menu
import requests
from streamlit_lottie import st_lottie

# lottie animationn
def lottie_api(url):
    r = requests.get(url)
    if r.status_code != 200:
        return None
    return r.json()
lottie = lottie_api("https://lottie.host/9c21083f-857c-4ad2-b3e3-1d3b3532c511/S4W85SKtwp.json")

# streamlit interface
st.set_page_config(layout="wide")

# css
st.markdown("""
        <style>
          .st-emotion-cache-1v0mbdj img{
            border-radius:50%;
          }
          .st-emotion-cache-nahz7x p a{
            margin-left:10px;
          }
          .st-emotion-cache-5rimss p a{
            margin-left:10px;
          }
        </style>
        """, unsafe_allow_html=True)
# menu options
with st.container():
    selected = option_menu(
        menu_title=None,
        options = ["About","Project","Contact","Blog"],
        icons = ["person-circle","palette","telephone","github"],
        orientation = "horizontal",
    )
if selected == "About":
    with st.container():
        col1,col2 = st.columns(2)
        with col1:
            st.write("##")
            st.title("Hi :wave:, I'm Aditya Yudha Perdana")
            st.write("A recent graduate from Telkom University and very interested in Python programming.")
            st.write("for more information you can contact me at :")
            st.write(
                "[Linkedin](https://www.linkedin.com/in/adityayudhaperdana/)",
                "[Instagram](https://www.instagram.com/mr_catnmouse/?hl=id)",
                "[Github](https://github.com/aditya21y)")
        with col2:
            # st_lottie(lottie)
            st.write("##")
            st.image("foto_kotak.jpg",width=300)
        st.write("___")
    
    with st.container():
        col3,col4 = st.columns(2)
        with col3:
            st.subheader("""
            :male-student: Education
            - 2017-2021
                - Telkom University
                    - Bachelors degree in ComputerEngineering
                    - GPA 3.22
            """)
            st.subheader("""
            :microscope: Skill And Languages
            - Technical Skills
                - Python
                - HTML
                - CSS
                - SQL
                - Javascript
            - Languages
                - Indonesia
                - English
            """)
        with col4:
            st.subheader("""
            :hourglass_flowing_sand: Experience
            - Sep 2022 - Des 2023
                - PT Rect Media Komputindo (BackEnd Developer / ERP Developer)
                    - Install and Customize ERPnext based on client business needs
                    - Creating APIs for business processes in ERPnext
                    - UI customization according to client business needs
            - Jan 2022 - Jun 2022
                - BrightChamps (Coding Educator)
                    - Provide learning about coding to students from grades 1 to 12 according to the curriculum
                    - Create learning projects that match their interests and grades
            - Des 2019 - Dec 2020
                - Everything Connected Laboratory (Laboratory Assistant)
                    - Guiding computer network practicum and cloud computing
                    - Guiding study groups for computer engineering students.
            - Jun 2020 - Jul 2020
                - ProcodeCG (Apprentice Programmer)
                    - Develop indoor people counter applications based on computer vision using opencv
            - Jun 2019 - Jul 2019
                -  PT. POS Indonesia (Intern Staff)
                    - Assist the customer service department in inputting shipping data and legalizing
                    - Assist the operational department in data collection of packages to be sent to the destination
                    - Helping the sales department enter company letters to be sent via ipos
            """)
