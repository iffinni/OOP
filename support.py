from hero import Hero

class Support(Hero):
    def __init__(self, name, power=0, hp=225):
        super().__init__(name, "서포터", power, hp)

    def action(self, heal=None, ult=None):
        if heal == "치유의 꽃":
            healing = self.power * 2
            print(f"[{self.name}] 서포터는 아군을 성공적으로 치유시켰습니다! (치유량: {healing})")
        elif ult == "생명의 나무":
            #라이프 위버만의 궁극기
            healing = self.power * 15
            print(f"[{self.name}] 궁극기 발동: 생명은 생명을 보호해요! (아군 전원에게 {healing}의 치유!)")
        else:
            super().action()