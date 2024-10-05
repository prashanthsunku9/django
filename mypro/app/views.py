from django.shortcuts import render,HttpResponse
from django.http import JsonResponse
from app.models import Details
import json
from django.views.decorators.csrf import csrf_exempt

# Create your views here.

def index(res):
    return HttpResponse('server started sucessfullyi')

# render consists of 2 mandatory parameters request object and template name in string format

def about(res):

    # context={
    #     "stuff":"this stuff is comming from backend server",
    #     "scrap":{
    #        "name":"prashanth sunku".title()
    #     }
    # }
    return JsonResponse({"message":"this is a json response"})
    # return render(res,'about.html',context)


@csrf_exempt  # Disable CSRF for this view
def contact(request):
    # if request.method == 'POST':
    #     try:
    #         data = json.loads(request.body)
    #         name = data.get('name')
    #         email = data.get('email')

    #         if not name or not email:
    #             return JsonResponse({"error": "Missing name or email"}, status=400)

    #         details = Details(name=name, email=email)
    #         details.save()

    #         return JsonResponse({"message": "Details saved successfully"}, status=201)

    #     except json.JSONDecodeError:
    #         return JsonResponse({"error": "Invalid JSON format"}, status=400)
    #     except Exception as e:
    #         return JsonResponse({"error": str(e)}, status=500)
    
    # return JsonResponse({"error": "Invalid request method"}, status=405)


     print(request.body)
     if request.method=='POST':
       
       data=json.loads(request.body)
       name=data.get('name')
       email=data.get('email')
       details=Details(name=name,email=email)
       details.save()

    # return HttpResponse("this is inside the contact")
   
    
       return JsonResponse({"message":"details saved successfully"},status=201)
       

    
    # return HttpResponse("this is contact us page")

def inscon(res):
    return HttpResponse("this is inside the contact")

