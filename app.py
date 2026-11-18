
import streamlit as st

# 웹사이트 기본 설정
st.set_page_config(
    page_title="Student Performance Predictor",
    page_icon="🎓",
    layout="centered"
)

# 웹사이트 제목
st.title("🎓 학생 성적 예측 AI")

st.write(
    "머신러닝을 활용하여 학생의 최종 성적을 예측하는 서비스입니다."
)

st.divider()

# 사용자 입력
g1 = st.number_input(
    "1차 성적 (G1)",
    min_value=0,
    max_value=20,
    value=10
)

g2 = st.number_input(
    "2차 성적 (G2)",
    min_value=0,
    max_value=20,
    value=10
)

studytime = st.selectbox(
    "주간 공부 시간",
    options=[1, 2, 3, 4],
    format_func=lambda x: {
        1: "2시간 미만",
        2: "2~5시간",
        3: "5~10시간",
        4: "10시간 초과"
    }[x]
)

# 예측 버튼
if st.button("AI 성적 예측하기"):
    st.info(
        "웹사이트 기본 화면이 완성되었습니다! "
        "다음 단계에서 머신러닝 모델을 연결합니다."
    )
