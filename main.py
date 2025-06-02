import streamlit as st

# 💖 설정
st.set_page_config(page_title="MBTI 직업 추천기", page_icon="🧠", layout="centered")

# 🎉 헤더
st.markdown("# 💼 MBTI 기반 직업 추천기 🔮")
st.markdown("당신의 MBTI를 선택하면 어울리는 직업을 추천해드려요! 🌟")
st.markdown("___")

# 🔠 MBTI 리스트
mbti_types = [
    "ISTJ", "ISFJ", "INFJ", "INTJ",
    "ISTP", "ISFP", "INFP", "INTP",
    "ESTP", "ESFP", "ENFP", "ENTP",
    "ESTJ", "ESFJ", "ENFJ", "ENTJ"
]

# 🌈 이모지 포함 직업 추천 데이터
mbti_jobs = {
    "ISTJ": ["📊 회계사", "🏛️ 공무원", "📚 도서관 사서"],
    "ISFJ": ["🏥 간호사", "👩‍🏫 교사", "🧾 사회복지사"],
    "INFJ": ["🧠 심리상담가", "🎨 작가", "📖 교육 컨설턴트"],
    "INTJ": ["💻 데이터 사이언티스트", "🔬 연구원", "📈 전략 기획자"],
    "ISTP": ["🔧 정비사", "🚗 자동차 기술자", "🛠️ 엔지니어"],
    "ISFP": ["🎨 디자이너", "📸 사진작가", "🎶 음악가"],
    "INFP": ["✍️ 시인", "📚 소설가", "🧘‍♂️ 심리상담가"],
    "INTP": ["🧬 과학자", "💡 발명가", "🧑‍💻 프로그래머"],
    "ESTP": ["📢 마케터", "🎤 MC", "🚓 경찰"],
    "ESFP": ["🎭 배우", "🎧 DJ", "🎤 유튜버"],
    "ENFP": ["🧑‍🏫 교육가", "🎯 창업가", "🧑‍🎤 퍼포먼스 아티스트"],
    "ENTP": ["📈 전략 컨설턴트", "🚀 스타트업 대표", "🎙️ 팟캐스터"],
    "ESTJ": ["🏦 은행원", "📋 관리자", "👮‍♂️ 군인"],
    "ESFJ": ["🧑‍🍳 요리사", "🎓 교육자", "🏥 의료 서비스직"],
    "ENFJ": ["🌍 NGO 활동가", "👩‍🏫 교수", "🎙️ 커뮤니케이터"],
    "ENTJ": ["💼 CEO", "🧠 기획자", "📊 경영 컨설턴트"]
}

# 🧠 사용자 입력
selected_mbti = st.selectbox("당신의 MBTI를 선택하세요! 💖", mbti_types)

# 💼 직업 추천 결과
if selected_mbti:
    st.markdown(f"## ✨ {selected_mbti} 유형에게 어울리는 직업은?")
    for job in mbti_jobs[selected_mbti]:
        st.markdown(f"- {job}")
    
    st.success("자신에게 어울리는 직업을 찾아보는 건 멋진 일이에요! 🌟")

# 🧭 하단 푸터
st.markdown("___")
st.markdown("Made with ❤️ by [당신의 이름]")

