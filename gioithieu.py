import streamlit as st
def main():
    st.title("🏫 GIỚI THIỆU LỚP 7A17")

    st.image(
        "anhlop.jpg",
        caption="Tập thể lớp 7A17",
        use_container_width=True
    )

    st.write("""
    Lớp 7A17 là một tập thể đoàn kết, chăm ngoan và tích cực tham gia
    các hoạt động học tập, văn nghệ, thể thao của nhà trường.
    """)
if __name__ == "__main__":
    main()