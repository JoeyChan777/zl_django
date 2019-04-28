from django.shortcuts import render,redirect,reverse
from .models import Student
from .forms import StudentsForm


def index(request):
    students = Student.objects.all()
    if request.method == 'POST':
        form = StudentsForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect(reverse('student:index'))
    else:
        form = StudentsForm()
        context = {
            'students': students,
            'form': form
        }
        return render(request, 'student/index.html', context=context)