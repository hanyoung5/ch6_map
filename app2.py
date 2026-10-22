import numpy as np
import pandas as pd
import streamlit as st
import folium
from streamlit_folium import st_folium

# 호선별 색상 지정 딕셔너리 (Folium 지원 색상명)
LINE_COLORS = {
    '1호선': 'orange',  # 주황
    '2호선': 'green',  # 초록
    '3호선': 'brown',  # 갈색
    '4호선': 'blue'  # 파랑
}

# 1. 페이지 제목 설정
st.title("🚇 부산 지하철 역별 이용객 수 지도 분석")
st.write("CSV 파일을 업로드하면 지도 위에 이용객 수를 원 크기로 보여줍니다.")

# 2. CSV 파일 업로드
uploaded_file = st.file_uploader("busan_subway.csv 파일을 업로드하세요", type=["csv"])

if uploaded_file is not None:
    # 데이터 불러오기
    df = pd.read_csv(uploaded_file)

    # 3. 호선 선택 필터 (multiselect)
    all_lines = list(df['호선'].unique())
    selected_lines = st.multiselect(
        "조회할 호선을 선택하세요:",
        options=all_lines,
        default=all_lines  # 기본값: 전체 호선 선택
    )

    # 선택된 호선만 필터링
    filtered_df = df[df['호선'].isin(selected_lines)]

    # 데이터 미리보기 표시
    st.subheader("📊 데이터 미리보기")
    st.dataframe(filtered_df.head())

    # 4. 부산 중심 좌표로 기본 지도 생성
    m = folium.Map(location=[35.17955, 129.07564], zoom_start=11)

    # 5. 필터링된 역 데이터를 지도에 CircleMarker로 표시
    for index, row in filtered_df.iterrows():
        # 원 면적이 이용객수에 비례하도록 제곱근(sqrt) 처리
        radius_size = np.sqrt(row['이용객수']) * 0.05

        # 호선별 지정된 색상 가져오기 (없으면 기본 gray)
        marker_color = LINE_COLORS.get(row['호선'], 'gray')

        folium.CircleMarker(
            location=[row['위도'], row['경도']],
            radius=radius_size,
            color=marker_color,  # 호선별 테두리 색상
            fill=True,
            fill_color=marker_color,  # 호선별 채우기 색상
            fill_opacity=0.6,
            tooltip=f"[{row['호선']}] {row['역명']}",  # 마우스 올렸을 때 역명
            popup=f"{row['역명']}: {row['이용객수']:,}명"  # 클릭했을 때 이용객 수
        ).add_to(m)

    # 6. Streamlit 화면에 Folium 지도 출력
    st.subheader("🗺️ 역별 이용객 수 지도")
    st_folium(m, width=700, height=500)

    # 7. 이용객 수 상위 5개 역 표로 표시
    st.subheader("🏆 이용객 수 상위 5개 역")
    top5_df = filtered_df.sort_values(by='이용객수', ascending=False).head(5)
    st.table(top5_df[['호선', '역명', '이용객수']].reset_index(drop=True))

else:
    st.info("상단의 상자를 클릭하여 CSV 파일을 먼저 업로드해 주세요.")