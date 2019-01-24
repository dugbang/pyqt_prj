from unittest import TestCase

from PyQt5.QtGui import QTransform, QVector2D


class TestQtVector2D(TestCase):
    def setUp(self):
        pass

    def test_01(self):
        rotation = QTransform()
        rotation.rotate(90)

        scaling = QTransform()
        scaling.scale(0.5, 1)

        vector = QVector2D(10, 10)
        vector = rotation * scaling * vector    # 된다고 했는데 안됨...ㅠ, 리플은 확인해봐야 한다.
        # C++ 의 예제임으로 파이썬에서 안된다고 하기에는 뭔가 문제가 있음.
        print(vector)
