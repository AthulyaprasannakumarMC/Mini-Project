from datetime import datetime, date

import razorpay

from django.contrib.auth.decorators import login_required
from django.core.files.storage import FileSystemStorage
from django.http import HttpResponse
from django.shortcuts import render, redirect
from django.contrib import auth

from CH_App.models import *


def main(request):
     return render(request,'Login/lo_index.html')

def logout(request):
    auth.logout(request)
    return render(request,"Login/lo_index.html")


def logincode(request):
    username=request.POST['textfield']
    password=request.POST['textfield2']
    try:
        ob=login_table.objects.get(username=username,password=password)
        if ob.type=="admin":
            request.session['lid'] = ob.id
            ob1 = auth.authenticate(username='admin', password='123')
            if ob1 is not None:
                auth.login(request, ob1)
            return HttpResponse('''<script>alert("Welcome Admin");window.location="/Homepage"</script>''')
        elif ob.type == "hardwareshop":
            request.session['lid'] = ob.id
            ob1 = auth.authenticate(username='admin', password='123')
            if ob1 is not None:
                auth.login(request, ob1)
            return HttpResponse('''<script>alert("Welcome Shop");window.location="/HWHome"</script>''')
        elif ob.type == "user":
            request.session['lid'] = ob.id
            ob1 = auth.authenticate(username='admin', password='123')
            if ob1 is not None:
                auth.login(request, ob1)
            return HttpResponse('''<script>alert("Welcome User");window.location="/UserHome"</script>''')
        elif ob.type == "blocked":
            return HttpResponse('''<script>alert("Account is Blocked");window.location="/"</script>''')

        else:
            return HttpResponse('''<script>alert("invalid");window.location="/"</script>''')


    except:
        return HttpResponse('''<script>alert("invalid");window.location="/"</script>''')



@login_required(login_url='/')

def AddCategory(request):
    return render(request,'Admin/Add Category.html')

@login_required(login_url='/')

def BlockUnblock(request):
    ob=hardwareshops_table.objects.all()
    return render(request,'Admin/Block and  Unblock.html',{'val':ob})


def blk_a_sch(request):
    n=request.POST['textfield']
    ob=hardwareshops_table.objects.filter(name__icontains=n)
    return render(request,"Admin/Block and  Unblock.html",{'val':ob})
@login_required(login_url='/')

def shop_sch(request):
    n=request.POST['textfield']
    ob = hardwareshops_table.objects.filter(name__icontains=n)
    return render(request,"Admin/Hardware shop accept_reject.html",{'val':ob})
@login_required(login_url='/')

def blk_hws(request,id):
    ob=login_table.objects.get(id=id)
    ob.type='blocked'
    ob.save()
    return HttpResponse('''<script>alert("Blocked");window.location='/BlockUnblock#about'</script>''')
@login_required(login_url='/')

def unblk_hws(request,id):
    ob=login_table.objects.get(id=id)
    ob.type='hardwareshop'
    ob.save()
    return HttpResponse('''<script>alert("UnBlocked");window.location='/BlockUnblock#about'</script>''')
@login_required(login_url='/')

def feedd_sch(request):
    n=request.POST['date']
    ob=feedback_table.objects.filter(date=n)
    return render(request,"Admin/Feedback and ratings.html",{'val':ob})
@login_required(login_url='/')

def a_comp_sch(request):
    n=request.POST['date']
    ob=complaint_table.objects.filter(date=n)
    return render(request,"Admin/Complaints and Replies.html",{'val':ob})

def Categorymgmt(request):
    ob = category_table.objects.all()
    return  render(request,'Admin/category mgmt.html',{'val':ob})
@login_required(login_url='/')

def dlt_catergory(request,id):
    ob=category_table.objects.get(id=id)
    ob.delete()
    return HttpResponse('''<script>alert("Deleted");window.location='/Categorymgmt#about'</script>''')
@login_required(login_url='/')

def notn_a_sch(request):
    n=request.POST['date']
    ob=notification_table.objects.filter(date=n)
    return render(request,"Admin/Notification.html",{'val':ob})
@login_required(login_url='/')

def addcategory(request):
    name=request.POST['textfield']
    ob=category_table()
    ob.name=name
    ob.save()
    return HttpResponse('''<script>alert("Added");window.location="/Categorymgmt#about"</script>''')

@login_required(login_url='/')

def Complaintsreplies(request):
    ob=complaint_table.objects.all()
    return render(request,'Admin/Complaints and Replies.html',{'val':ob})
@login_required(login_url='/')

def Feedbackratings(request):
    ob=feedback_table.objects.all()
    return render(request,'Admin/Feedback and ratings.html',{'val':ob})
@login_required(login_url='/')



def Homepage(request):
    return render(request,'Admin/admin_index.html')

def HwRegister(request):
    return render(request,'Admin/Hw Registerationpage.html')

@login_required(login_url='/')
def Hardwareshop_verify(request):
    ob=hardwareshops_table.objects.all()
    return render(request,'Admin/Hardware shop accept_reject.html',{'val':ob})

@login_required(login_url='/')
def accept_hw(request,id):
    ob=login_table.objects.get(id=id)
    ob.type="hardwareshop"
    ob.save()
    return HttpResponse('''<script>alert(" Accepted");window.location="/Hardwareshop_verify#about"</script>''')

@login_required(login_url='/')
def reject_hw(request,id):
    ob=login_table.objects.get(LOGIN__id=id)
    ob.type="Reject"
    ob.save()
    return HttpResponse('''<script>alert(" Rejected");window.location="/Hardwareshop_verify#about"</script>''')



@login_required(login_url='/')
def NotificationAdd(request):
    return render(request,'Admin/Notification Add.html')

