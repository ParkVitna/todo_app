import streamlit as st

st.title('🚗 Easy Compare My CAR 🚜')
st.header('')

# 더미 데이터
# 차량 이미지 예시
example_car_image = 'data:image/jpeg;base64,/9j/4AAQSkZJRgABAQAAAQABAAD/2wCEAAkGBwgHBgkIBwgKCgkLDRYPDQwMDRsUFRAWIB0iIiAdHx8kKDQsJCYxJx8fLT0tMTU3Ojo6Iys/RD84QzQ5OjcBCgoKDQwNGg8PGjclHyU3Nzc3Nzc3Nzc3Nzc3Nzc3Nzc3Nzc3Nzc3Nzc3Nzc3Nzc3Nzc3Nzc3Nzc3Nzc3Nzc3N//AABEIAK0AuQMBIgACEQEDEQH/xAAcAAABBAMBAAAAAAAAAAAAAAAABAUGBwIDCAH/xABPEAABAwMBBAUHBwYLBwUAAAABAgMEAAURBhIhMUEHUWFxgRMUFSIykdFCcoKSobHBFiNSYpPSJDNDREVTVFWDssIXc5TT4vDxJTQ1dKL/xAAVAQEBAAAAAAAAAAAAAAAAAAAAAf/EABYRAQEBAAAAAAAAAAAAAAAAAAABEf/aAAwDAQACEQMRAD8AvGiiigKKKKAooooCiiigKKKKAooooCiiigKKKKAooooCiiigKKKKAooooCiiigKKKKAooooCiiigKKKKAooooCiiigKKKKAooooCiiigKKKKAooooCiivDQe1itaUe0cZqK6v1zadNN7Mh8KlEeqw36yj4cu+qyuvSZdJTHlIrKGEuLw2lxSjlI47hjHdkigvNTyQMpyrupEL1D868zcU41KwSGnEFJUBxI5HwzVO2XpBlokp9IsNKaJBUqLtNupHWDnCu4jBq0ZUOPqa0I2lpW4AHYstA3jqWnqI3gjtNA6OXJKMbEZ9wHmgD8SKw9LDnClj6KfjVFzbnMiTH4U91fl2VlDgKyd4/CkbjsV/wDjQTnmhxST7waDoL0qjnElj/DHxr0XRn5TMhHzmjXOTtrjO72plwYH6klRz7zSJ2yXNGVRL/JxyDji0/aD+FB056Uif1hHegj8KyFyiH+WA7wa5UeZ1dGBLdxuCxyLMtZ/HNIhqHUzDhSu93RCh8lclzI8CaDrxMuOr2X0HxrclQUPVIPca5DTrbVLR9W+S1d69r76WMdJWr2CFC8OHHJTLZ/00HWVFUCzrDpSaZQ6u0GSgpCkqMY5IO/5CgaX2TprmQpwiastC2EcCtpBS4g9qVcR3b++gu+im6x3q236CmZaZjUpg/KbPsnqI4g99ONAUUUUBRRRQFFFFB4cVWfSX0iosoctdmKXJ5GHHeKWeztV2HcKfek3Ui9P6eUYqtmZKPkmOzPFXgK53k7Dzi1HgDgqJ3qVzJP/AHvBoEzjr9znlT7i3H315UtatontzSuW6FTQhH8WwnZTWVvYS0XH221LcSn1QkFR8BXkK1XBxe25AmBKsqWsxlgeO6g3w1kqyPfVu9Ed52kO2p5zenLzAzy4LA7OCh41ToLbbqksnABwd+akWjLoLbf4tyUr82yoJJ/UO5f2UEk6b7MYVzi3uOMNy0+Se3cHEjcfFO76NVw28ob+ZNdF66tR1Bo2dFQgGQG/KsjqcTvSPH2e5VU9ZNM22525mQl58bY9YBSfVUNxHs1QwNvqpU28qpW1oq3A7JmvjvKPhXtz0nDt9vckoluLUnASlSUnaJOMbqCNJeVW5puLLdQ1ccCOT66vJ7ZA7BShmK2T6xTtnfx30vVbkOErCAgHgkDgKYHixSej6xpDkGG6l7OTIcjlxZPYTnHcMVAuk3THm2oDPtyUuQrmgSmSjmT7Qxx47/pU/uWoHeOIqST7Qu6dGzSkp/hFqdUU9fkwfWH1SD9GoEnQxqHz+2rsM1WzKhJ2mSritnhjvScDuIqfXWzQLsz5C5Q2JTSt2HU5x2jqPdiqLt8iRZLtFusZGXo69rB5pPtJPYRkeIroO3yGblb2J0NW1HfQFoPYfx66CqLh0e3jS843no/uDqFJ3qhLWDtAcgTuWOxXvqV6F6UId7fFpv7Jtd6SdlTToKUOK7NreD+qfCpcU5zs43cc1X/SzpVm8WNVxQ3szIRDhdaQCtbQ9scd+BvHaMc6C2EnIzv8a9qj9Pa7vOilxoGrdq4WR5KTDurWV5QRkb/lDHI7x2jFXJarjDusNEy3yW5EdwZSttWRQLKKKKAooooIXrPQ7WqZrEqRPeZDCClDSANntO8cahr/AEOKSgJjXYLVx/ObifcKs+1wJTBkuzH23H3nM+oFY2RuTxJxuGTjdnPHjSlwPN7y3kdaTmgg9hutj0bDas2yyJbSR5wovtIccc5nC1BRGc47KeRrKM6seTjSV9QSgL/yk1n6f8pqJFtQ3GMbySi4tayl5Dg3hOwUjdjnk0vlRYLyCH4cR1HD1mQofdvoKz6TYsW/xEv2u2yE3VhfrJ80LZebxvByN+DgjxqDW2yXd6UiKi2yfLL+Spojf2k1YV10at29sP6euD1rbzl1lHrNY7E53fd1VYcFfm4bbIO1sjJO7a7c0Cq0tPxrVHblkLkNtJDmyPaVjfSb0HaHFlxMZhLrhypbYCSo9Zxzp2QcjNerxjfwoIrI0LYnnVumGhTiztElRyftpOvQmn0j85CI6yFLA/zYre9qIG8ybbsQm3mV7AakvKZLgIylQVgg5HIA8KcF3RUNO1cGZkdI3KcLQebPbtIyUjtUBQR1fR1pRZ2jbWFE8yFHPjtUoa0ZZGEhLDKW0jgEqcwP/wBVI4sqFcW9uK9HkoPy4zoV91bPM0HcCRjrG+gYmtOW5v8ARKDuVlKjjx2qVogIjxlxoj3k2F52klOQc7j76cvMhyOaDBoIq9ou0ut7S2GCO5QH31q/Ie1bKWgXEIQfVbRLfSlPgFYFS8QyneDivTDSvfwPZwNBAE9H1miSzIix5Tcgq2vKsTXgrPX7VPkdiVGGwt2e+g5ymQPKZ8SM1IPMVD5VBhLxhLmFcqCGPabty9NL088l9UHBSnaOVt5VkbJI5ctxxupv0vo1rS0vy1lvVyaQpWXGHFIW2vvGyPfU6W0+jIV40nMdKc5YbV1nFAsYvIG59Oesp5U4sSWnxtNKB6xzFRxSWM/xZHco14hLaVhTbryFDgQRuoJUK9pnYuiklKXk7aBxdSN47SKW+kYX9pa+tQD0xllWyVEnmByrUu4MlOPW3nFRJ255VnOPxrwXDJ45oJmhcVThX+b21AAqKcEgcMnnWL0CM9khOyT8pBxUWbuFKG7kpJGyop7jQOSrS6xtrZcQ7lJ3LTsn3/GvXk7De1JT5LHNXI0nVelpZySheCncRx3iq86TtevW5ltEQI88dylkYyEDmrHM8hQWvAmx3mwhLqCtPGspEgIOyBvrnzRWv7w3cW2r2sradP5uSWwktqPJWABsn7M1cjMoyWw4kgJI4UDHr21NTEJuCiAQjyb5PJHFK/onj2FVQGXe51oCY1ruNxjvA7K2dpKm0kbsAHcR7uNW2pQPqhI9biOumaV0fQJb5kRUoSo5Cml5AA/VIOR3bxyGAKCK2i9TXm0ibBgqlbQKZYa2HknO45HHup9XrV5orRcbWVpCiA9CdIUPoHn2UvZtsazJkImW19ZeRsFxaishOBwIBSPfUamNtuqyxJZceQcZJyo94STQSCw6qhT5pjJ1CY6jwZmMlpY7z7J7s5qZJjXEIBRcGnMjcFM4B+2qOvNqellJKNlad4Wlp3I7vV3HxrXZtZXzSchLLj5cjFWEsSuCh2jijv8AeDQWyvWUJiW/FevthbeYWW3EyJYbIUOI39R3Utj6h8uMsSbPISeBYnJUKovpAtkW9uStT2NlSFbl3W3up/OxVn+VA+UhX6Q3Z791ekI+UyRnkM0HYaJ89QyiChwfqyEfGsxMuPO0L8JCPjXHH5vOPJK99b2pCW9yVSU/Mex+FB2AZU9XGzuft2/jWpS5pOfRLg/x2/jXJybkAMGXch3SiP8ATWfpJPDzy5/8Wf3aDqR1matRPot0f47fxrStmQ36zzKWE/pOyEAffXMCpUVzc6q4OJ57Ugn/AE1gV2wAhuCtSuW2s/EUHUVpmW6XNXCi3C3SZTaStbLEkOqSngSUjtIHjTp5Nj+zx/2Y+Nc79FUp236kkXFMUNpiW6Q9sJT7eAAE9Zyop69+K1fljqz++pP7N392gsU7XEcOygOqrKw6jjQ2mlT4wkQJCUuJWkZU3tDO7rG/NS5m2WC9xfOLXIQocCptWdknkocR40ETS+pNZecq3U7XHS0yJlTBDyBvOzxFMSklKilYIUOIPEUClyatTeznGarW7IevuqHvR7QfdbSloOlOUMpHM9pO1Ur1PONuskh9CtlwgIQe07qb9HzYulm2VXE7LE7+DyljmXBuB6gkYJNA2qs0ZpiWqTqOSl6GlKn/ACbYLbZUoJAxz38s1NNK3XzuzsOIlIkKAwXU59ZQ47jvB57+uq9es8q0o1dZ5qlLd2WnUOng6hK9oLHWCMf9ipRpRESDFbhxGvJuqYblOJyTvUBnn1YHeDQTuPcF7Q8phWOs1IYN5YbHroX3jfUBLytoqFO1sUqUoIzsg86CUSrjEkLGxIQDkblnZP3V4v0fNGxIjNyd+4qDbuR1YyfuprmPWCCkC53SO26PkLdSFe6kbb+mZn8ROa38CHEn8aB7RpHTklkLcskYZ5BrY+wUqt+lLBbllcKzxGVkfxiWxte/jUf9FRyMxJ+Oo5KR7zurU+xeIaPKIkyFNj5TbxUPsoN+stLGQtN0tjiY10Zz5J4jKXBje04PlII3EVRGqLOptT062sLjNtqAmQVn1oK+W/m2o+yrhwB5VcL12nlGHJLy0cdlZyKa50dietLslrLyMhDrZUhwZ6lJIOPGgo7aeOCC2d3HIrNJmcktq+imrgc03aXVZXDRntSDn3jfwoRpOzq/mbf7Fn9ygqRBncozf7JPwraDcP7K39RA/CrbGkLMf5m3+xZ/5denR9mx/wCzR4Ms/wDLoKoSuePkRR84t/CslyLgpBT51GZ3cUSUJ+5VWedJWdBymIkfRQPuTWYsNvbI2I+zjmlRT9oIoGDozjOByfKeWXlOqZjtvFRVtYJdXgniB5NoH5wqxfKq/rF+4fCmVhpMY7TW1n2fKLWpxWDxGVE1s86c7aBh0Y/Au+n4cVL0dqU2yG9lclKFLIyNyV4zw5Gtk/T92tzwlQ3HWHh7DqVFlR8fZI7lGqZyTuJ3dXKrS6G9P3fULVyXC1BcLWzFKEoDCtptalBWQpBODgAe+gf4fSJqiy7KLvFTKa4BTyC0s9yhuPup/a1npzUTQTLjSYEo7gvZChnvHwFan9Ka4gghmRZbq3jfltURxfZhHq++mCTEuEI7V20VNYIVvdhJS6B25a/FJoEmv4+RaIrLzbzcmckDY37QxjeD86lepZ+mrwuNatRNrtT8V5QiyY6AWl4IGVoIxv2eymPUN1trsiyuRpayuNcW1uMvJwttI3qJ3J6v0alOv2NJRrhFn3hmS8UqU21HZy2h1e8nJHrHj1jjQhG5HQ5Cj2dM6FebsplSYDidtKixtA4UeHLHE8M1n6DZh6g9KSrg2yZaFxY8BKSTkE7WVHGMbPbT7oifIlsWz0faoFqtzrqyGFDYWWAn20gZJJURxON2eYwj1Uxa71frc09cGIGo7YUuqZIJbkoVhRSFfKVjdke7hiRa0qzjeMY7eFJbve12e0yJLRSHdnYa2lBPrnhvO7r8M0vfbSXVbsYVw+2ohr+2XC5xojVuZ8slDiluJCgDnA2SM/SqoidvYfdkOyZLuXnQStakF4nh+iD21udt4TEYWtVuCVuYSHE7C8/rZGcHv501nTl8Zwr0bKB60JJ+6trEbUbKtpuNdUj/AHbpH3UDyzbbomVLRbZDOWEFZMS4YSjcD6uFAE7+G/gaVtah1laI7Excl0xnM+TU/srSog4OydyuY99R0jUWMORp6x+iuKVA+BBrWUXROT6IKVf/AEcfcmgsS0dIVruaQm8p8xk814yhXj8af27rp57Cm73D38tsDFUquNNcO05aFlXYytNYKgSTj/0mQPoL+FBfTMmzK/pSOf8AEHxpYh+zY/8Ak4/1hXPKbfJ/uiUruQv4VtFskq/oSee5K/3aDoYSLN/ekcfSFCpNlA33WN4rFc+JtMk/0BcleC/3K2ItEs+zp2Yfn7Y/CgvV656eR7V5ho73Bv8Atpvfv2l0e1fYg7l5qnvyfuah6unXB9JXxr0aavavYsqU/OWPxNBZ72rNKMnPpYL7GmlKNJ/y40f/AG2b/wAPVdI0lqBR3wGkdpWjH2Gt35IX/wDRb/bpoMnOjnUrPtQkHqKXQal2mZOtdJWZMG125pplai64tRCitZ3E+4AeFW6tjcRS23CO0y43IxgKyMjPGgpeRr7XLZPlFhHckfCm57pH1gPanKT80D4VeEu12ScrZWyCTz2cD31HrpoKzvpKmX2mz1FQNBSl+1Ver7DMa6yC+yVBQChvSRzFWqI9t6QdDWebMO1KjPttuoT8pxPqqQeeFDB7jnlTNdujtDW0tqQyvqAVv8Kj1ouc/o8viXlM+d2x9Q8qwrOznrBPBQycHnv7wCuNqB6Sda3V5ZR5pCFvipSceTS65sEpxwO7P/ijUaI9+macvjTbT/lWUMuhR9RTrR9YLPIFPPqSqnK4L0PeGLo9Bvfo9N12FSmpDSgpCkHaGAAc7+rqzUMduca12h+xWGXIkRpCgqVKeR5ML/VQjilOOJJyeGACcg+S+kyMqS4o2ZCWyohBaVsbSeRxuxuxurFHSJZV/wAfapOP1HCf9dV2/hSgEklI4ZrVs0FoJ6QdNj+jLgkeH79bP9oOmz/M53geH21WDRCEOApSoKTjeN6TniO38M1pzzPHvoLW/L/Tf9TOH0x+7Xo19po8UTk96/8AoqqkLKeHOtyX1D/xQWcrXmmsbvPvBf8A0Umf6Q7KgfmY1wWf94gf6agLVwWg7v8ALTjG1HLjkbD5T3Cge3OkVKlYjWt1fz39/wBia2I1pdnceR08459dX3CtUPpBucfGJSsd1P8AC6XJrO5xSlD5tBotNx1feJSY8DSa9sjO26lxCE96lYH20yXDXF3t812JLtMePIZUUuNueUCkntwqp7F6Z44x5w2vI6k8ajevtQ6S1i0iTtvQrqhOyl8M7SXB1LH48snjQNI1Xd3Ijkpv0RhA2igLeKgO7apInW9zdjPrL8BhxGChhUdai53HeO3eRUQdb2VkZScHGQeNeoRz3+FBJm9eXtKxlENzG7BioP24NKv9oN4/sMP9gn4U0WDT8+9SwxDSwhR4qkPJaSB4nf4A1M/9j1y/vuy/XV8KC9xHJQCBmsfNSeIIpzTuSBjNB38sUDUqKRwAPdWhcY8xinspzyB7xWJbB4hQ8aCPuQwoYOfCmi6aZYuMZbDxVsL4p2Qc++pkuMkAq3eFDUZB9ZXCgpGZ0Pq2yqHdi2g8EOx848QoU2yOie8JH5q5RljtbUn410CoN4VhrcOBrSY6CNoDOaDnF7ouvrWT5aOv5qjSB7QN7Z9tsHuNdMmMg8U1iYbSv5MHvFBy25pO6N7iyT3VoVp2eniyoeFdSqtkU+0yg5601gbNDPFhv6ooOWFWSYOLSvdWHoqUOLSvdXUx09bVfzds/RrH8m7af5s39Wg5b9GSR/JK+rWQtsjmyo+FdRfkxbOcZv6tejTFs5Rm/q0HMKbY8eLS09wpQ3Y3lncMeFdLjTduTwjN/Vr0aegDhGb+rQc6s6TnOewyeGcgVpOn5pVsoYVgHGdnjXSQs0RHsx0DuTW+PbIaCStlIPL1aDm5nS1xWd0dR+jTlG0ncsj+DqHhXQSYccYSpv1N/qgYz31kGGtgoLYPUf0aCloOlbmhaSGyn76d/Ql9/rl1aIjpAA2eHOvfIJ/RoHUpzivNisxQaDUU1icp4VuIo2QeNAncJKcGsnFbOwDw51k8ACjHXWLivzgSRuUaDAJxtpHDGRQo7KUo6xmtyUkHAO4GsVMhSiSc0CYjG6iti0AcKxxQY14ayooMRXte0UHlFe0UHlFe0UGJoFZUYzQeYoxWWyDWWzgUGvFGK2ISCrFbfJCg/9k='

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
car1.image(st.session_state.get(f'selected_image_0'))
car2.image(st.session_state.get(f'selected_image_1'))
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
