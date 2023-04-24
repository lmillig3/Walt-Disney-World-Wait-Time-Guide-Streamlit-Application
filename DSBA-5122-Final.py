import numpy as np
import altair as alt
import pandas as pd
import streamlit as st

st.header('Walt Disney World Wait Time Guide')



import streamlit as st


st.write ('Which Month Are you Visiting Magic Kingdom?')

jan = st.checkbox('January')
feb = st.checkbox('February')
mar = st.checkbox('March')
apr = st.checkbox('April')
may = st.checkbox('May')
jun = st.checkbox('June')
jul = st.checkbox('July')
aug = st.checkbox('August')
sep = st.checkbox('September')
oct = st.checkbox('October')
nov = st.checkbox('November')
dec = st.checkbox('December')

if jan:
     st.write("Wait Times Are Average In January, This Is Not A Bad Option")

if feb: 
     st.write("Wait Times Are High In February, Choose Another Month If Possible")

if mar:
     st.write("Wait Times Are High In March, Choose Another Month If Possible")

if apr: 
     st.write("Great Choice, Wait Times Are Typically Below Average in April")

if may:
     st.write("Great Choice, Wait Times Are Typically Below Average in May")

if jun:
     st.write("Wait Times Are Average In June, This Is Not A Bad Option")

if jul: 
     st.write("Wait Times Are High In July, Choose Another Month If Possible")

if aug:
     st.write("Wait Times Are Average In August, This Is Not A Bad Option")

if sep: 
     st.write("Great Choice, Wait Times Are Typically Below Average in September")

if oct:
     st.write("Great Choice, Wait Times Are Typically Below Average in October")

if nov:
     st.write("Wait Times Are Average In November, This Is Not A Bad Option")

if dec:
     st.write("Wait Times Are High In December, Choose Another Month If Possible")

st.image("month.png")


st.write ('What Time Of Day Are You Interested In Riding An Attraction?')

morn = st.checkbox('Morning')
lun = st.checkbox('Lunchtime')
aft = st.checkbox('Afternoon')
eve = st.checkbox('Evening')
nigh = st.checkbox('Night')

if morn:
     st.write("This Is The Best Time To Visit The Most Popular Attractions")

if lun: 
     st.write("All Wait Times Will Be Above Average, Consider Less Popular Attractions")

if aft:
     st.write("Wait Times Are Average In January, This Is Not A Bad Option")

if eve: 
     st.write("Wait Times Will Be Average, Consider Popular Attractions With Shorter Wait Times")

if nigh: 
     st.write("This Is The Best Time To Visit The Most Popular Attractions")

st.image("time.png")
              

st.write ('Which Magic Kingdom Attraction Would You Like To Ride')

wtp = st.checkbox('The Many Adventures of Winnie The Pooh')
sdwarfs = st.checkbox('Seven Dwarfs Mine Train')
sm = st.checkbox('Space Mountain')
tm = st.checkbox('Thunder Mountain')
thm = st.checkbox('The Haunted Mansion')
jc = st.checkbox('Jungle Cruise')
tmsw = st.checkbox('Tomorrowland Speedway')
poc = st.checkbox('Pirates of the Caribbean')
blsrs = st.checkbox('Buzz Lightyears Space Ranger Spin')
ppf = st.checkbox('Peter Pans Flight')

if wtp:
     st.write("Good News! This Ride Typically Has A Low Wait Time!")

if sdwarfs: 
     st.write("Unfortunately, This Ride Typically Has A High Wait Time")

if sm:
     st.write("Unfortunately, This Ride Typically Has A High Wait Time")

if tm: 
     st.write("This Ride Typically Has A Medium Wait Time")

if thm:
     st.write("This Ride Typically Has A Medium Wait Time")

if jc:
     st.write("Unfortunately, This Ride Typically Has A High Wait Time")

if tmsw: 
     st.write("Good News! This Ride Typically Has A Low Wait Time!")

if poc:
     st.write("Good News! This Ride Typically Has A Low Wait Time!")

if blsrs: 
     st.write("This Ride Typically Has A Medium Wait Time")

if ppf:
     st.write("Unfortunately, This Ride Typically Has A High Wait Time")

st.image("ride.png")