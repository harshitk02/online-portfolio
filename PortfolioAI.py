import streamlit as st
import plotly.express as px
from streamlit_lottie import st_lottie
from streamlit_timeline import timeline
import streamlit.components.v1 as components
from constant import *
import requests
import base64

import plotly.graph_objs as go
import numpy as np
from PIL import Image

# Function to load Lottie animation from URL
def load_lottieurl(url: str):
    r = requests.get(url)
    if r.status_code != 200:
        return None
    return r.json()

# Loading assets
lottie_gif = load_lottieurl("https://assets9.lottiefiles.com/packages/lf20_x17ybolp.json")
python_lottie = load_lottieurl("https://assets6.lottiefiles.com/packages/lf20_2znxgjyt.json")
java_lottie = load_lottieurl("https://assets9.lottiefiles.com/packages/lf20_zh6xtlj9.json")
my_sql_lottie = load_lottieurl("https://assets4.lottiefiles.com/private_files/lf30_w11f2rwn.json")
git_lottie = load_lottieurl("https://assets9.lottiefiles.com/private_files/lf30_03cuemhb.json")
github_lottie = load_lottieurl("https://assets8.lottiefiles.com/packages/lf20_6HFXXE.json")
docker_lottie = load_lottieurl("https://assets4.lottiefiles.com/private_files/lf30_35uv2spq.json")
figma_lottie = load_lottieurl("https://lottie.host/5b6292ef-a82f-4367-a66a-2f130beb5ee8/03Xm3bsVnM.json")
js_lottie = load_lottieurl("https://lottie.host/fc1ad1cd-012a-4da2-8a11-0f00da670fb9/GqPujskDlr.json")

# Sample data for skills (replace with actual data)
skills = ['Python', 'Data Analysis', 'Machine Learning']
levels = [90, 75, 85]

# Set the background color
background_color = "#f0f0f0"  # You can change this to any color you like

# Wrap the entire content in a div with the background color
st.markdown(
    f"""
    <style>
    .reportview-container {{
        background-color: {background_color};
    }}
    .section-header {{
        font-size: 24px;
        margin-top: 30px;
        margin-bottom: 10px;
    }}
    </style>
    """,
    unsafe_allow_html=True
)

# Set up the Streamlit layout
st.markdown("""
    <div style='text-align: center;'>
    <br>
        <h2>💼 Online Portfolio</h2>
        <br>
        <!-- Apply CSS styling to create a circular image -->
        <img src='https://img.freepik.com/free-photo/portrait-young-businessman-with-mustache-his-face-3d-rendering_1142-38839.jpg?t=st=1712898682~exp=1712902282~hmac=455b3b4500d8ef306cbcac2d5bbce038ae13359b16181cceee41267818b5c035&w=740' style='width: 200px; border-radius: 50%;'>
        <!--<h5>Jack Codeheart</h5>-->
    </div>
""", unsafe_allow_html=True)

# ----------------- info ----------------- #
def gradient(color1, color2, color3, content1, content2):
    # Determine the appropriate font color based on the background color
    font_color = 'black' if (int(color1.lstrip('#'), 16) * 0.299 + int(color1[1:3], 16) * 0.587 + int(color1[3:], 16) * 0.114) > 186 else 'white'
    
    st.markdown(f'<div style="text-align: center; border-radius: 15px; padding: 20px; background-image: linear-gradient(to right, {color1}, {color2}); font-family: "Comic Sans MS", cursive, sans-serif;">'
                f'<h1 style="font-size: 30px; color: {font_color}; margin-bottom: 10px;">{content1}</h1>'
                f'<p style="color: white; font-size: 20px; font-weight: bold;">"{content2}"</p>'
                '</div>', 
                unsafe_allow_html=True)


with st.container():
    col1,col2 = st.columns([8,3])

full_name = info['Full_Name']

gradient('#FFD4DD', '#000395', 'e0fbfc', f"Hi, I'm {full_name}👋", info["Intro"])

#gradient('#FFD4DD','#e0fbfc','000395',f"Hi, I'm {full_name}👋", info["Intro"])
st.write("")
# Center-align the 'About' text
st.markdown(
    f"""
    <div style='text-align: center;'>
        {info['About']}
    </div>
    """,
    unsafe_allow_html=True
)

