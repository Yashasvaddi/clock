import streamlit as st
import time as t

# Create a placeholder
timestamp_placeholder = st.empty()
datestamp_holder=st.empty()
st.image("clock/batman-logo-png.png")

while True:
    # Get current time
    timestamp = t.strftime("%H:%M:%S:%p")
    # Update the placeholder with the new timestamp
    timestamp_placeholder.write(timestamp)
    if int(t.strftime("%H"))>=0 and int(t.strftime("%H"))<12 and t.strftime("%p")=="AM":
        datestamp_holder.write("Good Morning!!")
    if int(t.strftime("%H"))>=12 and int(t.strftime("%H"))<17 and t.strftime("%p")=="PM":
        datestamp_holder.write("Good Afternoon!!")
    if int(t.strftime("%H"))>=17 and int(t.strftime("%H"))<20 and t.strftime("%p")=="PM":
        datestamp_holder.write("Good Evening!!")
    if int(t.strftime("%H"))>=20 and int(t.strftime("%H"))<24 and t.strftime("%p")=="PM":
        datestamp_holder.write("Good Night!!")
    # Pause for 1 second before updating again
    t.sleep(1)
