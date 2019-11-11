from django.shortcuts import render




posts=[
		{"author":"CoreyMs",
		 "title":"Blog post First",
		 "content":"First post content",
		 "date_posted":" Novenmber 11, 2019"
		},
		{"author":"Rosaire",
		 "title":"Blog post Second",
		 "content":"Second post content",
		 "date_posted":" Novenmber 12, 2019"
		},
		{"author":"Wivine",
		 "title":"Blog post Third",
		 "content":"Third...Lorem ipsum... post content",
		 "date_posted":" Novenmber 12, 2019"
		}
]



def home(request):
	post_p=list(filter(lambda p:p['author']=='Rosaire' or p['author']=='CoreyMs',posts ))
	context={"posts":post_p}
	return render(request,"blog/home.html",context)

