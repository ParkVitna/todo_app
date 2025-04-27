import streamlit as st
from typing import List

st.title('🚗 Easy Compare My CAR 🚜')

row1 = st.columns(4)
row2 = st.columns(4)
row3 = st.columns(4)
row4 = st.columns(4)
row5 = st.columns(4)
row6 = st.columns(4)
row7 = st.columns(4)
row8 = st.columns(4)

row1[0].container(height=20)
row2[0].container(height=20)
row3[0].container(height=20)
row4[0].container(height=20)
row5[0].container(height=20)
row6[0].container(height=20)
row7[0].container(height=20)
row8[0].container(height=20)

row1[0].title = '종류'
row2[0].title = '차량이름'
row3[0].title = '차종'
row4[0].title = '출시일'
row5[0].title = '연료'
row6[0].title = '연비'
row7[0].title = '주행거리'
row8[0].title = '안전성'


