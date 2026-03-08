from django.shortcuts import render,redirect
from supabase import create_client
from django.conf import settings
from .models import Proposal

# Create your views here.
def home(request):
    if 'roll_no' not in request.session:
        return redirect('/login')

    roll_no = request.session['roll_no']
    fname = request.session.get('fname', '')

    try:
        proposal = Proposal.objects.get(roll_no=roll_no)
    except Proposal.DoesNotExist:
        proposal = None

    return render(request, 'student.html', {
        'fname': fname,
        'proposal': proposal,
    })


def submit_proposal(request):
    if 'roll_no' not in request.session:
        return redirect('/login')

    if request.method == 'POST':
        title = request.POST.get('title')
        file = request.FILES.get('file')
        roll_no = request.session['roll_no']

        # Upload file to Supabase Storage
        supabase = create_client(settings.SUPABASE_URL, settings.SUPABASE_KEY)
        file_path = f"{roll_no}/{file.name}"
        supabase.storage.from_('proposals').upload(file_path, file.read())

        # Get file URL
        file_url = supabase.storage.from_('proposals').get_public_url(file_path)

        # Save to database
        Proposal.objects.update_or_create(
            roll_no=roll_no,
            defaults={
                'title': title,
                'file_url': file_url,
                'status': 'Pending'
            }
        )

        return redirect('/student/')

    return redirect('/student/')


def logout_view(request):
    request.session.flush()
    return redirect('/login')