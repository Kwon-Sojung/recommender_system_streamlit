import streamlit as st


st.title("웹툰 추천")
title = st.text_input("👇 정확한 웹툰 제목을 입력하고 Enter를 눌러주세요. (카카오/네이버 웹툰만 입력 가능)")
st.empty()

st.write("""---""")
st.empty()

if not title:
    print(st.empty().info("입력 기다리는 중... "))
 
