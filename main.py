from dps import DPS
from support import Support
from tank import Tank
 
 
if __name__ == "__main__":
    # 인스턴스 생성
    p1 = DPS("메이", 110)
    p2 = Support("라이프 위버", 66)
    p3 = Tank("라인하르트", 100)
 
    characters = [p1, p2, p3]
 
    print("--- 1. 기본 공격 테스트 (인자 없음) ---")
    for c in characters:
        c.action()
 
    print("\n--- 2. 치유 테스트 ---")
    p1.action(heal="냉각총")       # 메이의 일반 무기 (super 호출)
    p2.action(heal="치유의 꽃")     # 라이프 위버의 특수 오버라이딩 발동
    p3.action(heal="로켓 해머")     # 라인하르트의 일반 무기 (super 호출)
 
    print("\n--- 3. 궁극기 테스트 ---")
    p1.action(ult="눈보라")       # 메이의 궁극기
    p2.action(ult="생명의 나무")    # 라이프 위버의 궁극기
    p3.action(ult="대지분쇄")      # 라인하르트의 궁극기