from django.shortcuts import render
from homepage.homepageDAO import homeList



# Create your views here.

h = homeList()
all_list = h.getAllList()

def home(request):
    

    return render(request, 'homepage/index2.html', {'group': 'main',
                                                   'all_list' : all_list})

def index(request):

    return render(request, 'homepage/index.html', {'group': 'main',
                                                   'all_list' : all_list})
    
def contact(request):
    list = h.getGroupList('contact')
    
    url = "homepage/" + list[0]['CATEGORY'] + "/" + list[0]['FILENAME']

    return render(request, 'homepage/index.html', {'group' : list[0]['CATEGORY'],
                                               'all_list' : all_list,
                                              'list' : list,
                                              'url': url,
                                              'num':list[0]['SEQ'],
                                              'name':list[0]['NAME']})

def page(request, page_url):
    
    if page_url == 'solution' or page_url == 'product' or page_url == 'service' or page_url == 'company' or page_url == 'resource': 
        list = h.getGroupList(page_url) 
    else : list = h.getList(page_url)
        
    
    
    url = "homepage/" + list[0]['CATEGORY'] + "/" + list[0]['FILENAME']

    return render(request, 'homepage/index.html', {'group' : list[0]['CATEGORY'],
                                               'all_list' : all_list,
                                              'url': url,
                                              'name':list[0]['NAME']})
    

