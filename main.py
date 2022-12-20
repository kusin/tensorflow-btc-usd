## ---------------------------------------------------------- ##
## - DEKLARASI PUSTAKA -------------------------------------- ##
## ---------------------------------------------------------- ##
# pustaka untuk manipulasi data-frame
import pandas as pd
from pandas import concat
from pandas import read_csv
from pandas import read_excel
from pandas_datareader import DataReader

# pustaka untuk madnipulasi data-array
import numpy as np
from numpy import concatenate
from numpy import array

# pustaka untuk visualisasi data
import seaborn as sns
import plotly.express as px
import plotly.graph_objects as go
from matplotlib import pyplot as plt

# pustaka dashboard
import streamlit as st

# pustaka file
from main_eda import set_year;

## ---------------------------------------------------------- ##
## - AKUISISI DATA ------------------------------------------ ##
## ---------------------------------------------------------- ##
# fungsi load dataset
def load_dataset():
    
    # load dataset
    df = pd.read_csv("D:/latihan-time-series/dataset/BTC-USD.csv");
    
    # set index tanggal
    df = df.set_index("Date");

    # return value
    return df;

# membaca dataset csv
dataset = load_dataset();

## ---------------------------------------------------------- ##
## - Main Dashboard ----------------------------------------- ##
## ---------------------------------------------------------- ##
# set config streamlit
st.set_page_config(page_title="My Dashboard", layout="wide", initial_sidebar_state="auto");

# st.sidebar.title("My Dashboard");
with st.sidebar:
    st.title("My Dashboard");
    st.selectbox('Choose Dataset', ('Bitcoin USD (BTC-USD)', 'Microsoft Corporation (MSFT)', 'Apple Inc. (AAPL)', 'Google Inc. (GOOG)', 'Amazon.com Inc. (AMZN)'));
    st.date_input("Start date");
    st.date_input("End date");
    st.selectbox('Choose Algorithm', ('LSTM-RNN', 'GRU-RNN', 'Xgboost', 'Prophet'));
    st.button('Submit');

# set a title dashboard
st.markdown('## Stock Price Prediction with LSTM - GRU - Xgboost - Prophet');

# show a dataset
st.subheader("Dataset of Bitcoin USD (BTC-USD)");
st.dataframe(dataset, use_container_width=True);

# multiple plot time OHLC
st.subheader("Data Visualization Open-High-Low-Close (OHLC)");
st.plotly_chart(px.line(dataset, x=dataset.index, y=["Close", "Open", "High", "Low"], color_discrete_sequence=["blue", "green", "orange", "red"]), use_container_width=True);

# set two columns
fig1, fig2 = st.columns(2, gap="small");
with fig1:
    st.text("Open price visualization");
    st.plotly_chart(px.line(dataset, x=dataset.index, y='Open', color_discrete_sequence=["blue"]), use_container_width=True);
with fig2:
    st.text("Close price visualization");
    st.plotly_chart(px.line(dataset, x=dataset.index, y='Close', color_discrete_sequence=["green"]), use_container_width=True);

# set two columns
fig1, fig2 = st.columns(2, gap="small");
with fig1:
    st.text("High price visualization");
    st.plotly_chart(px.line(dataset, x=dataset.index, y='High', color_discrete_sequence=["orange"]), use_container_width=True);
with fig2:
    st.text("Low price visualization");
    st.plotly_chart(px.line(dataset, x=dataset.index, y='Low', color_discrete_sequence=["red"]), use_container_width=True);

# plot EDA
st.subheader("Exploratory Data Analysis (EDA)");

st.dataframe(set_year(dataset), use_container_width=True);