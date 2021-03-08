from django.db import models
from django.contrib.auth.models import User

# Create your models here.
#OR to allow the user to input their own category
class Category(models.Model):
    myCategory = models.CharField(max_length=50,null=True,blank=True)
    user = models.ForeignKey(User, on_delete=models.CASCADE, null=True, blank=True)

    def __str__(self):
        return self.myCategory

class Todo(models.Model):
    DECISION = [
        ('Personal', 'Personal'),
        ('Official', 'Official')
    ]
    user = models.ForeignKey(User,null=True,blank=True,on_delete=models.CASCADE)
    category = models.ForeignKey(Category,max_length=50,null=True,blank=True, on_delete=models.CASCADE)
    title = models.CharField(max_length=300)
    decision = models.CharField(max_length=50,null=True,blank=True,choices=DECISION)    
    description = models.TextField(null=True,blank=True)
    completed_status = models.BooleanField(default=False)
    date_created = models.DateTimeField(auto_now_add=True)    

    # def __str__(self):
    #     return self.title
    
class Meta:
    db_table = 'todos'
    managed = True
    verbose_name = 'Todo'
    verbose_name_plural = 'Todos'

class Plan(models.Model):    
    user = models.OneToOneField(User,null=True,blank=True,on_delete=models.CASCADE)  
    your_plans = models.TextField(null=True,blank=True)
    alternatives = models.TextField(null=True, blank=True)

class Meta:
    db_table = 'plans'
    managed = True
    verbose_name = 'Plan'
    verbose_name_plural = 'Plans'

class Profile(models.Model):
    user = models.OneToOneField(User,null=True,blank=True,on_delete=models.CASCADE)
    address = models.CharField(max_length=100,null=True,blank=True)
    profile_pic = models.ImageField(default='defaultpic.jpg', null=True,blank=True)
    phone_number = models.CharField(max_length=20,null=True,blank=True)
    plan = models.ForeignKey(Plan, on_delete=models.CASCADE)

    def __str__(self):
        return self.user.username#we can pull by either username, email
    

    @property
    def email(self):
        if self.user_id is not None:
            return(self.user.email) 

    
    class Meta:
        db_table = 'profiles'
        managed = True
        verbose_name = 'Profile'
        verbose_name_plural = 'Profiles'

class Appraisal(models.Model):
    RATE = [
        ('Excellent', 'Excellent'),
        ('Very Good', 'Very Good'),
        ('Okay', 'Okay'),
        ('Bad', 'Bad'),
        ('Not Satisfactory','Not Satisfactory')
    ]
    user = models.OneToOneField(User,null=True,blank=True,on_delete=models.CASCADE)
    rate = models.CharField(max_length=50,choices=RATE)    
    experience = models.CharField(max_length=100, null=True,blank=True)
    thoughts = models.CharField(max_length=100)

    # def __str__(self):
    #     return self.title
    
class Meta:
    db_table = 'appraisals'
    managed = True
    verbose_name = 'Appraisal'
    verbose_name_plural = 'Appraisals'

    

