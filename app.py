import streamlit as st


GUIDES = {
    "음료 페트병": {
        "icon": "🧴",
        "material": "플라스틱 · 페트",
        "parts": ("비닐 라벨", "플라스틱 뚜껑", "페트병 본체"),
        "steps": (
            ("라벨과 뚜껑 분리하기", "라벨을 떼고 뚜껑과 고리를 분리해 주세요.", "라벨 · 뚜껑"),
            ("내용물을 비우고 압착하기", "병 안을 비운 뒤, 부피가 줄도록 납작하게 눌러 주세요.", "비우기 · 압착"),
            ("페트병 전용함에 배출하기", "투명 페트병은 라벨을 제거한 뒤 전용 수거함에 넣어 주세요.", "투명 페트"),
        ),
    },
    "배달 용기": {
        "icon": "🥡",
        "material": "플라스틱",
        "parts": ("밀봉 비닐", "플라스틱 뚜껑", "용기 본체"),
        "steps": (
            ("밀봉 비닐과 뚜껑 분리하기", "다른 재질의 부속물을 용기에서 떼어내 주세요.", "비닐 · 뚜껑"),
            ("남은 음식물을 비우고 세척하기", "기름기와 음식물이 남지 않도록 깨끗이 헹궈 주세요.", "비우기 · 세척"),
            ("플라스틱으로 배출하기", "물기를 털고 플라스틱 수거함에 넣어 주세요.", "플라스틱"),
        ),
    },
    "택배 상자": {
        "icon": "📦",
        "material": "종이",
        "parts": ("비닐 테이프", "운송장 스티커", "종이 상자"),
        "steps": (
            ("테이프와 운송장 떼어내기", "비닐 테이프와 개인정보가 적힌 운송장을 제거해 주세요.", "테이프 · 운송장"),
            ("상자를 펼쳐 접기", "상자 안의 내용물을 비우고 부피가 줄도록 펼쳐 주세요.", "펼치기 · 접기"),
            ("종이류로 배출하기", "젖지 않게 보관한 상자를 종이 수거함에 넣어 주세요.", "종이"),
        ),
    },
    "음료·통조림 캔": {
        "icon": "🥫",
        "material": "캔 · 고철",
        "parts": ("종이·비닐 라벨", "금속 뚜껑", "캔 본체"),
        "steps": (
            ("라벨과 뚜껑 분리하기", "떼어낼 수 있는 라벨과 뚜껑을 분리해 주세요.", "라벨 · 뚜껑"),
            ("내용물을 비우고 헹구기", "내용물을 비운 뒤 캔 안쪽을 가볍게 헹궈 주세요.", "비우기 · 세척"),
            ("캔·고철로 배출하기", "캔류 수거함에 넣고, 위험한 날카로운 부분은 주의해 주세요.", "캔 · 고철"),
        ),
    },
    "우유·종이팩": {
        "icon": "🥛",
        "material": "종이팩",
        "parts": ("플라스틱 캡", "빨대와 포장 비닐", "종이팩 본체"),
        "steps": (
            ("캡과 빨대 분리하기", "플라스틱 캡과 빨대, 포장 비닐을 떼어 주세요.", "캡 · 빨대"),
            ("팩을 펼쳐 헹구기", "팩을 펼쳐 안을 헹군 뒤 물기를 말려 주세요.", "펼치기 · 세척"),
            ("종이팩 전용함에 배출하기", "일반 종이와 분리해 종이팩 전용 수거함에 넣어 주세요.", "종이팩"),
        ),
    },
    "유리병": {
        "icon": "🍾",
        "material": "유리",
        "parts": ("금속·플라스틱 뚜껑", "종이 라벨", "유리병 본체"),
        "steps": (
            ("뚜껑과 라벨 분리하기", "분리 가능한 뚜껑과 라벨을 떼어 주세요.", "뚜껑 · 라벨"),
            ("내용물을 비우기", "병 안을 비우고, 깨지지 않도록 조심히 다뤄 주세요.", "비우기"),
            ("유리병으로 배출하기", "색상별 배출 기준에 맞춰 유리병 수거함에 넣어 주세요.", "유리"),
        ),
    },
}


