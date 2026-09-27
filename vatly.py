import streamlit as st

def main():
    st.title("🚗 Chương trình tính chuyển động")

    lua_chon = st.selectbox(
        "Chọn đại lượng cần tính:",
        ["Vận tốc", "Quãng đường", "Thời gian"]
    )

    if lua_chon == "Vận tốc":
        st.subheader("Tính vận tốc")
        s = st.number_input("Quãng đường (km)", min_value=0.0)
        t = st.number_input("Thời gian (giờ)", min_value=0.1)

        if st.button("Tính vận tốc"):
            v = s / t
            st.success(f"Vận tốc = {v:.2f} km/h")

    elif lua_chon == "Quãng đường":
        st.subheader("Tính quãng đường")
        v = st.number_input("Vận tốc (km/h)", min_value=0.0)
        t = st.number_input("Thời gian (giờ)", min_value=0.0)

        if st.button("Tính quãng đường"):
            s = v * t
            st.success(f"Quãng đường = {s:.2f} km")

    elif lua_chon == "Thời gian":
        st.subheader("Tính thời gian")
        s = st.number_input("Quãng đường (km)", min_value=0.0)
        v = st.number_input("Vận tốc (km/h)", min_value=0.1)

        if st.button("Tính thời gian"):
            t = s / v
            st.success(f"Thời gian = {t:.2f} giờ")

if __name__ == "__main__":
    main()