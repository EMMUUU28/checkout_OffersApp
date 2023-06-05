from django.shortcuts import render
from .models import Discount,Result
from django.contrib import messages

# Create your views here.
def index(request):
    
 offers=Discount.objects.all()
 result=Result.objects.create()
 
 for i in offers:
        c=request.POST.get(str(i.id))
        if c == '':
            result.discount.add(i) 
            result_discounts = result.discount.all()  # Retrieve the discounts associated with the result
            print(result_discounts)
        else:
            print("no")
 result.save()


 params={'offer':offers,'message':"Your choices have been saved successfully!"}
 return render(request,"index.html",params)