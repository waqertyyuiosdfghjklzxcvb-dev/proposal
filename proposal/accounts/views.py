from django.shortcuts import render,redirect
from django.http import HttpRequest,HttpResponse
from .models import Register

# Create your views here.

def register(request):

    if request.method == 'POST':
        fname = request.POST.get('fname')
        lname = request.POST.get('lname')
        roll_no = request.POST.get('roll_no')
        program = request.POST.get('program')
        section = request.POST.get('section')
        email = request.POST.get('email')
        phone_no = request.POST.get('phone_no')
        password = request.POST.get('password')

        if Register.objects.filter(roll_no=roll_no).exists():
            return render(request, "register.html", {'error': 'This Roll No is already registered!'})

        if Register.objects.filter(email=email).exists():
            return render(request, "register.html", {'error': 'This email is already registered!'})

        student = Register(fname=fname,lname=lname,roll_no=roll_no,program=program,section=section,email=email,phone_no=phone_no,password=password)
        student.save()   

        return render(request, "register.html", {'success': 'Account created successfully! You can now login.'})

    return render(request,"register.html")


def login(request):
    if request.method == 'POST':
        roll_no = request.POST.get('roll_no')
        program = request.POST.get('program')
        password = request.POST.get('password')

        try:
            student = Register.objects.get(roll_no=roll_no)

            if student.program != program:
                return render(request, "login.html", {'error': 'Invalid program'})

            if student.password != password:
                return render(request, "login.html", {'error': 'Invalid password'})

            request.session['roll_no'] = student.roll_no
            request.session['program'] = student.program
            request.session['fname'] = student.fname

            return redirect('/student/')  

        except Register.DoesNotExist:
            return render(request, "login.html", {'error': 'No account found with this roll number'})

    return render(request, "login.html")