@login_required(login_url='/')
def addnotifications(request):
    notification=request.POST['textfield']
    ob=notification_table()
    ob.notification=notification
    ob.date=datetime.today()
    ob.save()
    return HttpResponse('''<script>alert("Added");window.location="/mng_Notification#about"</script>''')

@login_required(login_url='/')
def mng_Notification(request):
    ob = notification_table.objects.all()
    return render(request,'Admin/Notification.html',{'val':ob})

@login_required(login_url='/')
def dlt_notn(request,id):
    ob=notification_table.objects.get(id=id)
    ob.delete()
    return HttpResponse('''<script>alert("Deleted");window.location='/mng_Notification#about'</script>''')




# =====================hardware=========================================================================>
@login_required(login_url='/')

def add_transaction(request):
    ob=products_table.objects.all()
    return render(request,'HardwareShops/Add_transactn.html',{'val':ob})

@login_required(login_url='/')

def editV_transaction(request,id):
    ob=transaction.objects.get(id=id)
    ob1=products_table.objects.all()
    request.session['tid']=id
    return render(request,'HardwareShops/edit_transactn.html',{'val':ob,'val2':ob1})

@login_required(login_url='/')

def dlt_trans(request,id):
    ob = transaction.objects.get(id=id)
    ob.delete()
    return HttpResponse('''<script>alert("Deleted");window.location='/mng_transactn#about'</script>''')

@login_required(login_url='/')

def trans_sch(request):
    n=request.POST['date']
    ob=transaction.objects.filter(date=n)
    return render(request,"HardwareShops/mng_transactn.html",{'val':ob})

@login_required(login_url='/')

def insert_tran(request):
    pro=request.POST['select']
    cname=request.POST['textfield']
    qty=request.POST['textfield3']
    date=request.POST['textfield4']
    bill_no=request.POST['textfield5']
    pob=products_table.objects.get(id=pro)
    ob=transaction()
    ob.PRODUCT=pob
    ob.cname=cname
    ob.quantity=qty
    ob.date=date
    ob.bill_no=bill_no
    ob.status="pending"
    ob.save()
    pob.quantity=int(pob.quantity)+int(qty)
    pob.save()
    return HttpResponse('''<script>alert("Added");window.location='/mng_transactn#about'</script>''')

@login_required(login_url='/')

def edit_tran(request):
    pro=request.POST['select']
    cname=request.POST['textfield']
    qty=request.POST['textfield3']
    date=request.POST['textfield4']
    bill_no=request.POST['textfield5']
    q=request.POST['q']
    q=int(qty)-int(q)
    obq=products_table.objects.get(id=pro)
    ob=transaction.objects.get(id=request.session['tid'])
    ob.PRODUCT=obq
    ob.cname=cname
    ob.quantity=qty
    ob.date=date
    ob.bill_no=bill_no
    ob.status="pending"
    ob.save()
    obq.quantity=int(obq.quantity)+q
    obq.save()
    return HttpResponse('''<script>alert("Added");window.location='/mng_transactn#about'</script>''')

@login_required(login_url='/')

def mng_transactn(request):
    ob=transaction.objects.all()
    return render(request,'HardwareShops/mng_transactn.html',{'val':ob})
@login_required(login_url='/')

def add_return(request):
    ob=products_table.objects.all()
    # request.session['tid']=id

    return render(request,"HardwareShops/Add_return.html",{'val':ob})
@login_required(login_url='/')

def return_sch(request):
    n=request.POST['date']
    ob=return_table.objects.filter(date=n)
    return render(request,"HardwareShops/mng_return.html",{'val':ob})

@login_required(login_url='/')

def insert_return(request):
    quantity=request.POST['textfield3']
    reason=request.POST['textfield']
    obt=transaction.objects.get(id=request.session['ttid'])
    obp=obt.PRODUCT
    ob=return_table()
    print(request.POST)
    ob.TRANSACTION=obt
    ob.quantity=quantity
    ob.date=date.today()
    ob.reason=reason
    ob.status="pending"
    ob.save()
    obp.quantity = int(obp.quantity) - int(quantity)
    obp.save()
    obt.quantity=int(obt.quantity)-int(quantity)
    obt.save()
    return HttpResponse('''<script>alert("Added");window.location='/mng_transactn#about'</script>''')








@login_required(login_url='/')


def mng_return(request,id,tid):
    print(request.POST)
    # ob=return_table.objects.filter(TRANSACTION__PRODUCT__id=id)
    request.session['tid']=id
    request.session['ttid']=tid
    return redirect("/mng_return1")
    # return render(request,"HardwareShops/mng_return.html",{'val':ob})

def mng_return1(request):


    id=request.session['tid']
    tid=request.session['ttid']
    ob = return_table.objects.filter(TRANSACTION__id=tid)
    return render(request,"HardwareShops/mng_return.html",{'val':ob})
@login_required(login_url='/')

def hw_pay_sch(request):
    n=request.POST['date']
    ob=order_table.objects.filter(date=n)
    return render(request,"HardwareShops/View_payment_sta.html",{'val':ob})

@login_required(login_url='/')

def Addoffers(request):
    ob=products_table.objects.all()
    return render(request,'HardwareShops/Add offers.html',{'val':ob})
@login_required(login_url='/')

def editV_offr(request,id):
    ob=offer_table.objects.filter(PRODUCTID__id=id)
    ob1=products_table.objects.all()
    request.session['pid']=id
    return render(request,'HardwareShops/edit_offers.html',{'val':ob,'val2':ob1})
@login_required(login_url='/')

def dlt_offr(request,id):
    ob=offer_table.objects.get(id=id)
    ob.delete()
    return HttpResponse('''<script>alert("Deleted");window.location='/Offer#about'</script>''')
@login_required(login_url='/')

