import streamlit as st
import pandas as pd
import numpy as np
import pydeck as pdk
import datetime #To use with Dates
import matplotlib.pyplot as plt #To help to plot
from PIL import Image


DATA_URL = (
"Motor_Vehicle_Collisions_-_Crashes.csv"
)

DATA_URL2 = (
    "Updated_Covid_Vaccine.csv"
)

_, col2, _ = st.columns([2, 4, 2])

with col2:
    st.title("Corona Hub")



st.markdown("## This is a dashboard, created by students from "
"the Junior Programming Project Team"
" for Science Day 2021 ")
st.markdown("### This **_Hub_** was made by:")
st.markdown("### Paavani, Priti, Karuna, " 
" Noor, Vinay & Achint")
st.markdown("### Mentored by Araz")


st.header("ABOUT THE HUB")

st.markdown("#### This hub was made by students to do something positive about fighting the Corona Virus, and learning from it's outcomes."
" The students made 2 projects for this Hub:  ")
st.markdown(" #### 1. **Games from MIT Scratch Game Development Platform:** These games are both fun to play and depict the importance of vaccines in fighting the Corona Virus")
show_game = st.checkbox("Show Games in Corona Hub", False)
st.markdown(" #### 2. **Data Analysis on the Vaccination Program in India, started in January 2021:** The analysis reveals how well India has done with vaccinating its citizens")
show_analysis = st.checkbox("Show Data Analysis of Corona Hub", False)

st.markdown("-----------------------------------------------------------------------------------------------------------------------")

if(show_game):
    st.markdown("#### GAMES")

    st.subheader('Shoot Coronavirus Game')
    game_img1 = Image.open("achint game.jpg")
    st.image(game_img1, caption = "Corona Shooter Game")
    st.markdown("#### This game is made by Achint named Shoot Coronavirus. The game is developed using Scratch. It's a Block coding app developed by MIT."
" In this game there is our spaceship coronavirus in the centre of the stage who shoots bullets at our corona warrior spaceship. We can dodge the bullets shooted by the virus by arrow keys and can shoot vaccines at corona to decrease it’s health. In this game different spaceship can also be choosen with diffrent colours.We can also see our score and high scrose.Play this game it will be a great fun! ")
    st.markdown("https://scratch.mit.edu/projects/474183631/")

    st.subheader('Covid Slicer Game')
    game_img1 = Image.open("vinay game.jpg")
    st.image(game_img1, caption = "Corona Slicer Game")
    st.markdown("#### Covid Slicer is a game made on the Scratch programming platform, by Vinay. It can be played on any device(Android,Ios,Windows,Mac) and it is child friendly and age appropriate. The game is fairly simple-Its objective being to slice fruit and dodge covid particles. People who play this game with a Scratch account can save a high score(Operated through the cloud.")
    st.markdown("https://scratch.mit.edu/projects/602807352/")

    st.subheader("Corona Warrior")
    game_img1 = Image.open("noor game.png")
    st.image(game_img1, caption = "Corona Warrior Game")
    st.markdown("#### This game is developed by Noor. The game is called Corona Warrior. The game is developed using Scratch. It's a Block coding app developed by MIT."
" The game is an attempt from my side to spread the message that all of us are warriors and just like this game we will win the fight against Corona. In this game, we have a vaccine, 3 Coronaviruses, and a Robo Warrior. Use arrow keys and save the warrior from coronaviruses and touch the vaccine to increase your health to get your health at 100.")
    st.markdown("https://scratch.mit.edu/projects/568251470")

@st.cache(persist=True, allow_output_mutation = True)
def load_data_vaccines():
    data = pd.read_csv(DATA_URL2)
    return data    

