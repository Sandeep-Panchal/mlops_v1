from typing import Union

class MathsOperation:

    def addition(self,
                value1: Union[int, float],
                value2: Union[int, float],
                ) -> Union[int, float]:

        return value1 + value2

    def subtraction(self,
                value1: Union[int, float],
                value2: Union[int, float],
                ) -> Union[int, float]:

        return value1 - value2

if __name__=="__main__":
    pass
    # obj = MathsOperation()
    # print(obj.addition(1,1))
    # print(obj.subtraction(2,1))

    
