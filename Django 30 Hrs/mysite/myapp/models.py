from django.db import models
from django.contrib.auth.models import User
from django.shortcuts import render


class home(models.Model):
    
    def __str__(self):
        return self.full_name
        
class Question(models.Model):
    User=models.ForeignKey(User,on_delete=models.CASCADE)
    title=models.CharField(max_length=300)
    detail=models.TextField()
    add_time=models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.title

# Answer Model
class Answer(models.Model):

    detail=models.TextField()
    add_time=models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.detail

class project(models.Model):
    User=models.ForeignKey(User,on_delete=models.CASCADE,null=True, blank=True)
    project_id=models.AutoField(primary_key=True)
    project_name=models.TextField()
    project_year_start = models.IntegerField()
    project_year_end = models.IntegerField()
    
    def __str__(self):
        return self.project_name
class contract(models.Model):
    contracte_id = models.AutoField(primary_key=True)
    project_id=models.ForeignKey(project,on_delete=models.CASCADE)
    contract_no=models.TextField()
    def __str__(self):
        return self.contract_no
    
class title(models.Model):
    title_id = models.AutoField(primary_key=True)
    contract_id = models.ForeignKey(contract, on_delete=models.CASCADE, null=True)
    title_name = models.TextField(null=True)

    def __str__(self):
        return self.title_name

 

class owner(models.Model):
    owner_id = models.AutoField(primary_key=True)
    title_id = models.ForeignKey(title, on_delete=models.CASCADE, null=True)
    depcode = models.TextField(null=True, blank=True)
    template = models.TextField(null=True, blank=True)

    def __str__(self):
        return str(self.title_id)

class result(models.Model):
    
    owner_id=models.ForeignKey(owner,on_delete=models.CASCADE,null=True, blank=True)
    quarter_no=models.IntegerField(null=True)
    data_confirm=models.TextField(null=True)
    result=models.TextField(null=True)
    problem=models.TextField(null=True)
    solution=models.TextField(null=True)
    year = models.IntegerField(null=True, blank=True)


class system_action(models.Model):
    userid=models.TextField
    action=models.TextField(null=True)
    depcode=models.TextField(null=True)
    readonly=models.TextField(null=True) 
   