# 딕셔너리를 이용한 커피 메뉴 만들기
menu_dic = {
    "Americano": ["Coffee", 2000, "기본 커피 입니다."],
    "Esspresso": ["Coffee", 2500, "진한 커피 입니다."],
    "Latte": ["Coffee", 4000, "우유가 들어 있는 커피 입니다."],
    "ColdBrew": ["Coffee", 4500, "연유가 들어 있는 커피 입니다."],
    "GreenTea": ["Tea", 4500, "녹차 입니다."],
    "BlackTea": ["Tea", 4500, "홍차 입니다."],
    "MlilTea" : ["Tea", 4000, "우유가 포함된 차 입니다."],
    "PeachAde": ["Ade", 5000, "복숭아 에이드 입니다."],
    "GreenAde": ["Ade", 5000, "포도 에이드 입니다."],
    "LemonAde": ["Ade", 4500, "레몬 에이드 입니다."]
}
while True:
    print("메뉴를 선택하세요. : ")
    menu =int(input("[1] 메뉴 보기, [2] 메뉴 조회, [3] 추가 하기, [4] 삭제 하기, [5] 종료 하기 : "))
    if menu == 1:
        for key in menu_dic: # key의 개수만큼 자동순회
            print(key, ":", menu_dic[key]) # 키와 키에 해당하는 값을 출력
    elif menu == 2:
        read_name = input("조회할 메뉴 입력하세요. : ")
        if read_name in menu_dic:
            print(menu_dic[read_name])
        else: print("찾는 메뉴가 존재하지 않습니다.")
    elif menu == 3:
        add_name = input("추가할 메뉴를 입력하세요. : ")
        if add_name not in menu_dic:
            cate = input("카테고리를 입력하세요. : ")
            price = int(input("가격을 입력하세요. : "))
            desc = input("메뉴 설명을 입력하세요. : ")
            menu_dic[add_name] = [cate, price, desc] # 해당 키에 값을 입력
        else: print("해당 메뉴가 이미 존재합니다.")
    elif menu == 4:
        del_name = input("삭제할 메뉴를 입력하세요. : ")
        if del_name in menu_dic:
            del menu_dic[del_name]
        else: print("삭제할 메뉴가 존재하지 않습니다.")
        for key in menu_dic:
            print(key, ":", menu_dic[key])
    elif menu == 5:
        print("메뉴를 종료합니다.")
        break
    else: print("잘못된 명령어입니다. 다시 입력해주세요.")