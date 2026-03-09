from typing import Any,Iterable
class DeleteItem:
    def __init__(self,iterable: Iterable[Any]):
        """

        :param iterable:
        :return:none
        """
        self.iterable = list(iterable)
    def delete(self,index: int)->list[Any]:
        """

        :param index:所要删除项的索引
        :return: 删除后的列表
        """
        for i in range(index,len(self.iterable)):
            self.iterable[i]=self.iterable[i+1]
        self.iterable.pop()
        return self.iterable












    

