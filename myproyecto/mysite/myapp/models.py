from django.db import models

import json


"""
class Projects(models.Model):
    id_project = models.CharField(max_length=50)
    status = models.CharField(max_length=50)
    title = models.CharField(max_length=500, null=True,blank=True)

"""



class Projects(models.Model):
    id_project = models.CharField(max_length=50)
    publishable = models.CharField(max_length=50, null=True)
    published = models.CharField(max_length=50, null=True)
    title = models.CharField(max_length=500, null=True,blank=True)
    main_language = models.CharField(max_length = 6, null=True,blank=True)
    start_date = models.DateField(null=True,blank=True)
    end_date = models.DateField(null=True,blank=True)
    status = models.CharField(max_length=50, null=True)
    coordinating_institution = models.CharField(max_length=50, null="NTNU")
    department = models.CharField(max_length=500, null=True,blank=True)
    manager_name = models.CharField(max_length=50, null=True)
    participant1_name = models.CharField(max_length=50, null=True)
    participant1_surname = models.CharField(max_length=50, null=True)
    
    
    participant2_name = models.CharField(max_length=50, null=True)
    participant2_surname = models.CharField(max_length=50, null=True)
    participant3_name = models.CharField(max_length=50, null=True)
    participant3_surname = models.CharField(max_length=50, null=True)
    participant4_name = models.CharField(max_length=50, null=True)
    participant4_surname = models.CharField(max_length=50, null=True)
    participant5_name = models.CharField(max_length=50, null=True)
    participant5_surname = models.CharField(max_length=50, null=True)
    participant6_name = models.CharField(max_length=50, null=True)
    participant6_surname = models.CharField(max_length=50, null=True)
    participant7_name = models.CharField(max_length=50, null=True)
    participant7_surname = models.CharField(max_length=50, null=True)
    
    participant8_name = models.CharField(max_length=50, null=True)
    participant8_surname = models.CharField(max_length=50, null=True)
    participant9_name = models.CharField(max_length=50, null=True)
    participant9_surname = models.CharField(max_length=50, null=True)
    participant10_name = models.CharField(max_length=50, null=True)
    participant10_surname = models.CharField(max_length=50, null=True)
    
    project_category1 = models.CharField(max_length=50, null=True)
    project_category2 = models.CharField(max_length=50, null=True)
    project_category3 = models.CharField(max_length=50, null=True)
    project_category4 = models.CharField(max_length=50, null=True)
    project_category5 = models.CharField(max_length=50, null=True)
    
    academic_discipline1 = models.CharField(max_length=50, null=True)
    academic_discipline2 = models.CharField(max_length=50,null=True)
    academic_discipline3 = models.CharField(max_length=50,null=True)
    academic_discipline4 = models.CharField(max_length=50, null=True)
    academic_discipline5 = models.CharField(max_length=50, null=True)
    
    keyword1 = models.CharField(max_length=50, null=True)
    keyword2 = models.CharField(max_length=50, null=True)
    keyword3 = models.CharField(max_length=50, null=True)
    keyword4 = models.CharField(max_length=50, null=True)
    keyword5 = models.CharField(max_length=50, null=True)
    
    summary = models.CharField(max_length=5000, null=True)
    
    funding1 = models.CharField(max_length=50, null="None")
    funding2 = models.CharField(max_length=50,null="None")
    funding3 = models.CharField(max_length=50, null="None")
    funding4 = models.CharField(max_length=50, null="None")
    funding5 = models.CharField(max_length=50, null="None")
    
    
    total_funding_amount = models.CharField(max_length=10, null= True)
    currency = models.CharField(max_length=60,null=True)
    contact_email = models.CharField(max_length=60,null=True)
    contact_phone = models.CharField(max_length=60,null=True)