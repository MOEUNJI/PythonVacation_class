class Fish_bread:
    def __init__(self,taste,count):
        self.taste = taste
        self.count = count

    def making(self):
        print(f"{self.taste}맛 붕어빵 {self.count}개 나왔습니다.")

fish_bread1 = Fish_bread("슈크림",3)
fish_bread2 = Fish_bread("팥",2)
fish_bread3 = Fish_bread("피자",1)

fish_bread1.making()
fish_bread2.making()
fish_bread3.making()


