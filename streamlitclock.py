import streamlit as st
import time as t

# Create a placeholder
timestamp_placeholder = st.empty()

while True:
    # Get current time
    timestamp = t.strftime("%H:%M:%S:%p")
    
    # Update the placeholder with the new timestamp
    timestamp_placeholder.write(timestamp)
    
    # Pause for 1 second before updating again
    t.sleep(1)
