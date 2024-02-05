from django.db import models
 


class User(models.Model):
        username=models.CharField(max_length=20)
        fname=models.CharField(max_length=20)
        lname=models.CharField(max_length=20)
        email=models.EmailField(max_length=100)
        pass1=models.CharField(max_length=20)

        class Meta:
                db_table = "accounts"

class Complaint(models.Model):
        name=models.CharField(max_length=50)
        rollno=models.CharField(max_length=20)
        branch=models.CharField(max_length=20)
        section=models.CharField(max_length=20)
        year=models.CharField(max_length=20)
        mobile=models.CharField(max_length=20)
        email=models.EmailField(max_length=100)
        complaint_type=models.CharField(max_length=60)
        location=models.CharField(max_length=30)
        describe=models.CharField(max_length=200)
        class Meta:
                db_table = "complaint"














# Create your models here.
