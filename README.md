## WEB3.O PROJECT
First we imported Math module

---
We made class named class CAR

Inside class CAR I made function which takes attributes of object as argument, self refers to the object to which I will add the attributes

```python
def __init__(self,make,model,year,speed,x,y):
    self.make=make
    self.model=model
    self.year=year
    self.speed=speed
    self.x=x
    self.y=y
```
Then I created aceelerate function accelerate which takes argument by which speed should be increase every time I ran the code
```python
def accelerate(self,speed_increment):
    self.speed+=speed_increment
```
After that I created brake function brake which takes argument by which speed should be decrease every time I ran the code 
```python
def brake(self,speed_decrement):
    self.speed-=speed_decrement
```
After that I created move function which takes self as argument and increases x coordinate and y coordinate
```python
def move(self):
    self.x+=self.speed
    self.y+=self.speed                    
```
After that I created detect_collison which takes self and car2 as argument ,which return result based on if car1 has collided to car2 or not
```python
if self.x==car2.x and self.y==car2.y:
    return True
else:
    return False
```
Now the function time_to_collison will tell time by calculating relative distance/relative velocity whenever direction changes
```python
def time_to_collison(self,car):
    dist = math.sqrt((car.x - self.x)**2 + (car.y - self.y)**2)
    rel_speed = math.fabs(car.speed - self.speed)
    return dist / rel_speed
```
Now I created object car1 and car2 of class CAR and passed attributes of respectively.
```python
car1=Car("Hyundai","Creta",1960,2,20,30)
car2=Car("Maruti","City",1980,1,20,30)
```
At last I printed whether cars will collide or not and if yes then what is time for them to collide
```python
print(car1.detect_collison(car2))
print(car1.time_to_collison(car2))
```
