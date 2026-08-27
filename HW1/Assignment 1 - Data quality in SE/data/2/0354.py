from django.db import models


ch=[
    ('Garment','Garment'),
    ('Hardgoods','Hardgoods'),
    ('Home Furnishing','Home Furnishing'),
]
class Factory(models.Model):
    name = models.CharField(max_length=30,choices=ch)

    def __str__(self):
        return self.name

class Fabric(models.Model):
    name = models.ForeignKey(Factory, on_delete=models.CASCADE,null=True,blank=True)
    fabric = models.CharField(unique=True,max_length=100,null=True,blank=True)

    def __str__(self):
        return self.fabric

class Wash(models.Model):
    name=models.ForeignKey(Fabric,on_delete=models.CASCADE,null=True,blank=True)
    wash = models.CharField(unique=True,max_length=100,null=True,blank=True)


    def __str__(self):
        return self.wash

class Category(models.Model):
    cat=models.ForeignKey(Factory,on_delete=models.CASCADE,blank=True)
    name = models.ForeignKey(Wash, on_delete=models.CASCADE,null=True,blank=True)
    category = models.CharField(unique=True,max_length=100,null=True,blank=True)

    def __str__(self):
        return self.category

class Subcategory(models.Model):
    name = models.ForeignKey(Category, on_delete=models.CASCADE,null=True,blank=True)
    subcategory = models.CharField(unique=True,max_length=100,null=True,blank=True)

    def __str__(self):
        return self.subcategory

class Department(models.Model):
    name = models.ForeignKey(Subcategory, on_delete=models.CASCADE,null=True,blank=True)
    department = models.CharField(unique=True,max_length=100,null=True,blank=True)

    def __str__(self):
        return self.department

class Sections(models.Model):
    name = models.ForeignKey(Department, on_delete=models.CASCADE,null=True,blank=True)
    section = models.CharField(unique=True,max_length=100,null=True,blank=True)

    def __str__(self):
        return self.section

class Subsection(models.Model):
    name = models.ForeignKey(Sections, on_delete=models.CASCADE,null=True,blank=True)
    subsection = models.CharField(unique=True,max_length=500,null=True,blank=True)

    def __str__(self):
        return self.subsection

class Person(models.Model):
    name=models.CharField(max_length=30)
    fact=models.ForeignKey(Factory,on_delete=models.CASCADE)
    fab=models.ForeignKey(Fabric,on_delete=models.CASCADE,null=True)
    was= models.ForeignKey(Wash, on_delete=models.CASCADE,null=True)
    cate = models.ForeignKey(Category, on_delete=models.CASCADE)
    subcat=models.ForeignKey(Subcategory,on_delete=models.CASCADE)
    dept = models.ForeignKey(Department, on_delete=models.CASCADE,null=True)
    sect=models.ForeignKey(Sections,on_delete=models.CASCADE,null=True)
    subsect=models.ForeignKey(Subsection,on_delete=models.CASCADE,null=True)

    def __str__(self):
        return str(self.name)
