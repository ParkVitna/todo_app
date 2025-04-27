import streamlit as st

st.title('🚗 Easy Compare My CAR 🚜')
st.header('')

# 더미 데이터
# 차량 이미지 예시
example_car_image = 'car_sample_image.jpeg'

# 차량 데이터 예시
dummy_data1 =  ["세단", "아반떼", "준중형", "2023-01", "가솔린", "15km/L", "500km", "5성"]
dummy_data2 =  ["SUV", "투싼", "중형", "2022-08", "디젤", "13km/L", "600km", "4성"]
dummy_data3 =  ["해치백", "i30", "소형", "2021-06", "가솔린", "14km/L", "450km", "4.5성"]

select_car_dialog_data = {
    '현대': ['아반떼', '투싼', 'i30'],
    '기아': ['K3', 'K5', '스포티지'],
    '제네시스': ['G70', 'G80', 'GV80']
}


# choosed_cars 초기화
if 'choosed_cars' not in st.session_state:
    st.session_state.choosed_cars = [] #Car 클래스 객체

# open_dialog_i 초기화
for i in range(3):
    if f'open_dialog_{i}' not in st.session_state:
        st.session_state[f'open_dialog_{i}'] = False

# selected_brand_i 초기화
for i in range(3):
    if f'selected_brand_{i}' not in st.session_state:
        st.session_state[f'selected_brand_{i}'] = False

# selected_image_i 초기화
for i in range(3):
    if f'selected_image_{i}' not in st.session_state:
        st.session_state[f'selected_image_{i}'] = False



# 비교 목록 리스트
specs = ['선택', '차량명', '차종', '출시일', '연료', '연비', '주행거리', '안정성', '가격']

# 차량 선택 버튼 클릭 함수
def clicked_select_car_button(i):
    st.session_state[f'open_dialog_{i}'] = True
    select_car_dialog(i)

# 차량 선택 다이얼로그
@st.dialog("차량을 선택해주세요.")
def select_car_dialog(index):
    st.write(f'🚗차량 선택{index+1} : 브랜드')
    brands = list(select_car_dialog_data.keys())

    # 브랜드 5개씩 n줄
    # Todo 브랜드 로고 이미지 넣기
    for i in range(0, len(brands), 5):
        cols = st.columns(5)

        for j in range(5):
            if i + j < len(brands):
                brand = brands[i + j]
                if cols[j].button(brand, key=f'brand_{brand}_{index}'):
                    st.session_state[f'selected_brand_{index}'] = brand

    # 브랜드 선택 후, 모델 선택
    selected_brand = st.session_state.get(f'selected_brand_{index}')
    if selected_brand:
        st.write(f'🚗차량 선택{index+1} : {selected_brand} 모델')

        model = st.selectbox(
            f'{selected_brand} 모델 리스트',
            select_car_dialog_data[selected_brand],
            key=f'model_select_{index}'
        )

        if st.button('선택 완료', key=f'confirm_select_{index}'):
            # 더미 데이터 매핑
            # Todo 데이터 쿼리로 매핑, 이미지 매핑
            if model == "아반떼":
                car_data = [f'{selected_brand} {model}'] + dummy_data1
                st.session_state[f'selected_image_{index}'] = example_car_image
            elif model == "투싼":
                car_data = [f'{selected_brand} {model}'] + dummy_data2
                st.session_state[f'selected_image_{index}'] = example_car_image
            elif model == "i30":
                car_data = [f'{selected_brand} {model}'] + dummy_data3
                st.session_state[f'selected_image_{index}'] = example_car_image
            else:
                car_data = [f'{selected_brand} {model}'] + ["-", "-", "-", "-", "-", "-", "-", "-"]
                st.session_state[f'selected_image_{index}'] = example_car_image

            # 선택한 차량 정보를 해당 index 위치에 넣음
            if len(st.session_state.choosed_cars) > index:
                st.session_state.choosed_cars[index] = car_data
            else:
                # 리스트 크기가 index보다 작으면 빈 칸 채우고 추가
                while len(st.session_state.choosed_cars) < index:
                    st.session_state.choosed_cars.append(["-"] * len(specs))
                st.session_state.choosed_cars.append(car_data)

            # 닫기
            st.session_state[f'open_dialog_{index}'] = False
            st.rerun()


# UI START

# 스펙별로 한 줄씩 그리기
title, car1, car2, car3 = st.columns(4, vertical_alignment='bottom')
car1.image('car_sample_image.jpeg')
car2.image(st.session_state.get('selected_image_1'))
car3.image(st.session_state.get(f'selected_image_2'))

for idx, spec in enumerate(specs):
    row = st.columns(4)  # 항목명 + 3대 차량 비교용
    row[0].write(f"**{spec}**")  # 맨 왼쪽에 항목명

    for car_idx in range(3):  # 최대 3대 비교
        # 차량 선택 버튼
        if idx == 0:
            row[car_idx + 1].button('차량 선택', key=f'select_button_{car_idx}', on_click=clicked_select_car_button, args=(car_idx,))

        if car_idx < len(st.session_state.choosed_cars):
            try:
                row[car_idx + 1].write(st.session_state.choosed_cars[car_idx][idx + 1])
            except IndexError:
                row[car_idx + 1].write("-")
        else:
            row[car_idx + 1].write("-")  # 데이터 없으면 비워두기

    st.divider()

# 초기화 버튼
if st.button("비교 초기화"):
    st.session_state.choosed_cars = []

    for i in range(3):
        st.session_state[f'open_dialog_{i}'] = False
        st.session_state.pop(f'selected_brand_{i}', None)

    st.rerun()
