from django.shortcuts import render
from django.template import loader
from django.http import HttpResponseRedirect
from .forms import NameForm
from . import chatbot as c 
# Create your views here.



def index(request):
	if request.method == "POST":
		word=request.POST.get("name",None)
		response=c.respond(word)
		if word == "Bye":
			response = "Bye"

		context = {
		'response':response,
		'word':word
		}
		return render(request, 'polls/name.html', context)

					

			


	return render(request,'polls/name.html',{})



def registration(request):
	return render(request,'polls/Registration/RegHome.html')


def login(request):
	return render(request,'polls/Customer log in/home.html')

def ForgHome(request):
	return render(request,'polls/Customer log in/ForgHome.html')



	



	
	
		