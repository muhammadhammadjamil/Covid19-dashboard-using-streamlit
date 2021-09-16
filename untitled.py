# -*- coding: utf-8 -*-
"""
Created on Fri Mar 12 13:33:27 2021

@author: Dell
"""
import pandas as pd
import streamlit as st
import altair as alt
st.cache(persist=True)
def load_data():
    covid = pd.read_csv("C:\\Users\\Dell\\Desktop\\data.csv")
    covid["Date"]=pd.to_datetime(covid["Date"],format="%d-%m-%Y")
    latest=covid[covid["Date"] == "2020-11-30"][["Country","Confirmed","Recovered","Deaths","Active"]]
    return covid,latest
covid,latest= load_data()



st.title('🦠 Covid-19 Dashborad 🦠 ')
st.sidebar.markdown('🦠 **Covid-19 Dashborad** 🦠 ')
st.sidebar.markdown(''' 
This app is to give insights about Covid-19 Infections around the world.
The data considerd for this analysis for 10 Months starting from 01-02-2020 to 30-11-2020
Select the different options to vary the Visualization
All the Charts are interactive. 

Designed by:    
    
    
** M hammad jamil**  ''')  

st.header("Select the Country to Visualize the Covid-19 Cases")   
cnty = st.selectbox("Select country",covid["Country"][:186])
st.header(f"View Daily New Cases/Recoveries/Deaths for {cnty}")
daily = st.selectbox("Select the option",('Daily New Cases', 'Daily New Recoveries','Daily New Deaths'))
typ = st.radio("Select the type of Chart",("Bar Chart","Scatter Chart"))
dnc = alt.Chart(covid[covid["Country"]==cnty]).mark_point().encode(
    x="Date",
    y="New cases",
    tooltip=["Date","Country","New cases"]
).interactive().properties(
    width=800,
    height=400
)
dnr = alt.Chart(covid[covid["Country"]==cnty]).mark_point().encode(
    x="Date",
    y="New recovered",
    tooltip=["Date","Country","New recovered"]
).interactive().properties(  width=800,
    height=400)                                                        
dnd = alt.Chart(covid[covid["Country"]==cnty]).encode(
     x="Date",
     y="New deaths",
     tooltip=["Date","Country","New deaths"]
    ).interactive()
if daily =='Daily New Cases':
    if typ == "Bar Chart":
        st.altair_chart(dnc.mark_bar(color='firebrick'))
    else:
        st.altair_chart(dnc.mark_circle(color='firebrick'))
elif daily=='Daily New Recoveries':
    if typ=='Bar Chart':
        st.altair_chart(dnr.mark_bar(color='Blue'))
    else:
        st.altair_chart(dnr.mark_circle(color='Black'))
elif daily=="Daily New Deaths":
    if typ=="Bar Chart":
        st.altair_chart(dnd.mark_bar(color='Black'))
    else:
        st.altair_chart(dnd.mark_circle(color='Blue'))
st.header(f"Summary of Covid-19 infections in {cnty}")
"From 01-02-2020 to 30-11-2020"
tot=latest[latest["Country"]==cnty]['Confirmed'].sum()

#st.subheader(f"Total Confirmed cases in {cnty} = {tot}")

reco = latest[latest["Country"]==cnty]['Recovered'].sum()

#st.subheader(f"Total Recovered in {cnty} = {reco}")

act = latest[latest["Country"]==cnty]['Active'].sum()

#st.subheader(f"Total Active cases in {cty} = {act}")

dths = latest[latest["Country"]==cnty]['Deaths'].sum()

#st.subheader(f"Total Deaths occured in {cty} = {dths}")
infsing = covid[covid["Country"]==cnty]['New cases'].max()

deasing = covid[covid["Country"]==cnty]['New deaths'].max()

recsing = covid[covid["Country"]==cnty]['New recovered'].max()

tab = {"Category":["Total Confirmed Cases","Total Recovered","Total Active Cases","Total Deaths","Maximum Cases on a Single Day","Maximum Deaths on a Single Day","Maximum Recoveries on a Single Day"],
       "Total Count":[tot,reco,act,dths,infsing,deasing,recsing]}
stat = pd.DataFrame(tab)
st.table(stat)
st.header(f"View Covid-19 Country Standings")
ques = st.radio("Select the option to know details",["Total Confirmed Cases","Total Recovered",
                                                      "Total Deaths","Total Active Cases"])
if ques=='Total Confirmed Cases':
    df=latest.sort_values(by='Confirmed',ascending=False)[['Country','Confirmed']]
    st.dataframe(df)
elif ques=='Total Recovered':
    df=latest.sort_values(by='Recovered',ascending=False)[['Country','Recovered']]
    st.dataframe(df)
elif ques=='Total Deaths':
    df=latest.sort_values(by='Deaths',ascending=False)[['Country','Deaths']]
    st.dataframe(df)
elif ques=='Total Active Cases':
    df=latest.sort_values(by='Active',ascending=False)[['Country','Active']]
    st.dataframe(df)