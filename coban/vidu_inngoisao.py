a=[5,4,3,2,1]
def Func1(a):
    def Func2(k):
        return k%2==0
    return sorted(list((filter(Func2, a))))
print(Func1(a))