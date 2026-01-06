import streamlit as st
from transformers import pipeline

st.title("AI 감성 분석기(모델 캐싱 실습)")


@st.cache_resource
def load_model():
    return pipeline(
        "sentiment-analysis", model="tabularisai/multilingual-sentiment-analysis"
    )


with st.spinner("모델 로딩 중... 잠시만 기다려주세요."):
    classifier = load_model()

st.write("문장을 입력하면 감성 분석을 수행합니다.")

user_input = st.text_area(
    "분석할 문장을 입력하세요:", "나는 AI 엔지니어링 과정이 재밌습니다."
)


if st.button("분석하기"):
    if user_input:
        result = classifier(user_input)[0]
        st.write(result)
        label = result["label"]
        score = result["score"]

        col1, col2 = st.columns(2)
        with col1:
            st.metric("감정 결과", label)
        with col2:
            st.progress(
                score,
                text="신뢰도",
            )

        if score > 0.5:
            if label == "Very Positive" or label == "Positive":
                st.success("긍정적인 문장입니다! 😊")
            elif label == "Neutral":
                st.success("중립적인 문장입니다. 😐")
            elif label == "Negative" or label == "Very Negative":
                st.error("부정적인 문장입니다. 😞")
        else:
            st.info("🤔 AI가 확신하지 못하는 문장입니다.")
    else:
        st.warning("분석할 문장을 입력해주세요.")
