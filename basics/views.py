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


def calc(request):
    #taking inputs
    if(request.method=="POST"):
        data=request.POST
        
        firstnumber=data.get("firstNumber")
        firstnumber=int(firstnumber)
        
        secondnumber=data.get("secondNumber")
        secondnumber=int(secondnumber)

        #on button press
        if("Add" in request.POST):
            result = firstnumber+secondnumber
            print(result)
            return render(request,"calc.html",context={"result":"Sum="+str(result)})
        elif("Subtract" in request.POST):
            result = firstnumber-secondnumber
            print(result)
            return render(request,"calc.html",context={"result":"Difference="+str(result)})
        elif("Multiply" in request.POST):
            result = firstnumber * secondnumber
            print(result)
            return render(request,"calc.html",context={"result":"Product="+str(result)})
        elif("Divide" in request.POST):
            result = firstnumber/secondnumber
            print(result)
            return render(request,"calc.html",context={"result":"Division="+str(result)})
        
        else:
            print("Enter valid")
    return render(request,'calc.html')


def index(request):
    return render(request,'index.html')