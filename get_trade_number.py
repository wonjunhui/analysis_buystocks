from bs4 import BeautifulSoup
import requests
import time
# soup = BeautifulSoup()
# web_url = 'http://finance.daum.net/domestic/market_cap?view=pc'
web_url = 'https://finance.naver.com/sise/sise_market_sum.nhn'

r = requests.get(web_url)
# print(r.text)
soup = BeautifulSoup(r.text, 'html.parser')
all_divs = soup.find("tbody")
# title = all_divs.find_all("td > a")
# print(title)
# print(all_divs.find_all('a'))
for modi_text in all_divs.find_all('a'):
    # print(modi_text.attrs['href'])
    if 'main' in modi_text.attrs['href']:
        print(modi_text.attrs['href'].split('code=')[1])
    # print(modi_text.attrs['href'])
# print(soup.find_all('a', attrs={'class':'title'}))
# tag = bs.find('div', attrs={'class': 'tit3'})


# 삼성전자
# SK하이닉스
# 삼성바이오로직스
# NAVER
# 셀트리온
# 삼성전자우
# LG화학
# 삼성SDI
# 카카오
# 삼성물산
# 현대차
# LG생활건강
# 엔씨소프트
# SK
# 현대모비스
# SK텔레콤
# POSCO
# KB금융
# 신한지주
# 삼성에스디에스
# 기아차
# LG
# 한국전력
# SK이노베이션
# LG전자
# KT&G
# 삼성전기
# 삼성생명
# 아모레퍼시픽
# 삼성화재
# 넷마블
# 하나금융지주
# S-Oil
# 우리금융지주
# 고려아연
# 한국조선해양
# KT
# 롯데케미칼
# 기업은행
# 코웨이
# 오리온
# LG유플러스
# CJ제일제당
# 한온시스템
# 한진칼
# KODEX 200
# 포스코케미칼
# 강원랜드
# 미래에셋대우
# LG디스플레이



# 005930
# 000660
# 207940
# 035420
# 068270
# 005935
# 051910
# 006400
# 035720
# 028260
# 005380
# 051900
# 036570
# 034730
# 012330
# 017670
# 005490
# 105560
# 055550
# 018260
# 000270
# 003550
# 015760
# 096770
# 066570
# 033780
# 009150
# 032830
# 090430
# 000810
# 251270
# 086790
# 010950
# 316140
# 010130
# 009540
# 030200
# 011170
# 024110
# 021240
# 271560
# 032640
# 097950
# 018880
# 180640
# 069500
# 003670
# 035250
# 006800
# 034220
