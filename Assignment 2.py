# -*- coding: utf-8 -*-
"""
Created on Tue Apr  4 06:53:37 2023

@author: fazmila
"""
#importing required libraries
import numpy as np
import matplotlib.pyplot as plt
import pandas as pd
import seaborn as sns

#Funtion to plot bar graph for percentage of co2 emissions from gaseous fuel consumption for 7 countries
def co2_emission(a):
    """
    This function reads files in the world bank data format, sets columns, renames columns with new names, Rows having null values are dropped and plots bar graph for countries(x-axis) vs Population(y-axis).Visualization method used is BAR GRAPH
    Parameters
    ----------
    a : TYPE
        DESCRIPTION.

    Returns
    -------
    None.

    """
    a.isnull().sum()
    a.describe()
    a.corr()
    a.cov()
    a.fillna(0,inplace=True)
    print(a)

    co2 = a[a['Indicator Name']=='CO2 emissions from gaseous fuel consumption (% of total)']
    print(co2)

    carbon = co2[co2['Country Name'].isin(['India','Japan','Pakistan','Poland','United States','Italy','Australia'])]
    print(carbon)

    bar_width = 0.1
    # variables declared to set the position of xticks for bar graphs
    r1 = np.arange(len(carbon))
    r2 = [x + bar_width for x in r1]
    r3 = [x + bar_width for x in r2]
    r4 = [x + bar_width for x in r3]
    r5 = [x + bar_width for x in r4]
    r6 = [x + bar_width for x in r5]
    r7 = [x + bar_width for x in r6]


    plt.subplots(figsize=(20,14))
    plt.bar(r1, carbon['2000'],color='darkslategray',width=bar_width,edgecolor='black', label='2000')
    plt.bar(r2, carbon['2001'],color='teal', width=bar_width,edgecolor='black', label='2001')
    plt.bar(r3, carbon['2002'],color='powderblue',width=bar_width,edgecolor='black', label='2002')
    plt.bar(r4, carbon['2003'],color='darkcyan',width=bar_width,edgecolor='black', label='2003')
    plt.bar(r5, carbon['2004'],color='cadetblue',width=bar_width,edgecolor='black', label='2004')
    plt.bar(r6, carbon['2005'],color='cyan',width=bar_width,edgecolor='black', label='2005')
    plt.bar(r7, carbon['2006'],color='black',width=bar_width,edgecolor='black', label='2006')
    plt.xlabel("Countries", fontsize=30)
    plt.title('CO2 Emission', size=35)    
    plt.xticks([r + bar_width*2 for r in range(len(carbon))], carbon['Country Name'],fontsize=25)
    plt.yticks(fontsize=25)
    plt.legend(fontsize=25)
    plt.savefig('co2 emission.png', bbox_inches="tight", dpi=300)
    plt.show()

#Funtion to plot line graph for percentage of annual urban population growth for 7 countries
def urban_pol(b):
    """
    This function plots line graph for years(x-axis) vs percentage of urban population(y-axis).Visualization method used is LINE GRAPH

    Parameters
    ----------
    b : TYPE
        DESCRIPTION.

    Returns
    -------
    None.

    """
    co2 = b[b['Indicator Name']=='Urban population growth (annual %)']
    urban = co2[co2['Country Name'].isin(['India','Japan','Pakistan','Poland','United States','Italy','Australia'])]
    #renaming columns, dropping null values and transposing for all dataframes
    Trans = urban.transpose()
    Trans.rename(columns=Trans.iloc[0], inplace = True)
    urban_transpose = Trans.iloc[4:]
    urban_transpose.fillna(0,inplace = True)

    print(urban_transpose)

    plt.figure(figsize=(20,14))
    plt.plot(urban_transpose.index,urban_transpose['India'],linestyle='dashed',label='India')
    plt.plot(urban_transpose.index,urban_transpose['Japan'],linestyle='dashed',label='Japan')
    plt.plot(urban_transpose.index,urban_transpose['Pakistan'],linestyle='dashed',label='Pakistan')
    plt.plot(urban_transpose.index,urban_transpose['Poland'],linestyle='dashed',label='Poland')
    plt.plot(urban_transpose.index,urban_transpose['United States'],linestyle='dashed',label='United States')
    plt.plot(urban_transpose.index,urban_transpose['Italy'],linestyle='dashed',label='Italy')
    plt.plot(urban_transpose.index,urban_transpose['Australia'],linestyle='dashed',label='Australia')
    plt.xlim('2000','2006')
    plt.xlabel('Year',fontsize=26)
    plt.ylabel('Percentage',fontsize=26)
    plt.title('Annual Percentage of Urban Population Growth', size=30)
    plt.xticks(fontsize=25)
    plt.yticks(fontsize=25)
    plt.legend(bbox_to_anchor=(1.0,1.0),fontsize=23)
    plt.savefig('urban pop.png', bbox_inches="tight", dpi=300)
    plt.show()

