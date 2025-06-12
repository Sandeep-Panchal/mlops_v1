import sys
sys.path.append("../")

from src.math_operation import MathsOperation

obj = MathsOperation()

def test_addition():
    assert obj.addition(1,1) == 2
    assert obj.addition(5,100) == 105

def test_subtraction():
    assert obj.subtraction(10,1) == 9
    assert obj.subtraction(2,10) == -8

def test_product():
    assert obj.product(10,10) == 100
    assert obj.product(2,10) == 20

if __name__=="__main__":
    pass
