import streamlit as st

st.set_page_config(page_title="Easy Compare My CAR", layout="wide")

st.title('🚗 Easy Compare My CAR 🚜')
st.header('')

# 더미 차량 DB (사진용)
example_car_image = 'https://media.istockphoto.com/id/1150931120/ko/%EC%82%AC%EC%A7%84/%EC%9D%BC%EB%B0%98-%EC%BB%B4%ED%8C%A9%ED%8A%B8-%ED%99%94%EC%9D%B4%ED%8A%B8-%EC%9E%90%EB%8F%99%EC%B0%A8-%EC%A0%84%EB%A9%B4-%EC%B8%A1%EB%A9%B4%EC%9D%98-3d-%EA%B7%B8%EB%A6%BC.jpg?s=612x612&w=0&k=20&c=evtR5CTByAQWEj-b_C0CeAyT6LQJlCxvo8J702KEhaI='

# 차량 데이터 예시 (더미)
dummy_data1 = ["세단", "아반떼", "준중형", "2023-01", "가솔린", "15km/L", "500km", "5성"]
dummy_data2 = ["SUV", "쏘나타", "중형", "2022-08", "디젤", "13km/L", "600km", "4성"]
dummy_data3 = ["해치백", "투싼", "소형", "2021-06", "가솔린", "14km/L", "450km", "4.5성"]

select_car_dialog_data = {
    '현대': ['아반떼', '쏘나타', '투싼'],
    '기아': ['K3', 'K5', '스포티지'],
    '제네시스': ['G70', 'G80', 'GV80']
}

# 세션 상태 초기화
if 'choosed_cars' not in st.session_state:
    st.session_state.choosed_cars = []

for i in range(3):
    if f'open_dialog_{i}' not in st.session_state:
        st.session_state[f'open_dialog_{i}'] = False

# 스펙 항목
specs = ['선택', '차량명', '차종', '출시일', '연료', '연비', '주행거리', '안정성', '가격']


# 차량 선택 버튼 클릭 핸들러
def clicked_select_car_button(i):
    st.session_state[f'open_dialog_{i}'] = True


# 차량 비교 UI 출력
for idx, spec in enumerate(specs):
    row = st.columns(4)  # 항목 + 3대 차량 비교
    row[0].write(f"**{spec}**")

    for car_idx in range(3):
        if idx == 0:
            row[car_idx + 1].button('차량 선택', key=f'select_button_{car_idx}', on_click=clicked_select_car_button,
                                    args=(car_idx,))
        try:
            row[car_idx + 1].write(st.session_state.choosed_cars[car_idx][idx + 1])
        except:
            row[car_idx + 1].write("-")

# 다이얼로그 구현
for dialog_index in range(3):
    if st.session_state.get(f'open_dialog_{dialog_index}', False):
        st.markdown(f"### 🚘 차량 {dialog_index + 1} 선택 중")
        brands = list(select_car_dialog_data.keys())

        for i in range(0, len(brands), 5):
            cols = st.columns(5)
            for j in range(5):
                if i + j < len(brands):
                    brand = brands[i + j]
                    if cols[j].button(brand, key=f'brand_{brand}_{dialog_index}'):
                        st.session_state[f'selected_brand_{dialog_index}'] = brand

        selected_brand = st.session_state.get(f'selected_brand_{dialog_index}')
        if selected_brand:
            st.write(f'선택된 브랜드: {selected_brand}')
            model = st.selectbox(
                f'{selected_brand} 모델 리스트',
                select_car_dialog_data[selected_brand],
                key=f'model_select_{dialog_index}'
            )

            if st.button('선택 완료', key=f'confirm_select_{dialog_index}'):
                # 더미 데이터 매핑
                if model == "아반떼":
                    car_data = [f'{selected_brand} {model}'] + dummy_data1
                elif model == "쏘나타":
                    car_data = [f'{selected_brand} {model}'] + dummy_data2
                elif model == "투싼":
                    car_data = [f'{selected_brand} {model}'] + dummy_data3
                else:
                    car_data = [f'{selected_brand} {model}'] + ["-", "-", "-", "-", "-", "-", "-", "-"]

                if len(st.session_state.choosed_cars) > dialog_index:
                    st.session_state.choosed_cars[dialog_index] = car_data
                else:
                    while len(st.session_state.choosed_cars) < dialog_index:
                        st.session_state.choosed_cars.append(["-"] * len(specs))
                    st.session_state.choosed_cars.append(car_data)

                # 다이얼로그 닫기
                st.session_state[f'open_dialog_{dialog_index}'] = False

        st.divider()

# 초기화 버튼
if st.button("비교 초기화"):
    st.session_state.choosed_cars = []
    for i in range(3):
        st.session_state[f'open_dialog_{i}'] = False
        st.session_state.pop(f'selected_brand_{i}', None)
