
class clockTime:
    def __init__(self):
        self.hour = None
        self.minute = None
        self.second = None
    
    def setHours(self,x):
        self.hour = x
        return
    def setMinutes(self,y):
        self.minute= y
        return
    def setSeconds(self,z):
        self.second = z
        return
    def setTime(self,x,y,z):
        self.setHours(x)
        self.setMinutes(y)
        self.setSeconds(z)

    def showTime(self):
        print("Time is"+ str(self.hour) +":" +str(self.minute)+":"+ str(self.second))

x=int(input("Hour: "))
y= int(input("Minute"))
z= int(input("Second"))
c = clockTime()
c.setHours(x)
c.setMinutes(y)
c.setSeconds(z)
c.showTime()
c.setTime(x,y,z)
c.showTime()
