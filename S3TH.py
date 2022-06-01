import urllib
import re
from bs4 import BeautifulSoup
import streamlit as st

st.set_page_config(page_title="My Website", page_icon=":tada", layout="wide")
st.subheader("Sensor 3")

st.write("Sensor 3 in the basement crosscut has detected temperatures greater than the threshold of 22℃")

