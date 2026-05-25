from hero import Hero

class DPS(Hero):
    def __init__(self, name, power=0, hp=300):
        super().__init__(name, "DPS", power, hp)

    def action(self, heal=None, ult=None):
        if heal:
            print(f"[{self.name}] DPS는 아군을 치유하는 법을 모릅니다! 아군에게 위협만 가했습니다.")
        elif ult == "눈보라":
            #메이만의 궁극기
            damage = self.power *5
            print(f"[{self.name}] 궁극기 발동: 꼼짝 마! 움직이지 마세요! ({damage}의 피해!)")
        else:
            super().action()