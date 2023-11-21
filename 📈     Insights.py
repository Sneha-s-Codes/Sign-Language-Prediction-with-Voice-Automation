import streamlit as st
import pandas as pd
import numpy as np
import altair as alt
import plotly.express as px
import seaborn as sns

hide_streamlit_style = """
            <style>
            MainMenu {
            visibility: hidden;
            }
            footer {
            visibility: show;
            }
            </style>
            """
st.markdown(hide_streamlit_style, unsafe_allow_html=True)

st.markdown(
    """
    <style>
    .title {
        margin-top: 0px;
        margin-bottom: 0px;
    }
    .subheader {
        font-size: 20px;  /* Adjust the font size as needed */
        font-weight: none;
        color: #D6DBDF;  /* Adjust the text color as needed */
        margin-top: 0px;
        margin-bottom: 10px;
    .tii {
        font-size: 18px;  /* Adjust the font size as needed */
        font-weight: none;
        color: #A3A3A3;  /* Adjust the text color as needed */
        margin-top: 0px;
        margin-bottom: 10px;
\    }
    </style>
    """
    , unsafe_allow_html=True
)


st.sidebar.title("\t SIGN CONNECT ")
st.sidebar.markdown("<p class='subheader' style = 'font-size : 14px; '> Connecting through Signs.   </p> <br \>", unsafe_allow_html=True)

st.title("INSIGHTS ON SIGNS!")


st.markdown("<p class='subheader'> Visualizations on different Sign Languages   </p> <br \>", unsafe_allow_html=True)

#-----------------------BAR CHART------------------------------
st.markdown("<p class='tii' style = 'font-size: 28px; font-weight: bold; margin-top: 0px;  margin-bottom: 0px;'> Bar Chart on popularity of different Sign Languages   </p> <br \>", unsafe_allow_html=True)
st.markdown("<p class='tii' style = 'font-size: 16px; font-weight: none; color: #A3A3A3; margin-top: 0px;  margin-bottom: 10px;'> This bar chart is a summary of the no. of speakers of 35 different Sign Languages along in which family that they belong to. "
            " Highest spoken Sign Langugae is the Indo-Pakistan Sign Language (belonging to the Nepalese Sign Language Family) has 6,300,000 speakers.   </p> <br \>", unsafe_allow_html=True)


df2 = pd.read_csv("C:/Users/sneha/OneDrive/Desktop/SL - Speakers.csv")
bar = st.bar_chart(data=df2, x='Short Form', y='Ethnologue Est', color='Family_or_Origin', width=0, height=600, use_container_width=True)


#------------------------ DOUGHNUT CHART ------------------------------
signlang = pd.read_csv("C:/Users/sneha/OneDrive/Desktop/Sign Lang.csv")

values = signlang.VITALITY.value_counts().reset_index()
values.columns = ["Category", "Value"]
df = pd.DataFrame(values)
def create_pie_chart():
    fig = px.pie(df, values='Value', names='Category', title='Vitality of Sign Languages',hole = 0.45, color_discrete_sequence=px.colors.sequential.Agsunset)
    return fig
st.markdown("<br /> <br /> <br /> <p class='tii' style = 'font-size: 28px; font-weight: bold; margin-top: 0px;  margin-bottom: 0px;'> Pie Chart on Vitality of different Sign Languages   </p> <br />", unsafe_allow_html=True)
st.markdown("<p class='tii' style = 'font-size: 16px; font-weight: none; color: #A3A3A3; margin-top: 0px;  margin-bottom: 10px;'> This pie chart is a summary of the vitality of 135 SLs which are recogonized world wide.  </p> <br \>", unsafe_allow_html=True)


pie_fig = create_pie_chart()
st.plotly_chart(pie_fig)

#------------------------- BAR CHART ----------------------------
shared = pd.read_csv("C:/Users/sneha/OneDrive/Desktop/Sign Lang - Shared.csv")
pop = shared.population.value_counts().reset_index()
pop.columns = ["Category", "Value"]
df3 = pd.DataFrame(pop)
cust_col = {'none': '#D6F599', '< 10K': '#436436'}
st.markdown("<br /> <br /> <br /> <p class='tii' style = 'font-size: 28px; font-weight: bold; margin-top: 0px;  margin-bottom: 0px;'> Count Plot on Popularity speaking Shared SL   </p> <br />", unsafe_allow_html=True)
st.markdown("<p class='tii' style = 'font-size: 16px; font-weight: none; color: #A3A3A3; margin-top: 0px;  margin-bottom: 10px;'> This count plot chart is a visualization on number of shared Sign Languages which are recogonized worldwide that have popularity among it's users.  </p> <br \>", unsafe_allow_html=True)

bar2 = px.bar(df3, x='Category', y='Value', color='Category', width=600, height=500, title='Population speaking Shared SL ', color_discrete_map={0: '#D6F599', 1: '#436436'})
st.plotly_chart(bar2)


# ------------------------ PIE CHART ----------------------------
shared = pd.read_csv("C:/Users/sneha/OneDrive/Desktop/Sign Lang - Shared.csv")
fam = df2.Family_or_Origin.value_counts().reset_index()
fam.columns = ["Family", "Value"]
fam2 = pd.DataFrame(fam)
def create_pie_chart():
    fig = px.pie(fam2, values='Value', names='Family', title='Family or Origin of Sign Languages', color_discrete_sequence=px.colors.sequential.Sunsetdark_r)
    return fig
st.markdown("<br /> <br /> <br /> <p class='tii' style = 'font-size: 28px; font-weight: bold; margin-top: 0px;  margin-bottom: 0px;'> Pie Chart on the families of SL   </p> <br />", unsafe_allow_html=True)
st.markdown("<p class='tii' style = 'font-size: 16px; font-weight: none; color: #A3A3A3; margin-top: 0px;  margin-bottom: 10px;'> This pie chart is a summary of the families that is shared by 135 world recogonized Sign Languages.  </p> <br \>", unsafe_allow_html=True)


pie_fig = create_pie_chart()
st.plotly_chart(pie_fig)

#-------------------------FOOTER--------------------------------
footer = """
        <style>
        a:link , a:visited{
        color: white;
        background-color: transparent;
        text-decoration: None;
        }

        a:hover,  a:active {
        color: green;
        background-color: transparent;
        text-decoration: None;
        }

        footer {
	    visibility: hidden;
	    }

        footer:after {
	    content:"App created by Sneha using Streamlit 🍁"; 
	    visibility: visible;
	    display: block;
	    position: relative;
	    #background-color: red;
	    padding: 5px;
	    top: 2px;
        }
        </style>
"""

st.markdown(footer, unsafe_allow_html=True)
