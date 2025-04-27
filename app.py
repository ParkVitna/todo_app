import streamlit as st

st.title('🚗 Easy Compare My CAR 🚜')

# 더미 차량 DB
car_db = {
    "현대": {
        "아반떼": {"fuel": "가솔린", "mileage": "15km/L", "release_date": "2023-01", "image": "https://via.placeholder.com/150"},
        "소나타": {"fuel": "디젤", "mileage": "13km/L", "release_date": "2022-06", "image": "https://via.placeholder.com/150"},
    },
    "기아": {
        "K3": {"fuel": "가솔린", "mileage": "14km/L", "release_date": "2022-08", "image": "https://via.placeholder.com/150"},
        "K5": {"fuel": "하이브리드", "mileage": "18km/L", "release_date": "2021-11", "image": "https://via.placeholder.com/150"},
    },
    "BMW": {
        "320i": {"fuel": "가솔린", "mileage": "12km/L", "release_date": "2022-05", "image": "https://via.placeholder.com/150"},
        "520d": {"fuel": "디젤", "mileage": "16km/L", "release_date": "2021-03", "image": "https://via.placeholder.com/150"},
    },
    "벤츠": {
        "C클래스": {"fuel": "가솔린", "mileage": "11km/L", "release_date": "2023-02", "image": "https://via.placeholder.com/150"},
        "E클래스": {"fuel": "디젤", "mileage": "14km/L", "release_date": "2020-09", "image": "https://via.placeholder.com/150"},
    }
}

# 초기 차량 리스트 (최대 3대)
if "cars" not in st.session_state:
    st.session_state.cars = []

st.title("TITLE(차량 스펙 비교)")

# 비교 영역
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
                st.write("### 브랜드/모델 선택")
                selected_brand = st.selectbox("브랜드", list(car_db.keys()), key=f"brand_{idx}")
                selected_model = st.selectbox("모델", list(car_db[selected_brand].keys()), key=f"model_{idx}")

                if st.button("추가하기", key=f"add_car_{idx}"):
                    car_info = car_db[selected_brand][selected_model]
                    new_car = {
                        "brand": selected_brand,
                        "model": selected_model,
                        "fuel": car_info["fuel"],
                        "mileage": car_info["mileage"],
                        "release_date": car_info["release_date"],
                        "image": car_info["image"]
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
