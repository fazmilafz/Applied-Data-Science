# -*- coding: utf-8 -*-
"""
Created on Sat Mar  4 14:43:09 2023

@author: fazmila
"""
"""
This program plots a line graph for annual percentage of food imports for certain countries which can be used to analyse the data
"""

#Importing required libraries
import pandas as pd
import matplotlib.pyplot as plt

#Reading the file to the dataframe 'data1'
data1 = pd.read_excel('C:/Users/user/OneDrive - University of Hertfordshire/Applied DS/food.xlsx', header=0)
print(data1)

#Funtion to plot graph for annual percentage of imports of food products for certain countries
def food(data):
    
    """
    This function plot a line grapgh  for annual percentage of food products for certain countries
    
    Parameters
    ----------
    data : TYPE
        DESCRIPTION.

    Returns
    -------
    None.
    """

    plt.figure()
    #Plotting the line graph for each country
    plt.plot(data['Year'], data['Australia'], label='Australia')
    plt.plot(data['Year'], data['Japan'], label='Japan')
    plt.plot(data['Year'], data['Spain'], label='Spain')
    plt.plot(data['Year'], data['United States'], label='US')
    plt.plot(data['Year'], data['United Kingdom'], label='UK')
    plt.xlabel('Year')
    plt.xticks(rotation='vertical')
    plt.ylabel('Percentage of imported food')
    plt.title(" Percentage of Food Imports ")
    plt.legend(bbox_to_anchor=(1.0,1.0))
    plt.savefig('line_plot.png')
    plt.show()
    
    return

#Calling the line function 
food(data1)

"""
This program plots a stacked bar plot for total covid active cases v/s total deaths for selected counties
"""
#Reading the file into a dataframe 'covid_df'
covid_df = pd.read_excel('C:/Users/user/OneDrive - University of Hertfordshire/Applied DS/cov.xlsx')
print(covid_df)

def bar(covid):
    """
    This function plot a stacked bar graph for total covid active cases v/s total deaths for selected counties

    Parameters
    ----------
    covid : TYPE
        DESCRIPTION.

    Returns
    -------
    None.

    """
    #Assaigning value to give width of the graph
    x = 0.5
    plt.figure(figsize=(12,7))
    
    #Plotting the bar graph for covid active cases v/s death cases for each contry
    plt.bar(covid['Country'], covid['Active Cases'],  width=x, label="Active Cases")
    plt.bar(covid['Country'], covid['Total Deaths'],  width=x, label="Total Deaths")
    plt.xlabel('Country')
    plt.ylabel('Population')
    plt.title("Total Covid Active Cases V/S Total Deaths")
    plt.legend()
    plt.save('bar_plot.png')
    plt.show()
    
    return

#Calling the bar function
bar(covid_df)

"""
This program plots a pie chart for total Covid cases over selected countries
"""

#Reading the file into a dataframe 'data'
data = pd.read_excel('C:/Users/user/OneDrive - University of Hertfordshire/Applied DS/cov.xlsx', header=0)
print(data)

def covid(x):
    """
    This function plot a pie chart for total Covid cases over selected countries

    Parameters
    ----------
    x : TYPE
        DESCRIPTION.

    Returns
    -------
    None.

    """
    #Plotting the pie graph of total covid cases for selected countries
    us_data= data[data["Country"] == "USA"]     
    us_sum_data= us_data["Total Cases"].sum()

    india_data= data[data["Country"] == "India"] 
    india_sum_data= india_data["Total Cases"].sum()

    france_data= data[data["Country"] == "France"] 
    france_sum_data= france_data["Total Cases"].sum()

    germany_data= data[data["Country"] == "Germany"] 
    germany_sum_data= germany_data["Total Cases"].sum()

    brazil_data= data[data["Country"] == "Brazil"] 
    brazil_sum_data= brazil_data["Total Cases"].sum()

    japan_data= data[data["Country"] == "Japan"] 
    japan_sum_data= japan_data["Total Cases"].sum()

    korea_data= data[data["Country"] == "South Korea"] 
    korea_sum_data= korea_data["Total Cases"].sum()

    italy_data= data[data["Country"] == "Italy"] 
    italy_sum_data= italy_data["Total Cases"].sum()
    
    uk_data= data[data["Country"] == "UK"] 
    uk_sum_data= uk_data["Total Cases"].sum()

    russia_data= data[data["Country"] == "Russia"] 
    russia_sum_data= russia_data["Total Cases"].sum()


    sum_list = [us_sum_data, india_sum_data, france_sum_data, germany_sum_data, brazil_sum_data, japan_sum_data , korea_sum_data, italy_sum_data, uk_sum_data, russia_sum_data ]
    country_names=["USA", "India","France","Germany","Brazil","Japan","South Korea","Italy","UK","Russia" ]
    plt.figure(figsize=(20,15))
    plt.pie(sum_list, autopct="%0.1f%%", labels=(country_names))
    plt.title("Total Covid Cases")
    plt.legend()
    plt.save('pie_plot.png')
    plt.show()
    
    return

#Calling the pie function
covid(data)