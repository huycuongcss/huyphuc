import streamlit as st

def main():

st.title("🎵 GÓC THƯ GIÃN")

st.write("Chọn một nội dung để nghe nhạc:")

st.markdown(
    """
    <a href="https://www.youtube.com" target="_blank">
        <button style="
            width: 100%;
            padding: 12px;
            font-size: 18px;
            cursor: pointer;
        ">
            🎵 MỞ YOUTUBE
        </button>
    </a>
    """,
    unsafe_allow_html=True
)

st.markdown(
    """
    <a href="https://www.youtube.com/results?search_query=nhac+thu+gian" target="_blank">
        <button style="
            width: 100%;
            padding: 12px;
            font-size: 18px;
            cursor: pointer;
        ">
            🌿 Nhạc thư giãn
        </button>
    </a>
    """,
    unsafe_allow_html=True
)

st.markdown(
    """
    <a href="https://www.youtube.com/results?search_query=nhac+cafe+chill" target="_blank">
        <button style="
            width: 100%;
            padding: 12px;
            font-size: 18px;
            cursor: pointer;
        ">
            ☕ Nhạc Cafe Chill
        </button>
    </a>
    """,
    unsafe_allow_html=True
)

st.markdown(
    """
    <a href="https://www.youtube.com/results?search_query=piano+relaxing+music" target="_blank">
        <button style="
            width: 100%;
            padding: 12px;
            font-size: 18px;
            cursor: pointer;
        ">
            🎹 Piano thư giãn
        </button>
    </a>
    """,
    unsafe_allow_html=True
)
