import streamlit as st

st.title("Hello, Streamlit!")
st.write("Welcome to your first Streamlit app.")
name = st.text_input("Enter your name:")
if name:
    st.write(f"Hello, {name}!")

st.title("Streamlit 텍스트 컴포넌트")
st.header("헤더 예시")
st.write("st.write로 출력된 일반 텍스트입니다.")
st.markdown("이것은 **마크다운** 텍스트입니다.")
st.text(
    "이것은 st.text로 출력된 고정폭 텍스트입니다."
)  # Added st.text for st.code reference
st.code("print('Hello Streamlit')", language="python")  # Using st.code to display code
st.subheader("서브헤더 예시")
