from django.shortcuts import render,redirect

from .models import *

# Create your views here.
def form(request):
	return render(request,'form_fun.html')

def home(request):
	ob=student.objects.all()
	return render(request,'home_fun.html',{"data":ob})


def formVal(request):
	# n=request.GET['name']
	# r=request.GET['roll']
	# c=request.GET['course']
	# m=request.GET['marks']
	n=request.POST['name']
	r=request.POST['roll']
	c=request.POST['course']
	m=request.POST['marks']
	
	#print(n,' ',r,' ',c,' ',m)
	s=student()
	s.name=n
	s.roll=r
	s.course=c
	s.marks=m
	s.save()
	return redirect('/')

def update(request,enteredRoll):#jehetu ekhane arg dichhi tai urls.py a amake akta parameter dite hochhe jeta /enteredRoll lekha ache
	ob=student.objects.get(roll=enteredRoll)
	return render(request,'updateForm.html',{"data":ob})

def updateForm(request):
	n=request.POST['name']
	enteredRoll=request.POST['roll']
	c=request.POST['course']
	m=request.POST['marks']
	#print(n,' ',r,' ',c,' ',m)
	# roll er through update hochhe tai object theke roll get krte hbe ,roll readonly ache
	s=student.objects.get(roll=enteredRoll)
	s.name=n
	s.course=c
	s.marks=m
	s.save()
	return redirect('/')

def delete(request,enteredRoll):
	ob=student.objects.get(roll=enteredRoll)
	ob.delete()
	return redirect('/')

