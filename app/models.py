from django.db import models

# Create your models here.

class Employee(models.Model):
    first_name = models.CharField(max_length=50)
    last_name = models.CharField(max_length=50)
    email = models.EmailField(max_length=100, unique=True)
    mob_num =  models.IntegerField()
    is_deleted = models.BooleanField(default=False)
    salary = models.IntegerField(default=25000)

    def __str__(self):
        return f"{self.first_name}"


class Product(models.Model):
    name = models.CharField(max_length=30)

    class Meta:
        abstract = True

class Person(models.Model):
    first_name = models.CharField(max_length=30)
    last_name = models.CharField(max_length=30)
    # profile = models.OneToOneField("Profile", on_delete=models.CASCADE)  # profile_id

    
    def __str__(self):
        return f"{self.first_name}"
    
    class Meta:
        db_table = "person"

# p1.address.all()

class Address(models.Model):
    street = models.CharField(max_length=100)  # nul;
    city = models.CharField(max_length=50)
    state = models.CharField(max_length=50)
    postal_code = models.CharField(max_length=10)
    person = models.ForeignKey(Person, on_delete=models.SET_NULL, null=True, related_name="address") # person_id


    def __str__(self):
        return f"{self.street}"

    class Meta:
        db_table = "address"



class Profile(models.Model):
    bio = models.TextField()
    birthdate = models.DateField()
    person = models.OneToOneField(Person, on_delete=models.CASCADE)  # person_id
    
    def __str__(self):
        return f"{self.bio}"


# ORM -- Object Relational Mapper -- Object Oriented API  -- Django ORM 



# Employee.objects.all()  # 


# person
# id fn ln
# 1  sayali pawar
# 2 




# profile
# bio bd           person_id
# student 01/4/1995 1 
#                   1




class FuelType(models.Model):
    name = models.CharField(max_length=255)

    
    def __str__(self):
        return self.name
    
    class Meta:
        db_table = "fuel"
    
    
class CarModel(models.Model):
    name = models.CharField(max_length=255)
    fueltype = models.ManyToManyField(FuelType, related_name='models')

    def __str__(self):
        return self.name
    
    class Meta:
        db_table = "car"