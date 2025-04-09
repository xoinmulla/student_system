from django.shortcuts import render, redirect, get_object_or_404
from .models import Student
from .forms import StudentForm

def home(request):
    return render(request, 'admissions/home.html')

def student_list(request):
    students = Student.objects.all()
    return render(request, 'admissions/index.html', {'students': students})

def student_detail(request, pk):
    student = get_object_or_404(Student, pk=pk)
    return render(request, 'admissions/student_detail.html', {'student': student})

def add_student(request):
    if request.method == 'POST':
        form = StudentForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('student_list')
    else:
        form = StudentForm()
    return render(request, 'admissions/add_student.html', {'form': form})
