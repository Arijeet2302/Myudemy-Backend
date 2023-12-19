from django.db import models

# Create your models here.

class Cart(models.Model):
    id = models.AutoField(primary_key=True)
    uid = models.CharField(max_length=1000)
    course_id = models.ForeignKey(default=0,to='Courses',on_delete=models.CASCADE) 
    cust_name = models.CharField(max_length=50)
    course_name = models.CharField(max_length=200)
    author_name = models.CharField(max_length=200,default="")
    price = models.FloatField()
    quantity = models.IntegerField(default=1)
    image = models.ImageField(upload_to="static",default="")

    def __str__(self):
        return self.cust_name
    
class Courses(models.Model):
    course_id = models.AutoField(primary_key=True)
    course_name = models.CharField(max_length=500)
    author_name = models.CharField(max_length=500)
    rating = models.FloatField()
    price = models.FloatField()
    image = models.ImageField(upload_to="static",default="")


    class Meta:
        constraints = [
            models.CheckConstraint(check=models.Q(rating__lte=5.0), name='rating_constraint'),
        ]

    def __str__(self) :
        return f"{self.course_name} (ID: {self.course_id})"
    
class UserCourses(models.Model):
    id = models.AutoField(primary_key=True)
    uid = models.CharField(max_length=1000)
    cust_name = models.CharField(max_length=50)
    course = models.ForeignKey(to='Courses', on_delete=models.CASCADE,default=0)
    rating = models.FloatField()
    author_name = models.CharField(max_length=200,default="")
    image = models.ImageField(upload_to="static",default="")

    def __str__(self):
        return f"{self.cust_name} - {self.course.course_name} (Rating: {self.rating})"
