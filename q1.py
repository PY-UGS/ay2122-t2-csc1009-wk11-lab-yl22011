class Calculator:
    def __init__(self,z,y):
        self.y = y
        self.z =z
    def adder(self):
        a = self.z + self.y
        return a
    def subtractor(self):
        a=self.z -self.y
        return a
    def multiplier(self):
        a=self.z * self.y
        return a
    def divider(self):
        a=self.y/self.z
        return a
    def clear(self):
        return 0

z= int(input("Input no1: "))
y= int(input("Input no2: "))
no=0
cal = Calculator(z,y)
s=1

while s==1:
    print("Current no: " + str(no))
    x = int(input("0 for adder,1 for subtractor,2 for multiplier,3 for divider,4 for clear"))
    match x:
        case 0:
            no =cal.adder()
            #print(no)
        case 1:
            no=cal.subtractor()
        case 2:
            no = cal.multiplier()
        case 3:
            no = cal.divider()
        case 4:
            no = cal.clear()
