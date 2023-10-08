from django.shortcuts import render

from pdf.models import Profile

def index(request):
    if request.method == 'POST':
        name = request.POST['name']
        phone= request.POST['phone']
        email= request.POST['email']
        school= request.POST['school']
        degree= request.POST['degree']
        university= request.POST['university']
        skill= request.POST['skill']
        about_you= request.POST['about_you']
        previous_work= request.POST['previous_work']

        profil = Profile(name=name, phone=phone, email=email, school=school, degree=degree, university=university, skill=skill, about_you=about_you, previous_work=previous_work)
        profil.save()

    return render(request, 'pdf/index.html')
