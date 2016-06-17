from django.shortcuts import render_to_response
from django.template import RequestContext

def hotel(request):
	hotel1 = {'name':'The Okura Prestige Taipei', 'address':'No.9 Nanjing E. Rd., Sec. 1, Taipei, Taiwan', 'price':'$157-$329', 'phone':'02-25231111','website': 'www.okurataipei.com.tw'}
	hotel2 = {'name':'Shangri-La Far Eastern Plaza Hotel Taipei', 'address':'No.201 Tun Hwa South Road, Section 2, Taipei 106, Taiwan', 'price':'$196 - $337 ', 'phone':'02-23763229','website': 'www.shangri-la.com/taipei/fareasternplazashangrila/'}
	hotel3 = {'name':'Swiio Hotel ', 'address':' Section 1, Daan Rd, Da’an District, Taipei City, 106', 'price':'$37 - $109', 'phone':'0807 877 882','website': 'www.swiio.com/hotels/daan'}
	hotel4 = {'name':'Dandy Hotel', 'address':'No. 2 Lane 728, Section 6, Zhongshan North Road, Shilin District, Taipei 111, Taiwan', 'price':'$79 - $125 ', 'phone':'02 2873 2222','website': 'www.dandyhotel.com.tw/new/M/tw/'}
	hotel5 = {'name':'Les Suites Taipei Ching Cheng', 'address':'No.12 Ching Cheng Street, Songshan District,Taipei 105, Taiwan', 'price':' $211 - $258 ', 'phone':'02-23763229','website': 'www.suitetpe.com.tw'}
	hotel6 = {'name':'San Want Residences Taipei', 'address':'No.128 Section 1, Nanjing East Road, Zhongshan District, Taipei, Taiwan', 'price':'$127 - $671 ', 'phone':'02 2511 5185','website': 'www.swresidences.com'}
	hotel7 = {'name':'Mandarin Oriental', 'address':'No.158 Dunhua North Road, Songshan District, Taipei 10548, Taiwan', 'price':'$323 - $480', 'phone':'02 2715 6888','website': 'www.mandarinoriental.com/taipei'}
	hotel8 = {'name':'Grand Hyatt Taipei', 'address':'No.2 SongShou Road, Xinyi District, Taipei 110, Taiwan', 'price':'$269 - $440 ', 'phone':'02 2720 1234','website': 'www.taipei.grand.hyatt.com'}
	hotel9 = {'name':'W Taipei', 'address':'No.10 Section 5, Zhongxiao East Road, Xinyi District, Taipei 110, Taiwan', 'price':'$295 - $427 ', 'phone':'02 7703 8888','website': 'www.wtaipei.com'}
	hotel10 = {'name':'Regent Taipei', 'address':'No.3, Lane 39, Section 2, Chungshan North Road, Taipei 104, Taiwan ', 'price':' $203 - $339', 'phone':'02 2523 8000','website': 'www.regenttaipei.com'}
	hotels = [hotel1,hotel2,hotel3,hotel4,hotel5,hotel6,hotel7,hotel8,hotel9,hotel10]
	return render_to_response('hotel.html',locals())

def taipei(request):
	return render_to_response('home.html',locals())

def home(request):
	return render_to_response('home.html',locals())

def transportation(request):
	return render_to_response('transportation.html',locals())

def contact(request):
	return render_to_response('contact.html',locals())

def taipei101(request):
	return render_to_response('taipei101.html',locals())

def cks(request):
	return render_to_response('Chiang Kai-shek Memorial Hall.html',locals())

def museum(request):
	return render_to_response('National Palace Museum.html',locals())

def yehliu(request):
	return render_to_response('Yeh Liu Geo Park.html',locals())

def yms(request):
	return render_to_response('Yangmingshan National Park.html',locals())

def huashan(request):
	return render_to_response('Huashan 1914 Creative Park.html',locals())

def xingtian(request):
	return render_to_response('xingtian temple.html',locals())

def tamsui(request):
	return render_to_response('Tamsui.html',locals())

def chiufen(request):
	return render_to_response('Chiufen.html',locals())

def longshan(request):
	return render_to_response('Longshan Temple.html',locals())