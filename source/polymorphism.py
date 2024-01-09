class Animal: 
  def type(self): 
    print("Various types of animals") 
       
  def age(self): 
    print("Age of the animal.") 
     
class Rabbit(Animal): 
  def age(self): 
    print("Age of rabbit.") 
       
class Horse(Animal): 
  def age(self): 
    print("Age of horse.") 
       
obj_animal = Animal() 
obj_rabbit = Rabbit() 
obj_horse = Horse() 
   
obj_animal.type() 
obj_animal.age() 
   
obj_rabbit.type() 
obj_rabbit.age() 
   
obj_horse.type() 
obj_horse.age()