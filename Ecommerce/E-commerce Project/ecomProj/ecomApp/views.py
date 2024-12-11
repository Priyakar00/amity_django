from django.shortcuts import render,redirect
from .models import *

import razorpay

from django.views.decorators.csrf import csrf_exempt


from django.http import JsonResponse # ata payu success failure er jonno

#  for payment gate way start
# ata csrf_exempt er jonno
from django.conf import settings

from django.http import HttpResponse
#from .PayTm import Checksum
#MERCHANT_KEY = 'opoTNnYFHTLcPtrb' #paytm merchant password


# Create your views here.
def home(request):
	return render(request, 'home.html')

def about(request):
	return render(request, 'about.html')

# def services(request):
# 	return render(request,'services.html')

def contact(request):
	return render(request,'contact.html')

def gallery(request):
	return render(request,'gallery.html')

def pricing(request):
	return render(request,'pricing.html')

def products(request):
	product_ob=product.objects.all()
	return render(request,"products.html",{"records":product_ob})

def single_details(request,id):
	item_ob=product.objects.get(slug=id)
	return render(request,"single_details.html",{"item_records":item_ob})

def carts(request):
	btn = request.POST['test']#test ta cart.html a buy now button er name
	# print(btn)
	qntity=request.POST['qntity']
	uslug=request.POST['slug'] # single_datails page e j slug name ta dewa ache seta holo ekhne post er vetorer ta
	print(qntity)
	print(uslug)
	item_obj=product.objects.get(slug=uslug)
	if(btn == "buy"):
		print("work for buy")
		total = int(qntity)*int(item_obj.pprice)
		request.session['total_amount'] = total
		return  redirect('/Checkout')

	else:
		print(item_obj.product_image_set.all()[0].image.url) #models e j image ache seta likhte hbe
		single_item={uslug:[item_obj.product_image_set.all()[0].image.url,item_obj.pname,item_obj.pprice,qntity]}
		# uslug key er modhhe product er object gulo k as value tola hochhe ar quantity ta sese e rakhte hobe karon er last(-1) index ta 84 no line a legeche
		print("--"*30)
		print(single_item)
		# print(btn)
			
		'''print(item_obj.product_image_set.all()[0].image.url) #models e j image ache seta likhte hbe
		single_item={uslug:[item_obj.product_image_set.all()[0].image.url,item_obj.pname,item_obj.pprice,qntity]}
		print("--"*30)
		print(single_item)'''
		try:
			print("---------------------hello")
			v=request.session['cart_info'] # session kora mane server e value tola mane website jotokhn open thakche sekhane value add thakche
			# cart_info er moddhe kono value nei tai error asbe bole try except dewa
			f=0
			#print("--"*10)
			#print(v)
			for x in v:
				if uslug in x:
						#print("--"*300)
						#print(x[uslug])
						h=int(x[uslug][-1]) # -1 mane uslug key er last value quantity ta k tulchi (see line 63)
						h+=int(qntity)
						x[uslug][-1]=str(h) #amra database a ja kori sob varchar tai str a convert
						f=1
			if f==0:
				v.append(single_item) # jodi aki item na hyy tahole notun kore add hbe
				request.session['cart_info']=v
		except Exception as e:
			request.session['cart_info']=[single_item] #session e single_item k list hisebe pathano hocche tar mane puro jinista 0 index e uthche
		
		print('details ',request.session['cart_info']) # show details e click korle sob value session e utche mane console e dekhabe

		request.session['cart_count']=len(request.session['cart_info'])  #cart a value add korle len barbe seta show hobe cart(1)
		return redirect('/Cart_Us')


def cartdisplay(request):
	#return render(request,"cartdisplay.html")
	try:
		# if len(request.session['cart_info'])==0:
		# 	request.session['cart_disp_count'] = False
		# 	return render(request,"cart_buy.html")	
		# ------not needed -------

		carts = request.session['cart_info'] # session er value carts e tola hocchhe
		print("=="*30)
		print(carts)
		request.session['cart_disp_count'] = True # cart_info te jodi value thake tahole true 
		gross_value=0
		
		for i in carts:
			for k,v in i.items(): #k=key  ekhane uslug   v=value ekhane uslug er each element
					gross_value+=int(v[-1])*int(v[-2])
		
		request.session['total_amount']=gross_value
		return render(request,"cartdisplay.html",{'allCart':carts}) # value thakle sob nie new html page e jbe
	except:
		request.session['cart_disp_count'] = False # cart_info te jodi value na thake tahole false
		return render(request,"cartdisplay.html") # value na thakle emni e jbe new page e


