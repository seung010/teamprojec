from django.shortcuts import render,redirect



def product(request):
    #인덱스를 실행시킬 때 


   return render(request, 'product/index.html')


def purchase(request):

   if request.method == "POST": 
      u = request.user
      up = request.POST.get("productnum")
      ucnum = request.POST.get("cardnum")
      ucname = request.POST.get("cardname")
      ucexp = request.POST.get("cardexp")
      ucvv = request.POST.get("cardCVV")
      u.productnum = up
      u.cardname = ucname
      u.cardnum = ucnum
      u.Expiration = ucexp
      u.CVV = ucvv
      u.save()
      return redirect('product:index')

   return render(request, 'product/purchase.html')

def product_check(request):


   return render(request, 'product/product_check.html')

def product_cancel(request):
   u = request.user
   u.productnum = ""
   u.save()
   return redirect('Main:index')


