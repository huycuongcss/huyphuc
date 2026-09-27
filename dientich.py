import streamlit as st

def main():

    st.title("📐 TÍNH DIỆN TÍCH CÁC HÌNH")

    hinh = st.selectbox(
        "Chọn hình cần tính",
        [
            "Hình chữ nhật",
            "Hình vuông",
            "Hình tam giác",
            "Hình tròn"
        ]
    )

    # HÌNH CHỮ NHẬT
    if hinh == "Hình chữ nhật":
        dai = st.number_input("Chiều dài", min_value=0.0)
        rong = st.number_input("Chiều rộng", min_value=0.0)

        if st.button("Tính diện tích"):
            dientich = dai * rong
            st.success(f"Diện tích = {dientich}")

    # HÌNH VUÔNG
    elif hinh == "Hình vuông":
        canh = st.number_input("Độ dài cạnh", min_value=0.0)

        if st.button("Tính diện tích"):
            dientich = canh ** 2
            st.success(f"Diện tích = {dientich}")

    # HÌNH TAM GIÁC
    elif hinh == "Hình tam giác":
        day = st.number_input("Độ dài đáy", min_value=0.0)
        cao = st.number_input("Chiều cao", min_value=0.0)

        if st.button("Tính diện tích"):
            dientich = day * cao / 2
            st.success(f"Diện tích = {dientich}")

    # HÌNH TRÒN
    elif hinh == "Hình tròn":
        bankinh = st.number_input("Bán kính", min_value=0.0)

        if st.button("Tính diện tích"):
            dientich = 3.14159 * bankinh ** 2
            st.success(f"Diện tích = {dientich}")

if __name__ == "__main__":
    main()