def remove_cart(request,kslug):
		i=0
		s=request.session['cart_info']
		for x in s:
			if kslug in x:
				break
			else:
				i+=1
		s.pop(i)
		print("---"*30)
		# print(s)
		request.session['cart_info'] = s
		request.session['cart_count'] = len(request.session['cart_info'])
		return redirect('/Cart_Us')

def signup(request):
	try:
		if request.session['error_message']==1:
			msg1="please create an account"
			del request.session['error_message']
	except:
		msg1=""
	# print(msg1)
	return render(request,"signup.html",{'msg1':msg1})

def signup1(request):
	n=request.POST['name']
	a=request.POST['address']
	e=request.POST['email']
	m=request.POST['mobileno']
	use=request.POST['username']
	pa=request.POST['password']
	print(n)
	print(a)
	print(e)
	print(m)
	print(use)
	print(pa)

	s=SIGN()
	s.name=n
	s.address=a
	s.email=e
	s.phone=m
	s.username=use
	s.password=pa
	s.save()

	return redirect('/Login_Us')

def login(request):
	msg1=""
	try:
		if request.session['error_message']==2:
			msg1="please enter correct details"
			del request.session['error_message']
	except:
		msg1=""
	# print(msg1)
	return render(request,"login.html",{'msg1':msg1})
	
def username(request):
	if request.method=='POST':
		usern=request.POST['usernam']
		passwo=request.POST['passwor']

	print(usern)
	print(passwo)

	try:
		signup_ob=SIGN.objects.get(username=usern)
		if((usern==signup_ob.username) and (passwo==signup_ob.password)):
			arr=[signup_ob.username,signup_ob.name,signup_ob.address,signup_ob.email,signup_ob.phone]
			request.session['user_info']=arr
			return redirect('/')
		else:
			request.session['error_message']=2
			return redirect('/Login_Us')
	except Exception as e:
		request.session['error_message']=1
		return redirect('/Signup_Us')

def userlogout(request):
	del request.session['user_info']
	return redirect('/Login_Us')