def insert_offr(request):
    p=request.POST['select']
    fmdate=request.POST['textfield']
    todate=request.POST['textfield2']
    offr=request.POST['textfield4']
    detail=request.POST['textfield5']

    ob=offer_table()
    ob.PRODUCTID=products_table.objects.get(id=p)
    ob.fromdate=fmdate
    ob.todate=todate
    ob.offer=offr
    ob.details=detail
    ob.save()
    return HttpResponse('''<script>alert("Added");window.location="/Offer#about"</script>''')
@login_required(login_url='/')

def edit_oofr(request):
        p = request.POST['select']
        fmdate = request.POST['textfield']
        todate = request.POST['textfield2']
        offr = request.POST['textfield4']
        detail = request.POST['textfield5']

        ob = offer_table()
        ob.PRODUCTID = products_table.objects.get(id=p)
        ob.fromdate = fmdate
        ob.todate = todate
        ob.offer = offr
        ob.details = detail
        ob.save()
        return HttpResponse('''<script>alert("Added");window.location="/Offer#about"</script>''')


@login_required(login_url='/')


def Addproduct(request):
    ob=category_table.objects.all()
    return render(request,'HardwareShops/Add  Product.html',{'val':ob})


@login_required(login_url='/')

def editV_pro(request,id):
    ob1=products_table.objects.get(id=id)
    ob=category_table.objects.all()
    request.session['pid']=id
    return render(request,'HardwareShops/edit_Product.html',{'val':ob1,'data':ob})
@login_required(login_url='/')

def dlt_product(request,id):
    ob=products_table.objects.get(id=id)
    ob.delete()
    return HttpResponse('''<script>alert("Deleted");window.location='/manageaddproducts#about'</script>''')
@login_required(login_url='/')


def insert_prdt(request):
    name=request.POST['textfield']
    category=request.POST['select']
    price=request.POST['textfield3']
    Quantity=request.POST['textfield4']
    Image=request.FILES['file']
    fs=FileSystemStorage()
    fsave=fs.save(Image.name,Image)
    ob=products_table()
    ob.name=name
    ob.price=price
    ob.quantity=Quantity
    ob.photo=fsave
    ob.CATEGORY=category_table.objects.get(id=category)
    ob.SHOPID=hardwareshops_table.objects.get(LOGIN__id=request.session['lid'])
    ob.save()
    return HttpResponse('''<script>alert("Added");window.location='/manageaddproducts#about'</script>''')
@login_required(login_url='/')

def edit_product(request):
    try:
        name = request.POST['textfield']
        category = request.POST['select']
        price = request.POST['textfield3']
        Quantity = request.POST['textfield4']
        Image = request.FILES['file']
        fs = FileSystemStorage()
        fsave = fs.save(Image.name, Image)
        ob = products_table.objects.get(id=request.session['pid'])
        ob.name = name
        ob.price = price
        ob.quantity = Quantity
        ob.photo = fsave
        ob.CATEGORY = category_table.objects.get(id=category)
        ob.SHOPID = hardwareshops_table.objects.get(LOGIN__id=request.session['lid'])
        ob.save()
        return HttpResponse('''<script>alert("Updated");window.location='/manageaddproducts#about'</script>''')
    except:
        name = request.POST['textfield']
        category = request.POST['select']
        price = request.POST['textfield3']
        Quantity = request.POST['textfield4']
        ob = products_table.objects.get(id=request.session['pid'])
        ob.name = name
        ob.price = price
        ob.quantity = Quantity
        ob.CATEGORY = category_table.objects.get(id=category)
        ob.SHOPID = hardwareshops_table.objects.get(LOGIN__id=request.session['lid'])
        ob.save()
        return HttpResponse('''<script>alert("Updated");window.location='/manageaddproducts#about'</script>''')


@login_required(login_url='/')

def Complaintsandreply(request):
    ob=complaint_table.objects.all()
    return render(request,'HardwareShops/Complaint and Reply.html',{'val':ob})
@login_required(login_url='/')

def complt_sch(request):
    n=request.POST['date']
    ob=complaint_table.objects.filter(date=n)
    return render(request,"HardwareShops/Complaint and Reply.html",{'val':ob})
@login_required(login_url='/')

def Feedbackandrating(request):
    ob=feedback_table.objects.all()
    return render(request,'HardwareShops/Feedback and Ratings.html',{'val':ob})
@login_required(login_url='/')

def feedback_sch(request):
    n=request.POST['date']
    ob=feedback_table.objects.filter(date=n)
    return render(request,"HardwareShops/Feedback and Ratings.html",{'val':ob})
@login_required(login_url='/')

def manageaddproducts(request):
    ob=products_table.objects.all()
    return render(request,'HardwareShops/Manage and add products.html',{'val':ob})
@login_required(login_url='/')

def product_sch(request):
    n=request.POST['textfield']
    ob = products_table.objects.filter(name__icontains=n)
    return render(request,"HardwareShops/Manage and add products.html",{'val':ob})
@login_required(login_url='/')

def Offer(request):
    ob=offer_table.objects.all()
    return render(request,'HardwareShops/Offer.html',{'val':ob})
@login_required(login_url='/')

def offr_sch(request):
    n=request.POST['textfield']
    nn=request.POST['textfield2']
    ob=offer_table.objects.filter(fromdate__gte=n,todate__lte=nn)
    print (ob)
    return render(request,"HardwareShops/Offer.html",{'val':ob})
@login_required(login_url='/')


def UpdateProfile(request):
    ob=hardwareshops_table.objects.get(LOGIN__id=request.session['lid'])
    return render(request,'HardwareShops/UpdateProfile.html',{'val':ob})
@login_required(login_url='/')

