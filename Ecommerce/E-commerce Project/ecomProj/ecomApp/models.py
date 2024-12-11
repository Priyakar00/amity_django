from django.db import models
from .constants import PaymentStatus
# Create your models here.
class categories(models.Model):
	name=models.CharField(max_length=30)#charfield=varchar
	status=models.BooleanField(default=True)

	def __str__(self):
		return self.name

class product(models.Model):
	pname=models.CharField(max_length=100)
	pprice=models.CharField(max_length=100)
	sdescrip=models.TextField()
	ldescrip=models.TextField()

	product_category=models.ForeignKey(categories,on_delete=models.CASCADE)#category delete hole product o delete hoe jabe cascade use korle
	quantity=models.CharField(max_length=100)
	slug=models.SlugField(primary_key=True)
	active=models.BooleanField(default=True)

	def __str__(self):
		return self.slug  #views.py te item_ob=prodcut.objects.get(slug=?)ei slug tai hochhe return kora slug value ta


class product_image(models.Model):
	single_product=models.ForeignKey(product,on_delete=models.CASCADE)
	image=models.ImageField(upload_to='product_image/',null=True)
	active=models.BooleanField(default=True)

	def __str__(self):
		return self.single_product.pname

# # sign part pore korbe

class SIGN(models.Model):
	name=models.CharField(max_length=100)
	address=models.CharField(max_length=100)
	email=models.CharField(max_length=100,primary_key=True)
	phone=models.IntegerField()
	username=models.CharField(max_length=100)
	password=models.CharField(max_length=100)



'''
class Orders(models.Model):
	order_id=models.AutoField(primary_key=True)
	items_json=models.CharField(max_length=100)
	amount=models.IntegerField()
	name=models.CharField(max_length=200)
	email=models.CharField(max_length=200)
	address=models.CharField(max_length=200)
	city=models.CharField(max_length=200)
	state=models.CharField(max_length=200)
	zip_code=models.CharField(max_length=200)
	phone=models.CharField(max_length=200,default='')

class OrderUpdate(models.Model):
	update_id=models.AutoField(primary_key=True)
	order_id=models.IntegerField(default='')
	update_desc=models.CharField(max_length=200)
	timestamp=models.DateField(auto_now_add=True)
'''
class Order(models.Model):
    name = models.CharField(("Customer Name"), max_length=254, blank=False, null=False)
    amount = models.FloatField(("Amount"), null=False, blank=False)
    status = models.CharField(
        ("Payment Status"),
        default=PaymentStatus.PENDING,
        max_length=254,
        blank=False,
        null=False,
    )
    provider_order_id = models.CharField(
        ("Order ID"), max_length=40, null=False, blank=False
    )
    payment_id = models.CharField(
        ("Payment ID"), max_length=36, null=False, blank=False
    )
    signature_id = models.CharField(
        ("Signature ID"), max_length=128, null=False, blank=False
    )

    def __str__(self):
        return f"{self.id}-{self.name}-{self.status}"#fstring
        
    def mark_as_paid(self):
        self.status = PaymentStatus.SUCCESS
        self.save()		