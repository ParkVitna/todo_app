import streamlit as st

st.title('🚗 Easy Compare My CAR 🚜')

# 차량 브랜드/차종 Dumy Data
brands = {
    "현대": ["아반떼", "소나타", "그랜저"],
    "기아": ["K3", "K5", "K7"],
    "BMW": ["320i", "520d", "X5"],
    "벤츠": ["C클래스", "E클래스", "S클래스"]
}

# 초기 차량 리스트 (최대 3대)
if "cars" not in st.session_state:
    st.session_state.cars = []

# 비교 영역
st.write("## 차량 선택")

cols = st.columns(3)

for idx, col in enumerate(cols):
    with col:
        if idx < len(st.session_state.cars):
            car = st.session_state.cars[idx]
            st.image(car["image"], use_column_width=True)
            st.markdown(f"**브랜드:** {car['brand']}")
            st.markdown(f"**차량명:** {car['model']}")
            st.markdown(f"**연료:** {car['fuel']}")
            st.markdown(f"**연비:** {car['mileage']}")
            st.markdown(f"**출시일:** {car['release_date']}")
        else:
            with st.popover(f"차량 {idx+1} 선택하기"):
                st.write("### 차량 선택")
                selected_brand = st.selectbox("브랜드 선택", list(brands.keys()), key=f"brand_{idx}")
                selected_model = st.selectbox("차량 모델 선택", brands[selected_brand], key=f"model_{idx}")
                uploaded_image = st.file_uploader("차량 이미지 업로드", type=["png", "jpg", "jpeg"], key=f"image_upload_{idx}")

                # 추가 스펙 입력
                fuel = st.text_input("연료", key=f"fuel_{idx}")
                mileage = st.text_input("연비", key=f"mileage_{idx}")
                release_date = st.text_input("출시일", key=f"release_{idx}")

                if st.button("추가하기", key=f"add_car_{idx}"):
                    if uploaded_image is not None:
                        new_car = {
                            "brand": selected_brand,
                            "model": selected_model,
                            "image": uploaded_image,
                            "fuel": fuel,
                            "mileage": mileage,
                            "release_date": release_date
                        }
                        st.session_state.cars.append(new_car)
                        st.experimental_rerun()

# 최대 3개 제한
if len(st.session_state.cars) >= 3:
    st.warning("최대 3대까지만 비교할 수 있습니다.")

# 초기화 버튼
if st.button("비교 초기화"):
    st.session_state.cars = []
    st.experimental_rerun()
