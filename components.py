import streamlit as st

from io import BytesIO
from urllib import request
from PIL import 

def webtoon_info_component(webtoon_info):
    st.subheader(f"{webtoon_info['title']")
    st.caption(
        f"장르: {webtoon_info['genre'] if webtoon_info['genre'] else '정보가 없습니다.'}"
    )
    st.write(
        f"**작가**: {webtoon_info['artist'] if webtoon_info['artist'] else '정보가 없습니다.'}"
    )
    st.write(f"**평점**: {webtoon_info['score'] if webtoon_info['score'] else '정보가 없습니다.'}")
    st.write(f"**줄거리**:")
    st.info(webtoon_info["story"])

def image_component(link):
    image = Image.open(BytesIO(request.urlopen(link).read()), mode="r")
    st.image(image)
