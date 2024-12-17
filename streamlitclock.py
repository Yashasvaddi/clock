import streamlit as st
import time as t

while(True):
    timestamp=t.strftime("%H:%M:%S:%p")
    st.write(timestamp)