from abc import ABC, abstractmethod

class HeroADT(ABC):
    """Hero의 Abstract Data Type (ADT) specification"""

    @property
    @abstractmethod
    def name(self):
        """이름 데이터에 접근하는 추상 프로퍼티"""
        pass

    @property
    @abstractmethod
    def role(self):
        """역할군 데이터에 접근하는 추상 프로퍼티"""
        pass

    @property
    @abstractmethod
    def power(self):
        """특전 파워 데이터에 접근하는 추상 프로퍼티"""
        pass

    @abstractmethod
    def introduce(self):
        """객체의 상태(이름, 역할군, 특전 파워)를 외부에 알리는 연산"""
        pass

    @abstractmethod
    def power_up(self, pw):
        """객체의 특전 파워를 특정 수치만큼 증가시키는 연산"""
        pass 

    @abstractmethod
    def action(self):
        """객체의 역할군 특성에 맞게 행동을 수행하는 연산"""
        pass