def update_hw(request):
    try:
        Name = request.POST['textfield']
        Place= request.POST['textfield2']
        Post=request.POST['textfield3']
        Pin=request.POST['textfield4']
        Phone=request.POST['textfield5']
        Email=request.POST['textfield6']
        Image=request.FILES['file']
        fs=FileSystemStorage()
        fsave=fs.save(Image.name,Image)

        aob=hardwareshops_table.objects.get(LOGIN__id=request.session['lid'])
        aob.name=Name
        aob.place=Place
        aob.post=Post
        aob.pin=Pin
        aob.phone=Phone
        aob.email=Email
        aob.photo=fsave
        aob.save()
        return HttpResponse('''<script>alert("Updated");window.location='/UpdateProfile#about'</script>''')
    except:
        Name = request.POST['textfield']
        Place = request.POST['textfield2']
        Post = request.POST['textfield3']
        Pin = request.POST['textfield4']
        Phone = request.POST['textfield5']
        Email = request.POST['textfield6']
        aob = hardwareshops_table.objects.get(LOGIN__id=request.session['lid'])
        aob.name = Name
        aob.place = Place
        aob.post = Post
        aob.pin = Pin
        aob.phone = Phone
        aob.email = Email
        aob.save()
        return HttpResponse('''<script>alert("Updated");window.location='/UpdateProfile#about'</script>''')
@login_required(login_url='/')

def ViewNotificationfromadmin(request):
    ob=notification_table.objects.all()
    return render(request,'HardwareShops/View Notification from Admin.html',{'val':ob})
@login_required(login_url='/')

def notatn_sch(request):
    n=request.POST['date']
    ob=feedback_table.objects.filter(date=n)
    return render(request,"HardwareShops/View Notification from Admin.html",{'val':ob})
@login_required(login_url='/')

def vieworder(request):
    ob=order_table.objects.all()
    return render(request,'HardwareShops/View order.html',{'val':ob})

@login_required(login_url='/')

def ordr_sch(request):
    n=request.POST['date']
    ob=order_table.objects.filter(date=n)
    return render(request,"HardwareShops/View order.html",{'val':ob})

@login_required(login_url='/')

def vieworderedproducts(request,id):
    ob = orderitem_table.objects.filter(ORDER__id=id)
    request.session['sid'] = id
    return render(request,'HardwareShops/view ordered products.html',{'val':ob})

def HWHome(request):
    return render(request,'HardwareShops/hw_index.html')
@login_required(login_url='/')

def send_reply(request,id):
    request.session['rep_id'] = id
    ob = complaint_table.objects.get(id=id)
    return render(request,"HardwareShops/send_reply.html",{'val':ob})
@login_required(login_url='/')

def edit_reply(request):
    s = request.POST['textfield']

    ob=complaint_table.objects.get(id=request.session['rep_id'])
    ob.reply=s
    ob.save()
    return HttpResponse('''<script>alert("Edited");window.location='/Complaintsandreply#about'</script>''')

@login_required(login_url='/')

def view_payment_status(request):
    ob=order_table.objects.all()
    return render(request,"HardwareShops/View_payment_sta.html",{'val':ob})



# ===================User=============================>>


@login_required(login_url='/')

def shops_sch(request):
    n=request.POST['textfield']
    ob=hardwareshops_table.objects.filter(name__icontains=n)
    print (ob)
    return render(request,"User/Shops.html",{'val':ob})

@login_required(login_url='/')

def myordr_sch(request):
    n=request.POST['date']
    ob=order_table.objects.filter(date=n)
    print (ob)
    return render(request,"User/View order status.html",{'val':ob})


def u_comp_sch(request):
    n=request.POST['date']
    ob=complaint_table.objects.filter(date=n)
    print (ob)
    return render(request,"User/send_complaintview_reply.html",{'val':ob})




@login_required(login_url='/')


def mng_Complaints(request):
    ob=complaint_table.objects.all()
    return render(request,'User/send_complaintview_reply.html',{'val':ob})
@login_required(login_url='/')

def add_complt(request):
    hw=request.POST['select']
    comp=request.POST['textfield']

    ob=complaint_table()
    ob.HARDWARESHOP=hardwareshops_table.objects.get(id=hw)
    ob.complaint=comp
    ob.date=datetime.today()
    ob.reply='pending'
    ob.USER=user_table.objects.get(LOGIN__id=request.session['lid'])
    ob.save()

    return HttpResponse('''<script>alert("Added");window.location='/mng_Complaints#about'</script>''')


@login_required(login_url='/')


def Feedback(request):
    ob=feedback_table.objects.all()
    return render(request,'User/feedback and ratings.html',{'val':ob})
@login_required(login_url='/')

def feed_sch(request):
    n=request.POST['date']
    ob=feedback_table.objects.filter(date=n)
    return render(request,"User/feedback and ratings.html",{'val':ob})
@login_required(login_url='/')

def Sendfeedbackrating(request):
    return render(request, 'User/send feedback and rating.html')
@login_required(login_url='/')

def inst_feed(request):
    feed=request.POST['textfield2']
    rate=request.POST['select2']

    ob=feedback_table()
    ob.feedback=feed
    ob.rating=rate
    ob.date=datetime.today()
    ob.USER=user_table.objects.get(LOGIN__id=request.session['lid'])
    ob.save()

    return HttpResponse('''<script>alert("Thank you for the feedback");window.location='/Feedback#about'</script>''')


def UserHome(request):
    return render(request,'User/user_index.html')
@login_required(login_url='/')

def Offernotification(request):
    ob=offer_table.objects.all()
    return render(request,'User/Offer Notification.html',{'val':ob})
@login_required(login_url='/')

def placeorder(request):
    return render(request,'User/place order.html')
@login_required(login_url='/')

