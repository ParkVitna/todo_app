import streamlit as st

st.title('🚗 Easy Compare My CAR 🚜')
st.header('')

# 더미 차량 DB
example_car_image = 'https://media.istockphoto.com/id/1150931120/ko/%EC%82%AC%EC%A7%84/%EC%9D%BC%EB%B0%98-%EC%BB%B4%ED%8C%A9%ED%8A%B8-%ED%99%94%EC%9D%B4%ED%8A%B8-%EC%9E%90%EB%8F%99%EC%B0%A8-%EC%A0%84%EB%A9%B4-%EC%B8%A1%EB%A9%B4%EC%9D%98-3d-%EA%B7%B8%EB%A6%BC.jpg?s=612x612&w=0&k=20&c=evtR5CTByAQWEj-b_C0CeAyT6LQJlCxvo8J702KEhaI='

# 차량 데이터 예시 (더미 데이터)
dummy_data1_car_brand = 'brand1'
dummy_data1_car_model = 'model1'
dummy_data1 =  ["세단", "아반떼", "준중형", "2023-01", "가솔린", "15km/L", "500km", "5성"]
dummy_data2_car_brand = 'brand2'
dummy_data2_car_model = 'model2'
dummy_data2 =  ["SUV", "투싼", "중형", "2022-08", "디젤", "13km/L", "600km", "4성"]
dummy_data3_car_brand = 'brand3'
dummy_data3_car_model = 'model3'
dummy_data3 =  ["해치백", "i30", "소형", "2021-06", "가솔린", "14km/L", "450km", "4.5성"]

select_car_dialog_data = {
    '현대': ['아반떼', '쏘나타', '투싼'],
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

if 'choosed_cars' not in st.session_state:
    st.session_state.choosed_cars = [] #Car 클래스 객체

# 차량 선택
# st.session_state['todos'].append(dummy_data1)
# st.session_state['todos'].append(dummy_data2)
# st.session_state['todos'].append(dummy_data3)

# 비교 목록 리스트
specs = ['선택', '차량명', '차종', '출시일', '연료', '연비', '주행거리', '안정성', '가격']

# 차량 선택 버튼 클릭 함수
def clicked_select_car_button(i):
    st.session_state[f'open_dialog_{i}'] = True
    select_car_dialog(i)

# 차량 선택 다이얼로그
@st.dialog("차량을 선택해주세요.")
def select_car_dialog(index):
    st.write(f'차량{index+1} 브랜드 선택')
    brands = list(select_car_dialog_data.keys())

    # 브랜드 5개씩 n줄
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
        st.write(f'차량{index+1} {selected_brand} 모델 선택')

        model = st.selectbox(
            f'{selected_brand} 모델 리스트',
            select_car_dialog_data[selected_brand],
            key=f'model_select_{index}'
        )

        if st.button('선택 완료', key=f'confirm_select_{index}'):
            # 닫기
            st.session_state[f'open_dialog_{index}'] = False




# UI START

# 스펙별로 한 줄씩 그리기
for idx, spec in enumerate(specs):
    row = st.columns(4)  # 항목명 + 3대 차량 비교용
    row[0].write(f"**{spec}**")  # 맨 왼쪽에 항목명

    for car_idx in range(3):  # 최대 3대 비교
        # 차량 선택 버튼
        if idx == 0:
            row[car_idx + 1].button('차량 선택', key=f'select_button_{car_idx}', on_click=clicked_select_car_button, args=(car_idx,))

        if car_idx < len(st.session_state.choosed_cars):
            row[car_idx + 1].write(st.session_state.choosed_cars[car_idx][idx + 1])
        else:
            row[car_idx + 1].write("-")  # 데이터 없으면 비워두기


# 초기화 버튼
if st.button("비교 초기화"):
    st.session_state.choosed_cars = []
