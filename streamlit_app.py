import streamlit as st

st.title("👋 자기 소개")

st.header("안녕하세요!")
st.write("저는 경복비즈니스고등학교 교사 안이옥입니다.")

# 내 사진
import os
if os.path.exists("aio.JPG"):
    st.image("aio.JPG", caption="안이옥 선생님", width=200)

# 학교 찾아오는 길 이미지
if os.path.exists("kb.png"):
    st.image("kb.png", caption="경복비즈니스고등학교 찾아오는 길")

st.subheader("📖 소개")
st.write("""
저는 [간단한 소개 문장]. 

**요즘 관심사:**
- AI 대학원 졸업
- AI 대학원 수업
- AI 대학원 과제

**경험:**
- 스피드 스케이팅
- 테니스

더 자세한 정보가 필요하시면 연락주세요!
""")

st.subheader("📧 연락처")
st.write("이메일: 2ok25@edaum.net")

