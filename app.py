import streamlit as st
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import time
from PIL import Image
from plotter import comp_plots,time_series_plot

# make the dataframe
df = pd.read_csv('cleaned_data.csv')
df.set_index('date',inplace=True)

# title for the app
st.title('Oil Well Operation Parameters (2013-2021), Siberia, Russia')

# sidebar title
st.sidebar.title("Time Series Analysis")

years = ['All'] + list(df['year'].unique())  

# 1st option for sidebar
analysis = st.sidebar.selectbox(label='Choose the Analysis',
                                options=['Descriptive Analysis',
                                        'Predictive Analysis'])

if analysis == 'Descriptive Analysis':
    year = st.sidebar.selectbox(label='Choose the Year',
                                options=years)
    
    
    desc_btn = st.sidebar.button(label='Press for Analysis')
    if desc_btn:
        
        if year == 'All':
            st.subheader('Sample of Data')
            # print a few rows of the dataframe
            st.dataframe(df.iloc[:,0:-2].sample(10),width=1500)
            
            # plot the plots for the complete data
            st.subheader('Plots')
            
            # plot the time series plots
            fig1,fig2 = time_series_plot(data_frame=df,year=year)
            
            #plot the graph for oil volume
            st.pyplot(fig1)
            
            # plot the graph for reservoir pressure
            st.pyplot(fig2)
            
            # plot the comparison plots
            fig3,fig4 = comp_plots(data_frame=df,year=year)
            
            # plot the comparison graphs for liquids
            st.pyplot(fig3)
            
            # plot the comparison graphs for working hours
            st.pyplot(fig4)
                
        else:
            st.subheader('Sample of Data')
            filt_year = df[df['year'] == year]
            # print a few columns of the dataframe
            st.dataframe(filt_year.iloc[:,0:-2].sample(10),width=1500)
            
            st.subheader('Plots')
            
            # plot the time series plots
            fig1,fig2 = time_series_plot(data_frame=filt_year,year=year)
            
            #plot the graph for oil volume
            st.pyplot(fig1)
            
            # plot the graph for reservoir pressure
            st.pyplot(fig2)
            
            # plot the comparison plots
            fig3,fig4 = comp_plots(data_frame=filt_year,year=year)
            
            # plot the comparison graphs for liquids
            st.pyplot(fig3)
            
            # plot the comparison graphs for working hours
            st.pyplot(fig4)
         
            
    
elif analysis == 'Predictive Analysis':
      pred_btn = st.sidebar.button('Press for Prediction')
      
      if pred_btn:
        prog_bar = st.progress(value=0,text='Model is Training')
        
        for i in range(100):
            time.sleep(0.3)
            prog_bar.progress(value=i + 1,text='Model is Training')
        
        st.success('Model training is completed')
        
        st.subheader('Results')
        results_df = pd.read_csv('results copy.csv')
        results_df.drop(columns=results_df.columns[0],inplace=True)
        
        st.dataframe(results_df,width=800)
        
        st.subheader('Prediction Plot')
        
        image = 'prediction copy.png'
        image_file = Image.open(image)
        
        st.image(image=image_file,width=800)
        