import streamlit as st
from streamlit_option_menu import option_menu
import requests
from PIL import Image
import base64

# Find more emojis here: https://www.webfx.com/tools/emoji-cheat-sheet/
st.set_page_config(page_title="My Webpage", page_icon=":innocent:")


# Use local CSS
def local_css(file_name):
    with open(file_name) as f:
        st.markdown(f"<style>{f.read()}</style>", unsafe_allow_html=True)


local_css("style/style.css")

# # ---- LOAD ASSETS ----
img_profile = Image.open("images/profile_2.JPG")
with open("files/RESUME.pdf", "rb") as pdf_file:
    PDFbyte = pdf_file.read()


# -----Title----
st.write('''<div style = "text-align: center"> <b>“Torture the data, and it will confess to anything.”</b> – <i>By Ronald Coase</i> </div><br>''',
            unsafe_allow_html=True
            )
# -----Option menu----

selected = option_menu(None, ["About me", "Resume", "Contact me"],
    icons=['file-person', 'file-earmark', 'envelope-open'],
    menu_icon="cast", default_index=0, orientation="horizontal",
    styles={
           "container": {"padding": "0!important"},
           "icon": {"font-size": "16px"},
           "nav-link": {"font-size": "16px", "text-align": "left", "margin": "10px"}
           }
                       )


if selected == "About me":

    with st.container():
        img_column, right_column = st.columns(2)
        with img_column:
            st.markdown('''
            ''')
            st.image(img_profile,
                     width = 300
                     )
        with right_column:
            st.markdown('''
                        ## Hi there 👋, I am Daksh
                        <p style = "text-align: jusitfied">
                                                
                        #### ML and Python Developer
                        
                        I am a student at SRM Univerity pursuing Computer Science Engineering. I love to code, specifically in Python. I am also passionate about Machine Learning, would like to learn & work on projects based on Machine Learning and/or Deep Learning. Trying my best to fit in through my skills and my learnings. Always ready to face challenges....Try It!!!! 
                        Programmer at Heart: Coding is my passion.  **CARPE DIEM**
                        </p>
                        
                        #### **WHAT I DO**
                          - 🔭 I’m currently working as Data Scientist
                          - 🌱 I’m currently learning SQL and Streamlit
                          - 👯 I’m looking to collaborate on projects based on Data Science and Machine Learning
                          - 🏓 In Free time I play Table Tennis and 📚 Read Books
                       
                        ''',
                        unsafe_allow_html = True
                        )