def Sendcomplaints(request):
    ob=hardwareshops_table.objects.all()
    return render(request,'User/send complaints.html',{'val':ob})

@login_required(login_url='/')

def Shops(request):
    ob=hardwareshops_table.objects.all()
    return render(request,'User/Shops.html',{'val':ob})
@login_required(login_url='/')


def myordr(request):
    ob=order_table.objects.all()
    return render(request,'User/View order status.html',{'val':ob})
@login_required(login_url='/')

def u_pro_sch(request):
    n=request.POST['date']
    # import json
    # ob=products_table.objects.filter(name__icontains=n)
    # print (ob)
    # from django.db import connection
    # ob=user_table.objects.get(LOGIN__id=id)
    # cursor = connection.cursor()
    # cursor.execute("SELECT `ch_app_products_table`.*,`ch_app_offer_table`.* ,`ch_app_category_table`.`name` FROM `ch_app_products_table` JOIN `ch_app_category_table` ON `ch_app_category_table`.`id`=`ch_app_products_table`.`CATEGORY_id` LEFT JOIN `ch_app_offer_table` ON `ch_app_products_table`.`id`=`ch_app_offer_table`.`PRODUCTID_id`  WHERE `ch_app_products_table`.`SHOPID_id`='"+ str(id) +"' AND ch_app_products_table.`name` LIKE '%"+n+"%' ")

    # cursor.execute("SELECT `ch_app_products_table`.*, `ch_app_offer_table`.*, `ch_app_category_table`.`name` FROM `ch_app_products_table` JOIN `ch_app_category_table` ON `ch_app_category_table`.`id` = `ch_app_products_table`.`CATEGORY_id` LEFT JOIN `ch_app_offer_table` ON `ch_app_products_table`.`id` = `ch_app_offer_table`.`PRODUCTID_id`  WHERE `ch_app_products_table`.`SHOPID_id` = '" + str(id) + "' AND ch_app_products_table.`name` LIKE '%"+n+"%'")

        # "SELECT `ch_app_products_table`.*,`ch_app_offer_table`.* ,`ch_app_category_table`.`name` FROM `ch_app_products_table` JOIN `ch_app_category_table` ON `ch_app_category_table`.`id`=`ch_app_products_table`.`CATEGORY_id` LEFT JOIN `ch_app_offer_table` ON `ch_app_products_table`.`id`=`ch_app_offer_table`.`PRODUCTID_id`  WHERE  `ch_app_products_table`.`SHOPID_id`='" + str(
        #     id) + "'  name like '%n%'' ")
    from django.db import connection
    # ob=user_table.objects.get(LOGIN__id=id)
    cursor = connection.cursor()
    cursor.execute(
        "SELECT `ch_app_products_table`.*,`ch_app_offer_table`.* ,`ch_app_category_table`.`name` FROM `ch_app_products_table` JOIN `ch_app_category_table` ON `ch_app_category_table`.`id`=`ch_app_products_table`.`CATEGORY_id` LEFT JOIN `ch_app_offer_table` ON `ch_app_products_table`.`id`=`ch_app_offer_table`.`PRODUCTID_id`  WHERE `ch_app_products_table`.`SHOPID_id`='" + str(
            request.session['sid']) + "' AND ch_app_products_table.`name` LIKE '%"+n+"%'")
    row = cursor.fetchall()
    print(row,"=======================================")
    print(row,"=======================================")
    print(row,"=======================================")
    # row = cursor.fetchall()
    # print(row)
    # request.session['sid'] = id

    return render(request,"User/view product.html",{'val':row})

def ordr_pro(request,id):
    ob=orderitem_table.objects.filter(ORDER__id=id)
    for i in ob:
        obb = pro_return_table.objects.filter(ORDERITEM__id=i.id)
        if len(obb)==0:
            i.rs="1"
        # if i.quantity==0:
        #     obb=pro_return_table.objects.filter(ORDERITEM__id=i.id)
        #     i.rstatus=obb[0].status
        else:
            obb = pro_return_table.objects.filter(ORDERITEM__id=i.id)
            i.rstatus = obb[0].status
            i.rs=0
    return render(request,'User/ordr_product.html',{'val':ob})




@login_required(login_url='/')
def proreturn(request,id,qty):
    print(request.POST)
    request.session['rqid']=id
    request.session['qqty']=qty
    return redirect('/reasonre#about')


@login_required(login_url='/')
def reasonre(request):

    return render(request,"User/return_reason.html")


@login_required(login_url='/')
def proreturnreason(request):
    print(request.POST)
    rsn=request.POST['textfield']
    obpp = orderitem_table.objects.get(id=request.session['rqid'])
    obpp.quantity=0
    obpp.save()
    request.session['ooid'] = obpp.ORDER.id
    obp = products_table.objects.get(id=obpp.PRODUCT.id)
    obp.quantity = float(obp.quantity) + int(request.session['qqty'])
    obp.save()

    ob2 = orderitem_table.objects.filter(ORDER__id=request.session['ooid'])
    if len(ob2) == 0:
        ob1 = order_table.objects.get(id=request.session['ooid'])
        ob1.amount=int(ob1.amount)-(int(obp.price)*int(request.session['qqty']))
        ob1.save()

    ob=pro_return_table()
    ob.ORDERITEM=obpp
    ob.date=datetime.today()
    ob.reason=rsn
    ob.qty=request.session['qqty']
    ob.status="pending"
    ob.save()
    return HttpResponse('''<script>alert("returned");window.location='/myordr'</script>''')




@login_required(login_url='/')

def offr_notn_sch(request):
    n = request.POST['textfield']
    nn = request.POST['textfield2']
    ob = offer_table.objects.filter(fromdate__gte=n, todate__lte=nn)
    return render(request,"User/Offer Notification.html",{'val':ob})


