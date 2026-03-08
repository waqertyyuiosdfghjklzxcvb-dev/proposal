# from django.shortcuts import render

# # Create your views here.
# def server(request):
#     return render(request,'server.html')

from django.shortcuts import render, redirect
from .models import Teacher
from student.models import Proposal

def login(request):
    if request.method == 'POST':
        roll_no = request.POST.get('roll_no')
        password = request.POST.get('password')

        try:
            teacher = Teacher.objects.get(roll_no=roll_no)
            if teacher.password != password:
                return render(request, 'teacher_login.html', {'error': 'Invalid password'})

            request.session['teacher_roll_no'] = teacher.roll_no
            request.session['teacher_name'] = teacher.name
            return redirect('/teacher/dashboard')

        except Teacher.DoesNotExist:
            return render(request, 'teacher_login.html', {'error': 'No account found'})

    return render(request, 'teacher_login.html')


def dashboard(request):
    if 'teacher_roll_no' not in request.session:
        return redirect('/teacher/login')

    status_filter = request.GET.get('status', 'All')

    if status_filter == 'All':
        proposals = Proposal.objects.all().order_by('-submitted_at')
    else:
        proposals = Proposal.objects.filter(status=status_filter).order_by('-submitted_at')

    return render(request, 'teacher_dashboard.html', {
        'proposals': proposals,
        'teacher_name': request.session['teacher_name'],
        'status_filter': status_filter,
        'total': Proposal.objects.count(),
        'pending': Proposal.objects.filter(status='Pending').count(),
        'approved': Proposal.objects.filter(status='Approved').count(),
        'rejected': Proposal.objects.filter(status='Rejected').count(),
    })


def review_proposal(request, proposal_id):
    if 'teacher_roll_no' not in request.session:
        return redirect('/teacher/login')

    proposal = Proposal.objects.get(id=proposal_id)

    if request.method == 'POST':
        status = request.POST.get('status')
        feedback = request.POST.get('feedback')

        proposal.status = status
        proposal.feedback = feedback
        proposal.save()

        return redirect('/teacher/dashboard')

    return render(request, 'teacher_review.html', {'proposal': proposal})


def logout(request):
    request.session.flush()
    return redirect('/teacher/login')