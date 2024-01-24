from django.db import models

class user_deatils (models.Model):
    Date= models.DateTimeField(auto_now_add=True,null=False)
    name= models.CharField(max_length=255,null=False)
    Task=models.CharField(max_length=255,null=False)
    task_type=models.CharField(max_length=255,null=False)
    Type=models.CharField(max_length=255,null=False)
    Pr_prod=models.CharField(max_length=255,null=False)
    clx_cat=models.CharField(max_length=255,null=False)
    clocked=models.IntegerField(null=False)
    minimum=models.CharField(max_length=255,null=False)
    starting_Row=models.IntegerField(null=False)
    ending_Row=models.IntegerField(null=False)
    Rows=models.IntegerField(null=False)
    from_innerid=models.IntegerField(null=False)
    end_innerid=models.IntegerField(null=False)
    inner_id=models.IntegerField(null=False)
    files=models.IntegerField(null=False)
    file_type=models.CharField(max_length=255,null=False)
    parameter=models.IntegerField(null=False)
    count=models.IntegerField(null=False)
    comment=models.CharField(max_length=255,null=False)
    
    

    




