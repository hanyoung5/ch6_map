# 🚇 부산 지하철 역별 이용객 수 지도 분석 앱

Streamlit과 Folium을 활용하여 부산 지하철 역별 이용객 수 데이터를 지도 위에 직관적으로 시각화하는 웹 애플리케이션입니다.

---

## 📌 주요 기능

1. **데이터 업로드 및 조회**
   * 부산 지하철 역별 이용객 수 CSV 파일 (`busan_subway.csv`) 업로드
   * 업로드된 데이터 테이블 형식으로 미리보기 지원

2. **호선 필터링 (Multiselect)**
   * 원하는 호선(1호선~4호선)만 선택하여 지도 및 통계 데이터 필터링

3. **인터랙티브 지도 시각화 (Folium)**
   * **원 크기 시각화**: 이용객 수의 제곱근($\sqrt{N}$)에 비례하도록 원(CircleMarker)의 크기를 조절하여 면적 비율 반영
   * **호선별 색상 구분**:
     * 🟠 1호선: 주황색
     * 🟢 2호선: 초록색
     * 🟤 3호선: 갈색
     * 🔵 4호선: 파랑색
   * **툴팁 & 팝업**: 마우스를 올리면 역명 표시, 원을 클릭하면 상세 이용객 수 출력

4. **상위 5개 역 정보 제공**
   * 선택된 필터 기준 이용객 수가 가장 많은 상위 5개 역을 순위표로 제공

---

## 🛠️ 기술 스택 (Tech Stack)

* **Language:** Python
* **Web Framework:** Streamlit
* **Data Manipulation:** Pandas, NumPy
* **Map Visualization:** Folium, Streamlit-Folium

---

## 🚀 실행 방법 (Local Execution)

### 1. 저장소 클론 (Clone Repository)
```bash
git clone https://github.com/사용자이름/저장소이름.git
cd 저장소이름
```

### 2. 패키지 설치 (Install Dependencies)
```bash
pip install -r requirements.txt
```

### 3. 앱 실행 (Run App)
```bash
streamlit run app.py
```

---

## 📂 CSV 데이터 형식 (`busan_subway.csv`)

업로드할 CSV 파일은 아래와 같은 열(Column) 구성을 가져야 합니다:

| 호선 | 역명 | 위도 | 경도 | 이용객수 |
|---|---|---|---|---|
| 1호선 | 서면 | 35.1577 | 129.0591 | 65000 |
| 2호선 | 해운대 | 35.1631 | 129.1636 | 32000 |
