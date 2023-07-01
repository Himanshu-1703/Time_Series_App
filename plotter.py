import pandas as pd
import matplotlib.pyplot as plt

def time_series_plot(data_frame,year):
    # plot for time series data for oil volume
    
    fig1,ax1 = plt.subplots(figsize=(12,7))
    data_frame[data_frame.columns[0]].plot(ax=ax1)
    plt.title(f'Analysis plot for {data_frame.columns[0]} for year {year}',fontdict={'size':20})
    ax1.set_ylabel('Oil Volume(m^3/day)',fontdict={'size':20})
    plt.xticks(rotation=60)
    plt.tight_layout()

    # plot for time series data of reservoir pressure
    
    fig2,ax2 = plt.subplots(figsize=(12,7))
    data_frame[data_frame.columns[7]].plot(ax=ax2)
    plt.title(f'Analysis plot for {data_frame.columns[7]} for year {year}',fontdict={'size':20})
    ax2.set_ylabel('Reservoir Pressure(atm)',fontdict={'size':20})
    plt.xticks(rotation=60)
    plt.tight_layout()
    
    return fig1,fig2
    
def comp_plots(data_frame,year):
    # plot the comparison plots for liquids
    
    fig1,ax1 = plt.subplots(figsize=(12,7))
    data_frame[['oil_volume','volume_of_liquid', 'water_volume']].plot(ax=ax1)
    plt.title(f'Analysis plot for year {year}',fontdict={'size':20})
    ax1.set_ylabel('Volume(m^3/day)',fontdict={'size':20})
    plt.legend(prop={'size':15})
    plt.xticks(rotation=60)
    plt.tight_layout()
    
    # plot the comparison plot for working hours
    
    fig2,ax2 = plt.subplots(figsize=(12,7))
    data_frame[['working_hours']].plot(ax=ax2)
    plt.title(f'Analysis plot for year {year}',fontdict={'size':20})
    ax2.set_ylabel('No. of Hours',fontdict={'size':20})
    plt.legend(prop={'size':15})
    plt.xticks(rotation=60)
    plt.tight_layout()
    
    return fig1,fig2


    