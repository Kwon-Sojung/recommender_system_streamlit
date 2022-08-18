import streamlit as st
from PIL import Image
import pandas as pd
import numpy as np
from sklearn.metrics.pairwise import cosine_similarity
from image_model import image_recommendation
from IPython.core.display import HTML



st.set_page_config(
    page_title="Webtoon Recommender App Page Introduction",
    page_icon="📚",
    layout="wide",
)

title_name = []
st.markdown("# 그림체 기반 웹툰 추천 📚")

st.balloons()

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
    image = Image.open('jamanchu_family.jpg')
    st.image(image)
 
    
   
def to_img_tag(path):
    return '<img src="'+ path + '" width="200" >'


if options:
    image_recommend_df = image_recommendation(options)
    image_recommend_df = image_recommend_df[["title", "image", "genre", "artist", "story", "score"]]
    image_recommend_df.rename(columns={"title":"제목", "image":"웹툰", "genre":"장르", "artist":"작가", "story":"줄거리", "score":"평점"},
                                       inplace=True)

    table = HTML(image_recommend_df.to_html(escape=False,index=False,
                                         float_format='{0:.4g}'.format,formatters=dict(웹툰=to_img_tag)))

    st.write(table)



    




    
    
