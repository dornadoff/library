from django.shortcuts import render, redirect
from django.views import View
from .models import *

def loginview(request):
    return render(request, "login.html")

class MuallifView(View):
    def get(self, request):
        data = {
            "muallif":Muallif.objects.all()
        }
        return render(request, "muallif.html", data)

    def post(self, request):
        Muallif.objects.create(
            ism=request.POST.get("ism"),
            tirik = True,
            kitob_soni = request.POST.get("kitob_soni"),
            jins = request.POST.get("jins"),
            tugilgan_sana = request.POST.get("tugilgan_sana")
        )
        return redirect("/muallif/")

class KitobView(View):
    def get(self, request):
        data = {
            "kitob":Kitob.objects.all(),
            "muallif":Muallif.objects.all()
        }
        return render(request, "kitob.html", data)

    def post(self, request):
        Kitob.objects.create(
            nom=request.POST.get("nom"),
            sahifa=request.POST.get("sahifa"),
            muallif=Muallif.objects.get(id=request.POST.get("muallif")),
            janr=request.POST.get("janr")
        )
        return redirect("/kitob/")

class TalabView(View):
    def get(self, request):
        data = {
            "talaba":Talaba.objects.all()
        }
        return render(request, "talaba.html", data)

    def pots(self, request):
        Talaba.objects.create(
            ism=request.POST.get("ism"),
            bitiruvchi=True,
            kitobla_soni=request.POST.get("kitoblar_soni"),
            kurs = request.POST.get("kurs")
        )
        return redirect("/talaba/")

class AdminView(View):
    def get(self, request):
        data = {
            "admin":Admin.objects.all()
        }
        return render(request, "admin.html", data)

    def pots(self, request):
        Admin.objects.create(
            ism=request.POST.get("ism"),
            ish_vaqti="11:00:00"
        )
        return redirect("/adminview/")

class RecordView(View):
    def get(self, request):
        data = {
            "record":Record.objects.all(),
            "talaba":Talaba.objects.all(),
            "kitob":Kitob.objects.all(),
            "admin":Kitob.objects.all()
        }
        return render(request, "record.html", data)

    def pots(self, request):
        Record.objects.create(
            talaba=Talaba.objects.get(id=request.POST.get("talaba")),
            kitob=Kitob.objects.get(id=request.POST.get("kitob")),
            admin=Admin.objects.get(id=request.POST.get("admin")),
            olingan_sana=request.POST.get("olingan_sana"),
            qaytarsih_sana=request.POST.get("qaytarish_sana"),
            qaytardi=False
        )
        return redirect("/record/")