
# class person:
#     ''' person class '''
#     def __init__(self,num,avg,price):
#         self.num=num
#         self.avg=avg
#         self.price=price
#         self.new= f"the avg is {avg} and num is {num}"

#     pi=3.14 

#     def calc(self):
#         return (person.pi*self.num)

# class child(person):
#     def __init__(self,num,avg,price,detail):
#         super().__init__(num,avg,price)
#         self.detail=detail


# c1=child(8,3,4,5)

# print(c1.calc())

# def add(a,b):
#     if (type(a) is int) and (type(b) is int):
#         return a+b
#     else:
#         raise TypeError ("wrong datatype")

# print(add(5,'3'))

l = [2,'abc',99.9,'g']
m = [1,2,3]
print(f'The original list: {l}')
l.insert(3,21)
print(f'The list after inserting: {l}')
l.pop(2)
print(f'The list after popping: {l}')
del l[1]
print(f'The list after deleting: {l}')
l.extend(m)
print(f'The list after extendong l and m: {l}')