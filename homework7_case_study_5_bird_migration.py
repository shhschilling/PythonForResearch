#------------------------------------------------
# Homework 7 of course "Python for Research"
# HarvardX -  PH526xEdX, EdX
# Bird migration
#------------------------------------------------

import pandas as pd
birddata=pd.read_csv("bird_tracking.csv")
import matplotlib.pyplot as plt
import numpy as np
bird_names=pd.unique(birddata.bird_name)

#Exercise 1--------------------
#Group data frame by bird name
grouped_birds=birddata.groupby(by='bird_name')
grouped_birds[ix].head()
#Mean speed of each bird
grouped_birds.speed_2d.mean()
mean_altitude=grouped_birds.altitude.mean()
bird_names=pd.unique(birddata.bird_name)
bird_names[0]
grouped_birds
ix=grouped_birds.bird_name=='Eric'
ix

for name in bird_names:
    ix=birddata.bird_name==name
    birddata[ix].head()
#much shorter:
grouped_birds.head()
#Excercise 2--------------------
# Convert birddata.date_time to the `pd.datetime` format.
birddata.date_time = pd.to_datetime(birddata.date_time)
#Extract only date
onlydate=birddata.date_time.dt.date
birddata["date"]=onlydate

#Use `groupby()` to group the data by date.
grouped_bydates = birddata.groupby(by="date")

type(grouped_bydates)
# Find the mean `altitude` for each date.
mean_altitudes_perday=grouped_bydates.altitude.mean()

#Excercise 3--------------------
#group by two columns, first bird name, then date
# Example: df.groupby(['name', 'title'])

grouped_birdday = birddata.groupby(by=['bird_name','date'])

mean_altitudes_perday=grouped_birdday.altitude.mean()


#Excercise 4--------------------
#Panda series object are accessed as normal arrays
mean_speed_perday=grouped_birdday.speed_2d.mean()

eric_daily_speed  = mean_speed_perday['Eric']
sanne_daily_speed = mean_speed_perday['Sanne']
nico_daily_speed  = mean_speed_perday['Nico']


eric_daily_speed.plot(label="Eric")
sanne_daily_speed.plot(label="Sanne")
nico_daily_speed.plot(label="Nico")
plt.legend(loc="upper left")
plt.show()