st.set_page_config(
    page_title="Re:Step | 분리배출 가이드",
    page_icon="♻️",
    layout="wide",
    initial_sidebar_state="expanded",
)

st.markdown(
    """
    <style>
    @import url('https://fonts.googleapis.com/css2?family=DM+Sans:wght@400;500;600;700&family=Noto+Sans+KR:wght@400;500;600;700;800&display=swap');

    :root {
        --ink: #19332c;
        --muted: #71817a;
        --green: #27664e;
        --lime: #d8f278;
        --line: #e7ece6;
        --paper: #f7f8f3;
    }
    html, body, [class*="css"] {
        font-family: 'DM Sans', 'Noto Sans KR', sans-serif;
        color: var(--ink);
    }
    .stApp { background: var(--paper); }
    [data-testid="stSidebar"] {
        background: #f0f3eb;
        border-right: 1px solid #e5eae1;
    }
    [data-testid="stSidebar"] > div { padding-top: 1.4rem; }
    .block-container { max-width: 1320px; padding: 2rem 3.2rem 3rem; }
    .brand { display: flex; align-items: center; gap: 10px; margin: 0 0 2rem 0.35rem; }
    .brand-mark {
        width: 38px; height: 38px; border-radius: 13px; background: var(--green);
        display: flex; align-items: center; justify-content: center; color: white; font-size: 20px;
    }
    .brand-name { font-size: 20px; font-weight: 800; letter-spacing: -0.8px; color: var(--ink); }
    .brand-name span { color: #8eaa43; }
    .side-caption {
        color: #9aa69d; font-size: 10px; font-weight: 700; letter-spacing: 1.4px;
        margin: 1.2rem 0 0.45rem 0.5rem;
    }
    .side-nav {
        padding: 0.65rem 0.75rem; margin: 0.25rem 0; border-radius: 10px;
        color: #65756d; font-size: 13px; font-weight: 600;
    }
    .side-nav.active { background: #e2eadb; color: var(--green); }
    .side-note {
        margin-top: 2.2rem; border-radius: 16px; padding: 1rem;
        background: #e4ebde; color: #58705f; font-size: 12px; line-height: 1.6;
    }
    .eyebrow {
        text-transform: uppercase; letter-spacing: 1.6px; color: #82965a;
        font-size: 11px; font-weight: 700; margin: 0 0 0.6rem;
    }
    .hero-title { color: var(--ink); font-weight: 800; font-size: clamp(32px, 3vw, 44px); line-height: 1.25; letter-spacing: -2px; margin: 0; }
    .hero-title em { color: var(--green); font-style: normal; }
    .hero-copy { color: var(--muted); font-size: 14px; line-height: 1.8; margin-top: 0.7rem; }
    .top-chip {
        background: #edf2e5; color: #557047; border-radius: 30px; display: inline-block;
        padding: 8px 13px; font-size: 11px; font-weight: 700; margin-top: 0.3rem;
    }
    .upload-card, .guide-card, .impact-card {
        border: 1px solid var(--line); border-radius: 20px; background: white;
        padding: 1.3rem 1.4rem; box-shadow: 0 8px 26px rgba(34, 62, 44, 0.035);
    }
    [data-testid="stVerticalBlockBorderWrapper"] {
        border-color: var(--line); border-radius: 20px; background: white;
        box-shadow: 0 8px 26px rgba(34, 62, 44, 0.035);
    }
    .card-heading { font-size: 16px; font-weight: 700; margin: 0; color: var(--ink); }
    .card-sub { color: #87938c; font-size: 12px; margin-top: 5px; }
    [data-testid="stFileUploader"] section {
        background: #fbfcf9; border: 1px dashed #cbd7c8; border-radius: 14px;
    }
    [data-testid="stFileUploader"] section > div { padding: 0.7rem; }
    [data-testid="stFileUploader"] button {
        background: #edf3e9; border: 0; color: var(--green); font-weight: 700; border-radius: 8px;
    }
    .stButton > button {
        border: 0; border-radius: 11px; background: var(--green); color: white;
        min-height: 46px; font-weight: 700; transition: all 0.15s ease;
    }
    .stButton > button:hover { background: #1f543f; color: white; border: 0; }
    .stSelectbox label, .stFileUploader label { color: #52645a; font-size: 12px; font-weight: 700; }
    .stat-label { color: #809087; font-size: 11px; font-weight: 600; }
    .stat-value { color: var(--ink); font-size: 23px; font-weight: 800; letter-spacing: -0.7px; }
    .stat-unit { color: #849188; font-size: 11px; }
    .impact-card {
        background: #244f40; color: white; overflow: hidden; position: relative;
        padding: 1.45rem 1.5rem; min-height: 178px;
    }
    .impact-kicker { color: #c6d8b3; font-size: 11px; font-weight: 700; letter-spacing: 1px; }
    .impact-title { color: white; font-size: 20px; line-height: 1.45; font-weight: 700; margin-top: 10px; }
    .impact-title span { color: var(--lime); }
    .impact-orbit { float: right; font-size: 54px; margin: 8px 0 0 10px; opacity: 0.9; }
    .section-title { font-size: 19px; font-weight: 800; letter-spacing: -0.6px; margin: 0; }
    .section-copy { color: #849188; font-size: 12px; margin-top: 5px; }
    .step-no {
        display: inline-flex; width: 31px; height: 31px; align-items: center; justify-content: center;
        background: #edf3e9; color: var(--green); border-radius: 10px; font-size: 13px; font-weight: 800;
    }
    .step-tag { color: #829087; font-size: 10px; font-weight: 700; letter-spacing: 0.7px; }
    .step-title { font-size: 14px; font-weight: 700; margin: 0.45rem 0 0.3rem; }
    .step-copy { color: #718078; font-size: 12px; line-height: 1.7; }
    .prototype-note {
        padding: 10px 13px; border-radius: 10px; background: #f2f5ed; color: #78866f;
        font-size: 11px; line-height: 1.6; margin-top: 1rem;
    }
    div[data-testid="stImage"] img { border-radius: 12px; }
    hr { border-color: var(--line); margin: 1.2rem 0; }
    @media (max-width: 800px) {
        .block-container { padding: 1.4rem 1.1rem 2rem; }
        .hero-title { letter-spacing: -1.4px; }
    }
    </style>
    """,
    unsafe_allow_html=True,
)

