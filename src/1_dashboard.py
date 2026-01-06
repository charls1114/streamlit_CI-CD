import streamlit as st
import pandas as pd
import numpy as np


st.set_page_config(layout="wide", page_title="나만의 포트폴리오")

st.title("📈매출 데이터 분석 리포트")
st.markdown("---")

with st.sidebar:
    st.header("설정")
    uploaded_file = st.file_uploader("CSV 파일 업로드", type=["csv"])

    chart_type = st.selectbox(
        "차트 유형 선택", ["Line Chart", "Bar Chart", "Area Chart"]
    )

    head_num = st.slider("표시할 데이터 수", min_value=5, max_value=50, value=10)
    show_pos = st.checkbox("양수 값만 보기", value=False)

if uploaded_file is not None:
    df = pd.read_csv(uploaded_file)
    st.success("파일이 성공적으로 업로드되었습니다!")
else:
    st.info(
        "왼쪽 사이드바에서 CSV 파일을 업로드해주세요. 현재 보이는 데이터셋은 샘플 데이터입니다."
    )
    df = pd.DataFrame(np.random.randn(20, 3), columns=["A", "B", "C"])

if show_pos:
    df = df[df["A"] > 0]

# 레이아웃 - 컬럼으로 화면 분할
col1, col2 = st.columns(2)

with col1:
    st.subheader("📊데이터 미리보기")
    st.dataframe(df.head(head_num))

with col2:
    st.subheader("📉차트 시각화")
    if chart_type == "Line Chart":
        st.line_chart(df)
    elif chart_type == "Bar Chart":
        st.bar_chart(df)
    elif chart_type == "Area Chart":
        st.area_chart(df)


with st.expander("🔧데이터 통계 보기"):
    st.subheader("🔍기술 통계")
    st.write(df.describe())