#Funtion to plot heatmap for India
def heatmap(c):
    """
    This function plots heatmap for India by using indicators CO2 emissions from gaseous fuel consumption (% of total), Other greenhouse gas emissions (% change from 1990), Urban population growth (annual %), Arable land (% of land area), Agricultural land (% of land area)

    Parameters
    ----------
    c : TYPE
        DESCRIPTION.

    Returns
    -------
    None.

    """
    indicator = ['CO2 emissions from gaseous fuel consumption (% of total)','Other greenhouse gas emissions (% change from 1990)','Urban population growth (annual %)','Arable land (% of land area)','Agricultural land (% of land area)']
    
    country=data.loc[data['Country Name']=='India']
    
    df = country[country['Indicator Name'].isin(indicator)]
    print(df)
    
    indicator_df = df.pivot_table(df,columns= data['Indicator Name'])
    indicator_df.corr()

    plt.figure(figsize=(20,14))
    sns.heatmap(indicator_df.corr(),fmt='.2g',annot=True,cmap='BuPu',linecolor='black')
    plt.title('India',fontsize=30)
    plt.savefig('heatmap1.png', bbox_inches="tight", dpi=300)
    plt.show()

#Funtion to plot bar graph for percentage of total greenhouse gas emission
def greenhouse(d):
    """
    This function plots bar graph for countries(x-axis) vs Total greenhouse gas emissions(y-axis).Visualization method used  is BAR GRAPH

    Parameters
    ----------
    d : TYPE
        DESCRIPTION.

    Returns
    -------
    None.

    """
    green_house = d[d['Indicator Name']=='Total greenhouse gas emissions (% change from 1990)']
    print(green_house)

    cfc = green_house[green_house['Country Name'].isin(['India','Japan','Pakistan','Poland','United States','Italy','Australia'])]
    print(cfc)

    bar_width = 0.1
    # variables declared to set the position of xticks for bar graphs
    r1 = np.arange(len(cfc))
    r2 = [x + bar_width for x in r1]
    r3 = [x + bar_width for x in r2]
    r4 = [x + bar_width for x in r3]
    r5 = [x + bar_width for x in r4]
    r6 = [x + bar_width for x in r5]
    r7 = [x + bar_width for x in r6]


    plt.subplots(figsize=(20,14))
    plt.bar(r1, cfc['2000'],color='lightcoral',width=bar_width,edgecolor='black', label='2000')
    plt.bar(r2, cfc['2001'],color='mistyrose', width=bar_width,edgecolor='black', label='2001')
    plt.bar(r3, cfc['2002'],color='tomato',width=bar_width,edgecolor='black', label='2002')
    plt.bar(r4, cfc['2003'],color='peachpuff',width=bar_width,edgecolor='black', label='2003')
    plt.bar(r5, cfc['2004'],color='rosybrown',width=bar_width,edgecolor='black', label='2004')
    plt.bar(r6, cfc['2005'],color='peru',width=bar_width,edgecolor='black', label='2005')
    plt.bar(r7, cfc['2006'],color='pink',width=bar_width,edgecolor='black', label='2006')    
    plt.xlabel("Countries", fontsize=30)
    plt.title('Total Green House Gas Emission',size=35)
    plt.xticks([r + bar_width*2 for r in range(len(cfc))], cfc['Country Name'],fontsize=25)
    plt.yticks(fontsize=25)
    plt.legend(fontsize=25)
    plt.savefig('emission.png', bbox_inches="tight", dpi=300)
    plt.show()