def checkout_fun(request):
	# razorpay integration
	if request.method == "POST":
		name = request.session['user_info'][1]
		print(name)
		amount = request.session['total_amount']
		print(amount)
		client = razorpay.Client(auth=('rzp_test_QvJmsxzaVwb2t4', 'kDUiANWg5ziCQylXRcAsZXaH'))
		razorpay_order = client.order.create(
            {"amount": int(amount) * 100, "currency": "INR", "payment_capture": "1"}
            )
		print(razorpay_order)
		order = Order.objects.create(
        	name=name, amount=amount, provider_order_id=razorpay_order["id"]
        	)
		print(order)
		order.save()
		return render(
			request,
			"payment.html",
			{
				# "callback_url": "http://" + "127.0.0.1:8000" + "/callback/", 
				"callback_url": "http://localhost:8000/callback",
				"razorpay_key": 'rzp_test_QvJmsxzaVwb2t4.',
				"order": order,
			},
		)
	return render(request, "payment.html")
	'''
	#paytm
	if request.method=="POST":
		print("-------------------------test--------------------")
		items_json = request.POST.get('itemsJson', '')
		name = request.POST.get('name', '')
		amount = request.session['total_amount']
		email = request.POST.get('email', '')
		address = request.POST.get('address1', '') + " " + request.POST.get('address2', '')
		city = request.POST.get('city', '')
		state = request.POST.get('state', '')
		zip_code = request.POST.get('zip_code', '')
		phone = request.POST.get('phone', '')
		order = Orders(items_json=items_json, name=name, email=email, address=address, city=city,
                       state=state, zip_code=zip_code, phone=phone, amount=amount)
		order.save()
		update = OrderUpdate(order_id=order.order_id, update_desc="The order has been placed")
		update.save()
		thank = True
		id = order.order_id
		#return render(request, 'checkout.html', {'thank':thank, 'id': id})
		# Request paytm to transfer the amount to your account after payment by user
		param_dict = {

			'MID': 'SffUiy89646079730067',# paytm merchant id
			'ORDER_ID': str(order.order_id),
			'TXN_AMOUNT': str(amount),
			'CUST_ID': email,
			'INDUSTRY_TYPE_ID': 'Retail',
			'WEBSITE': 'WEBSTAGING',
			'CHANNEL_ID': 'WEB',
			'CALLBACK_URL':'http://127.0.0.1:8000/handlerequest/', # handlerequest er por oneksomoy / dile run kore na abar / dile run kore
		}
		param_dict['CHECKSUMHASH'] = Checksum.generate_checksum(param_dict, MERCHANT_KEY)
		return render(request, 'paytm1.html', {'param_dict': param_dict})

	return render(request, 'checkout.html')
	'''
	'''
	#payu money
	#print(request.session['user_info'])
	try:
		if(request.session['user_info']):
			# single_user=request.user
			#print("true test-------------------------------------")
			if request.method=='POST': # 1st e ekhne ese check korche value gulo POST kina 1st e seta hcchhe na bole else part e gie current_datetime.html page e jacchee
				#print("post test--------")
				hash_object=hashlib.sha256(b'randint(0,20)')
				txnid=hash_object.hexdigest()[:20]
				data = {'txnid':txnid,
				'amount': request.session['total_amount'], # def cart_details er total_amount copy kore dite hbe [] er vetore
				'firstname': request.POST['firstname'], 
				'email': request.POST['email'],
				'phone': request.POST['phone'],
				'productinfo':request.POST['productinfo'], 
				'lastname': request.POST['lastname'],
				'address1': request.POST['address1'], 
				'address2': request.POST['address2'],
				'city': request.POST['city'], 
				'state': request.POST['state'],
				'country':request.POST['country'], 
				'zipcode': request.POST['zipcode']#, 
				# 'udf1': '', 
				# 'udf2': '', 'udf3': '', 'udf4': '', 'udf5': ''
				}
				payu_data=payu.transaction(**data)
				#print("form test--------------------------")
				return render(request,"payu_checkout.html",{'posted':payu_data}) # current_datetime.html page e j design ache sekhane submit korle payu_checkout.html page e jabe 
			#print("test hello==========================================")
			return render(request,"current_datetime.html") # jodi user_info te value thake tahole current_datetime.html page e jabe
		else:
			#print("else test--------------------------------->")
			return redirect('/LogIn')
	except Exception as e:
		#print("exception test---------------------------------------->",e)
		return redirect('/LogIn')
	'''
# user_info te value na thakle else part e asbe bolbe age login korte tarpor payment korte
# user_info te value na thakle exception eo aste pare tai sekhane geleo bolbe age login korte
'''
@csrf_exempt
def payu_success(request):
    data = {k: v[0] for k, v in dict(request.POST).items()}
    response = payu.verify_transaction(data)
    return JsonResponse(response)

@csrf_exempt
def payu_failure(request):
    data = {k: v[0] for k, v in dict(request.POST).items()}
    response = payu.verify_transaction(data)
    return JsonResponse(response)    
'''
@csrf_exempt
def callback(request):
    def verify_signature(response_data):
        client = razorpay.Client(auth=('rzp_test_QvJmsxzaVwb2t4', 'kDUiANWg5ziCQylXRcAsZXaH'))
        return client.utility.verify_payment_signature(response_data)

    print("Request POST data:", request.POST)

    if "razorpay_signature" in request.POST:
        payment_id = request.POST.get("razorpay_payment_id", "")
        print(payment_id)
        provider_order_id = request.POST.get("razorpay_order_id", "")
        print(provider_order_id)
        signature_id = request.POST.get("razorpay_signature", "")
        print(signature_id)
        order = Order.objects.get(provider_order_id=provider_order_id)
        order.payment_id = payment_id
        order.signature_id = signature_id
        order.save()
        if verify_signature(request.POST):
            order.status = PaymentStatus.SUCCESS
        else:
            order.status = PaymentStatus.FAILURE
        order.save()
        return render(request, "callback.html", context={"status": order.status})
    else:
        payment_id = json.loads(request.POST.get("error[metadata]")).get("payment_id")
        provider_order_id = json.loads(request.POST.get("error[metadata]")).get(
            "order_id"
        )
        order = Order.objects.get(provider_order_id=provider_order_id)
        order.payment_id = payment_id
        order.status = PaymentStatus.FAILURE
        order.save()
        return render(request, "callback.html", context={"status": order.status})