def HardwareshopRegistration(request):
    return render(request, 'HardwareShops/HardwareshopRegistration.html')

def shop_reg(request):
    Name = request.POST['textfield2']
    Place = request.POST['textfield3']
    Post = request.POST['textfield4']
    Pin = request.POST['textfield5']
    Phone = request.POST['textfield6']
    Email = request.POST['textfield7']
    Image = request.FILES['file']
    fs = FileSystemStorage()
    fsave = fs.save(Image.name, Image)
    username = request.POST['textfield8']
    password = request.POST['textfield9']

    ob = login_table()
    ob.username = username
    ob.password = password
    ob.type = "pending"
    ob.save()

    aob = hardwareshops_table()
    aob.name = Name
    aob.place = Place
    aob.post = Post
    aob.pin = Pin
    aob.phone = Phone
    aob.email = Email
    aob.photo = fsave
    aob.LOGIN = ob
    aob.save()
    return HttpResponse('''<script>alert("Registed");window.location='/'</script>''')




def register(request):
    return render(request, 'Login/reg_index.html')


def userRegistration(request):
    FirstName = request.POST['textfield']
    LastName = request.POST['textfield2']
    Place= request.POST['textfield3']
    Post=request.POST['textfield4']
    Pin=request.POST['textfield5']
    Phone=request.POST['textfield6']
    Email=request.POST['textfield7']
    Image=request.FILES['file']
    fs=FileSystemStorage()
    fsave=fs.save(Image.name,Image)
    username=request.POST['textfield8']
    password=request.POST['textfield9']

    ob=login_table()
    ob.username=username
    ob.password=password
    ob.type='user'
    ob.save()

    aob=user_table()
    aob.name=FirstName
    aob.lastname=LastName
    aob.place=Place
    aob.post=Post
    aob.pin=Pin
    aob.phone=Phone
    aob.email=Email
    aob.photo=fsave
    aob.LOGIN=ob
    aob.save()
    return HttpResponse('''<script>alert("Registed");window.location='/'</script>''')

@login_required(login_url='/')

def profileupdate(request):
    ob=user_table.objects.get(LOGIN__id=request.session['lid'])
    return render(request,'User/Update Profile.html',{'val':ob})

@login_required(login_url='/')

def inst_pro(request):
    try:
        FirstName = request.POST['textfield']
        LastName = request.POST['textfield2']
        Place = request.POST['textfield3']
        Post = request.POST['textfield4']
        Pin = request.POST['textfield5']
        Phone = request.POST['textfield6']
        Email = request.POST['textfield7']

        aob = user_table.objects.get(LOGIN__id=request.session['lid'])
        aob.name = FirstName
        aob.lastname = LastName
        aob.place = Place
        aob.post = Post
        aob.pin = Pin
        aob.phone = Phone
        aob.email = Email
        aob.save()
        return HttpResponse('''<script>alert("Updated");window.location='/profileupdate#about'</script>''')
    except:
        FirstName = request.POST['textfield']
        LastName = request.POST['textfield2']
        Place= request.POST['textfield3']
        Post=request.POST['textfield4']
        Pin=request.POST['textfield5']
        Phone=request.POST['textfield6']
        Email=request.POST['textfield7']

        aob=user_table.objects.get(LOGIN__id=request.session['lid'])
        aob.name=FirstName
        aob.lastname=LastName
        aob.place=Place
        aob.post=Post
        aob.pin=Pin
        aob.phone=Phone
        aob.email=Email
        aob.save()
        return HttpResponse('''<script>alert("Updated");window.location='/profileupdate#about'</script>''')


@login_required(login_url='/')

def viewproduct(request,id):
    # ob=products_table.objects.filter(SHOPID__id=id)
    from django.db import connection
    # ob=user_table.objects.get(LOGIN__id=id)
    cursor= connection.cursor()
    cursor.execute("SELECT `ch_app_products_table`.*,`ch_app_offer_table`.* ,`ch_app_category_table`.`name` FROM `ch_app_products_table` JOIN `ch_app_category_table` ON `ch_app_category_table`.`id`=`ch_app_products_table`.`CATEGORY_id` LEFT JOIN `ch_app_offer_table` ON `ch_app_products_table`.`id`=`ch_app_offer_table`.`PRODUCTID_id`  WHERE `ch_app_products_table`.`SHOPID_id`='"+ str(id) +"'")
    row=cursor.fetchall()
    print(row)
    request.session['sid']=id
    return render(request,'User/view product.html',{'val':row})


@login_required(login_url='/')

def view_return_history(request):
    from django.db import connection
    ob=hardwareshops_table.objects.get(LOGIN__id=request.session['lid'])
    cursor = connection.cursor()
    cursor.execute("SELECT `ch_app_pro_return_table`.*,`ch_app_products_table`.`name`,`ch_app_products_table`.`photo`,`ch_app_products_table`.`price`,`ch_app_order_table`.`date`,`ch_app_order_table`.`id`,`ch_app_user_table`.`name`,`ch_app_user_table`.`lastname`,`ch_app_orderitem_table`.`quantity`,`ch_app_products_table`.`id` FROM `ch_app_pro_return_table` JOIN `ch_app_orderitem_table` ON `ch_app_orderitem_table`.`id`=`ch_app_pro_return_table`.`ORDERITEM_id` JOIN `ch_app_products_table` ON `ch_app_products_table`.`id`=`ch_app_orderitem_table`.`PRODUCT_id` JOIN `ch_app_order_table` ON `ch_app_order_table`.`id`=`ch_app_orderitem_table`.`ORDER_id` JOIN `ch_app_user_table` ON `ch_app_user_table`.`id`=`ch_app_order_table`.`USER_id` WHERE `ch_app_products_table`.`SHOPID_id`='"+str(ob.id)+"'")
    row = cursor.fetchall()
    print(row)
    return render(request, 'HardwareShops/View_cart.html', {'val': row})




