import streamlit as st

st.title('🚗 Easy Compare My CAR 🚜')

# 더미 차량 DB
example_car_image = 'https://media.istockphoto.com/id/1150931120/ko/%EC%82%AC%EC%A7%84/%EC%9D%BC%EB%B0%98-%EC%BB%B4%ED%8C%A9%ED%8A%B8-%ED%99%94%EC%9D%B4%ED%8A%B8-%EC%9E%90%EB%8F%99%EC%B0%A8-%EC%A0%84%EB%A9%B4-%EC%B8%A1%EB%A9%B4%EC%9D%98-3d-%EA%B7%B8%EB%A6%BC.jpg?s=612x612&w=0&k=20&c=evtR5CTByAQWEj-b_C0CeAyT6LQJlCxvo8J702KEhaI='

# 차량 데이터 예시 (더미 데이터) - 나중에 선택된 차량들 정보로 채우면 됨
# 4열: 차량1, 차량2, 차량3, 차량4 (필요에 따라 갯수 조절)
dummy_data = [
    ["세단", "아반떼", "준중형", "2023-01", "가솔린", "15km/L", "500km", "5성"]
]

# dummy_data = [
#     ["세단", "아반떼", "준중형", "2023-01", "가솔린", "15km/L", "500km", "5성"],
#     ["SUV", "투싼", "중형", "2022-08", "디젤", "13km/L", "600km", "4성"],
#     ["해치백", "i30", "소형", "2021-06", "가솔린", "14km/L", "450km", "4.5성"]
# ]

# 초기 차량 리스트 (최대 3대)
if "cars" not in st.session_state:
    st.session_state.cars = []

# 비교 목록 리스트
specs = ['선택', '차량명', '차종', '출시일', '연료', '연비', '주행거리', '안정성', '가격']

# 스펙별로 한 줄씩 그리기
for idx, spec in enumerate(specs):
    row = st.columns(5)  # 항목명 + 3대 차량 비교용
    row[0].write(f"**{spec}**")  # 맨 왼쪽에 항목명

    for car_idx in range(3):  # 최대 3대 비교
        if car_idx < len(dummy_data):
            row[car_idx + 1].write(dummy_data[car_idx][idx])
        else:
            row[car_idx + 1].write("-")  # 데이터 없으면 비워두기
#
#
# # 비교 영역
# cols1 = st.columns(3)
#
# for idx, col in enumerate(cols1):
#     with col:
#         if idx < len(st.session_state.cars):
#             car = st.session_state.cars[idx]
#             st.image(car["image"], use_column_width=True)
#             st.markdown(f"**브랜드:** {car['brand']}")
#             st.markdown(f"**차량명:** {car['model']}")
#             st.markdown(f"**연료:** {car['fuel']}")
#             st.markdown(f"**연비:** {car['mileage']}")
#             st.markdown(f"**출시일:** {car['release_date']}")
#         else:
#             with st.popover(f"차량 {idx+1} 선택하기"):
#                 st.write("### 브랜드/모델 선택")
#                 selected_brand = st.selectbox("브랜드", list(car_db.keys()), key=f"brand_{idx}")
#                 selected_model = st.selectbox("모델", list(car_db[selected_brand].keys()), key=f"model_{idx}")
#
#                 if st.button("추가하기", key=f"add_car_{idx}"):
#                     car_info = car_db[selected_brand][selected_model]
#                     new_car = {
#                         "brand": selected_brand,
#                         "model": selected_model,
#                         "fuel": car_info["fuel"],
#                         "mileage": car_info["mileage"],
#                         "release_date": car_info["release_date"],
#                         "image": car_info["image"]
#                     }
#                     st.session_state.cars.append(new_car)
#                     st.experimental_rerun()
#
# # 최대 3개 제한
# if len(st.session_state.cars) >= 3:
#     st.warning("최대 3대까지만 비교할 수 있습니다.")
#
# # 초기화 버튼
# if st.button("비교 초기화"):
#     st.session_state.cars = []
#     st.experimental_rerun()
