

from multiprocessing import context
from django.shortcuts import redirect, render
import random 


def index(request):
    request.session["great_num"]= random.randint(1, 100)
    print(request.session["great_num"])
    return render(request, "index1.html")


def RanNum(request):
    num = int(request.POST['num'])

    def checking():
        if num == request.session["great_num"]:
            return 0
        elif num < request.session["great_num"]:
            return 1
        else:
            return 2


    context = {
    "arterCheck":int(checking())
           }
    return render(request,"index1.html",context)
