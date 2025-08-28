from bs4 import BeautifulSoup


from urllib import request


weather_url = "https://www.kma.go.kr/repositary/xml/fct/mon/img/fct_mon1rss_108_20250828.xml"


request.urlopen(weather_url)
data = request.urlopen(weather_url)


with request.urlopen(weather_url) as response:
 soup = BeautifulSoup(response,"xml")


for loc in soup.select("local_ta"):
    city = loc.select_one("local_ta_name").get_text(strip=True)
    print(f"\n[{city}]")

    # 1~4주차를 규칙적으로 뽑기
    for i in range(1, 5):
        base = f"week{i}_local_ta_"
        normal = loc.select_one(base + "normalYear").get_text(strip=True)
        rng    = loc.select_one(base + "similarRange").get_text(strip=True)
        minv   = loc.select_one(base + "minVal").get_text(strip=True)
        maxv   = loc.select_one(base + "maxVal").get_text(strip=True)
        sim    = loc.select_one(base + "similarVal").get_text(strip=True)

        print(f"  {i}주차 | 평년 {normal}℃ | 범위 {rng}℃ | 최저 {minv}℃ | 최고 {maxv}℃ | 유사사례 {sim}")