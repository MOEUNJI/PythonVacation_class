'''
무한 반복하는 반복문을 만들어 커피를 뽑는 자판기를 만들것이다.
사용자에게 돈을 받는다 ( 초기 입력 : 300원 이상 )
사용자가 돈을 넣으면 커피를 몇잔 뽑겠냐고 물어볼것이다.
커피는 한 잔에 300원이다. 만약 사용자가 1000원을 넣었다면
최대 3잔 뽑을 수 있음을 알려주고 그 범위 안에서 잔 수를 입력받는다.
만약 사용자가 300원 이하의 금액을 투입했다면 300원 이상 넣어달라는 문구를 추가한다
사용자가 선택한 잔 수만큼 가격을 차감하여 거스름돈을 출력한다.
만약 남은 거스름돈이 커피를 더 뽑을 수 있는 금액이라면
더 뽑으시겠습니까? (예 : 1 / 아니오 : 0)으로 구분하여
뽑겠다고 하면 몇잔을 뽑으시겠습니까? 최대 *잔 가능 출력
아니오를 선택했다면 잔돈을 돌려주기
만약 거스름돈이 커피를 더 뽑을 수 없는 금액이라면
잔돈이 부족합니다. 추가 투입 하시겠습니까? 출력
1 : 예 / 0 : 아니오 로 구분하여
추가 투입을 선택했다면 얼마를 투입할것이냐 물어보기
0을 선택했다면 자판기 종료 후 잔돈 돌려주기

'''
while True:  # 전체 자판기 루프 (손님 한 명 시작)
    money = int(input("돈을 넣어주세요 (300원 이상) : "))
    if money < 300:
        print("300원 이상 넣어주세요!")
        continue

    coffee_price = 300

    while True:  # ← 구매/추가투입 루프 (money 유지)
        max_coffee = money // coffee_price

        # 수량 입력 검증 루프
        while True:
            coffee_count = int(input(f"몇 잔을 뽑으시겠습니까? 최대 {max_coffee}잔 가능 : "))
            if 1 <= coffee_count <= max_coffee:
                break
            print(f"1~{max_coffee} 사이로 입력해주세요")

        money -= coffee_price * coffee_count
        print(f"커피{coffee_count} 잔을 뽑았습니다. 남은 잔돈 : {money}원")

        if money < coffee_price:
            choice = input("잔돈이 부족합니다. 추가 투입 하시겠습니까? (1 : 예 / 0 : 아니오 ) : ")
            if choice == '1':
                add_money = int(input("얼마를 투입하시겠습니까? "))
                money += add_money
                # 이 continue는 '구매/추가투입 루프'로 돌아감
                continue
            elif choice == '0':
                if money > 0:
                    print(f"자판기에 잔돈{money}원을 돌려드립니다. 코드를 종료합니다.")
                else:
                    print("자판기를 종료합니다.")
                break  # 구매/추가투입 루프 종료
            else:
                print("잘못된 입력입니다. 자판기를 종료합니다.")
                break  # 구매/추가투입 루프 종료

        # 돈이 300원 이상 남아 있으면 더 살지 물어볼 수도 있음 (선택)
        more = input("더 뽑으시겠습니까? (1: 예 / 0: 아니오) : ")
        if more != '1':
            if money > 0:
                print(f"잔돈 {money}원을 돌려드립니다.")
            break  # 구매/추가투입 루프 종료

    break  # 전체 자판기 루프 종료 (필요에 따라 계속 돌리고 싶으면 제거)
