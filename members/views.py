from django.http import HttpResponse , HttpResponseRedirect
from django.template import loader
from django.shortcuts import render
from django.urls import reverse
from .forms import ImageForm , ImageForm2
from .models import Lost , Find
from .models import Members
import face_recognition 
import re
 
#................
def index(request):
  mymembers = Members.objects.all().values()
  template = loader.get_template('login.html')
  
  context = {
    'mymembers': mymembers,
  }
  return HttpResponse(template.render(context, request))

def add(request):
  template = loader.get_template('add.html')
  return HttpResponse(template.render({}, request))

def addrecord(request):
  x = request.POST['User']
  y = request.POST['Password']
  Email = request.POST['Email']
  member = Members(Username=x, Password=y, Email = Email)
  member.save()
  return HttpResponseRedirect(reverse('index'))

  
def login(request):
  UserName = request.POST['uname']
  UserPassword = request.POST['psw']
  if ((Members.objects.filter(Username = UserName).values()) and (Members.objects.filter(Password = UserPassword).values())):
    template = loader.get_template('main.html')
    return HttpResponse(template.render({}, request))
  else:
    return HttpResponseRedirect(reverse('index'))

def Lost(request):
  if request.method == "POST":
    form = ImageForm(request.POST, request.FILES)
    if form.is_valid():
      form.save()
  form = ImageForm()
  return render(request, 'Lost.html',{'form':form})

def Find(request):
  global r1
  img_name_f = "<MultiValueDict: {'photo': [<InMemoryUploadedFile: img1.jpg (image/jpeg)>]}>"

  if request.method == "POST":
    form = ImageForm2(request.POST, request.FILES)
    print("this>*****************************************************************************************************")
    print(str(request.FILES))
    img_name_f = str(request.FILES)

    if form.is_valid():
      form.save()
    #************************
      x = img_name_f.split(":")
      print(x)
      for y in x:
        print(y)
      z = y.split("(")

      print(z)

      for z1 in z:
        r1=z1.strip()
        break
      print(r1)
    #************************  
  
  form = ImageForm2()
  
  return render(request, 'find.html',{'form':form})

def Search(request):

  #Image comparison
  print("////////////////////////////////////////////////////")
  print(r1)
  Find_U = face_recognition.load_image_file('/Users/alrif/Desktop/SE4A Project/media/Find_Images/' + str(r1))
  Img_Find = Members.objects.raw('SELECT id, photo from members_lost')
  for testuser in Img_Find:
    Sr_Lost_User = testuser.photo.split('/')
    print("photo:")
    print(Sr_Lost_User)
    print(Sr_Lost_User[-1])
    Lost_U = face_recognition.load_image_file('/Users/alrif/Desktop/SE4A Project/media/Lost_Images/' + Sr_Lost_User[-1])
    Recog_Image1 = face_recognition.face_encodings(Find_U)[0]
    Recog_Image2 = face_recognition.face_encodings(Lost_U)[0]
    result = face_recognition.compare_faces([Recog_Image1],Recog_Image2 )
    if result[0]:
      mymembers = "Match Found for " + r1 
      print("True")
      break
    else:
      mymembers = "Match not Found for " + r1
      print("False")

  return HttpResponse(mymembers)