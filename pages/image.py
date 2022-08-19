import streamlit as st
from PIL import Image
import pandas as pd
import numpy as np
import random
from math import dist
import seaborn as sns
import matplotlib.pyplot as plt
from sklearn.metrics.pairwise import cosine_similarity
# from image_model import single_distance, image_recommendation
from IPython.core.display import HTML



st.set_page_config(
    page_title="Webtoon Recommender App Page Introduction",
    page_icon="📚",
    layout="wide",
)

title_name = []
st.markdown("# 비슷한 그림체의 웹툰을 추천해드려요 📚")

st.balloons()

df_origin = pd.read_csv("webtoon_total_final.csv")
title_list = df_origin["title"].tolist()

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
 
###
df_euclidien_distance = pd.read_parquet('Euclidien_distance_v2.parquet')
# df_euclidien_distance.genre = df_euclidien_distance.genre.str.strip('['']').str.replace("'","")
    
def single_distance(title):
    similar_df =df_euclidien_distance[[title]] #what is this
    similar_df.columns = ['title']
    return similar_df

# 스타일 loss 값 저장한 csv에서 불러오는 부분
title_list = df_euclidien_distance.index.tolist()


def image_recommendation(title_input):
    if not title_input:
        st.write("아직 선택한 웹툰이 없습니다")
        return pd.DataFrame()
    
    # result 데이터 프레임 만들기
    empty_list = [0 for i in range(len(df_euclidien_distance))]
    result = pd.DataFrame()
    result['result'] = empty_list
    result.index = title_list
    
    for title in title_input:
        tmp = single_distance(title)
        result['result'] = result.values + tmp.values
        
    result.sort_values('result',inplace=True)
    result.drop(title_input, inplace=True)
    
    result_title_list = result[:10].index.tolist()
    
    final_df = pd.DataFrame(columns=['title', 'artist', 
                                     'genre', 'story',
                                     'image', 'from', 'score'])
    
    for r in result_title_list:
        tmp = df_origin[df_origin['title']== r]
        final_df = pd.concat([final_df,tmp])
    
    final_df['genre'] = final_df['genre'].str.strip('['']').str.replace("'","")
    return final_df


###   
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



    




    
    