#Funtion to plot line graph for percentage of arable land area for 7 countries
def arable_land(e):
    """
    This function plots line graph for years(x-axis) vs percentage of arable land area(y-axis).Visualization method used is LINE GRAPH

    Parameters
    ----------
    e : TYPE
        DESCRIPTION.

    Returns
    -------
    None.

    """
    cfc = e[e['Indicator Name']=='Arable land (% of land area)']
    urban_pop = cfc[cfc['Country Name'].isin(['India','Japan','Pakistan','Poland','United States','Italy','Australia'])]
    #renaming columns, dropping null values and transposing for all dataframes
    Trans_new = urban_pop.transpose()
    Trans_new.rename(columns=Trans_new.iloc[0], inplace = True)
    urban_trans = Trans_new.iloc[4:]
    urban_trans.fillna(0,inplace = True)

    print(urban_trans)
    
    plt.figure(figsize=(18,12))
    plt.plot(urban_trans.index,urban_trans['India'],linestyle='dashed',label='India')
    plt.plot(urban_trans.index,urban_trans['Japan'],linestyle='dashed',label='Japan')
    plt.plot(urban_trans.index,urban_trans['Pakistan'],linestyle='dashed',label='Pakistan')
    plt.plot(urban_trans.index,urban_trans['Poland'],linestyle='dashed',label='Poland')
    plt.plot(urban_trans.index,urban_trans['United States'],linestyle='dashed',label='United States')
    plt.plot(urban_trans.index,urban_trans['Italy'],linestyle='dashed',label='Italy')
    plt.plot(urban_trans.index,urban_trans['Australia'],linestyle='dashed',label='Australia')
    plt.xlim('2000','2006')
    plt.xlabel('Year',fontsize=26)
    plt.ylabel('Percentage',fontsize=26)
    plt.title('Percentage of Arable Land Area', size=30)
    plt.xticks(fontsize=25)
    plt.yticks(fontsize=25)
    plt.legend(loc='best',fontsize=23)                               
    plt.savefig('arable land.png', bbox_inches="tight", dpi=300)
    plt.show()
    

#Funtion to plot heatmap for India
def heat_map2(f):
    """
    This function plots heatmap for Japan by using indicators CO2 emissions from gaseous fuel consumption (% of total), Other greenhouse gas emissions (% change from 1990), Urban population growth (annual %), Arable land (% of land area), Agricultural land (% of land area)


    Parameters
    ----------
    f : TYPE
        DESCRIPTION.

    Returns
    -------
    None.

    """
    indicator = ['CO2 emissions from gaseous fuel consumption (% of total)','Other greenhouse gas emissions (% change from 1990)','Urban population growth (annual %)','Arable land (% of land area)','Agricultural land (% of land area)']
    country_new = data.loc[data['Country Name']=='Japan']
    df_new = country_new[country_new['Indicator Name'].isin(indicator)]
    print(df_new)
    indicator_df1 = df_new.pivot_table(df_new,columns= data['Indicator Name'])
    indicator_df1.corr()
    
    plt.figure(figsize=(20,14))
    sns.heatmap(indicator_df1.corr(),fmt='.2g',annot=True,cmap='BuPu',linecolor='black')
    plt.title('Japan',fontsize=30)
    plt.savefig('heatmap2.png', bbox_inches="tight", dpi=300)
    plt.show()

#Reading the file to the dataframe 'data'
data = pd.read_csv('C:/Users/user/Documents/assignment2/C02 emission.csv')
print(data)
#calling the c02_emission function
co2_emission(data)
#calling the urban_pol function
urban_pol(data)
#calling the heatmap function
heatmap(data)
#calling the greenhouse function
greenhouse(data)
#calling the arable_land function
arable_land(data)
#calling the heat_map function
heat_map2(data)
