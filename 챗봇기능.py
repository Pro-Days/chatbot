import time
import random
from selenium import webdriver

global driver

# selenium 모듈 install 필요
# 컴퓨터 크롬 버전과 맞는 크롬드라이버 필요
options = webdriver.ChromeOptions()
options.add_argument('headless')

driver = webdriver.Chrome('chromedriver.exe', options=options)


# 초기상태: 반복 True
loop = True


# 오류(잘못된 입력)시 작동 함수
def error_code(error="잘못된 입력"):
    print(f"\n잘못된 입력입니다. ({error})")


# 사칙연산에서 사용되는 공통함수
def add_num(msg):
    cmd = []
    a = True
    while a:
        input_msg = input(msg)
        try:
            cmd.append(float(input_msg))
        except:
            if input_msg == "종료":
                a = False
            else:
                error_code("실수를 입력해주세요.")
    return cmd


# float 변수를 int로 변환시키는 함수
def f_to_i(sum):
    if type(sum).__name__ == "float" and sum.is_integer():
        sum = int(sum)
    return sum


# 더하기 함수
def plus():
    sum = 0
    cmd = add_num('\n더할 숫자를 입력하세요 (종료하려면 "종료"를 입력하세요.): ')
    if len(cmd) == 0:
        error_code("숫자가 입력되지 않았습니다.")
    else:
        print()
        for i in range(len(cmd)):
            cmd[i] = f_to_i(cmd[i])
            sum += cmd[i]
            print(f"{cmd[i]}", end=" ")
            if (i + 1) != len(cmd):
                print("+", end=" ")
        sum = f_to_i(sum)
        print(f"= {round(sum, 5)}")


# 빼기 함수
def minus():
    try:
        sum = float(input("\n처음 숫자를 입력하세요: "))
    except:
        error_code("실수를 입력해주세요.")
    else:
        cmd = add_num('\n뺄 숫자를 입력하세요 (종료하려면 "종료"를 입력하세요.): ')
        print()
        sum = f_to_i(sum)
        print(str(sum)+" ", end="")
        for i in range(len(cmd)):
            cmd[i] = f_to_i(cmd[i])
            sum -= cmd[i]
            print(f"- {cmd[i]} ", end=" ")

            # if (i + 1) != len(cmd):
            #     print("-", end=" ")
        sum = f_to_i(sum)
        print(f"= {round(sum, 5)}")


# 곱하기 함수
def multiply():
    result = 1
    cmd = add_num('\n곱할 숫자를 입력하세요 (종료하려면 "종료"를 입력하세요.): ')
    if len(cmd) == 0:
        error_code("숫자가 입력되지 않았습니다.")
    else:
        print()
        for i in range(len(cmd)):
            cmd[i] = f_to_i(cmd[i])
            result *= cmd[i]
            print(f"{cmd[i]}", end=" ")
            if (i + 1) != len(cmd):
                print("x", end=" ")
        result = f_to_i(result)
        print(f"= {round(result, 5)}")


# 나누기 함수
def divide():
    a = True
    cmd = []
    try:
        result = float(input("\n처음 숫자를 입력하세요: "))
    except:
        error_code("실수를 입력해주세요.")
    else:
        while a:
            input_msg = input('\n나눌 숫자를 입력하세요 (종료하려면 "종료"를 입력하세요.): ')
            try:
                if input_msg == "0":
                    error_code("0으로는 나눌 수 없습니다.")
                else:
                    cmd.append(float(input_msg))
            except:
                if input_msg == "종료":
                    a = False
                else:
                    error_code("실수를 입력해주세요.")
        print()
        result = f_to_i(result)
        print(str(result) + " ", end="")
        for i in range(len(cmd)):
            cmd[i] = f_to_i(cmd[i])
            result /= cmd[i]
            print(f"÷ {cmd[i]}", end=" ")
        result = f_to_i(result)
        print(f"= {round(result, 5)}")


# 날짜 함수
def date():
    print()
    print("현재 시각은 " + time.strftime('%Y-%m-%d  %H:%M:%S',
          time.localtime(time.time())) + " 입니다.")


# 인사 함수
def hello():
    hello_world = ["안녕하세요!", "안녕~", "반가워요!", "정말 반가워요!",
                   "좋은 하루 되세요!", "오랜만이에요! 반갑습니다"]
    print()

    # 랜덤 체크
    # l0 = l1 = l2 = l3 = l4 = l5 = 0
    # for i in range(1000):
    #     hi = random.choice(hello_world)
    #     if hi == hello_world[0]:
    #         l0 += 1
    #     elif hi == hello_world[1]:
    #         l1 += 1
    #     elif hi == hello_world[2]:
    #         l2 += 1
    #     elif hi == hello_world[3]:
    #         l3 += 1
    #     elif hi == hello_world[4]:
    #         l4 += 1
    #     elif hi == hello_world[5]:
    #         l5 += 1
    # print(l0, l1, l2, l3, l4, l5)
    ##
    print(random.choice(hello_world))


