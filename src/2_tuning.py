import streamlit as st
import pandas as pd
import time
import random

st.title("🧪 하이퍼파라미터 튜닝 시뮬레이터")

if "history" not in st.session_state:
    st.session_state.history = []

with st.form("training_form"):
    st.subheader("모델 하이퍼파라미터 설정")

    col1, col2 = st.columns(2)
    with col1:
        learning_rate = st.slider("학습률 (Learning Rate)", 0.0001, 0.1, 0.01)
    with col2:
        epochs = st.slider("에포크 수 (Epochs)", 1, 100, 10)
    batch_size = st.selectbox("배치 크기 (Batch Size)", [16, 32, 64, 128], index=1)
    submitted = st.form_submit_button("모델 훈련 시작")

if submitted:
    st.write(
        f"학습 시작 - 학습률: {learning_rate}, 에포크 수: {epochs}, 배치 크기: {batch_size}"
    )
    progress_bar = st.progress(0)
    status_text = st.empty()

    for i in range(100):
        time.sleep(0.01)
        progress_bar.progress(i + 1)
        status_text.text(f"훈련 진행 중... {i + 1}% 완료")
    accuracy = random.uniform(0.7, 0.99)
    loss = random.uniform(0.1, 0.5)

    st.session_state.history.append(
        {
            "learning_rate": learning_rate,
            "epochs": epochs,
            "batch_size": batch_size,
            "accuracy": accuracy,
            "loss": loss,
        }
    )
    st.success(f"훈련 완료! 최종 정확도: {accuracy:.2f}, 최종 손실: {loss:.2f}")


with st.sidebar:
    clear_session = st.button("세션 기록 초기화")
    if clear_session:
        st.session_state.history.clear()
        st.rerun()

if len(st.session_state.history) > 0:
    st.markdown("---")
    st.subheader("📊모델 훈련 기록")
    df = pd.DataFrame(st.session_state.history)
    st.dataframe(df)

    st.line_chart(df["accuracy"])

    st.write(f"🏆 현재 최고 기록:{max(df['accuracy']):.4f}")