with st.sidebar:
    st.markdown(
        '<div class="brand"><div class="brand-mark">↻</div>'
        '<div class="brand-name">Re:<span>Step</span></div></div>',
        unsafe_allow_html=True,
    )
    st.markdown('<div class="side-caption">WORKSPACE</div>', unsafe_allow_html=True)
    st.markdown('<div class="side-nav active">⌂　 분리배출 가이드</div>', unsafe_allow_html=True)
    st.markdown('<div class="side-nav">◷　 나의 실천 기록</div>', unsafe_allow_html=True)
    st.markdown('<div class="side-nav">♧　 분리배출 사전</div>', unsafe_allow_html=True)
    st.markdown('<div class="side-caption">MY ACTIVITY</div>', unsafe_allow_html=True)
    st.markdown(
        """
        <div class="side-note">
            <b>작은 분리가 만드는 변화</b><br>
            쓰레기를 하나씩 제대로 분리하면<br>다시 쓸 수 있는 자원이 늘어나요. 🌱
        </div>
        """,
        unsafe_allow_html=True,
    )
    st.caption("Re:Step · 딱착 분리배출")

header_left, header_right = st.columns([3.2, 1], vertical_alignment="center")
with header_left:
    st.markdown('<div class="eyebrow">SORT SMARTER, LIVE GREENER</div>', unsafe_allow_html=True)
    st.markdown(
        '<h1 class="hero-title">헷갈리는 분리배출,<br><em>한 단계씩 딱착.</em></h1>',
        unsafe_allow_html=True,
    )
    st.markdown(
        '<div class="hero-copy">사진을 올리고, 부속물부터 본체까지 차근차근 분리해요.<br>'
        '오늘의 작은 실천이 더 깨끗한 내일을 만듭니다.</div>',
        unsafe_allow_html=True,
    )
