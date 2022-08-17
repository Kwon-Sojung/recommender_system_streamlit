import streamlit as st
from PIL import Image
import pandas as pd
import numpy as np
from sklearn.metrics.pairwise import cosine_similarity
from genre_model import genre_model


st.set_page_config(
    page_title="Webtoon Recommender App Page Introduction",
    page_icon="📚",
    layout="wide",
)

title_name = []
st.markdown("# 웹툰 추천 📚")

webtoon_df = pd.read_csv("webtoon_total_final.csv")
title_list = webtoon_df["title"].tolist()

options = st.multiselect(
     '👇 선호하는 웹툰 제목을 입력하고 Enter를 눌러주세요. (복수 입력 가능하며, 카카오/네이버 웹툰만 입력 가능)',
     title_list
     )

# st.write('You selected:', options)

select_area = st.empty()
st.write("""---""")

if not options:
    print(st.empty().info("입력 기다리는 중…⏳"))
    image = Image.open('wating.jpg')
    st.image(image)
 
if options:
    genre_recommend_df = genre_model(options)
    st.write(genre_recommend_df)
    
   
