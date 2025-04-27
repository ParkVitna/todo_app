import streamlit as st

st.title('🚗 Easy Compare My CAR 🚜')
st.header('')

# 예시 이미지
example_car_image = 'https://media.istockphoto.com/id/1150931120/ko/%EC%82%AC%EC%A7%84/%EC%9D%BC%EB%B0%98-%EC%BB%B4%ED%8C%A9%ED%8A%B8-%ED%99%94%EC%9D%B4%ED%8A%B8-%EC%9E%90%EB%8F%99%EC%B0%A8-%EC%A0%84%EB%A9%B4-%EC%B8%A1%EB%A9%B4%EC%9D%98-3d-%EA%B7%B8%EB%A6%BC.jpg?s=612x612&w=0&k=20&c=evtR5CTByAQWEj-b_C0CeAyT6LQJlCxvo8J702KEhaI='

# 차량 데이터 예시 (더미 데이터)
car_data = {
    '현대': ['아반떼', '쏘나타', '투싼'],
    '기아': ['K3', 'K5', '스포티지'],
    '제네시스': ['G70', 'G80', 'GV80']
}

# 스펙 리스트
specs = ['선택', '차량명', '차종', '출시일', '연료', '연비', '주행거리', '안정성', '가격']

# 세션 초기화
if 'choosed_cars' not in st.session_state:
    st.session_state.choosed_cars = []

for i in range(3):
    if f'open_dialog_{i}' not in st.session_state:
        st.session_state[f'open_dialog_{i}'] = False
    if f'selected_brand_{i}' not in st.session_state:
        st.session_state[f'selected_brand_{i}'] = None
    if f'selected_model_{i}' not in st.session_state:
        st.session_state[f'selected_model_{i}'] = None

# 차량 선택 버튼 클릭 함수
def clicked_select_car_button(i):
    st.session_state[f'open_dialog_{i}'] = True

# 차량 선택 다이얼로그
def select_car_dialog(i):
    if st.session_state.get(f'open_dialog_{i}', False):
        with st.dialog("차량을 선택해주세요."):
            st.subheader("🚗 브랜드 선택")
            col1, col2, col3 = st.columns(3)

            with col1:
                if st.button('현대', key=f'brand_hyundai_{i}'):
                    st.session_state[f'selected_brand_{i}'] = '현대'
            with col2:
                if st.button('기아', key=f'brand_kia_{i}'):
                    st.session_state[f'selected_brand_{i}'] = '기아'
            with col3:
                if st.button('제네시스', key=f'brand_genesis_{i}'):
                    st.session_state[f'selected_brand_{i}'] = '제네시스'

            # 브랜드를 선택한 경우 모델 선택
            brand = st.session_state.get(f'selected_brand_{i}')
            if brand:
                st.subheader(f"🚙 {brand} 모델 선택")
                model = st.selectbox(
                    f"{brand} 모델을 선택하세요",
                    car_data.get(brand, []),
                    key=f'model_select_{i}'
                )

                st.session_state[f'selected_model_{i}'] = model

                # 선택 완료 버튼
                if st.button("✅ 선택 완료", key=f'confirm_select_{i}'):
                    selected_car = [
                        "선택됨",    # 선택
                        f"{brand} {model}",  # 차량명
                        "세단",     # 차종 (예시)
                        "2024-01", # 출시일 (예시)
                        "가솔린",   # 연료 (예시)
                        "15km/L",  # 연비 (예시)
                        "500km",   # 주행거리 (예시)
                        "5성",     # 안정성 (예시)
                        "3천만원"  # 가격 (예시)
                    ]

                    # 기존에 있는 차를 수정 또는 추가
                    if len(st.session_state.choosed_cars) > i:
                        st.session_state.choosed_cars[i] = selected_car
                    else:
                        st.session_state.choosed_cars.append(selected_car)

                    st.session_state[f'open_dialog_{i}'] = False



# UI START --------------------------------------------------------------------------------------
for idx, spec in enumerate(specs):
    row = st.columns(4)
    row[0].write(f"**{spec}**")

    for car_idx in range(3):
        if idx == 0:
            if row[car_idx + 1].button('차량 선택', key=f'select_button_{car_idx}', on_click=clicked_select_car_button, args=(car_idx,)):
                pass
            # 버튼 눌렀으면 다이얼로그 열기
            select_car_dialog(car_idx)

        if car_idx < len(st.session_state.choosed_cars):
            row[car_idx + 1].write(st.session_state.choosed_cars[car_idx][idx])
        else:
            row[car_idx + 1].write("-")

# 비교 초기화 버튼
if st.button("비교 초기화"):
    st.session_state.choosed_cars = []
    for i in range(3):
        st.session_state[f'selected_brand_{i}'] = None
        st.session_state[f'selected_model_{i}'] = None
