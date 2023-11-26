from django.db import models

# Create your models here.
class login_table(models.Model):
    username=models.CharField(max_length=100)
    password = models.CharField(max_length=10)
    type=models.CharField(max_length=20)


class hardwareshops_table(models.Model):
    LOGIN=models.ForeignKey(login_table,on_delete=models.CASCADE)
    name=models.CharField(max_length=100)
    email=models.CharField(max_length=30)
    place=models.CharField(max_length=50)
    post=models.CharField(max_length=50)
    pin=models.IntegerField()
    phone=models.BigIntegerField()
    photo=models.FileField()

class user_table(models.Model):
    LOGIN = models.ForeignKey(login_table, on_delete=models.CASCADE)
    name=models.CharField(max_length=100)
    lastname = models.CharField(max_length=100)
    email = models.CharField(max_length=30)
    place = models.CharField(max_length=50)
    post = models.CharField(max_length=50)
    pin=models.IntegerField()
    phone = models.BigIntegerField()
    photo = models.FileField()

class complaint_table(models.Model):
    USER=models.ForeignKey(user_table,on_delete=models.CASCADE)
    complaint=models.CharField(max_length=100)
    date=models.DateField()
    reply=models.CharField(max_length=100)
    HARDWARESHOP=models.ForeignKey(hardwareshops_table,on_delete=models.CASCADE)

class feedback_table(models.Model):
    USER = models.ForeignKey(user_table, on_delete=models.CASCADE)
    feedback= models.CharField(max_length = 100)
    date = models.DateField()
    rating = models.IntegerField()

class notification_table(models.Model):
    notification=models.CharField(max_length=100)
    date=models.DateField()

class category_table(models.Model):
    name=models.CharField(max_length=100)

class products_table(models.Model):
    CATEGORY=models.ForeignKey(category_table,on_delete=models.CASCADE)
    SHOPID=models.ForeignKey(hardwareshops_table,on_delete=models.CASCADE)
    name = models.CharField(max_length=100)
    price=models.IntegerField()
    quantity=models.IntegerField()
    photo=models.FileField()

class transaction(models.Model):
    PRODUCT=models.ForeignKey(products_table,on_delete=models.CASCADE)
    cname=models.CharField(max_length=100)
    quantity=models.CharField(max_length=100)
    date=models.CharField(max_length=50)
    bill_no=models.IntegerField()
    status=models.CharField(max_length=100)

class return_table(models.Model):
    TRANSACTION=models.ForeignKey(transaction,on_delete=models.CASCADE)
    quantity = models.CharField(max_length=100)
    date = models.CharField(max_length=50)
    reason = models.CharField(max_length=100)
    status = models.CharField(max_length=100)






class offer_table(models.Model):
    PRODUCTID = models.ForeignKey(products_table, on_delete=models.CASCADE)
    fromdate=models.CharField(max_length=50)
    todate=models.CharField(max_length=50)
    offer=models.CharField(max_length=100)
    details=models.CharField(max_length=100)


class order_table(models.Model):
    USER = models.ForeignKey(user_table, on_delete=models.CASCADE)
    date = models.DateField()
    amount = models.IntegerField()
    status=models.CharField(max_length=100)

class orderitem_table(models.Model):
    ORDER = models.ForeignKey(order_table, on_delete=models.CASCADE)
    offer=models.CharField(max_length=100)
    PRODUCT = models.ForeignKey(products_table, on_delete=models.CASCADE)
    quantity = models.IntegerField()



class pro_return_table(models.Model):
    ORDERITEM=models.ForeignKey(orderitem_table,on_delete=models.CASCADE)

    date = models.CharField(max_length=50)
    qty = models.IntegerField()
    reason = models.CharField(max_length=100)
    status = models.CharField(max_length=100)
