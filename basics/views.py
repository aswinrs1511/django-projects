from django.shortcuts import render , redirect , get_object_or_404

from basics.models import StudentDepartment, StudentDetails


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


def department(request):
    if(request.method=="POST"):
        data=request.POST
        
        deptname=data.get("textdepartmentname")
        deptdesc=data.get("textdepartmentdesc")

        StudentDepartment.objects.create(DEPT_NAME=deptname,DEPT_DESC=deptdesc)
        result = "Department details saved successfully "
        return render(request,'department.html',context={'result':result})

    return render(request,'department.html')




def departmentview(request):
    getdepartments=StudentDepartment.objects.all()
    return render(request,'departmentview.html',context={'getdepartments':getdepartments})


def marks(request):
    if(request.method=="POST"):
        data=request.POST

        hours=data.get("texthours")
        age=data.get("textage")
        internet=data.get("textinternet")

        if "predict" in request.POST:
            import pandas as pd
            path ="C:\\Users\\Aswin\\OneDrive\\Desktop\\Datanew\\Exammarks.csv"
            data = pd.read_csv(path)



            #to handle missing values find median values
            median_value=data.hours.median()
            # 7.109999999999999 is the median

            #fill missing values with median
            data.hours=data.hours.fillna(median_value)

            inputs =  data.drop('marks','columns')
            output = data.drop(['hours','age','internet'],'columns')

            import sklearn
            from sklearn import linear_model
            model=linear_model.LinearRegression()
            model.fit(inputs,output)
            result = model.predict([[float(hours),int(age),int(internet)]])

            return render(request,'marks.html',context={'result':"Marks="+str(result)})





    return render(request,"marks.html")



def departmentupdate(request,id):
    getdepartments=StudentDepartment.objects.get(id=id)
    if(request.method=="POST"):
        data=request.POST
        
        deptname=data.get("textdepartmentname")
        deptdesc=data.get("textdepartmentdesc")
        
        getdepartments.DEPT_NAME=deptname
        getdepartments.DEPT_DESC=deptdesc

        getdepartments.save()

        return redirect('/deptview/')
    return render(request,'departmentupdate.html',context={'getdepartments':getdepartments})



def student(request):
    getdepartments=StudentDepartment.objects.all()

    if request.method=="POST":
        data = request.POST

        studentname=data.get('textstudentname')
        studentemail=data.get('textstudentemail')
        studentdepartment=data.get('dropdowndepartment')

        StudentDetails.objects.create(STU_NAME=studentname,STU_EMAIL=studentemail,STU_DEPT=studentdepartment)
        result = "Student details saved successfully "
        return render(request,'student.html',context={'result':result})


    return render(request,'student.html',context={'getdepartments':getdepartments})


def studentview(request):
    getstudents=StudentDetails.objects.all()
    return render(request,'studentview.html',context={'getstudents':getstudents})

def delete_student(request, student_id):
    student = get_object_or_404(StudentDetails, id=student_id)
    if request.method == "POST":
        student.delete()
        return redirect('studentview')  # Update to match the name of your student list view
    return render(request, 'confirm_delete.html', {'student': student})
