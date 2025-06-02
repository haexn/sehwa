import streamlit as st

# 🌟 페이지 기본 설정
st.set_page_config(page_title="MBTI 직업 추천기 🔍", page_icon="💼", layout="centered")

# 🎨 타이틀 및 설명
st.markdown("""
    <h1 style='text-align: center; color: #6C63FF;'>MBTI 기반 직업 추천 💡</h1>
    <h3 style='text-align: center;'>당신의 성격에 어울리는 직업을 찾아보세요! 🔍</h3>
    <p style='text-align: center;'>MBTI를 선택하면 추천 직업을 알려드립니다 💼✨</p>
""", unsafe_allow_html=True)

# 🔮 MBTI 리스트
mbti_types = [
    "ISTJ 🧠", "ISFJ 💖", "INFJ 🌌", "INTJ 🧙‍♂️",
    "ISTP 🛠️", "ISFP 🎨", "INFP 📖", "INTP 🔬",
    "ESTP 🎯", "ESFP 🎭", "ENFP 🌈", "ENTP 🧠⚡",
    "ESTJ 📋", "ESFJ 👩‍🏫", "ENFJ 🎤", "ENTJ 🧑‍💼"
]

# 🧠 직업 추천 매핑
job_recommendations = {
    "ISTJ": ["회계사 📊", "데이터 분석가 📈", "행정관 👮"],
    "ISFJ": ["간호사 🏥", "초등교사 📚", "사회복지사 ❤️"],
    "INFJ": ["상담가 🧘", "작가 ✍️", "심리학자 🧠"],
    "INTJ": ["전략기획자 🎯", "연구원 🔬", "시스템 설계자 🧮"],
    "ISTP": ["엔지니어 🔧", "파일럿 ✈️", "경찰관 👮‍♂️"],
    "ISFP": ["디자이너 🎨", "사진작가 📸", "플로리스트 🌸"],
    "INFP": ["시인 📝", "소설가 📖", "예술가 🎭"],
    "INTP": ["교수 📚", "프로그래머 👨‍💻", "이론 물리학자 🧪"],
    "ESTP": ["영업사원 💼", "기업가 🚀", "스턴트맨 🎬"],
    "ESFP": ["연예인 🌟", "MC 🎤", "홍보 담당자 📢"],
    "ENFP": ["광고기획자 📺", "작가 ✍️", "공익활동가 🌍"],
    "ENTP": ["창업가 💡", "기획자 🧠", "컨설턴트 🧳"],
    "ESTJ": ["프로젝트 매니저 📋", "경영자 🏢", "감독관 🎓"],
    "ESFJ": ["교사 👩‍🏫", "상담사 🧘‍♀️", "간호 관리자 💊"],
    "ENFJ": ["강사 🎤", "리더십 코치 🧑‍🏫", "홍보전문가 📢"],
    "ENTJ": ["CEO 👔", "정치가 🗳️", "전략가 🧠"]
}

# 📥 사용자 선택
selected_mbti = st.selectbox("당신의 MBTI를 선택해주세요 😊", mbti_types)

# 🔍 실제 MBTI 코드 추출 (이모지 제거)
pure_mbti = selected_mbti.split()[0]

# 💼 결과 출력
if pure_mbti:
    st.markdown("---")
    st.markdown(f"## 🧬 당신의 MBTI 유형: **{pure_mbti}**")
    st.success("🔍 추천 직업 리스트:")
    for job in job_recommendations[pure_mbti]:
        st.write(f"👉 {job}")

    st.markdown("---")
    st.info("🎯 MBTI는 참고용이며, 다양한 직업 경험을 통해 자신에게 맞는 길을 찾아가보세요!")

