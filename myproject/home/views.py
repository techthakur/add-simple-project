from home.models import Student
from django.http.response import HttpResponse
from django.shortcuts import render,redirect
from django.contrib.auth.models import User
from django.contrib.auth import authenticate,login,logout
from datetime import datetime
from django.contrib import messages

# Create your views here.

def home(request):
    return render(request, "home.html")

    







def handlesignup(request):
    if request.method == "POST":
        username = request.POST['username']
        fname = request.POST['fname']
        lname = request.POST['lname']
        email = request.POST['email']
        pass1 = request.POST['pass1']
        pass2 = request.POST['pass2']


        if len(username)<1:
            messages.success(request,    ' Please fill the form ! Try Again ')
            return redirect('home')


        if len(username)>15:
            messages.success(request,    'Take Username is under 15 characters! Please Try Again ')
            return redirect('home')

        if len(username)<4:
            messages.success(request,    ' Your Username is to Smaller! Please Try Again ')
            return redirect('home')
            
        if not username.isalnum():
            messages.success(request,    ' Take Username Only letter or number ! Please Try Again ')
            return redirect('home')



        # check first name 
        if len(fname)>15:
            messages.success(request,    ' Your First name is to Long ! Please Try Again ')
            return redirect('home')
        

        if len(fname)<2:
            messages.success(request,    ' Your First name is to Smaller ! Please Try Again ')
            return redirect('home')
        

        


        # check Last Name
        if len(lname)>15:
            messages.success(request,    ' Your Last Name is to Long ! Please Try Again ')
            return redirect('home')
        

        if len(lname)<2:
            messages.success(request,    ' Your Last name is to Smaller ! Please Try Again ')
            return redirect('home')

        
        # check password
        if len(pass1)<3:
            messages.success(request,    ' Your Password is to week  ! Please Try Again ')
            return redirect('home')





        if pass1 != pass2:
            messages.success(request,    ' Your Password is does not  match ! Please Try Again ')
            return redirect('home')

        myuser = User.objects.create_user(username,email,pass1)
        myuser.first_name = fname
        myuser.last_name = lname
        myuser.save()
        messages.success(request, ' Your Account has been created successfully !')
        return redirect('home')

    
    else:

        return HttpResponse("  error  404 ")












def handlelogin(request):
    if request.method == "POST":
        loginuser = request.POST['loginuser']
        loginpass = request.POST['loginpass']
        user = authenticate(username=loginuser , password = loginpass)

        if len(loginuser)<1:
            messages.success(request, ' Please fill the form ! try again ')
            return redirect('home')


        if user is not None:
            login(request,user)
            messages.success(request, 'you are successfully logged in ')
            return redirect('home')

        else:
            messages.success(request, 'invalid username or password ! Please Try')
            return redirect('home')

    return HttpResponse(" error  404 ")








def handlelogout(request):
    logout(request)
    return redirect('home')









def student(request):
    if request.method == "POST":
        name = request.POST.get('name')
        college = request.POST.get('college')
        rollnumber = request.POST.get('rollnumber')
        phone = request.POST.get('phone')
        desc = request.POST.get('desc')
        student =Student(name=name, college=college, rollnumber=rollnumber,   phone=phone, desc=desc, date=datetime.today())

        
        if len(name)<1:
            messages.error(request, ' Please fill the form ! try Again')
            return redirect('home')

        if len(name)<3:
            messages.success(request, ' Your name is to Smaller ! Please try Again')
            return redirect('home')

        if len(college)<3:
            messages.success(request, ' Your name is to Smaller ! Please try Again')
            return redirect('home')

        if len(phone)<5:
            messages.success(request, 'Your phone number is to Smaller ! Please try Again')
            return redirect('contact')

        if len(phone)>13:
            messages.success(request, 'Your phone number is to long ! Please try Again')
            return redirect('contact')

        if len(desc)<4:
            messages.success(request,    ' Please fill More  Contant ! in Description ')
            return redirect('contact')


        student.save()
        messages.success(request, ' Your message has been sent! ')
    return render(request, "student.html")





















