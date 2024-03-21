#계좌 개설
def open_account(name): #매개변수와 반환값이 있는 함수선언
    print(f"{name}님의 계좌가 개설되었습니다.")
    return name
def deposit(balance, input): # 잔액과 입금액을 매개변수로 전달받음
    print(f"{input}원이 입금되었습니다. 잔액은 {balance + input}원 입니다.")
    return balance+input
def withdraw(balance, input):
    if balance >= input:
        print(f"{input}원이 출금되었습니다. 잔액은 {balance - input}원 입니다.")
        return balance-input
    else:
        print(f"출금할 수 없습니다. 잔액은 {balance}원 입니다.")
        return balance

balance = 0
name = open_account("김도영")
balance = deposit(balance, 1000)
balance = withdraw(balance, 500)
print(f"{name}님의 잔액은 {balance}원 입니다.")