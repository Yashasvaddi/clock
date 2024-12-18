import streamlit as st
import time as t

# Create a placeholder
timestamp_placeholder = st.empty()

while True:
    # Get current time
    timestamp = t.strftime("%H:%M:%S:%p")
    
    # Update the placeholder with the new timestamp
    timestamp_placeholder.write(timestamp)
    if int(t.strftime("%H"))>=0 and int(t.strftime("%H"))<12 and t.strftime("%p")=="AM":
        st.write("Good Morning!!")
    if int(t.strftime("%H"))>=12 and int(t.strftime("%H"))<5 and t.strftime("%p")=="PM":
        st.write("Good Afternoon!!")
    if int(t.strftime("%H"))>=5 and int(t.strftime("%H"))<8 and t.strftime("%p")=="PM":
        st.write("Good Evening!!")
    if int(t.strftime("%H"))>=8 and int(t.strftime("%H"))<12 and t.strftime("%p")=="PM":
        st.write("Good Night!!")
    # Pause for 1 second before updating again
    t.sleep(1)
