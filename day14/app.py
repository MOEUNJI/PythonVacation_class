from flask import Flask
from bs4 import BeautifulSoup
from urllib import request

app = Flask(__name__)
WEATHER_URL = "https://www.kma.go.kr/repositary/xml/fct/mon/img/fct_mon1rss_108_20250828.xml"

@app.route("/")
def hello():
    # 1) XML 불러오기/파싱
    with request.urlopen(WEATHER_URL) as resp:
        soup = BeautifulSoup(resp.read(), "xml")  # resp 자체가 아니라 .read()

    # 2) 화면에 보낼 HTML 만들기
    html = ["<h1>월간 기온 전망</h1>"]

    for loc in soup.select("local_ta"):
        city = loc.select_one("local_ta_name").get_text(strip=True)
        html.append(f"<h2>{city}</h2><ul>")

        for i in range(1, 5):
            base = f"week{i}_local_ta_"
            normal = loc.select_one(base + "normalYear").get_text(strip=True)
            rng    = loc.select_one(base + "similarRange").get_text(strip=True)
            minv   = loc.select_one(base + "minVal").get_text(strip=True)
            maxv   = loc.select_one(base + "maxVal").get_text(strip=True)
            sim    = loc.select_one(base + "similarVal").get_text(strip=True)

            html.append(
                f"<li>{i}주차 | 평년 {normal}℃ | 범위 {rng}℃ | "
                f"최저 {minv}℃ | 최고 {maxv}℃ | 유사사례 {sim}</li>"
            )
        html.append("</ul>")

    # 3) 루프 모두 끝난 뒤 반환
    return "\n".join(html)

@app.route("/setting")
def setting():
    return "<h1>설정창으로 들어왔어요</h1>"

if __name__ == "__main__":
    app.run(debug=True)
