
import streamlit as st
import pandas as pd
import joblib

# 웹사이트 설정
st.set_page_config(
    page_title="Student Performance Predictor",
    page_icon="🎓",
    layout="centered"
)

# 모델 불러오기
@st.cache_resource
def load_model():
    model = joblib.load("student_model.pkl")
    preprocessor = joblib.load("preprocessor.pkl")
    feature_columns = joblib.load("feature_columns.pkl")
    default_values = joblib.load("default_values.pkl")

    return model, preprocessor, feature_columns, default_values

model, preprocessor, feature_columns, default_values = load_model()

# 제목
st.title("🎓 학생 성적 예측 AI")

st.write(
    "학생의 학습 정보와 이전 성적을 입력하면 "
    "머신러닝 모델이 최종 성적을 예측합니다."
)

st.divider()

st.subheader("📚 학생 정보 입력")

# 사용자 입력
g1 = st.slider(
    "1차 성적 (G1)",
    min_value=0,
    max_value=20,
    value=10
)

g2 = st.slider(
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

absences = st.number_input(
    "결석 횟수",
    min_value=0,
    max_value=93,
    value=0
)

failures = st.selectbox(
    "과거 낙제 횟수",
    options=[0, 1, 2, 3]
)

st.divider()

# 예측 버튼
if st.button("🔮 AI 성적 예측하기", use_container_width=True):

    # 기본값을 이용해 전체 입력 변수 구성
    input_data = default_values.copy()

    # 사용자가 입력한 값으로 변경
    input_data["G1"] = g1
    input_data["G2"] = g2
    input_data["studytime"] = studytime
    input_data["absences"] = absences
    input_data["failures"] = failures

    # 학습 당시와 동일한 변수 순서로 정렬
    input_df = pd.DataFrame(
        [input_data],
        columns=feature_columns
    )

    # 데이터 전처리
    processed_data = preprocessor.transform(input_df)

    # 머신러닝 예측
    prediction = model.predict(processed_data)[0]

    # 점수 범위 제한
    prediction = max(0, min(20, prediction))

    # 결과 표시
    st.success("예측이 완료되었습니다!")

    st.metric(
        label="AI 예상 최종 성적",
        value=f"{prediction:.2f} / 20점"
    )

    st.progress(prediction / 20)

    st.caption(
        "본 결과는 머신러닝 모델의 예측값이며 "
        "실제 성적과 차이가 있을 수 있습니다."
    )

st.divider()

st.info(
    "본 서비스는 UCI Student Performance 데이터셋을 "
    "활용하여 직접 학습한 Random Forest 모델을 사용합니다."
)
