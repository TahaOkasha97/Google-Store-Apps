

import streamlit as st
import pandas as pd
import plotly.express as px
from models.dummies import *

df = pd.read_csv("google_apps_cleaned_data.csv")

st.title("Google Store Apps Project")
st.info("Final Project")
st.dataframe(df)

x = [['Rating', 'Reviews', 'Price', 'Last Updated Year',
       'Min Android Ver',"Category","Type","Content Rating"]

custom_data=[]
for inp in x:
    print(f'{inp}:')
    val=float(input())
    custom_data.append(val)
Rating = st.number_input("Enter Rating")
Rating = st.number_input("Reviews")
Rating = st.number_input("Price")
Rating = st.number_input("Last Updated Year")
Rating = st.number_input("Min Android Ver as 1.0")
Category = st.selectbox("Select Category",{'Category_AUTO_AND_VEHICLES', 'Category_BEAUTY',
       'Category_BOOKS_AND_REFERENCE', 'Category_BUSINESS', 'Category_COMICS',
       'Category_COMMUNICATION', 'Category_DATING', 'Category_EDUCATION',
       'Category_ENTERTAINMENT', 'Category_EVENTS', 'Category_FAMILY',
       'Category_FINANCE', 'Category_FOOD_AND_DRINK', 'Category_GAME',
       'Category_HEALTH_AND_FITNESS', 'Category_HOUSE_AND_HOME',
       'Category_LIBRARIES_AND_DEMO', 'Category_LIFESTYLE',
       'Category_MAPS_AND_NAVIGATION', 'Category_MEDICAL',
       'Category_NEWS_AND_MAGAZINES', 'Category_PARENTING',
       'Category_PERSONALIZATION', 'Category_PHOTOGRAPHY',
       'Category_PRODUCTIVITY', 'Category_SHOPPING', 'Category_SOCIAL',
       'Category_SPORTS', 'Category_TOOLS', 'Category_TRAVEL_AND_LOCAL',
       'Category_VIDEO_PLAYERS', 'Category_WEATHER'})
