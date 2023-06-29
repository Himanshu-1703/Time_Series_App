import streamlit as st
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import time
from PIL import Image

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
        
        # plot the trend plot
        # filter the df
        if year == 'All':
            col1,col2 = st.columns(2)
            st.subheader('Sample of Data')
            # print a few columns of the dataframe
            st.dataframe(df.iloc[:,0:-2].sample(10),width=1500)
            
            st.subheader('Plots')
            fig1,ax1 = plt.subplots(figsize=(12,7))
            df[df.columns[0]].plot(ax=ax1,)
            plt.title(f'Analysis plot for {df.columns[0]}',fontdict={'size':20})
            ax1.set_ylabel('Oil Volume(m^3/day)',fontdict={'size':20})
            plt.xticks(rotation=60)
            plt.tight_layout()
            st.pyplot(fig1)
            

            fig2,ax2 = plt.subplots(figsize=(12,7))
            df[df.columns[7]].plot(ax=ax2)
            plt.title(f'Analysis plot for {df.columns[7]}',fontdict={'size':20})
            ax2.set_ylabel('Reservoir Pressure(atm)',fontdict={'size':20})
            plt.xticks(rotation=60)
            plt.tight_layout()
            st.pyplot(fig2)
            
            fig3,ax3 = plt.subplots(figsize=(12,7))
            df[['oil_volume','volume_of_liquid', 'water_volume']].plot(ax=ax3)
            plt.title(f'Analysis plot for year {year}',fontdict={'size':20})
            ax3.set_ylabel('Volume(m^3/day)',fontdict={'size':20})
            plt.legend(prop={'size':15})
            plt.xticks(rotation=60)
            plt.tight_layout()
            st.pyplot(fig3)
            
            fig4,ax4 = plt.subplots(figsize=(12,7))
            df[['working_hours']].plot(ax=ax4)
            plt.title(f'Analysis plot for year {year}',fontdict={'size':20})
            ax4.set_ylabel('No. of Hours',fontdict={'size':20})
            plt.legend(prop={'size':15})
            plt.xticks(rotation=60)
            plt.tight_layout()
            st.pyplot(fig4)
                
        else:
            st.subheader('Sample of Data')
            filt_year = df[df['year'] == year]
            # print a few columns of the dataframe
            st.dataframe(filt_year.iloc[:,0:-2].sample(10),width=1500)
            
            st.subheader('Plots')
            
            fig1,ax1 = plt.subplots(figsize=(12,7))
            filt_year[df.columns[0]].plot(ax=ax1,)
            plt.title(f'Analysis plot for {df.columns[0]} for year {year}',fontdict={'size':20})
            ax1.set_ylabel('Oil Volume(m^3/day)',fontdict={'size':20})
            plt.xticks(rotation=60)
            plt.tight_layout()
            st.pyplot(fig1)
            
    
            fig2,ax2 = plt.subplots(figsize=(12,7))
            filt_year[df.columns[7]].plot(ax=ax2)
            plt.title(f'Analysis plot for {df.columns[7]} for year {year}',fontdict={'size':20})
            ax2.set_ylabel('Reservoir Pressure(atm)',fontdict={'size':20})
            plt.xticks(rotation=60)
            plt.tight_layout()
            st.pyplot(fig2)
            
            
            fig3,ax3 = plt.subplots(figsize=(12,7))
            filt_year[['oil_volume','volume_of_liquid', 'water_volume']].plot(ax=ax3)
            plt.title(f'Analysis plot for year {year}',fontdict={'size':20})
            ax3.set_ylabel('Volume(m^3/day)',fontdict={'size':20})
            plt.legend(prop={'size':15})
            plt.xticks(rotation=60)
            plt.tight_layout()
            st.pyplot(fig3)
            
            fig4,ax4 = plt.subplots(figsize=(12,7))
            filt_year[['working_hours']].plot(ax=ax4)
            plt.title(f'Analysis plot for year {year}',fontdict={'size':20})
            ax4.set_ylabel('No. of Hours',fontdict={'size':20})
            plt.legend(prop={'size':15})
            plt.xticks(rotation=60)
            plt.tight_layout()
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
        
        image = 'D:\Web-Applications\Oil well\prediction copy.png'
        image_file = Image.open(image)
        
        st.image(image=image_file,width=800)
        