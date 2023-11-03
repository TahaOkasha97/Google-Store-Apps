import streamlit as st
import pandas as pd
from dummies import *

import joblib
model=joblib.load('regression_model.h5')
scaler=joblib.load('scaler.h5')
 
st.title("Google Store Apps Project")
st.info("A rough prediction of the number of potential users (Installs) for android app")

#Rating= st.number_input("Enter Rating")
Rating = st.slider(Rating, min_value=0, max_value=5, value=4, step=0.1)
Reviews= st.number_input("Reviews")
Price= st.number_input("Price")
Last_Updated_Year= st.number_input("Last Updated Year")
Min_Android_Ver = st.number_input("Min Android Ver ",step=1e-1)
Category_select = st.selectbox("Select Category",{"Category_ART_AND_DESIGN",'Category_AUTO_AND_VEHICLES', 'Category_BEAUTY',
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
Category = category_dummies[Category_select]

Content_Rating_select = st.selectbox("Select content rating",{'Content_Rating_Everyone', 'Content_Rating_Everyone 10+',
       'Content_Rating_Mature 17+', 'Content_Rating_Teen',
       'Content_Rating_Unrated',"Content_Rating_Adults only 18+"})
Content_Rating = Content_Rating_dummies[Content_Rating_select]

data = [Rating,Reviews,Price,Last_Updated_Year,Min_Android_Ver]
data = data + Category + Content_Rating

# create a new empty DataFrame with the correct column names
df = pd.DataFrame(columns=['Rating', 'Reviews', 'Price', 'Last_Updated_Year',
       'Min_Android_Ver','Category_AUTO_AND_VEHICLES', 'Category_BEAUTY',
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
       'Category_VIDEO_PLAYERS', 'Category_WEATHER','Content_Rating_Everyone', 'Content_Rating_Everyone 10+',
       'Content_Rating_Mature 17+', 'Content_Rating_Teen',
       'Content_Rating_Unrated'])

# append the new row to the DataFrame
df.loc[len(df)] = data
st.write(df)
data_scaled = scaler.transform(df)
result = model.predict(df)
st.write("Predicted Installs")
st.write(result)
