import streamlit as st
import ran
import duaxe
import chim 
import dientich
import thoikhoabieu

st.title("📚 LỚP 7A17")
st.write("Trường THCS Nguyễn Du")


menu = st.sidebar.selectbox(
    "Chọn chức năng",
    [
        "📅 Thời khóa biểu",
        "📐 Tính diện tích",
        "🎮 Giải trí",
        "Giới thiệu về lớp học"
    ]
)
if menu == "📅 Thời khóa biểu":
    thoikhoabieu.main()
    

elif menu == "🎮 Giải trí":

    st.header("🎮 KHU GIẢI TRÍ")

    game = st.selectbox(
        "🎯 Chọn game",
        [
            "🐍 Rắn săn mồi",
            "🏎️ Đua xe",
            "🐦 chim"
        ]
    )

    if game == "🐍 Rắn săn mồi":
        ran.main()

    elif game == "🏎️ Đua xe":
        duaxe.main()

    elif game == "🐦 chim":
        chim.main()
elif menu == "📐 Tính diện tích":
    dientich.main()

elif menu =="Giới thiệu về lớp học":
    st.subheader("📚 Trang web đang được hoàn thiện")
    st.write("Mình là Nguyễn Huy Phúc")
