# -*- coding: utf-8 -*-
"""
Created on Mon Dec  5 16:08:30 2022

@author: Anjikutty
"""

# importing the required packages

import pandas as pd
import numpy as np
import matplotlib.pyplot as plt


# Function to transpose the datas in csv file
def transpose_data(file):
    """
    to read the file and to transpose the datas.
    file:- name of the dataframe.
    """

    data_for_graphs = pd.read_csv(file)
    data_for_graphs = data_for_graphs.transpose()
    data_for_graphs.columns = data_for_graphs.iloc[0]
    data_for_graphs = data_for_graphs.iloc[50:57]
    data_for_graphs = data_for_graphs[data_for_graphs["Belgium"].notna()]
    return data_for_graphs


# Line plot of Methane gas emission and greenhouse gas emission

def lineplot(data_f, year, countries, xlab, ylab, title, image_destination):
    """
    this function produces line graphs plotting the change in greenhouse gas
    emission and the methane gas emission with year and country in the x and
    y-axis respectively.
    data_f:- name of the dataframe.
    year:- years to be plotted.
    countries:- the countried being used.
    xlab,ylab:- labels for x and y-axis.
    title:- title for the kine plot.
    image_destination:- the destination of figure.
    """

    plt.figure(figsize=(10, 8))
    plt.plot(year, data_f[countries], label=countries)
    plt.xlabel(xlab, fontsize=15)
    plt.ylabel(ylab, fontsize=15)
    plt.title(title, fontsize=20, color="red")
    plt.legend(loc="upper right", fontsize=20)
    plt.savefig(image_destination, dpi=200)
    plt.show()
    return


# data for bar plot

def filter_bar(data):
    """
    This function returns the data after filtering it to mentioned countries and years.
    data:- the csv file to be filtered.
    """

    data = data[['Country Name', 'Indicator Name',
                 '1994', '1996', '2002', '2000', '2010', '2020']]
    data = data[(data["Country Name"] == "Austria") |
                (data["Country Name"] == "Belgium") |
                (data["Country Name"] == "Denmark") |
                (data["Country Name"] == "France") |
                (data["Country Name"] == "Ireland") |
                (data["Country Name"] == "Portugal")]
    return data

# plotting bar graph of population growth and electricity production


def barplot(bar_data, xlab, ylab, title_bar, image_desti):
    """
    This function is to produce multiple bar plots with different countries.
    bar_data:- name of the dataframe.
    xlab:- label for x axis.
    ylab:- label for y axis.
    title_bar:- title for the bar graph.
    image_desti:- the image destination to be saved as png file.
    """

    plt.figure(figsize=(28, 20))
    sub = plt.subplot(1, 1, 1)
    arr = np.arange(6)
    width = 0.2

    bar_dia1 = sub.bar(
        arr, bar_data["1994"], width, label=1994, color="violet")
    bar_dia2 = sub.bar(
        arr+width, bar_data["2000"], width, label=2000, color="indigo")
    bar_dia3 = sub.bar(
        arr+width*2, bar_data["2002"], width, label=2002, color="blue")

    sub.set_xlabel(xlab, fontsize=30)
    sub.set_ylabel(ylab, fontsize=30)
    sub.set_title(title_bar, fontsize=45)
    sub.set_xticks(arr, countries, fontsize=30, rotation=90)
    sub.legend(loc="upper right", fontsize=30)

    sub.bar_label(bar_dia1, padding=2, rotation=90, fontsize=25)
    sub.bar_label(bar_dia2, padding=2, rotation=90, fontsize=25)
    sub.bar_label(bar_dia3, padding=2, rotation=90, fontsize=25)
    plt.savefig(image_desti, dpi=200)
    plt.show()
    return


def population_average(country):
    """
    creates a function to calculate the average population growth
    of 6 countries.
    country:- the countries to be plotted.
    """
    avg_population = country.sum()/country.count()
    return avg_population


def pie(country1, country2, country3, country4, country5, country6, destination):
    """
    creates a pie chart of population growth of 6 countries 
    during the time 2006 to 2020.
    country1, country2, country3, country4, country5, 
    country6:- countries being plotted.
    """
    population_c1 = population_average(population_trans[country1])
    population_c2 = population_average(population_trans[country2])
    population_c3 = population_average(population_trans[country3])
    population_c4 = population_average(population_trans[country4])
    population_c5 = population_average(population_trans[country5])
    population_c6 = population_average(population_trans[country6])

    colors = ['Green', 'Yellow', 'Orange', 'Red', 'teal', 'purple']

    # list for pie chart
    avg_population = [population_c1, population_c2,
                      population_c3, population_c4, population_c5, population_c6]
    # list for pie chart labels
    data_countries = [country1, country2,
                      country3, country4, country5, country6]
    plt.figure()
    plt.pie(avg_population, labels=data_countries,
            colors=colors, startangle=160, autopct='%1.2f%%')
    plt.title("Mean population growth", color='blue', fontsize=25)
    plt.savefig(destination, dpi=200)
    pie = plt.show()
    return pie


# the countries used datas filtering the data as per need
countries = ['Austria', 'Belgium', 'Denmark', 'France', 'Ireland', 'Portugal']


"""
Importing the csv files and sorting it for plotting the datas
"""
# line plot visualisation

methane_emission = transpose_data("Methane emissions (% change from 1990).csv")
greenhouse_emission = transpose_data(
    "Total greenhouse gas emissions (% change from 1990).csv")


# bar plot visualisation

electricity_production = pd.read_csv(
    "Electricity production from coal sources (% of total).csv")
electricity_production = filter_bar(electricity_production)

population_growth = pd.read_csv("Population growth (annual %).csv")
population_growth = filter_bar(population_growth)

# pie chart visualisation

population_trans = transpose_data("Population growth (annual %).csv")

"""
Calling the defined function to plot the graphs
"""

# Calling line plot function

lineplot(methane_emission, methane_emission.index, countries, "years--->", "methane gas emission-->",
         "Methane gas emission during the year 2000-12", "lineplotOfMethane.png")
lineplot(greenhouse_emission, greenhouse_emission.index, countries, "years--->", "greenhouse gas emission-->",
         "greenhouse gas emission during the year 2000-12", "lineplotOfgreenhouse.png")

# calling the bar plot

barplot(electricity_production, "Countries--->", "electricity production--->",
        "The electricity production 1990-2002", "electricityProduction.png")
barplot(population_growth, "Countries--->", "population growth--->",
        "The change in the population growth 1990-2002", "populationGrowth.png")


# Calling pie chart

pie('Austria', 'Belgium', 'Denmark', 'France',
    'Ireland', 'Portugal', "Average_population.png")
