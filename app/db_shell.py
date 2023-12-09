from app.models import *

# exec(open(r'E:\Python-B10\Files\Django_Projects\first_project\app\db_shell.py').read())

# CRUD  - Read

# from django.db.models import Sum, Avg

# # Get the total count of objects
# total_count = Employee.objects.count()
# print(total_count)

# # Get the sum of a numeric field
# total_sum = Employee.objects.aggregate(Sum('salary'))
# print(total_sum)

# # Get the average of a numeric field
# average_value = Employee.objects.aggregate(Avg('salary'))
# print(average_value)


# data = Employee.objects.order_by('-salary')
# print(data)
# 

# filtered_and_ordered = Employee.objects.filter(mob_num__startswith=54).order_by('id')
# print(filtered_and_ordered)



# # create 1 
# emp = Employee(first_name="Emp3", last_name="lstname", email="emp3@gmail.com", mob_num=54545154)
# emp.save()


# create 2
# emp = Employee.objects.create(first_name="Emp3", last_name="lstname", email="emp3@gmail.com", mob_num=54545154)


# Employee.objects.get(id=4).delete()



# emp_obj = Employee.objects.get(id=3)
# emp_obj.first_name = "Employee3"
# emp_obj.last_name = "EmpLastname"
# emp_obj.save()


# filter().delete()


# all_emps = Employee.objects.all()
# print(all_emps)
# for emp in all_emps:
#     print(emp.id)

# try:
#     emp = Employee.objects.get(first_name__startswith="E")
#     print(emp)
# except Employee.DoesNotExist as msg:
#     print(msg)


# emps = Employee.objects.filter(first_name__startswith="A")
# print(emps)


# emps = Employee.objects.filter(first_name__in=["Emp1", "Emp2"])
# print(emps)


# emps = Employee.objects.filter(first_name__contains="E")[0]
# print(emps)

from datetime import datetime

# p3 = Person.objects.create(first_name="p3", last_name="pln3")


# print(p3.__dict__)

# Profile.objects.create(bio="student3", birthdate=datetime(1990, 1, 15), person=p3)

# pr1 = Profile.objects.get(id=1)
# print(pr1.person)


# p1 = Person.objects.get(id=4)
# print(dir(p1))
# print(p1.address_set.all())


# adr1 = Address.objects.get(id=4)
# print(adr1.person)

# p1 = Person.objects.create(first_name="p1", last_name="pln1")


# Address.objects.filter(id__in=[1,2]).update(person=p1)





# p1.delete()

# Address.objects.create(street="DP road", city="Pune", state="MH",postal_code=412451, person=p1)
# Address.objects.create(street="wakad road", city="Pune", state="MH",postal_code=411057, person_id=p1.id)



# many to many

# c180 = CarModel.objects.create(name="C180")
# c200 = CarModel.objects.create(name="C200")

# print(CarModel.objects.all())


# gas = FuelType.objects.create(name="Gas")
# diesel = FuelType.objects.create(name="Diesel")
# hybrid = FuelType.objects.create(name="Hybrid")

# print(FuelType.objects.all())

# exec(open(r'E:\Python-B10\Files\Django_Projects\first_project\app\db_shell.py').read())


c180 = CarModel.objects.get(name="C180") #  1


f1 = FuelType.objects.get(name="Gas") # 2
# f2 = FuelType.objects.get(name="Diesel") # 2
# f3 = FuelType.objects.get(name="Hybrid") # 2


# c200.fueltype.add(f1, f2, f3) # CarModelObject.fueltype.add(FuelTypeObject)

# c200.fueltype.create(name="Bio Diesel")


# print(c180.fueltype.all())

# 1 2

# print(f1.models.all())

c180.fueltype.clear()



d = {"a": 1}




