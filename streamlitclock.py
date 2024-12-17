import streamlit as st
import time as t

timestamp=t.strftime("%H:%M:%S:%p")
while(True):
    st.write(timestamp)