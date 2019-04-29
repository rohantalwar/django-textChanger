#this file was made by me

from django.http import HttpResponse
from django.shortcuts import render

final_text = " "

def index(request):
	return render(request,'index.htm')
	

def about(request):
	return render(request,'about.htm');

def analyse(request):
	input_text=request.POST.get('text','default')
	remove =request.POST.get('removepun','off')
	spaceremove = request.POST.get('spaceremover','off')
	caps = request.POST.get('capitalize','off')
	charcount = request.POST.get('charcount','off')
	newlineremover = request.POST.get('newlineremover','off')
	final_text=input_text
	print(remove)
	print(input_text)
	if input_text == 'default':
		HttpResponse("Enter some Text")
	if remove == 'on' :
		temp_text=' '
		punctutaion="''!@#$%^&*();'.,/:?>'"
		for i in final_text:
			if i not in punctutaion:
				temp_text+=i
		final_text=temp_text
		
	if spaceremove == 'on' :
		temp_text =''
		space = ' '
		for i in final_text :
			if i not in space :
				temp_text+=i
		final_text = temp_text
	
	if caps ==  'on' :
		temp_text = ''
		for i in final_text :
			temp_text+=i.upper()
		final_text=temp_text	 			 		
	
	if newlineremover == 'on':
		temp_text=''
		
		for i in final_text :
			if i !='\n' and i!='\r':
				temp_text+=i
		
		final_text=temp_text		

	if charcount == 'on' :
		count = 0 
		for i in final_text:
			++count
	params1 = {'purpose':'Analyse Text','analyzed_text':final_text}		
	return render(request,'analyse_text.htm',params1)	