@login_required(login_url='/')

def view_cart(request):
    from django.db import connection
    ob=user_table.objects.get(LOGIN__id=request.session['lid'])
    cursor = connection.cursor()
    cursor.execute("SELECT `ch_app_products_table`.*,`ch_app_orderitem_table`.`quantity`,`ch_app_orderitem_table`.`id`,`ch_app_products_table`.`id` as pid FROM `ch_app_orderitem_table` JOIN `ch_app_products_table` ON `ch_app_products_table`.`id`=`ch_app_orderitem_table`.`PRODUCT_id` JOIN `ch_app_order_table` ON  `ch_app_order_table`.`id`=`ch_app_orderitem_table`.`ORDER_id` WHERE `ch_app_order_table`.`USER_id`='"+str(ob.id)+"' and `ch_app_order_table`.`status`='pending'")
    row = cursor.fetchall()
    print(row)
    return render(request, 'User/View_cart.html', {'val': row})

@login_required(login_url='/')

def delete_cart(request,id,qty):
    obd=orderitem_table.objects.get(id=id)


    request.session['oid'] = obd.ORDER.id
    obp = products_table.objects.get(id=obd.PRODUCT.id)
    obp.quantity = float(obp.quantity) + int(qty)
    obp.save()
    obd.delete()
    ob2 = orderitem_table.objects.filter(ORDER__id=request.session['oid'])
    if len(ob2) == 0:
        ob1 = order_table.objects.get(id=request.session['oid'])
        ob1.delete()


    return HttpResponse('''<script>alert("deleted");window.location='/view_cart#about'</script>''')


@login_required(login_url='/')

def view_pro2(request):
    from django.db import connection
    cursor = connection.cursor()
    cursor.execute("SELECT `ch_app_products_table`.*,`ch_app_offer_table`.* ,`ch_app_category_table`.`name` FROM `ch_app_products_table` JOIN `ch_app_category_table` ON `ch_app_category_table`.`id`=`ch_app_products_table`.`CATEGORY_id` LEFT JOIN `ch_app_offer_table` ON `ch_app_products_table`.`id`=`ch_app_offer_table`.`PRODUCTID_id`  WHERE `ch_app_products_table`.`SHOPID_id`='" + str(request.session['sid']) + "'")
    row = cursor.fetchall()
    print(row)
    return render(request, 'User/view product.html', {'val': row})


@login_required(login_url='/')
def view_pro_t(request):

        ob = orderitem_table.objects.filter(ORDER__USER__LOGIN__id=request.session['lid'],ORDER__status='pending')
        ta=ob[0].ORDER.amount
        for i in ob:
            ofr=0
            try:
                ofr=float(i.offer)
            except:
                pass
            i.tp=float(i.PRODUCT.price)*float(i.quantity)
            i.tp=i.tp-(i.tp*ofr/100)
        request.session['tot']=ta
        request.session['oid']=ob[0].ORDER.id
        return render(request, "User/view pro_t.html", {'val': ob,"ta":ta,"id":request.session['sid']})
# ===================ADD TO CART==========================>
@login_required(login_url='/')


def order_pro_u(request,id):
    try:

        ob=products_table.objects.get(id=id)
        ob1=offer_table.objects.filter(PRODUCTID=ob.id,fromdate__lte=datetime.today(),todate__gte=datetime.today())
        # request.session['sid']=id

        request.session['pid']=id
        return render(request,"User/ordr.html",{'val':ob,'val2':ob1[0]})
    except:
        ob = products_table.objects.get(id=id)
        ob1 = offer_table.objects.all()
        ob1.offer="No offer"
        # request.session['sid']=id

        request.session['pid'] = id
        return render(request, "User/ordr.html", {'val': ob, 'val2': ob1})


@login_required(login_url='/')

def ordrprdctcode1(request):
    return HttpResponse('''<script>alert('placed order successfuly');window.location='/user_pay_proceed#about'</script>''')
@login_required(login_url='/')

