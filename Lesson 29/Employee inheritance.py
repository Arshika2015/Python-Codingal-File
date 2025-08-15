#parent class
class person(object):
  def __init__(self,name,idnumber):
    self.name = name
    self.idnumber = idnumber
  def display(self):
    print(self.name)
    print(self.idnumber)
#child class
class employee(person):
  def __init__(self,name,idnumber,salary,post):
    self.post = post
    self.salary = salary
    person.__init__(self,name,idnumber)
p = employee("Arshika",27,10000000,"student")
p.display()
    




  
