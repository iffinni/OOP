from hero_adt import HeroADT


class Hero(HeroADT):
    def __init__(self, name, role, power=0, hp=0):
        """생성자: Person 객체의 초기 상태(데이터)를 설정"""
        self.__name = name
        self.__role = role
        self.__power = power
        self._hp = hp

    # --- Properties (Getters) ---
    @property
    def name(self): return self.__name

    @property
    def role(self): return self.__role

    @property
    def power(self): return self.__power

    @property
    def hp(self): return self._hp

    # --- Properties (Setters) ---
    @name.setter
    def name(self, value):
        if not isinstance(value, str) or len(value) == 0:
            print(f"[에러] 유효하지 않은 이름입니다: {value}")
        else:
            self.__name = value

    @role.setter
    def role(self, value):
        print(f"[경고] {self.name}의 역할군을 {self.role}에서 {value}(으)로 변경합니다.")
        self.__role = value

    @power.setter
    def power(self, value):
        if value < 0:
            print(f"[에러] 특전 파워는 0보다 작을 수 없습니다. (입력값: {value})")
        else:
            self.__power = value

    @hp.setter
    def hp(self, value):
        if value < 0:
            self._hp = 0
            print(f"[{self.name}] 체력이 0이 되어 더 이상 전투할 수 없습니다!")
        else:
            self._hp = value

    def introduce(self):
        print(f"- Name: {self.name}({self.role}), LV: {self.power}, HP: {self._hp}")

    def power_up(self, pw=50):
        self.__power += pw
        print(f"특전 파워가 {pw}만큼 올라 {self.name}님은 총 {self.power}이 되었습니다.")

    # [오버로딩 (Overloading) 구현]
    # 매개변수(heal, ult)의 입력 여부에 따라 내부에서 분기 처리
    def action(self, heal=None, ult=None):
        if heal:
            damage = self.power
            print(f"[{self.name}의 치유!] '{heal}' 발동! (치유량: {damage})")
        elif ult:
            damage = self.power * 5
            print(f"[{self.name}의 궁극기 발동!] {ult}을(를) 시전! (피해량: {damage})")
        else:
            damage = self.power
            print(f"[{self.name}의 기본 공격!] 기본 타격! (피해량: {damage})")