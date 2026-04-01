import streamlit as st
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

st.title("🎈 Streamlit 요소들 예시 페이지")

st.header("1. 텍스트 요소들")
st.write("이것은 st.write()로 작성된 텍스트입니다.")
st.text("이것은 st.text()로 작성된 일반 텍스트입니다.")
st.markdown("**이것은 마크다운 텍스트입니다.** *기울임*, `코드` 등 지원합니다.")
st.latex(r"E = mc^2")  # 수식 예시

st.header("2. 입력 위젯들")
if st.button("버튼 클릭"):
    st.success("버튼이 클릭되었습니다!")

checkbox = st.checkbox("체크박스")
if checkbox:
    st.write("체크박스가 선택되었습니다.")

radio = st.radio("라디오 버튼 선택", ["옵션 1", "옵션 2", "옵션 3"])
st.write(f"선택된 라디오: {radio}")

select = st.selectbox("셀렉트박스", ["A", "B", "C"])
st.write(f"선택된 옵션: {select}")

multi = st.multiselect("멀티셀렉트", ["X", "Y", "Z"], default=["X"])
st.write(f"선택된 옵션들: {multi}")

slider = st.slider("슬라이더", 0, 100, 50)
st.write(f"슬라이더 값: {slider}")

text_input = st.text_input("텍스트 입력", "기본 텍스트")
st.write(f"입력된 텍스트: {text_input}")

text_area = st.text_area("텍스트 영역", "여러 줄 텍스트를 입력하세요.")
st.write(f"입력된 텍스트 영역: {text_area}")

number = st.number_input("숫자 입력", min_value=0, max_value=100, value=10)
st.write(f"입력된 숫자: {number}")

date = st.date_input("날짜 선택")
st.write(f"선택된 날짜: {date}")

st.header("3. 데이터 표시 요소들")
df = pd.DataFrame({
    '이름': ['Alice', 'Bob', 'Charlie'],
    '나이': [25, 30, 35],
    '점수': [85, 90, 95]
})
st.dataframe(df)

st.table(df)

st.json({"이름": "Alice", "나이": 25, "점수": 85})

col1, col2, col3 = st.columns(3)
col1.metric("온도", "70 °F", "1.2 °F")
col2.metric("바람", "9 mph", "-8%")
col3.metric("습도", "86%", "4%")

st.header("4. 차트 및 미디어")
fig, ax = plt.subplots()
ax.plot([1, 2, 3, 4], [10, 20, 25, 30])
st.pyplot(fig)

st.image("https://via.placeholder.com/300", caption="샘플 이미지")

st.header("5. 레이아웃 요소들")
with st.sidebar:
    st.header("사이드바")
    sidebar_option = st.selectbox("사이드바 옵션", ["홈", "설정", "도움말"])
    st.write(f"선택된 사이드바 옵션: {sidebar_option}")

with st.expander("펼쳐보기"):
    st.write("이것은 펼쳐보기 컨테이너 내부입니다.")

container = st.container()
container.write("컨테이너 내부 텍스트")

st.header("6. 기타 요소들")
progress = st.progress(0)
for i in range(100):
    progress.progress(i + 1)

with st.spinner("로딩 중..."):
    import time
    time.sleep(1)
st.success("완료되었습니다!")

if st.button("풍선 터뜨리기"):
    st.balloons()
