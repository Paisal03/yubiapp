from django.shortcuts import render
from django.http import HttpResponse
from django.views.decorators.http import require_http_methods
from Tracker.models import user_deatils
from datetime import datetime

def index (request):
    print(request.POST)
    param=dict(request.POST)
    Names_list=['Bharathi','Naveen','Payaskhan','Pandipriya','Santhosh','Aarthi','Afrin Rukshana','Logeswari','Priya','vaidheki','Priyadharshini','Pradheepa','Mohanaselvan','Dillibabu','Ponvivek','Karthick','Srigovarasan Sakthivel']
    

    




    # Date=datetime(param["Date"][0])
    name=str(param["name"][0])
    Task=str(param["Task"][0])
    task_type=str(param["task_type"][0])
    Type=str(param["Type"][0])
    Pr_prod=str(param["Pr_prod"][0])
    clx_cat=str(param["clx_cat"][0])
    clocked=int(param["clocked"][0])
    minimum=int(param["minimum"][0])
    starting_Row=int(param["starting_Row"][0])
    ending_Row=int(param["ending_Row"][0])
    # Rows=str(param[" Rows"][0])
    from_innerid=int(param["from_innerid"][0])
    end_innerid=int(param["end_innerid"][0])
    # inner_id=str(param["inner_id"][0])
    files=int(param["files"][0])
    file_type=str(param["file_type"][0])
    parameter=int(param["parameter"][0])
    count=int(param["count"][0])
    comment=str(param["comment"][0])

    Rows=ending_Row-starting_Row+1
    inner_id=end_innerid-from_innerid+1

    if name in Names_list:
        result = user_deatils.objects.create(name=name,Task=Task,task_type=task_type,Type=Type,Pr_prod=Pr_prod,clx_cat=clx_cat,clocked=clocked,minimum=minimum,starting_Row=starting_Row,ending_Row=ending_Row,Rows=Rows,from_innerid=from_innerid,end_innerid=end_innerid,inner_id=inner_id,files=files,file_type=file_type,parameter=parameter,count=count,comment=comment)
    
     
        print(result)

        return HttpResponse("succesfully saved")

    else:

    
    
    
        return HttpResponse ("failed")

    






















    return HttpResponse("I am a calculator")

# Create your views here.