# Define the list of Lottie animation URLs for each skill
lotties = [python_lottie, java_lottie, my_sql_lottie, git_lottie, github_lottie, docker_lottie, figma_lottie, js_lottie]

# Define the number of columns based on the screen width
num_columns = min(len(lotties), 4)  # Maximum 4 columns

# Define the width for each column
col_width = f"{100 // num_columns}%"  # Calculate the width dynamically

# ----------------- skillset ----------------- #
with st.container():
    st.subheader('⚒️ Skills')

    # Display the Lottie animations in the columns
    cols = st.columns(num_columns)
    for i, lottie in enumerate(lotties):
        with cols[i % num_columns]:
            st_lottie(lottie, height=100, width="100%", key=lottie, speed=2.5)

    
# ----------------- timeline ----------------- #
with st.container():
    st.markdown("""""")
    st.subheader('📌 Career Snapshot')

    # load data
    with open('example.json', "r") as f:
        data = f.read()

    # render timeline
    timeline(data, height=400)
    
    
# # Display the achievements section
st.header('🏆 Achievements')
st.markdown("""
- Developed a machine learning model with 95% accuracy
- Published 5 research papers in top-tier journals
- Presented at international conferences
""")

#Sample data for strengths (replace with actual data)
strengths = ['Analytical', 'Communicative', 'Motivated']
values = [4, 3, 3]  # Equal values to represent each strength equally

# Display the strengths section
st.header('💪 Strengths')
colors = ['#FFA07A', '#87CEEB', '#FFD700']

# Function to create a Plotly graph for strengths
def create_strengths_chart(strengths, values, colors):
    fig = px.pie(names=strengths, values=values, title='')
    fig.update_traces(textposition='inside', textinfo='label', marker=dict(colors=colors))
    return fig

# Display the chart
st.plotly_chart(create_strengths_chart(strengths, values, colors), use_container_width=True)

# Sample data: random scores for 5 days
np.random.seed(42)  # For reproducible results
days = ['Day 1', 'Day 2', 'Day 3', 'Day 4', 'Day 5']
scores = np.random.randint(1, 11, size=5)  # Random scores out of 10

# Function to create an enhanced Plotly bar chart with simple colors for each bar and responsiveness upon hovering
def create_scores_chart(days, scores):
    # Define custom colors for each bar
    custom_colors = ['#FFA07A', '#87CEEB', '#FFD700', '#FF6347', '#7FFF00']

    # Define the data for the bar chart with custom colors
    data = go.Bar(
        x=days,
        y=scores,
        marker=dict(color=custom_colors, line=dict(color='rgba(0,0,0,0)')),  # Set custom colors for the bars and remove border color
        hoverinfo='y',  # Show the score on hover
        hoverlabel=dict(bgcolor='white', font=dict(color='black')),  # Set hover label style
    )

    # Define the layout of the chart
    layout = go.Layout(
        xaxis=dict(title='Day'),  # Set the label for the x-axis
        yaxis=dict(title='Score'),  # Set the label for the y-axis
        plot_bgcolor='rgba(0,0,0,0)',  # Set the background color of the plot
        template='plotly_dark',  # Dark theme for a modern look
        hovermode='closest',  # Show hover information for the closest point
        hoverdistance=50,  # Set the distance for hover sensitivity
    )

    # Create the figure
    fig = go.Figure(data=[data], layout=layout)

    # Add additional interactivity
    fig.update_xaxes(showgrid=False)  # Hide the gridlines on the x-axis
    fig.update_yaxes(showgrid=True, gridwidth=1, gridcolor='rgba(255, 255, 255, 0.2)')  # Customize gridlines on y-axis

    return fig

# Display the quiz scores section with a Plotly bar chart
st.header('🎯 Assesment Scores')
scores_chart = create_scores_chart(days, scores)
st.plotly_chart(scores_chart, use_container_width=True)


