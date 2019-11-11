from django.http import HttpResponse
from django.shortcuts import render
from .form import ContactForm


etudiants=[
	{'id':1,"nom":'KOTA',"promotion":"L2","pourcentage":71},
	{'id':2,"nom":'SEKA',"promotion":"L2","pourcentage":70},
	{'id':1,"nom":'LUFUNGULA',"promotion":"L2","pourcentage":68},
	{'id':1,"nom":'TSHANDA',"promotion":"G2","pourcentage":64},
	{'id':1,"nom":'MUSEME',"promotion":"L1","pourcentage":52},
	{'id':1,"nom":'KASONGO',"promotion":"G1","pourcentage":70},
	{'id':1,"nom":'KIPEMBA',"promotion":"G2","pourcentage":60},
	{'id':1,"nom":'BAKOMBA',"promotion":"G2","pourcentage":63},
	{'id':1,"nom":'KATETA',"promotion":"L2","pourcentage":64},
	{'id':1,"nom":'ONANU',"promotion":"L2","pourcentage":58},
	]

def home_page(request):

	
	#context={"etudiant":etudiants}
	return render(request,"home_page.html",{})



def about_page(request):

	
	context={"etudiant":etudiants}
	return render(request,"home_page.html",context)




def contact_page(request):
	formulaire=ContactForm(request.POST or None)

	etudiants_l2=list(filter(lambda et:et['nom']=='kota'.upper(),etudiants))
	context={"title":"Welcome to the contact",
			"form":formulaire}
	if formulaire.is_valid():
		print(formulaire.cleaned_data)
		
	return render(request,"contact/view.html",context)




def student_page(request):

	etudiants_l2=list(filter(lambda et:et['nom']=='kota'.upper(),etudiants))
	context={"etudiant":etudiants_l2}
	return render(request,"home_page.html",context)































def home_page_Old(request):
	html_body="""
	<!DOCTYPE html>
		<html>
		<head>
			<title>Projet Django</title>
			<link rel="stylesheet" href="https://stackpath.bootstrapcdn.com/bootstrap/4.3.1/css/bootstrap.min.css">
		</head>
		<body>
			
			<div class="container">
				<h1 class=text-center> Hello Word </h1>
			</div>
		  
		</body>
		</html>
	"""
	return HttpResponse(html_body)
