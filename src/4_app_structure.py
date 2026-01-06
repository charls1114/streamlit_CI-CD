import streamlit as st
from model_4 import MyModel

st.set_page_config(page_title="구조화된 AI 앱")

st.title("구조화된 AI 앱 예제(FastAPI 준비)")
st.info("UI 코드와 모델 로직을 분리하여 개발")


@st.cache_resource
def get_model_instance():
    return MyModel()


model = get_model_instance()

text = st.text_input("스팸 메일인지 테스트할 문장 입력")

with st.sidebar:
    st.subheader("스팸 필터 설정")
    spam_filter = st.text_input(
        "스팸으로 간주할 단어들을 콤마(,)로 구분하여 입력하세요:",
        "무료,광고",
    ).split(",")

if st.button("검사"):
    result = model.predict(text, spam_filter=spam_filter)

    st.json(result)

    st.info(f"감지된 이유: {result['reason']}")

    if result["is_spam"]:
        st.warning(f"스팸일 확률이 높습니다!")
    else:
        st.success(f"스팸이 아닐 확률이 높습니다!")
