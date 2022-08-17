import streamlit as st
from PIL import Image

st.set_page_config(
    page_title="Webtoon Recommender App Page Introduction",
    page_icon="📚",
    layout="wide",
)

title_name = []
st.markdown("# 소개글 📚")
# title = st.text_input("👇 정확한 웹툰 제목을 입력하고 Enter를 눌러주세요. (카카오/네이버 웹툰만 입력 가능)")
# st.empty()
# st.write("""—--""")
# st.empty()
# title_name.append(title)

# if not title:
#     print(st.empty().info("입력 기다리는 중…⏳"))
#     image = Image.open('wating.jpg')
#     st.image(image)

# else:
#    print(st.write(title_name))

options = st.multiselect(
     'What are your favorite colors',
     ['Green', 'Yellow', 'Red', 'Blue', '바니와 오빠들']
     )

st.write('You selected:', options)
