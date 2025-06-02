import streamlit as st

st.set_page_config(page_title="MBTI 직업 추천기 🔍", page_icon="💼", layout="centered")

# 🎨 타이틀 및 설명
st.markdown("""
    <h1 style='text-align: center; color: #6C63FF;'>MBTI 기반 직업 추천 💡</h1>
    <h3 style='text-align: center;'>당신의 성격에 어울리는 직업을 찾아보세요! 🔍</h3>
    <p style='text-align: center;'>MBTI를 선택하면 추천 직업과 설명, 소개 영상을 알려드립니다 💼✨</p>
""", unsafe_allow_html=True)

# 🔮 MBTI 리스트
mbti_types = [
    "ISTJ 🧠", "ISFJ 💖", "INFJ 🌌", "INTJ 🧙‍♂️",
    "ISTP 🛠️", "ISFP 🎨", "INFP 📖", "INTP 🔬",
    "ESTP 🎯", "ESFP 🎭", "ENFP 🌈", "ENTP 🧠⚡",
    "ESTJ 📋", "ESFJ 👩‍🏫", "ENFJ 🎤", "ENTJ 🧑‍💼"
]

# 🧠 직업 추천 + 설명 + 유튜브 링크 매핑
job_recommendations = {
    "ISTJ": [
        ("회계사 📊", "정확하고 신중한 성향을 살려 재무 데이터를 분석하고 관리합니다.", "https://www.youtube.com/watch?v=6l6N6bKFY64"),
        ("데이터 분석가 📈", "숫자와 패턴을 분석해 비즈니스 인사이트를 도출합니다.", "https://www.youtube.com/watch?v=8blh2rmM91w"),
        ("행정관 👮", "정책과 절차를 철저히 지키며 조직의 운영을 돕습니다.", "")
    ],
    "INFP": [
        ("시인 📝", "섬세한 감정과 언어 감각으로 감동을 전합니다.", ""),
        ("소설가 📖", "상상력과 깊은 내면을 글로 풀어냅니다.", ""),
        ("예술가 🎭", "창의적 표현으로 자신의 세계를 펼칩니다.", "https://www.youtube.com/watch?v=Y0g30UWBn5U")
    ],
    "ENTJ": [
        ("CEO 👔", "목표를 명확히 하고 조직을 이끄는 리더입니다.", "https://www.youtube.com/watch?v=_X5b4o2zK14"),
        ("정치가 🗳️", "사회 변화와 리더십을 통해 영향력을 행사합니다.", ""),
        ("전략가 🧠", "전략적 사고로 큰 그림을 설계합니다.", "")
    ],
    # 추가 MBTI 유형도 필요 시 넣어드릴 수 있습니다.
}

# 📥 사용자 선택
selected_mbti = st.selectbox("당신의 MBTI를 선택해주세요 😊", mbti_types)

# 🔍 실제 MBTI 코드 추출
pure_mbti = selected_mbti.split()[0]

# 💼 결과 출력
if pure_mbti:
    st.markdown("---")
    st.markdown(f"## 🧬 당신의 MBTI 유형: **{pure_mbti}**")
    st.success("🔍 추천 직업과 설명:")

    if pure_mbti in job_recommendations:
        for job, desc, youtube_link in job_recommendations[pure_mbti]:
            st.markdown(f"### 👉 {job}")
            st.markdown(f"<span style='color:gray'>{desc}</span>", unsafe_allow_html=True)
            if youtube_link:
                st.video(youtube_link)
    else:
        st.warning("❗ 아직 이 MBTI 유형에 대한 직업 정보가 준비되지 않았습니다.")

    st.markdown("---")
    st.info("🎯 MBTI는 참고용이며, 다양한 경험을 통해 자신에게 맞는 길을 찾아보세요!")
