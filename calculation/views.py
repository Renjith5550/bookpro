from django.shortcuts import render
from django.views.generic import View
from calculation.forms import OperationForm
# Create your views here.
class IndexView(View):
    def get(self,request):
        return render(request,"home.html")

class AddView(View):
    def get(self,request):
        form=OperationForm()
        return render(request,"add.html",{"form":form})
    def post(self,request):
        # n1=int(request.POST.get("num1"))
        # n2=int(request.POST.get("num2"))
        form=OperationForm(request.POST)
        if form.is_valid():
            n1=form.cleaned_data.get("num1")
            n2=form.cleaned_data.get("num2")
            result=int(n1)+int(n2)
            return render(request,"add.html",{"result":result})
        else:
            return render(request,"add.html",{"form":form})
def add(request):
    print(request.method)
    if request.method=="POST":
        n1=int(request.POST.get("num1"))
        n2=int(request.POST.get("num2"))
        result=n1+n2
        return render(request,"add.html",{"result": result})
    return render(request,"add.html")
class SubView(View):
    def get(self,request):
        form=OperationForm()
        return render(request,"sub.html",{"form":form})
    def post(self,request):
        # n1=int(request.POST.get("num1"))
        # n2=int(request.POST.get("num2"))
        form = OperationForm(request.POST)
        if form.is_valid():
            n1 = form.cleaned_data.get("num1")
            n2 = form.cleaned_data.get("num2")
            result=int(n1)-int(n2)
            return render(request,"sub.html",{"result":result})
        else:
            return render(request, "sub.html", {"form": form})
def sub(request):
    if request.method=="POST":
        n1 = int(request.POST.get("num1"))
        n2 = int(request.POST.get("num2"))
        result=n1-n2
        return render(request,"sub.html", {"result": result})
    return render(request,"sub.html")
class MulView(View):
    def get(self,request):
        form=OperationForm
        return render(request,"Mul.html",{"form":form})
    def post(self,request):
        # n1=int(request.POST.get("num1"))
        # n2=int(request.POST.get("num2"))
        form = OperationForm(request.POST)
        if form.is_valid():
            n1 = form.cleaned_data.get("num1")
            n2 = form.cleaned_data.get("num2")
            result=int(n1)*int(n2)
            return render(request,"Mul.html",{"result":result})
        else:
            return render(request, "Mul.html", {"form": form})
def mul(request):
    if request.method == "POST":
        n1 = int(request.POST.get("num1"))
        n2 = int(request.POST.get("num2"))
        result=n1*n2
        return render(request,"mul.html", {"result": result})
    return render(request,"mul.html")
class DivView(View):
    def get(self,request):
        form=OperationForm()
        return render(request,"Div.html",{"form":form})
    def post(self,request):
        # n1=int(request.POST.get("num1"))
        # n2=int(request.POST.get("num2"))
        form = OperationForm(request.POST)
        if form.is_valid():
            n1 = form.cleaned_data.get("num1")
            n2 = form.cleaned_data.get("num2")
            result=int(n1)/int(n2)
            return render(request,"Div.html",{"result":result})
        else:
            return render(request, "Div.html", {"form": form})
def div(request):
    if request.method == "POST":
        n1 = int(request.POST.get("num1"))
        n2 = int(request.POST.get("num2"))
        result=n1/n2
        return render(request,"div.html", {"result": result})
    return render(request,"div.html")
def getvowels(request):
    if request.method == "POST":
        word=request.POST.get("word")
        vowels=[ char for char in word if char in["a","e","i","o","u"]]
        return render(request,"getwov.html",{"result":vowels})
    return render(request,"getwov.html")