if selected == "Resume":
    with st.container():
    # ---Download---
        st.download_button(label="Download",
                           data=PDFbyte,
                           file_name="Daksh_Patel.pdf",
                           mime='application/octet-stream'
                           )

    #Name
        st.markdown('''
        # <div style = "text-align: center">Daksh Patel</div>''',
                    unsafe_allow_html=True
        )
    #links
        st.markdown(
            """ <p style = "text-align: center">
                <a style = "text-align: center"> Gujarat,India</a> <span>&nbsp;</span> | <span>&nbsp;</span>
                <a style='text-align: center;' href="https://linkedin.com/in/iamdaksh/">LinkedIn</a> <span>&nbsp;</span> | <span>&nbsp;</span>
                <a style='text-align: center;' href="https://github.com/helloitsdaksh/">Github</a> <span>&nbsp;</span> | <span>&nbsp;</span>
                <a style='text-align: center;' href="(+91) 757-484-3778">(+91) 757-484-3778</a> <span>&nbsp;</span> | <span>&nbsp;</span>
                <a style='text-align: center;' href="iamdakshpatel@gmail.com">iamdakshpatel@gmail.com</a>
                </p>
            """,
            unsafe_allow_html=True,
        )
    #Education
        st.markdown(
            """ 
            ### Education 
             **SRM Institute of Science and Technology**, **Chennai, Tamil Nadu** <br>
             Bachelors of Technology in Computer Science, **Cumulative GPA:** 9.57/10.0<br> May 2023
            * Areas Of Interest: Machine Learning, Computer Vision, Data Science, Research                   
            """,
            unsafe_allow_html=True,
        )

    # WORK EX
        st.markdown(
            '''
            ### Work Experience
            **Sixth Consultancy Chennai India** <br>
            *Data Scientist* <br>
            *12/2021- 02/2022*
            
              * Created a Script to handle streaming data of the stock market and reviewing it every min with a script written in python.
              * Creating a script that allows storing the data of a particular company in the database every minute from the API.
              * Tested my Script over various Companies listed in BSE and NSE.
                        
            **ACM-W,** <br>
            *Machine Learning Executive* <br>
            *10/2021-Present*
            
              * Helping newcomers into the field of Machine Learning as a Mentor.
              * Trying to find new opportunities under ACM-W chapter
                        
            **Infigon Futures Mumbai, India**<br>
            *Python Developer Intern*<br> 
            *4/2021- 6/2021*
              
              * Worked on College Prediction Module, Scraped data for the same of more than 200+ colleges.
              * Created A Welcome Email Module for the new users and also a WhatsApp Automator for automating messages.
              * Created and Tested more than 10 APIs for different purposes of the App using Flask and Postman.
                        
            **Aakash Research Labs Chennai, India** <br>
            *ML Intern* <br>
            *2/2021-5/2022*            
                      
              * Made my first ever Deep Learning model of Digit Recognition and deployed it over Heroku using Flask API in an App.
              * Created my own 3 Layered Neural Network from scratch using NumPy only.                        
              * Working on Healthcare Project with my teammate at Aakash Research Labs
                        
            *Graphic Designer* <br>
            *3/2020- 3/2021*
                        
              * Tasked to make Posters for various events organized by the Organisation
              * Tasked to create promotional posters and stories for the Organisation.
                        
            **Elixar Tech Chennai, India** <br>
            *Graphic Designer*<br> 
            *3/2020- 3/2021*
                        
              * Tasked to make Logo for clients and also design UI/UX for the Mobile Apps
              * Designed Brochures for the Organisation and worked on many projects such as designing business Cards, Instagram Stories and posts and many other ways of digital marketing services.
            ''',
            unsafe_allow_html =True
        )

    # Leadership Experience
        st.markdown(
            '''
            ### LEADERSHIP EXPERIENCE
            **Aakash Research Labs,** <br>
            *Machine Learning Head* <br>
            *6/2022-Present*
              * Evaluating and Guiding Juniors in the team, also making them work on projects.
              * Uplifting the team with new skills and making them learn new technologies.
              
            *Deputy Secretary* <br>
            *6/2021-5/2022*
              * Evaluating and Managing the Organisation, Bringing forth an excellent track record towards the Organisation.
              * Organised event Tekmux for school students of class 12 in the month of August.
                  
            **Infigon Futures,** <br>
            *Python Developer/Data Science Team Lead* <br>
            *6/2021-11/2021*
                    
              * Managed and Analyzed the workflow of the Python Developer Team on the Projects and also lead 3 different teams of new interns.
              * Managed the Deployment side of the Projects using AWS(ECS).
              * Implemented my very own Resume-Parser Module using NLP, Data-extracting and many more.
            '''
            ,unsafe_allow_html = True
        )
    # Publication:
        st.markdown(
        '''
        ### PUBLICATIONS
        **Weather Prediction using ANN**<br>
        *IJARESM Journal*<br>
        *July 2022*<br>
           * A Back Propagation Neural Network Technique predict on weather condition on real time dataset. Basically we calculated the Gradient Descent to minimize error in the Artificial Neural Network.
        ''',
        unsafe_allow_html=True
        )
    # Projects
        st.markdown(
            '''
            ### PROJECTS                      
            **Plant-Disease-Identification** <br>
              * Created a Deep Learning model for the classification of 38 types of different diseases in plants. The model I used is EfficientNetB0 which worked better than ResNetV250, approaching the accuracy of 98.79% for the detection of diseases in particular images of a leaf.
            
            **Neural-Network from Scratch**<br>
              * Built a Neural Network of 3 layers using NumPy and by coding all the equations from scratch. The accuracy achieved 84% on MNIST data.
            
            **Document-Enhancer** <br>
              * Document Enhancer is basically an Application that can be used to detect documents using Images as well as by capturing the image from the user's mobile camera, followed by taking part in a hackathon as a team where we were among the top 5 teams.
            
            **Digit-Recognizer**<br>
              * Created an app that detects handwritten digits from 0 to 9 using neural networks; the dataset used was mnist.npz, an official dataset provided by TensorFlow. The model is deployed on Heroku using a FLASK REST API.
            ''',
            unsafe_allow_html = True
        )

    # SKILLS and INTERESTS:
        st.markdown(
            '''
            ### SKILLS & INTERESTS
            **Computer Skills:** Python, C, C++, Docker, AWS(ECS), Flask,
                        Tensorflow, Numpy, Pandas, Basic OpenCV, Scikit-Learn, Matplotlib.
                        Linux, Seaborn.
            <br>
            **Interests:** Deep Learning, Image Segmentation, Research
            ''',
            unsafe_allow_html = True
        )

    # ----Contact me----
if selected == "Contact me":
    with st.container():
        st.header("Get In Touch With Me!")

        # Documention: https://formsubmit.co/ !!! CHANGE EMAIL ADDRESS !!!
        contact_form = """
        <form action="https://formsubmit.co/iamdakshpatel@gmail.com" method="POST">
        <input type="hidden" name="_captcha" value="false">
        <input type="text" name="name" placeholder="Your name" required>
        <input type="email" name="email" placeholder="Your email" required>
        <textarea name="message" placeholder="Your message here" required></textarea>
        <button type="submit">Send</button>
        </form>
        """
        left_column, right_column = st.columns(2)
        with left_column:
            st.markdown(contact_form, unsafe_allow_html=True)
        with right_column:
            st.empty()
