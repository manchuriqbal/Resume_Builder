from django.shortcuts import render
from django.http import HttpResponse
from django.template import loader

import pdfkit
import io

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

    return render(request, 'templates/pdf/index.html')


def resume(request, pk):
    user_profile = Profile.objects.get(pk=pk)
    template = loader.get_template('templates/pdf/resume.html')
    html = template.render({'user_profile':user_profile})
    option = {
        'page-size' : 'Letter',
        'encoding' : 'UTF-8'
    }
    pdf_config = pdfkit.configuration(wkhtmltopdf='C:\Program Files\wkhtmltopdf\\bin\wkhtmltopdf.exe')
    pdf = pdfkit.from_string(html, False, option, configuration=pdf_config)
    response = HttpResponse(pdf,content_type='application/pdf')
    response['Content-Dispositon'] = 'attachments'
    return response

def list(request):
    profile = Profile.objects.all()
    return render(request, 'templates/pdf/list.html', {'profile': profile})