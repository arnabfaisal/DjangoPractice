from django.shortcuts import render, redirect
from django.views.generic import CreateView, ListView, UpdateView
from .forms import StudentRegistrationForm
from .models import Student 
from django.urls import reverse_lazy
from django.contrib import messages
# Create your views here.
class StudentRegistrationView(CreateView):
    form_class = StudentRegistrationForm
    template_name = 'student/studentRegistration.html'
    success_url = reverse_lazy('home')

    def form_valid(self, form):
        form.save()
        messages.success(self.request, "Student has been successfully registered!")
        return super().form_valid(form)
    


def HomeView(request):
    context = {}
    students = Student.objects.prefetch_related('coursesTaken').all()
    context['students'] = students
    return render(request, 'student/studentList.html', context)


def studentProfile(request, id):
    student = Student.objects.get(id=id)
    return render(request, 'student/studentProfile.html', {'student': student})

class StudentUpdateView(UpdateView):
    model = Student
    pk_url_kwarg = 'pk'	
    extra_context = {'edit': True}
    fields = ['name', 'email', 'phone', 'coursesTaken']
    template_name = 'student/studentRegistration.html'
    success_url = reverse_lazy('home')
    def form_valid(self, form):
        response = super().form_valid(form)
        messages.success(self.request, "Student has been successfully updated!")
        return response


def studentDelete(request, id):
    student = Student.objects.get(id=id)
    student.delete()
    messages.success(request, "Student has been successfully deleted!")
    return redirect('home')