with header_right:
    st.markdown('<div class="top-chip">🌿　오늘도 지구에 한 걸음</div>', unsafe_allow_html=True)

st.write("")
left, right = st.columns([1.35, 0.85], gap="large")

with left:
    with st.container(border=True):
        st.markdown('<div class="card-heading">무엇을 버리시나요?</div>', unsafe_allow_html=True)
        st.markdown(
            '<div class="card-sub">사진을 올리고 품목을 선택해 분리 순서를 확인해 보세요.</div>',
            unsafe_allow_html=True,
        )
        uploaded_image = st.file_uploader(
            "사진 추가",
            type=["jpg", "jpeg", "png", "webp"],
            help="쓰레기 전체가 잘 보이도록 촬영한 사진을 선택해 주세요.",
        )
        if uploaded_image is not None:
            st.image(uploaded_image, caption="업로드한 사진", use_container_width=True)
        selected_item = st.selectbox("품목 선택", options=list(GUIDES), index=0)
        analyze = st.button("분리 방법 확인하기　→", use_container_width=True)

with right:
    st.markdown(
        """
        <div class="impact-card">
            <div class="impact-orbit">♻️</div>
            <div class="impact-kicker">ONE PHOTO, THREE SIMPLE STEPS</div>
            <div class="impact-title">분리배출은<br><span>하나씩, 제대로.</span></div>
        </div>
        """,
        unsafe_allow_html=True,
    )
    st.write("")
    stat_a, stat_b = st.columns(2)
    with stat_a:
        st.markdown(
            '<div class="upload-card"><div class="stat-label">함께 분리하는 품목</div>'
            '<div class="stat-value">06<span class="stat-unit"> 종류</span></div></div>',
            unsafe_allow_html=True,
        )
    with stat_b:
        st.markdown(
            '<div class="upload-card"><div class="stat-label">쉬운 분리 순서</div>'
            '<div class="stat-value">03<span class="stat-unit"> 단계</span></div></div>',
            unsafe_allow_html=True,
        )

st.write("")
st.markdown('<div class="section-title">이렇게 분리해요</div>', unsafe_allow_html=True)
st.markdown(
    '<div class="section-copy">부속물 제거부터 마지막 배출까지, 순서대로 따라 해보세요.</div>',
    unsafe_allow_html=True,
)

if analyze:
    st.session_state["guide_item"] = selected_item

guide_item = st.session_state.get("guide_item", selected_item)
guide = GUIDES[guide_item]
st.write("")
summary_left, summary_right = st.columns([2.7, 1], vertical_alignment="center")
with summary_left:
    st.markdown(
        f'<div class="guide-card"><span style="font-size:22px">{guide["icon"]}</span>　'
        f'<b>{guide_item}</b><span style="color:#829087;font-size:12px">　·　{guide["material"]}</span>'
        f'<div class="card-sub" style="margin-top:8px">예상 구성: {" · ".join(guide["parts"])}</div></div>',
        unsafe_allow_html=True,
    )
with summary_right:
    st.markdown(
        '<div class="prototype-note">파일럿 화면 · 현재 AI 이미지 탐지는 연결 전이며, '
        '선택한 품목의 예시 가이드를 보여드립니다.</div>',
        unsafe_allow_html=True,
    )

step_columns = st.columns(3, gap="medium")
for index, (step_column, step) in enumerate(zip(step_columns, guide["steps"]), start=1):
    title, description, tag = step
    with step_column:
        st.markdown(
            f'<div class="guide-card"><span class="step-no">{index:02d}</span>'
            f'<div class="step-tag" style="margin-top:14px">{tag}</div>'
            f'<div class="step-title">{title}</div>'
            f'<div class="step-copy">{description}</div></div>',
            unsafe_allow_html=True,
        )

st.markdown(
    '<div class="prototype-note">지역과 수거 방식에 따라 배출 기준이 다를 수 있어요. '
    '정확한 기준은 거주 지역의 안내를 확인해 주세요.</div>',
    unsafe_allow_html=True,
)
