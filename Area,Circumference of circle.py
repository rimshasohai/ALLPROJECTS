class Circle:
    radius=0
    colour='None'
    def setradius(self,r=radius):
        self.radius=r
    def getradius(self):
        return self.radius
    def setcolour(self,c=colour):
        self.colour=c
    def getcolour(self):
        return self.colour
    def area(self,r=radius):
        return 3.142*self.radius**2
    def circumference(self,r=radius):
        return 2*3.142*self.radius
a1=Circle()
a1.setradius(4)
a1.setcolour('Blue')
print('COLOUR OF CIRCLE:',a1.getcolour())
print('AREA OF CIRCLE IS:',a1.area())
print('CIRCUMFERENCE OF CIRCLE IS:',a1.circumference())
