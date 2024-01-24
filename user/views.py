


# Create your views here.

from django.http import HttpResponse
from django.views.decorators.http import require_http_methods
from user.models import userdata
from django.shortcuts import render
# from django.contrib.auth import authenticate, login
# from calculator.models import yubi1
def index (request):
    return HttpResponse("I am a calculator")


def createuser(request):
    print(request.POST)
    param=dict(request.POST)
    

    name=str(param["name"][0])
    username=str(param["username"][0])
    phone_no=str(param["phone_no"][0])
    mail_id=str(param["mail_id"][0])
    password=str(param["password"][0])
    filename=username+".""txt"

    if userdata.objects.filter(user_name=username).exists():
            return HttpResponse("Username already exists. Please choose a different username.")

    with open(filename,'w') as file:
        file.writelines(name+","+username+","+phone_no+","+mail_id+","+password)
        file.close()

    userdata.objects.create(user_name=username,user_file=filename)

    return HttpResponse("succesfully cretaed")






    





def login(request):
    param=dict(request.POST)
    username=str(param["username"][0])
    password=str(param["password"][0])
    result = userdata.objects.filter(user_name=username).values()
    print(result)
    files = []
    for a in result:
        files.append(a['user_file'])
    print(files)
    # result = userdata.objects.filter(user_name=username).values('user_file')
    # fil = []
    # for res in result:
    #     fil.append(res['user_file'])
    all_content = []
    # for i in fil:
    with open (files[0],'r') as file:
            content=file.read()
            # all_content=content
    all_content.append(content)
    detail_string=all_content[0]
    details_list=detail_string.split(',')
    # for i in content:
    #     all_content.append(i)
    print(details_list)
    if username ==details_list[1] and password==details_list[4]:
            return HttpResponse("log in succesful")
    else:
        return HttpResponse("failed")



# def login (request):
#     print(request.POST)
#     param=dict(request.POST)
#     username=str(param["username"][0])
#     password=str(param["password"][0])
#     res = userdata.objects.values('user_name')
#     a = []
#     for i in res:
#         a.append(i['user_name'])
#     res = userdata.objects.values('user_file')
#     b = []
#     for j in res:
#         b.append(j['user_file'])
#     d = []
#     for r in b:
#         with open (r,'r') as file:
#             c=file.read()
#     d.append(c)
#     string=d[0]
#     lis=string.split(',')
#     print(lis)

#     if username ==lis[1] and password==lis[4]:
#             return HttpResponse("log in succesful")
#     else:
#         return HttpResponse("failed")
    





# def login(request):
#     if request.method == 'POST':
#         # Get the POST data
#         param = dict(request.POST)

#         # Check if 'username' and 'password' keys exist in POST data
#         if 'username' in param and 'password' in param:
#             username = param['username'][0]
#             password = param['password'][0]

#             # Query the database to get user data
#             try:
#                 user_data =userdata.objects.get(user_name=username)
#             except userdata.DoesNotExist:
#                 return HttpResponse("Failed: User does not exist")

#             # Check if the provided password matches the stored password
#             if password == user_data.user_password:
#                 return HttpResponse("Login successful")
#             else:
#                 return HttpResponse("Failed: Incorrect password")
#         else:
#             return HttpResponse("Failed: Username or password missing in POST data")
#     else:
#         return HttpResponse("Failed: Only POST requests are allowed for login")



def getuser(request):
    if request.method == 'GET':
        user_files = userdata.objects.values_list('user_file')
        file_paths = [file[0] for file in user_files]
        
        user_information_all = "\n".join(
            ",".join(line.rstrip().split(',')[:-1]) for file_path in file_paths
            for line in open(file_path, 'r').readlines()
        )

        return HttpResponse(user_information_all)
    


    








