import streamlit as st
import ran

st.title("📚 LỚP 7A17")
st.write("Trường THCS Nguyễn Du")


menu = st.sidebar.selectbox(
    "Chọn chức năng",
    [
        "📅 Thời khóa biểu",
        "🎮 Giải trí",
        "Giới thiệu về lớp học"
    ]
)
if menu == "📅 Thời khóa biểu":
    st.subheader("📚 THỜI KHÓA BIỂU 7A17")
    st.write("Năm học 2026 - 2027")
    # Màu
    mau = {
        "Toán": "blue",
        "Ngữ văn": "red",
        "Văn": "red",
        "Tiếng Anh": "green",
        "Ngoại Ngữ": "green",
        "Ngoại ngữ": "green",
        "Địa lý": "orange",
        "Lịch sử": "brown",
        "Tin học": "purple",
        "Công nghệ": "teal",
        "Thể dục": "green",
        "Giáo dục thể chất": "green",
        "Âm nhạc": "pink",
        "Nhạc": "pink",
        "Mĩ thuật": "orange",
        "Mỹ Thuật": "orange",
        "Sinh học": "darkgreen",
        "Vật Lý": "darkblue",
        "Hóa học": "darkorange",
        "Giáo dục công dân": "purple",
        "Hoạt động trải nghiệm": "crimson",
        "Sinh hoạt Lớp": "gray",
        "Sinh hoạt lớp": "gray",
        "Sinh hoạt dưới cờ": "brown"
    }

    # Thời khóa biểu
    tkb = {
        "Thứ Hai": [
            "Sinh hoạt dưới cờ",
            "Ngữ văn",
            "Lịch sử",
            "Toán",
            "Sinh học"
        ],

        "Thứ Ba": [
            "Ngoại Ngữ",
            "Vật Lý",
            "Giáo dục công dân",
            "Toán",
            "Toán"
        ],

        "Thứ Tư": [
            "Địa lý",
            "Nhạc",
            "Tin học",
            "Ngoại ngữ",
            "Hóa học",
            "Buổi chiều: Tiết 2: Giáo dục địa phương"
        ],

        "Thứ Năm": [
            "Thể dục",
            "Vật Lý",
            "Hoạt động trải nghiệm",
            "Hoạt động trải nghiệm"
        ],

        "Thứ Sáu": [
            "Văn",
            "Giáo dục thể chất",
            "Toán",
            "Ngoại ngữ",
            "Mỹ Thuật"
        ],

        "Thứ Bảy": [
            "Văn",
            "Văn",
            "Lịch sử",
            "Công nghệ",
            "Sinh hoạt Lớp"
        ],

        "Chủ nhật": [
            "Nay cuối tuần nghỉ bạn nhé"
        ]
    }

    # Chọn thứ ở thanh bên trái
    thu = st.sidebar.selectbox(
        "📅 Chọn thứ",
        tkb.keys()
    )

    # Hiển thị thời khóa biểu
    st.header(thu)

    for i, mon in enumerate(tkb[thu], 1):

        # Dòng riêng cho Giáo dục địa phương
        if mon.startswith("Buổi chiều"):
            st.markdown(
                f"""
                <div style="
                    font-size:18px;
                    color:white;
                    background-color:#e67e22;
                    padding:8px;
                    margin-top:10px;
                    border-radius:8px;
                    font-weight:bold;
                ">
                🌅 {mon}
                </div>
                """,
                unsafe_allow_html=True
            )

        else:
            st.markdown(
                f"""
                <div style="
                    font-size:20px;
                    color:{mau.get(mon, 'black')};
                    margin-bottom:5px;
                ">
                Tiết {i}: {mon}
                </div>
                """,
                unsafe_allow_html=True
            )

    st.caption("Cập nhật bởi huyphuc-7a17")

elif menu == "🎮 Giải trí":
    ran.main()
elif menu =="Giới thiệu về lớp học":
    st.subheader("📚 Trang web đang được hoàn thiện")
    st.write("Mình là Nguyễn Huy Phúc")