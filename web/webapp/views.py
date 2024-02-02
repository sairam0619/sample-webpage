from django.shortcuts import render, redirect
from .forms import UserForm
from .models import UserSubmission
from datetime import datetime

def index(request):
    form = UserForm()
    if request.method == 'POST':
        form = UserForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('submission_success')
    return render(request, 'index.html', {'form': form})

def submission_success(request):
    submissions = UserSubmission.objects.all()
    current_time = datetime.now()
    return render(request, 'submission_success.html', {'submissions': submissions, 'current_time': current_time})