def ordrprdctcode(request):
    # print(request.session['pid'],"kiiiiiiiiiiiiiiiiiii")
    btn=request.POST['Submit']
    if btn == "Continue":
        qty=request.POST['textfield']
        qq=products_table.objects.get(id=request.session['pid'])
        obf = offer_table.objects.filter(PRODUCTID__id=request.session['pid'], fromdate__lte=datetime.today(),
                                         todate__gte=datetime.today())
        ofp=0
        if len(obf)>0:
            ofp=float(obf[0].offer.split("%")[0])
        tt = int(qq.price)* int(qty)
        tt=tt-(tt*ofp/100)
        stock = int(qq.quantity)
        print(stock,qty,"jjjjjjjjjjjjjjjjjjjjjj")
        nstk = int(stock) - int(qty)
        if stock >= int(qty):
            up=products_table.objects.get(id=request.session['pid'])
            up.quantity=nstk
            up.save()
            q=order_table.objects.filter(USER=user_table.objects.get(LOGIN__id=request.session['lid']),status='pending')
            if len(q)==0:
                qt=order_table()
                qt.date=datetime.today()
                qt.USER=user_table.objects.get(LOGIN__id=request.session['lid'])
                qt.status='pending'
                qt.amount=tt
                qt.save()


                qty1=orderitem_table()
                qty1.quantity=qty
                qty1.PRODUCT=products_table.objects.get(id=request.session['pid'])
                qty1.ORDER=qt
                qty1.date = datetime.today()



                qty1.offer = ofp
                qty1.save()

                return HttpResponse('''<script>window.location='/view_pro_t#about'</script>''')
            else:

                total = int(q[0].amount) + int(tt)

                qt=order_table.objects.get(id=q[0].id)
                qt.amount=total
                qt.save()

                qty1=orderitem_table.objects.filter(PRODUCT__id=request.session['pid'],ORDER__id=q[0].id)
                if len(qty1)==0:
                    qqt=orderitem_table()
                    qqt.ORDER=q[0]
                    qqt.PRODUCT=products_table.objects.get(id=request.session['pid'])
                    qqt.quantity=qty
                    qqt.offer=ofp





                    qqt.save()
                else:
                    qry1=orderitem_table.objects.get(id=qty1[0].id)
                    quty=int(qty1[0].quantity) + int(qty)
                    qry1.quantity=quty
                    qry1.save()
                return HttpResponse('''<script>window.location='/view_pro_t'</script>''')
        else:
            return HttpResponse('''<script>alert('No stock');window.location='/view_pro2#about'</script>''')
    else:
        qty = request.POST['textfield']
        qq = products_table.objects.get(id=request.session['pid'])
        tt = int(qq.price) * int(qty)
        stock = int(qq.quantity)
        print(stock, qty, "jjjjjjjjjjjjjjjjjjjjjj")
        nstk = int(stock) - int(qty)
        if stock >= int(qty):
            up = products_table.objects.get(id=request.session['pid'])
            up.quantity = nstk
            up.save()
            q = order_table.objects.filter(USER=user_table.objects.get(LOGIN__id=request.session['lid']),
                                           status='pending')
            if len(q) == 0:
                qt = order_table()
                qt.date = datetime.today()
                qt.USER = user_table.objects.get(LOGIN__id=request.session['lid'])
                qt.status = 'pending'
                qt.amount = tt
                request.session['tot']=tt
                qt.save()
                request.session['oid']=qt.id
                qty1 = orderitem_table()
                qty1.quantity = qty
                qty1.PRODUCT = products_table.objects.get(id=request.session['pid'])
                qty1.ORDER = qt
                qty1.date = datetime.today()
                qty1.save()
                return HttpResponse(
                    '''<script>alert('placed order successfuly');window.location='/user_pay_proceed#about'</script>''')
            else:
                total = int(q[0].amount) + int(tt)
                request.session['tot']=total
                qt = order_table.objects.get(id=q[0].id)
                qt.amount = total
                qt.save()
                request.session['oid']=qt.id
                qty1 = orderitem_table.objects.filter(PRODUCT__id=request.session['pid'], ORDER__id=q[0].id)
                if len(qty1) == 0:
                    qqt = orderitem_table()
                    qqt.ORDER = q[0]
                    qqt.PRODUCT = products_table.objects.get(id=request.session['pid'])
                    qqt.quantity = qty
                    qqt.save()

                else:
                    qry1 = orderitem_table.objects.get(id=qty1[0].id)
                    quty = int(qty1[0].quantity) + int(qty)
                    qry1.quantity = quty
                    qry1.save()


                return HttpResponse('''<script>alert(' success');window.location='/user_pay_proceed#about'</script>''')
        else:
            return HttpResponse('''<script>alert('out of stock');window.location='/UserHome#about'</script>''')






@login_required(login_url='/')
def user_pay_proceed(request):
    total=request.session['tot']
    print(total,"=======")
    # request.session['pay_amount'] = amount
    client = razorpay.Client(auth=("rzp_test_edrzdb8Gbx5U5M", "XgwjnFvJQNG6cS7Q13aHKDJj"))
    print(client)
    payment = client.order.create({'amount': str(total)+"00", 'currency': "INR", 'payment_capture': '1'})
    res=user_table.objects.get(LOGIN__id=request.session['lid'])
    return render(request,'User/UserPayProceed.html', {'p':payment,'val':res,})


@login_required(login_url='/')


def on_payment_success(request):
    # amt = request.session['pay_amount']
    ob=order_table.objects.get(id=request.session['oid'])
    ob.status='paid'
    ob.save()

    # qry = "UPDATE `charity_information` SET `amount`=`amount`-%s WHERE `id`=%s"
    # iud(qry, (amt,charity))

    return HttpResponse('''<script>alert("Success! Thank you for your Order");window.location="UserHome#about"</script>''')


@login_required(login_url='/')
def senddeliverynote(request,id):
    request.session['dnid']=id
    return render(request,"User/send_delivery_note.html")


@login_required(login_url='/')
def senddeliverynotepost(request):
    dnote=request.POST['']
    ob=pro_return_table.objects.get(id=request.session['dnid'])
    ob.status=dnote
    ob.save()
    return HttpResponse('''<script>alert("sent");window.location="manageaddproducts#about"</script>''')


@login_required(login_url='/')

def returnnoti(request,id,qty,oooid,pid):
    request.session['nnid']=id
    request.session['qtyyyy']=qty
    request.session['oooooid']=oooid
    request.session['piiid']=pid
    return redirect('/rnoti')

@login_required(login_url='/rnoti')

def rnoti(request):
    return render(request,"HardwareShops/return_noti.html")


@login_required(login_url='/')
def insert_returnnoti(request):

    notiii=request.POST['textfield']
    ob=products_table.objects.get(id=request.session['piiid'])
    ob.quantity=int(ob.quantity)-int(request.session['qtyyyy'])
    ob.save()

    obb=orderitem_table.objects.get(id=request.session['oooooid'])
    obb.quantity=int(obb.quantity)+int(request.session['qtyyyy'])
    obb.save()


    obt=pro_return_table.objects.get(id=request.session['nnid'])
    obt.status=notiii
    obt.save()
    return HttpResponse('''<script>alert("Added");window.location='/view_return_history#about'</script>''')


