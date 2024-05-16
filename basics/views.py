from django.shortcuts import render


# Create your views here.
def about(request):
    return render(request,'about.html')

def aboutus(request):
    return render(request,'aboutus.html')

def register(request):
    #taking inputs
    if(request.method=="POST"):
        data=request.POST
        firstname=data.get("firstName")
        lastname=data.get("lastName")
        #on button press
        if("buttonSubmit" in request.POST):
            result = firstname+" "+lastname
            print(result)
            return render(request,"register.html",context={"result":result})

    return render(request,'register.html')