# 평균 함수
def average():
    result = 0
    cmd = add_num('\n평균을 구할 숫자를 입력하세요 (종료하려면 "종료"를 입력하세요.): ')
    if len(cmd) == 0:
        error_code("숫자가 입력되지 않았습니다.")
    else:
        print()
        for i in range(len(cmd)):
            cmd[i] = f_to_i(cmd[i])
            result += cmd[i]
            print(f"{cmd[i]}", end="")
            if (i + 1) != len(cmd):
                print(",", end=" ")
        result = result/len(cmd)
        result = f_to_i(result)
        print(f"의 평균 = {round(result, 5)}")


# 날씨 함수
def weather():
    region = input("\n지역을 입력해주십시오.  ")
    driver.get(f'https://www.google.com/search?q={region} 날씨')
    try:
        tem = driver.find_element_by_xpath('//*[@id="wob_tm"]').text
        gg = driver.find_element_by_xpath(
            '//*[@id="wob_wc"]/div[1]/div[2]/div[1]').text
        ss = driver.find_element_by_xpath(
            '//*[@id="wob_wc"]/div[1]/div[2]/div[2]').text
        pp = driver.find_element_by_xpath(
            '//*[@id="wob_wc"]/div[1]/div[2]/div[3]').text
    except:
        error_code("해당 지역의 날씨를 불러올 수 없습니다.")
    else:
        print()
        print(f"{region} 날씨: \n기온: {tem}\n{gg}\n{ss}\n{pp}")


# 네이버 검색 함수
def naver_search():
    word = input("\n검색어를 입력해주십시오.  ")
    driver.get(f'https://search.naver.com/search.naver?query={word}')
    titles = driver.find_elements_by_css_selector(
        'section.sp_ntotal a.link_tit')
    num = 1
    print()
    for i in titles:
        text = i.get_property('textContent')
        url = i.get_attribute('href')
        print(f'{num}. 제목 : {text}\n링크 : {url}\n')
        num += 1


# 구글 검색 함수
def google_search():
    word = input("\n검색어를 입력해주십시오.  ")
    driver.get(f'https://www.google.com/search?q={word}')
    titles = driver.find_elements_by_xpath(
        '//*[@id="rso"]/div/div/div[1]/div/a')
    num = 1
    print()
    for i in titles:
        text = i.get_property('textContent').split("http")[0]
        url = i.get_attribute('href')
        print(f'{num}. 제목 : {text}\n링크 : {url}\n')
        num += 1


# 사각형 그리기 함수
def draw():
    try:
        a = int(input("\n한 변의 길이가 몇인가요? "))
    except:
        error_code("자연수를 입력해주세요.")
    else:
        if a <= 0:
            error_code("자연수를 입력해주세요.")
        else:
            print()
            print("*"*a)
            for i in range(a-2):
                print("*" + " "*(a-2) + "*")
            print("*"*a)


# 업다운 게임 함수
def updown():
    coin = 6
    ans = random.randint(1, 100)
    while coin >= 1:
        try:
            num = int(input("\n숫자를 입력하세요(1~100)"))
        except:
            error_code("정수를 입력해주세요.")
        else:
            if 1 <= num <= 100:
                if num == ans:
                    print("\n정답!")
                    coin = -1
                elif num > ans:
                    print("\n다운!")
                else:
                    print("\n업!")
                coin -= 1
                if coin == 0:
                    print("\n실패! 정답: " + str(ans))


print("\n"*50)


# 루프 시작
#loop = True
while loop:
    msg = input("\n명령어를 입력하세요: ")

    if msg == "더하기":
        plus()

    elif msg == "빼기":
        minus()

    elif msg == "곱하기":
        multiply()

    elif msg == "나누기":
        divide()

    elif msg == "평균":
        average()

    elif msg == "사각형":
        draw()

    elif msg == "날짜" or msg == "시간":
        date()

    elif msg == "인사" or msg == "안녕":
        hello()

# 셀레니움 필요
    elif msg == "검색":
        engine = input("\n구글 / 네이버 중 검색엔진을 선택해주세요. ")
        if engine == "구글":
            google_search()
        if engine == "네이버":
            naver_search()

    elif msg == "날씨":
        weather()
# 셀레니움 필요

    elif msg == "업다운게임":
        updown()

    # elif msg == "끝말잇기":
    #     pass

    elif msg == "명령어" or msg == "도움말":
        print("""\n  ----명령어----

    더하기
    빼기
    곱하기
    나누기
    평균
    사각형
    날짜, 시간
    인사, 안녕
    검색
    날씨
    업다운게임
    명령어
    종료""")

    elif msg == "종료":
        loop = False
        print("이용해주셔서 감사합니다.")
        driver.quit()

    else:
        error_code()


# def interpret_msg(msg):
#     msg.split()
#     msg = msg[0]
#     msg_factor = msg[1:]
#     return msg, msg_factor
