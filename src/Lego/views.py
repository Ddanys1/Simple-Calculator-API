from django.shortcuts import render
from django.http import HttpResponse


value_list=[]
opr_list=['+','-','*','/']


def home(request):
	return render(request,'set.html',{})


def answer(request):
	global value_list

	x_forwarded_for = request.META.get('HTTP_X_FORWARDED_FOR')
	if x_forwarded_for:
		ip = x_forwarded_for.split(",")[0]
	else:
		ip = request.META.get("REMOTE_ADDR")

	ip_list = []		
	for item in value_list:		
		if item.get(str(ip)):
			ip_list.append(item)

	v1 = ''
	v2 = ''
	v3 = ''

	if len(ip_list)==1:
		v1 = ip_list[0].get(str(ip))
	if len(ip_list)==2:
		v1 = ip_list[0].get(str(ip))
		v2 = ip_list[1].get(str(ip))
	if len(ip_list)==3:
		v1 = ip_list[0].get(str(ip))
		v2 = ip_list[1].get(str(ip))
		v3 = ip_list[2].get(str(ip))

	if len(ip_list)==3:
		if ip_list[2].get(str(ip))=='-':
			result = ip_list[0].get(str(ip)) - ip_list[1].get(str(ip))
			for item in ip_list:
				value_list.remove(item)
			return render(request,'answer.html',{'result':result})
		elif ip_list[2].get(str(ip))=='+':
			result = ip_list[0].get(str(ip)) + ip_list[1].get(str(ip))
			for item in ip_list:
				value_list.remove(item)
			return render(request,'answer.html',{'result':result})		
		elif ip_list[2].get(str(ip))=='*':
			result = ip_list[0].get(str(ip)) * ip_list[1].get(str(ip))
			for item in ip_list:
				value_list.remove(item)
			return render(request,'answer.html',{'result':result})
		elif ip_list[2].get(str(ip))=='/':
			result = ip_list[0].get(str(ip)) / ip_list[1].get(str(ip))
			for item in ip_list:
				value_list.remove(item)
			return render(request,'answer.html',{'result':result})		
	else:
		return render(request,'bad.html', {'v1':v1,'v2':v2,'v3':v3})	


def check_list(request):
	return render(request,'ok.html',{'list':value_list})


def ipaddress(request):
	global value_list
	x_forwarded_for = request.META.get('HTTP_X_FORWARDED_FOR')
	if x_forwarded_for:
		ip = x_forwarded_for.split(",")[0]
	else:
		ip = request.META.get("REMOTE_ADDR")

	ip_list = []		
	for item in value_list:		
		if item.get(str(ip)):
			ip_list.append(item)


	if len(ip_list) == 0:
		try:
			val1 = int(request.POST['numb1'])	
		except:
			return render(request,'bad3.html',{'list':value_list})
		else:
			res = val1
			res_dic = {ip:res}
			value_list.append(res_dic)
			return render(request,'get.html',{'result':res,'value':val1, 'list':value_list}) 

	elif len(ip_list) == 1:
		try:
			val1 = int(request.POST['numb1'])	
		except:
			return render(request,'bad4.html',{'list':value_list})
		else:
			res = val1
			res_dic = {ip:res}
			value_list.append(res_dic)
			return render(request,'get.html',{'result':res,'value':val1, 'list':value_list, 'ip':ip_list}) 
	

	elif len(ip_list)==2:
		try:
			val3 = request.POST['numb1']
		except:
			return render(request,'bad5.html',{'list':value_list})
		if val3 not in opr_list:
			return render(request,'bad5.html',{})
		else:
			opr = val3
			res_dic = {ip:opr}
			value_list.append(res_dic)
			return render(request,'get.html',{'value':val3, 'list':value_list, 'ip':ip_list})

	else:
		return render(request,'bad2.html',{})