if(show_analysis):
    st.markdown("#### Data Analysis")

    st.markdown("#### The following analysis is for the vaccine doses administered in Indian States")
    st.markdown("#### The dataset used for the analysis can be found at:")
    st.markdown("##### https://www.kaggle.com/sudalairajkumar/covid19-in-india?select=covid_vaccine_statewise.csv")
    st.markdown("#### You can customise the plots by selecting the parameters from the checkboxes provided")
    vaccine_data = load_data_vaccines()
    vaccine_data["Updated On"] = pd.to_datetime(vaccine_data["Updated On"])
    states = list(vaccine_data["State"].unique())
    vaccine_data.loc[:159,"Male (Doses Administered)"] = vaccine_data[:160]["Male(Individuals Vaccinated)"]
    vaccine_data.loc[:159,"Female (Doses Administered)"] = vaccine_data[:160]["Female(Individuals Vaccinated)"]
    vaccine_data.loc[:159,"Transgender (Doses Administered)"] = vaccine_data[:160]["Transgender(Individuals Vaccinated)"]
    
    #Select the State and show the stats according to that
    state_selected = st.selectbox("State to show Analysis for:", states)

    vaccine_data.dropna(subset=['Total Doses Administered'], inplace=True)
    vaccine_data_state = vaccine_data[vaccine_data["State"]==state_selected]

    if st.checkbox("Show the Raw Data", False):
        st.write(vaccine_data_state.iloc[:,1:13])
    
    st.subheader('Total Doses of a Vaccine for '+ str(state_selected))

    fig = plt.figure(figsize = (10, 10))
    plt.bar(vaccine_data_state["Updated On"], vaccine_data_state["Total Doses Administered"]) #Bar Plot with X-Axis as the Dates (Updated On) & Y-axis as Number Of Vaccinations
    plt.xticks(rotation='vertical') #X-Axis par labels ko rotate karna by 90 degrees
    plt.yticks()
    plt.yscale('log') #Y-Axis ko we make in Log Scale - Using exponents to express the values - because number of vaccinations are vv large - so we express in exponents
    plt.title("Vaccine Total Doses Admininstered Across " + str(state_selected)) #Title for the Plot
    plt.ylabel("Number of Vaccines - - >") # Y-Axis ko define
    plt.xlabel("Time - - >") # X-Axis ko define
    plt.show()
    st.pyplot(fig)

    st.subheader('Doses according to Gender for '+ str(state_selected))

    have_male = st.checkbox("Include Male Data", True)
    have_female = st.checkbox("Include Female Data", True)
    have_trans = st.checkbox("Include Transgender Data", True)

    if(have_female or have_male or have_trans):

        fig = plt.figure(figsize = (10, 10))
        if(have_male):
            plt.bar(vaccine_data_state["Updated On"], vaccine_data_state["Male (Doses Administered)"],0.8, label="Male")
        if(have_female):
            plt.bar(vaccine_data_state["Updated On"], vaccine_data_state["Female (Doses Administered)"],0.8, label="Female")
        if(have_trans):
            plt.bar(vaccine_data_state["Updated On"], vaccine_data_state["Transgender (Doses Administered)"],0.8, label="Transgender")
        plt.yscale('log')
        plt.xticks(rotation='vertical')
        plt.legend() #Adds the Key
        plt.title("Doses Administered Gender Wise")
        plt.ylabel("Number of Vaccines - - >") # Y-Axis ko define
        plt.xlabel("Time - - >") # X-Axis ko define
        plt.show()
        st.pyplot(fig)

    st.subheader('Doses according to the Vaccine Company for '+ str(state_selected))

    have_covaxin = st.checkbox("Include Covaxin Data", True)
    have_covishield = st.checkbox("Include Covishield Data", True)

    if(have_covishield or have_covaxin):
        fig = plt.figure(figsize = (10, 10))
        if(have_covishield):
            plt.bar(vaccine_data_state["Updated On"], vaccine_data_state["CoviShield (Doses Administered)"],0.8, label="CoviShield")
        if(have_covaxin):
            plt.bar(vaccine_data_state["Updated On"], vaccine_data_state[" Covaxin (Doses Administered)"],0.8, label="Covaxin")
        
        plt.yscale('log')
        plt.xticks(rotation='vertical')
        plt.legend() #Adds the Key
        plt.title("Doses Administered Vaccine Company Wise")
        plt.ylabel("Number of Vaccines - - >") # Y-Axis ko define
        plt.xlabel("Time - - >") # X-Axis ko define
        plt.show()
        st.pyplot(fig)




