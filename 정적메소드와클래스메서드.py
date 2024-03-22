# 정적메서드 : 클래스와 관련있어 클래스 안에 두기는 하지만 클래스, 인스턴스와는 무관
class Car:
    is_instance_cnt = 0

    def __init__(self, size, model):
        self.size = size
        self.model = model
        self.speed = None
        Car.is_instance_cnt += 1
        print(f"자동차 생산 대수 : {Car.is_instance_cnt}")

    def move(self, speed):
        self.speed = speed
        print(f"자동차 {self.size}차 {self.model}(이)가 시속 {self.speed}로 달립니다.")

    @staticmethod
    def check_type(code):
        if 20 > code >= 10:
            print("전기차 입니다.")
        elif 30 > code >= 20:
            print("가솔린차 입니다.")
        elif 40 > code >= 30:
            print("디젤차 입니다.")
        else:
            ("분류 코드가 없습니다.")


morning = Car("소형", "모닝")
sonata = Car("중형", "소나타")
morning.move(90)
sonata.move(100)
Car.check_type(11)
