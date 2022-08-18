import streamlit as st
from st_aggrid import AgGrid, GridUpdateMode
from st_aggrid.grid_options_builder import GridOptionsBuilder

import seaborn as sns
import matplotlib.pyplot as plt
import koreanize_matplotlib
import pandas as pd
import numpy as np
import random
from math import dist

from sklearn.metrics.pairwise import cosine_similarity

from IPython.core.display import HTML

st.markdown("# 그림체 기반 추천 🌈")

# 데이터 프레임 불러오고 전처리 하기
df_origin = pd.read_csv("webtoon_total_final.csv")

raw_title_list = df_origin["title"].tolist()

df = df_origin[['title','score', 'genre']]
df.genre = df.genre.str.strip('['']')

#데이터 프레임 체크 박스 만들기
gd = GridOptionsBuilder.from_dataframe(df)
gd.configure_selection(selection_mode='multiple', use_checkbox=True)
gridoptions = gd.build()
    
grid_table = AgGrid(df, height=250, gridOptions=gridoptions,
                    update_mode=GridUpdateMode.SELECTION_CHANGED)


   
st.write('## Selected')

selected_row = grid_table["selected_rows"]

# 선택한 행의 제목들을 리스트 형태로 추출한다.
st.dataframe(selected_row)

df2 = pd.DataFrame(selected_row)

if len(df2) == 0:
    title_input=[]
else:
    title_input = df2.title.tolist()

# 그림체 기반 추천 알고리즘
df_euclidien_distance = pd.read_parquet('Euclidien_distance.parquet')
    
def single_distance(title):
    similar_df =df_euclidien_distance[[title]]
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

    return final_df


g = image_recommendation(title_input)

if len(g) == 0:
    st.write('웹툰 항목에서 최소 하나의 웹툰을 선택해주세요!')
    
elif len(g) != 0:
    df_result = g[['title', 'artist', 'genre','story','score','image']]
    def to_img_tag(path):
        return '<img src="'+ path + '" width="100" >'
    a= HTML(df_result.to_html(escape=False,formatters=dict(image=to_img_tag)))
    st.write(a)
