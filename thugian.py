import streamlit as st
import webbrowser
def main():
    st.set_page_config(
    page_title="🎵 Thư giãn",
    page_icon="🎵"
    )

    st.title("🎵 GÓC THƯ GIÃN")
    st.write("Chọn thể loại nhạc bạn muốn nghe:")

    if st.button("🎵 Nhạc thư giãn"):
        webbrowser.open(
    "https://www.youtube.com/results?search_query=nhạc+thư+giãn"
    )

    if st.button("🌿 Nhạc thiên nhiên"):
        webbrowser.open(
    "https://www.youtube.com/results?search_query=nhạc+thiên+nhiên+thư+giãn"
    )

    if st.button("☕ Nhạc cà phê"):
        webbrowser.open(
    "https://www.youtube.com/results?search_query=nhạc+cafe+chill"
    )

    if st.button("🎹 Piano nhẹ nhàng"):
        webbrowser.open(
    "https://www.youtube.com/results?search_query=piano+nhẹ+nhàng"
    )

    if st.button("🎶 YouTube"):
        webbrowser.open("https://www.youtube.com")
