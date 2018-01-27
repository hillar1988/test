from django.db import models

# Create your models here.
class Person(models.Model):
    def __str__(self):
        return self.name
    name = models.CharField(u'名字', max_length=30)
    age = models.IntegerField(u'年龄')

class Person1(models.Model):
    first_name = models.CharField(max_length=50)
    last_name = models.CharField(max_length=50)
    def my_property(self):
        return self.first_name + ' ' + self.last_name

    my_property.short_description = "Full name of the person"

    full_name = property(my_property)






