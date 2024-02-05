# from imaplib import _Authenticator
from django.contrib.auth import authenticate
from django.db import connection
from django.shortcuts import redirect, render
from django.http import HttpResponse
from django.contrib.auth.models import User
from django.contrib import messages
from django.contrib.auth import authenticate, login, logout
from santhosh import settings
from django.conf import settings
from django.core.mail import send_mail
from django.contrib.sites.shortcuts import get_current_site
from django.template.loader import render_to_string
from django.utils.http import urlsafe_base64_encode
from django.utils.encoding import force_bytes,force_text
from . tokens import generate_token
from django.core.mail import EmailMessage,send_mail
from django.utils.http import urlsafe_base64_decode,urlsafe_base64_encode
import mysql.connector as sql  
from django.db import connection,connections
from .models import Complaint


from django.db import connection,transaction
cursor = connection.cursor()

# Create your views here.
def home(request):
    return render(request,"login/videohome.html")


def signup(request):

    if request.method == "POST":
        username=request.POST['username']  
        fname=request.POST['firstname']
        lname=request.POST['lastname']
        email=request.POST['email']
        pass1=request.POST['password']
        pass2=request.POST['re-password']

        if User.objects.filter(username=username):
            messages.error(request, "Username alreday exits! Please try some other name")
            # return redirect('home')
            return render(request,"login/signup.html")


        # if User.objects.filter(email=email):
        #      messages.error(request, "E-mail alreday exits! Please try some other email")
        #      return redirect('home')
        if len(username)>10:
            messages.error(request, "Username must be under 10 characters")
            return render(request,"login/signup.html")

        if(pass1 != pass2):
            messages.error(request,"Password didn't match")
            return render(request,"login/signup.html")

        if not username.isalnum():
            messages.error(request, "Username must be Alpha-Numeric")
            return render(request,"login/signup.html")
        
        myuser = User.objects.create_user(username,email,pass1)
        # myuser=user(username=username,first_name=fname,last_name=lname)
        myuser.username=username
        myuser.first_name=fname
        myuser.last_name=lname
        myuser.is_active = False


        

        myuser.save()
        messages.success(request,"Your account is saved")


      



        subject = "Welcome to GFG django "
        message="Hello"+myuser.first_name + "|! \n" + "Welcome to KEC Portal \n Thank you"
        from_email = settings.EMAIL_HOST_USER
        to_list = [myuser.email]
        send_mail(subject,message,from_email,to_list, fail_silently=True)
        
       
        # Enail address confirmation mail

        current_site = get_current_site(request)
        email_subject = "Confirm your email"
        message2 = render_to_string('email_confirmation.html',{
            'name': myuser.username,
            'domain': current_site.domain,
            'uid': urlsafe_base64_encode(force_bytes(myuser.pk)),
            'token': generate_token.make_token(myuser)
        })
        email = EmailMessage(
            email_subject,
            message2,
            settings.EMAIL_HOST_USER,
            [myuser.email],
        )
        email.fail_silently = True
        email.send()


        return redirect(signin)
    
    return render(request,"login/signup.html")
         


def signin(request):


    if request.method == 'POST':
        username =request.POST['username']
        pass1=request.POST['password']

        user=authenticate(username=username, password=pass1)

        if user is not None:
            login(request, user)
            fname=user.username
            # return render(request,"login/index.html",{'fname': fname})

            
            po=Complaint.objects.filter(rollno=fname)

            print(po)
            
            print(connection.queries)
            
            return render(request,"login/videohome.html",{'data':po,'fname':fname})
        
            
        
            
        else:
            messages.error(request,"Bad Credential")
            # return redirect('home')
            return render(request, "login/signin.html")

    return render(request, "login/signin.html")

def signout(request):
    logout(request)
    messages.success(request,"Logged out successfully")
    return redirect('home')

def activate(request, uidb64, token):
    try:
        uid = force_text(urlsafe_base64_decode(uidb64))
        myuser = User.objects.get(pk=uid)
    except (TypeError,ValueError,OverflowError, User.DoesNotExist):
        myuser = None
    if myuser is not None and generate_token.check_token(myuser,token):
        myuser.is_active = True
        myuser.save()
        login(request, myuser)
        
        fname=myuser.username
        return render(request,"login/videohome.html",{'fname': fname})


        # return redirect('home')
    else:
        return render(request, 'activation_failed.html')






def videohome(request):
    return render(request,'login/videohome.html')
def complaint(request):
    return render(request,'login/complaint.html')

def another_page(request, *args, **kwargs):
    user = request.user

def student(request):
    # po=User.objects.raw("SELECT * FROM student.complaint")
      
    # po = User.objects.select_related('Complaint')
    # ("SELECT complaint.email FROM student.auth_user inner join student.complaint on student.auth_user.email=complaint.email;")
    
    po=Complaint.objects.filter(email='santhoshm.21cse@kongu.edu')

    print(po)
    print(connection.queries)
    # return redirect(request,student)
    return render(request,'login/index.html',{'data':po})

def update_complaint(request):
  
    # if request.method == "POST":
    #     name=request.POST['name'] 
    #     rollno=request.POST['rollno']
    #     dept=request.POST['branch']  
    #     section=request.POST['section'] 
    #     year=request.POST['year'] 
    #     type=request.POST['type'] 
    #     location=request.POST['location'] 
    #     describe=request.POST['describe'] 
    #     mobile=request.POST['mobile'] 
    #     email=request.POST['email'] 


    if request.method == "GET":
        name=request.GET['name'] 
        rollno=request.GET['rollno']
        dept=request.GET['branch']  
        section=request.GET['section'] 
        year=request.GET['year'] 
        type=request.GET['type'] 
        location=request.GET['location'] 
        describe=request.GET['describe'] 
        mobile=request.GET['mobile'] 
        email=request.GET['email'] 



        myuser=Complaint(name=name,rollno=rollno,branch=dept,section=section,year=year,mobile=mobile,email=email,complaint_type=type,location=location,describe=describe)
        myuser.save()
        messages.success(request,"Your complaint is saved")
        

        # cursor = connection.cursor()

    
    
        # query = "INSERT INTO complaint (name,rollno,email) VALUES (%s,%s,%s)",[name,rollno,email]
      
    # here build_query_list() represents some function to populate
    # the list with multiple records
    # in the tuple format (value1, value2, value3).
    
    
        # cursor.execute("INSERT INTO student.complaint (name,rollno,branch,section,year,mobile,email,complaint_type,location,describe) VALUES (%s,%s,%s,%s,%s,%s,%s,%s,%s,%s)",['name','rollno','dept','section','year','mobile','email','type','location','describe'])
        return render(request,"login/complaint.html")
    else:
        return render(request,"login/signin.html")
    
    
