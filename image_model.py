import matplotlib.pyplot as plt
import koreanize_matplotlib
import pandas as pd
import numpy as np
import random
from math import dist

df_euclidien_distance = pd.read_parquet('Euclidien_distance.parquet')

    
def single_distance(title):
    similar_df =df_euclidien_distance[[title]] #이게 뭐지?
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
