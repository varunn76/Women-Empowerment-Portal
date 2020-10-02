from django.shortcuts import redirect
from .models import Feedback


def feedback(request):
    if request.method == "POST":
        first_name = request.POST['first_name']
        last_name = request.POST['last_name']
        email = request.POST['email']
        phone_no = request.POST['phone_no']
        message = request.POST['message']
        fdback = Feedback(first_name=first_name, last_name=last_name, email=email, Phone_no=phone_no, message=message)
        fdback.save()
        return redirect('/')