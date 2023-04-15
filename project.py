import math
class Car:
    def __init__(self,make,model,year,speed,x,y):
        self.make=make
        self.model=model
        self.year=year
        self.speed=speed
        self.x=x
        self.y=y
        
    def accelerate(self,speed_increment):
        self.speed+=speed_increment

    def brake(self,speed_decrement):
        self.speed-=speed_decrement   

    def move(self):
        self.x+=self.speed
        self.y+=self.speed    

    def detect_collison(self,car2):
        if self.x==car2.x and self.y==car2.y:
            return True
        else:
            return False
        
    def time_to_collison(self,car):
 
        dist = math.sqrt((car.x - self.x)**2 + (car.y - self.y)**2)
        rel_speed = math.fabs(car.speed - self.speed)
        return dist / rel_speed

        
car1=Car("Hyundai","Creta",1960,2,20,30)
car2=Car("Maruti","City",1980,1,20,30)
print(car1.detect_collison(car2))
print(car1.time_to_collison(car2))
