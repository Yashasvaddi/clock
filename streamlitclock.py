import streamlit as st
import time as t
from datetime import timedelta,datetime

# Create a placeholder
imagestamp_holder=st.empty()
timestamp_placeholder = st.empty()
datestamp_holder=st.empty()


while True:
    # Get current time
    current_timestamp = datetime.now()
    newtime=current_timestamp+timedelta(hours=5,minutes=30)
    formatted_time=newtime.strftime("%H:%M:%S:%p")
    hour=int(newtime.strftime("%H"))
    mins=int(newtime.strftime("%M"))
    timeofday=newtime.strftime("%p")
    # Update the placeholder with the new timestamp
    timestamp_placeholder.write(formatted_time)
    if hour>=0 and hour<12 and timeofday=="AM":
        datestamp_holder.write("Good Morning!!")
    if hour>=12 and hour<17 and timeofday=="PM":
        datestamp_holder.write("Good Afternoon!!")
    if hour>=17 and hour<20 and timeofday=="PM":
        datestamp_holder.write("Good Evening!!")
    if hour>=20 and hour<24 and timeofday=="PM":
        datestamp_holder.write("Good Night!!")
    # Pause for 1 second before updating again
    if(int(t.strftime("%S"))%2==0):
        imagestamp_holder.image("batman-logo-png.png")
    else:
        imagestamp_holder.image("pngwing.com.png")
    t.sleep(1)
