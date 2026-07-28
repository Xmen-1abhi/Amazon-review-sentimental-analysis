import streamlit as st
import pandas as pd
from vaderSentiment.vaderSentiment import SentimentIntensityAnalyzer
import plotly.express as px
st.set_page_config(page_title="Amazon Review Sentimental analysis ",page_icon="https://cdn-icons-png.freepik.com/512/14510/14510040.png")
st.title(":violet[Amazon Review Sentimental  Analysis]",text_alignment="center")
choice=st.sidebar.selectbox(":violet[MY MENU]",("HOME","MOBILE","LAPTOP"))
st.logo("https://cdn-icons-png.flaticon.com/512/1379/1379403.png")
st.markdown("<style>[data-testid=stSidebarContent] {color:#B2FF66; background-color: #FFB266; }</style>", unsafe_allow_html=True)
if(choice=="HOME"):
    st.badge("NEW")
    st.markdown(":violet-badge[:material/star: Favorite] :orange-badge[⚠️ Needs review]")
    st.image("https://miro.medium.com/1*_JW1JaMpK_fVGld8pd1_JQ.gif",width=400)
    st.header("*Title*")
    st.markdown("This is a project which helps you to understand public oponion from sources like reviews, social media and surveys to improve the products. :star:")
    st.markdown("This sentimental analysis gives the postive, negative and neutral sentiments of the products accoording to the reviews given by the users to understand the standard of the products.")
elif(choice=="MOBILE"):
    st.header(":red[Mobile Sentimental Analysis]",text_alignment="center")
    df=pd.read_csv("results.csv")
    choice2=st.selectbox(":red[Choose visualization]",("None","Pie Chart","Histogram","Table Chart"))
    if(choice2=="Pie Chart"):
        posper=(len(df[df["Sentimental"]=="Positive"])/len(df))*100
        negper=(len(df[df["Sentimental"]=="Negative"])/len(df))*100
        neuper=(len(df[df["Sentimental"]=="Neutral"])/len(df))*100
        fig=px.pie(values=[posper,negper,neuper],names=["Positive","Negative","Neutral"])
        st.plotly_chart(fig)
    elif(choice2=="Histogram"):
        c=st.selectbox("Choose Column",df.columns)
        fig=px.histogram(x=df[c],color=df["Sentimental"])
        st.plotly_chart(fig)
    elif(choice2=="Table Chart"):
        st.dataframe(df)
elif(choice=="LAPTOP"):
    st.header(":red[Laptop Sentimental Analysis]",text_alignment="center")
    df1=pd.read_csv("results1.csv")
    choice3=st.selectbox(":red[Choose visualization]",("None","Pie Chart","Histogram","Table Chart"))
    if(choice3=="Pie Chart"):
        posper1=(len(df1[df1["Sentimental"]=="Positive"])/len(df1))*100
        negper1=(len(df1[df1["Sentimental"]=="Negative"])/len(df1))*100
        neuper1=(len(df1[df1["Sentimental"]=="Neutral"])/len(df1))*100
        fig1=px.pie(values=[posper1,negper1,neuper1],names=["Positive","Negative","Neutral"])
        st.plotly_chart(fig1)
    elif(choice3=="Histogram"):
        c1=st.selectbox("Choose Column",df1.columns)
        fig1=px.histogram(x=df1[c1],color=df1["Sentimental"])
        st.plotly_chart(fig1)
    elif(choice3=="Table Chart"):
        st.dataframe(df1)
    
    
