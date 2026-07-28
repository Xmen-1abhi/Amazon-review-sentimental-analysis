import streamlit as st
import pandas as pd
from vaderSentiment.vaderSentiment import SentimentIntensityAnalyzer
import plotly.express as px
st.set_page_config(page_title="Sentimental analysis system",page_icon="https://cdn-icons-png.flaticon.com/512/9850/9850903.png")
st.title("[Sentimental System Analysis]",text_alignment="center")
choice=st.sidebar.selectbox("My Menu",("HOME","ANALYSIS","VISUALIZATION"))
st.markdown("<style>[data-testid=stSidebar] { background-color: #ff000050; }</style>", unsafe_allow_html=True)
st.markdown("<style>[sidebar.sidebar-content]{color:blue;}</style>",unsafe_allow_html=True)
if(choice=="HOME"):
    st.badge("NEW")
    st.markdown(":violet-badge[:material/star: Favorite] :orange-badge[⚠️ Needs review]")
    st.image("https://miro.medium.com/v2/resize:fit:1280/1*TxNDsw1op7sxikKd6Sk08w.gif",width=400)
    st.header("*About*")
    st.markdown("This is a project which helps you to understand public oponion from sources like reviews, social media and surveys to improve the products. :star:")
elif(choice=="ANALYSIS"):
    url=st.text_input(":blue[Enter google sheet url]")
    cn=st.text_input(":blue[Enter column name to be analyzed]")
    btn=st.button("analyze")
    if btn:
        df=pd.read_csv("https://docs.google.com/spreadsheets/d/1ik-JvaLiYBR7g1ABiXDcTp7AtlWI3Dr04N04qxMhXI0/export?format=csv&usp=sharing")
        x=df['Opinion']
        mymodel=SentimentIntensityAnalyzer()
        l=[]
        for k in x:
            pred=mymodel.polarity_scores(k)
            if(pred['compound']>0.01):
                l.append( "Positive")
            elif(pred['compound']<-0.01):
                l.append( "Negative")
            else:
                l.append("Neutral")
        df['Sentimental']=l
        print(df)
        df.to_csv("results.csv",index=False)
        st.write("Analysis is successfull and result are saved as result.csv file")
elif(choice=="VISUALIZATION"):
    st.markdown(":violet-badge[:material/star: Graph]")
    df=pd.read_csv("results.csv")
    choice2=st.selectbox("Choose Visualization",("None","Pie Chart","Histogram","Table Chart"))
    if(choice2=="Table Chart"):
        st.dataframe(df)
    elif(choice2=="Pie Chart"):
        posper=(len(df[df["Sentimental"]=="Positive"])/len(df))*100
        negper=(len(df[df["Sentimental"]=="Negative"])/len(df))*100
        neuper=(len(df[df["Sentimental"]=="Neutral"])/len(df))*100
        fig=px.pie(values=[posper,negper,neuper],names=["Positive","Negative","Neutral"])
        st.plotly_chart(fig)
    elif(choice2=="Histogram"):
        c=st.selectbox("Choose Column",df.columns)
        fig=px.histogram(x=df[c],color=df["Sentimental"])
        st.plotly_chart(fig)
