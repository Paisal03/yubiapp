from django.http import HttpResponse
from django.views.decorators.http import require_http_methods
from calculator.models import Request
# from calculator.models import yubi1
def index (request):
    return HttpResponse("I am a calculator")

@require_http_methods(["GET"])  
def index1(request):
    print(request.GET)
    
    
    #req=Request.objects.filter(id=1).get()
    #print(req)
    param =dict(request.GET)
    #param =dict(request.GET)
    # c=param["a"]+param["b"]
    a=str(param["a"][0])
    b=str(param["b"][0])
    # files=[a+''+b]
    filename=a+".""txt"
    file=open(filename,'w')
    file.writelines(a+","+b)

    # with open ('test.txt','w') as f:
    #     f.write('files')
    #     f.close()
    with open(filename,'r') as f :
      txt=f.read()
      print(txt)

    

    # Request.objects.create (param_a=a,param_b=b,param_c=a+b,operator="add")
    return HttpResponse(a,b)
   #"x="+str(a)+" "+"y="+str(b)+" "+ " "+"x+y="+str(int(a)+int(b))

    
    
    return HttpResponse("I am a Add function") 
    
@require_http_methods(["POST"])
def index2 (request):
    print (request.GET)
    print (request.POST)

    param =dict(request.POST)
    param =dict(request.POST)
    # c=param["a"]+param["b"]
    a=int(param["a"][0])
    b=int(param["b"][0])
    Request.objects.create (param_a=a,param_b=b,param_c=a-b,operator="sub")
    return HttpResponse("a="+str(a)+" "+"b="+str(b)+" "+ " "+"a-b="+str(int(a)-int(b)))

    
    return HttpResponse("I am a substraction") 

#@require_http_methods(["GET","POST"])
# @require_http_methods(["POST"])    
def index3 (request):
     
 if request.method == 'POST':
    param=dict(request.POST)
    print(param)
    a=int(param["a"][0])
    b=int(param["b"][0])
    Request.objects.create (param_a=a,param_b=b,param_c=a*b,operator="multi")
    return HttpResponse("a= "+str(a) +" b= "+str(b)+ " a*b= "+str(int(a)*int(b)))
 else :
    request.method == 'GET'
    param=dict(request.GET)
    print(param)
    a=int(param["a"][0])
    b=int(param["b"][0])
    Request.objects.create (param_a=a,param_b=b,param_c=a*b,operator="multi")
    return HttpResponse("a= "+str(a) +" b= "+str(b)+ " a*b= "+str(int(a)*int(b)))

    return HttpResponse("I am a multiplication") 

    
def index4 (request):
 
 if request.method == 'GET':
    param=dict(request.GET)
    print(param)
    a=int(param["a"][0])
    b=int(param["b"][0])
    Request.objects.create (param_a=a,param_b=b,param_c=a//b,operator="div")
    return HttpResponse("a= "+str(a) +" b= "+str(b)+ " a//b= "+str(int(a)//int(b)))
 else :
    request.method == 'POST'
    param=dict(request.POST)
    print(param)
    a=int(param["a"][0])
    b=int(param["b"][0])
    Request.objects.create (param_a=a,param_b=b,param_c=a//b,operator="div")
    return HttpResponse("a= "+str(a) +" b= "+str(b)+ " a//b= "+str(int(a)//int(b)))
    #return HttpResponse (" I am a division")  

    
              

    