from django.shortcuts import render, redirect
from covid19callcenter.models import Caller, Patient

def index(request):
    return render(request, "covid19callcenter/index.html")

def behalf(request):
    if request.POST.get("yes") == "yes":
        caller = Caller(firstName = request.POST['firstName'], lastName = request.POST['lastName'], age = request.POST['age'], phoneNumber = request.POST['phone'], gender = request.POST['gender'], address = request.POST['address'])
        caller.save()
        return render(request, "covid19callcenter/behalf.html")
    global age
    age = int(request.POST['age'])
    global person
    person = Patient(firstName = request.POST['firstName'], lastName = request.POST['lastName'], age = request.POST['age'], phoneNumber = request.POST['phone'], gender = request.POST['gender'], address = request.POST['address'])
    person.save()
    return render(request, "covid19callcenter/suspected.html")

def suspected(request):
    if request.POST.get("yes") == "yes":
        return render(request, "covid19callcenter/positivetest.html")
    return render(request, "covid19callcenter/additional.html")

def test(request):
    if request.POST.get("yes") == "yes":
        return render(request, "covid19callcenter/testyessymp.html")
    return render(request, "covid19callcenter/testnosymp.html")

def risk(request):
    if request.POST.get("yes") == "yes":
        return render(request, "covid19callcenter/monitor-phy.html")
    return render(request, "covid19callcenter/fine.html")

def yessymp(request):
    if request.POST.get("yes") == "yes":
        return render(request, "covid19callcenter/call140.html")
    return render(request, "covid19callcenter/risk.html")

def nosymp(request):
    if request.POST.get("yes") == "yes":
        return render(request, "covid19callcenter/call140.html")
    elif request.POST.get("no") == "no" and age > 2:
        return render(request, "covid19callcenter/interact.html")
    else:
        #if patient is younger than 2, the website will take you to the main page
        return render(request, "covid19callcenter/index.html")

def interact(request):
    if request.POST.get("yes") == "yes":
        return render(request, "covid19callcenter/yexpsymp.html")
    return render(request, "covid19callcenter/nexpsymp.html")

def symptoms(request):
    if request.POST.get("yes") == "yes":
        return render(request, "covid19callcenter/record.html")
    return render(request, "covid19callcenter/monitor-symp.html")

def record(request):
    person.symptoms = request.POST.get("symptoms")
    person.save()
    # once the symptoms are recorded, the website will take you to the main page
    return render(request, "covid19callcenter/index.html")

def common(request):
    if request.POST.get("common") == "common":
        return render(request, "covid19callcenter/common.html")
    return render(request, "covid19callcenter/monitor-symp.html")