# -----------------  endorsement  ----------------- #
with st.container():
    # Divide the container into three columns
    col1, col2 = st.columns([2, 2])
    # In the first column (col1)        
    with col1:
        # Add a subheader to introduce the coworker endorsement slideshow
        st.subheader("🗣️ Coworker Feedback")
        # Embed an HTML component to display the slideshow
        components.html(
            f"""
            <!DOCTYPE html>
            <html>
            <head>
            <meta name="viewport" content="width=device-width, initial-scale=1">
            <!-- Styles for the slideshow -->
            <style>
                * {{box-sizing: border-box;}}
                .mySlides {{display: none;}}
                img {{vertical-align: middle;}}

                /* Slideshow container */
                .slideshow-container {{
                position: relative;
                margin: auto;
                width: 100%;
                }}

                /* The dots/bullets/indicators */
                .dot {{
                height: 15px;
                width: 15px;
                margin: 0 2px;
                background-color: #eaeaea;
                border-radius: 50%;
                display: inline-block;
                transition: background-color 0.6s ease;
                }}

                .active {{
                background-color: #6F6F6F;
                }}

                /* Fading animation */
                .fade {{
                animation-name: fade;
                animation-duration: 1s;
                }}

                @keyframes fade {{
                from {{opacity: .4}} 
                to {{opacity: 1}}
                }}

                /* On smaller screens, decrease text size */
                @media only screen and (max-width: 300px) {{
                .text {{font-size: 11px}}
                }}
                </style>
            </head>
            <body>
                <!-- Slideshow container -->
                <div class="slideshow-container">
                    <div class="mySlides fade">
                    <img src={endorsements["img1"]} style="width:100%">
                    </div>

                    <div class="mySlides fade">
                    <img src={endorsements["img2"]} style="width:100%">
                    </div>

                    <div class="mySlides fade">
                    <img src={endorsements["img3"]} style="width:100%">
                    </div>

                </div>
                <br>
                <!-- Navigation dots -->
                <div style="text-align:center">
                    <span class="dot"></span> 
                    <span class="dot"></span> 
                    <span class="dot"></span> 
                </div>

                <script>
                let slideIndex = 0;
                showSlides();

                function showSlides() {{
                let i;
                let slides = document.getElementsByClassName("mySlides");
                let dots = document.getElementsByClassName("dot");
                for (i = 0; i < slides.length; i++) {{
                    slides[i].style.display = "none";  
                }}
                slideIndex++;
                if (slideIndex > slides.length) {{slideIndex = 1}}    
                for (i = 0; i < dots.length; i++) {{
                    dots[i].className = dots[i].className.replace("active", "");
                }}
                slides[slideIndex-1].style.display = "block";  
                dots[slideIndex-1].className += " active";
                }}

                var interval = setInterval(showSlides, 2500); // Change image every 2.5 seconds

                function pauseSlides(event)
                {{
                    clearInterval(interval); // Clear the interval we set earlier
                }}
                function resumeSlides(event)
                {{
                    interval = setInterval(showSlides, 2500);
                }}
                // Set up event listeners for the mySlides
                var mySlides = document.getElementsByClassName("mySlides");
                for (i = 0; i < mySlides.length; i++) {{
                mySlides[i].onmouseover = pauseSlides;
                mySlides[i].onmouseout = resumeSlides;
                }}
                </script>

                </body>
                </html> 
            """,
            height=270,
        )

        
# Add a footer with a colored banner and text
footer_html = """
<div style="background-color: #CC00FF; padding: 10px; text-align: center;">
    <p style="color: white; font-size: 16px;">GuideGuru.ai - Your portfolio builder</p>
</div>
"""
st.markdown(footer_html, unsafe_allow_html=True)

# -----------------  contact  ----------------- 
with col2:
    st.subheader("📨 Contact Me")
    contact_form = f"""
    <style>
        /* CSS styling for contact form */
        input[type="text"],
        input[type="email"],
        textarea,
        button[type="submit"] {{
            width: 100%;
            padding: 10px;
            margin-bottom: 10px;
            border: 1px solid #ccc;
            border-radius: 5px;
            box-sizing: border-box;
            font-size: 16px;
        }}
        button[type="submit"] {{
            background-color: #007bff;
            color: #fff;
            cursor: pointer;
        }}
        button[type="submit"]:hover {{
            background-color: #0056b3;
        }}
    </style>
    <form action="https://formsubmit.co/{info["Email"]}" method="POST">
        <input type="hidden" name="_captcha" value="false">
        <input type="text" name="name" placeholder="Your name" required>
        <input type="email" name="email" placeholder="Your email" required>
        <textarea name="message" placeholder="Your message here" required></textarea>
        <button type="submit">Send</button>
    </form>
    """
    st.markdown(contact_form, unsafe_allow_html=True)

