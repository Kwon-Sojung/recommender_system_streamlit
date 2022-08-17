import streamlit as st


st.title("웹툰 추천")
title = st.text_input("정확한 웹툰 제목을 입력하고 Enter를 눌러주세요. (카카오/네이버 웹툰만 입력 가능)")
select_area = st.empty()

st.write("""---""")

placeholder = st.empty()
webtoon_area = st.empty()

st.write("""---""")
rating_area = st.empty()
tab_area = st.empty()

if not title:
    print(placeholder.success("입력을 기다리고 있어요... "))

# Add a placeholder 진행 상황 바
latest_iteration = st.empty()
bar = st.progress(0)
for i in range(100):
    # Update the progress bar with each iteration.
    latest_iteration.text(f'Loading {i+1}')
    bar.progress(i + 1)
    time.sleep(0.01)
 
