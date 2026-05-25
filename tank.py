from hero import Hero

class Tank(Hero):
    def __init__(self, name, power=0, hp=700):
        super().__init__(name, "탱커", power, hp)

    def action(self, heal=None, ult=None):
        if heal:
            print(f"[{self.name}] 아군을 치유하는 법을 모르는 탱커는 아군에게 오는 공격을 대신 맞아줍니다.")
        elif ult == "대지분쇄":
            #라인하르트만의 궁극기
            damage = self.power *10
            print(f"[{self.name}] 궁극기 발동: 망치 나가신다! ({damage}의 피해를 주며 적군 전원을 기절시켰습니다!)")
        else:
            super().action()