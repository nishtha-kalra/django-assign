import json

from django.http import HttpResponse
from django.shortcuts import HttpResponseRedirect
from django.shortcuts import render_to_response
from django.template import RequestContext
from django.template import loader
from helpers.lib import *

#from django.contrib import auth
#from django.core.context_processors import csrf

# Create your views here.

def index(request):
    template = loader.get_template('polls/index.html')
    return HttpResponse(template.render(request))

def register(request):
    if request.method == "GET":
        return render_to_response('polls/register.html', context_instance=RequestContext(request))
    else:
        name = request.POST.get('Name')
        email = request.POST.get('Email')
        password = request.POST.get('Password')
        re_password = request.POST.get('RePassword')
        RegisterHelp.add_details(name, email, password, re_password)
        return render_to_response('polls/index.html', context_instance=RequestContext(request))

def login(request):
    print request.method
    if request.method == "GET":
        return render_to_response('polls/login.html', context_instance=RequestContext(request))
    else:
        name = request.POST.get('Name')
        password = request.POST.get('Password')
        obj = RegisterHelp.validate_details(name, password)
        if obj is not None:
            request.session['name'] = obj.name
            return render_to_response('polls/home.html', context_instance=RequestContext(request))
        else:
            return render_to_response('polls/login.html', context_instance=RequestContext(request))

def check_login(view):
    def _check(request, *args, **kwargs):
        if 'name' in request.session:
            return view(request, *args, **kwargs)
        else:
            return HttpResponseRedirect('/polls/login')
    return _check

@check_login
def home(request):
    template = loader.get_template('polls/home.html')
    return render_to_response('polls/home.html', context_instance=RequestContext(request))

def logout(request):
    print request.method
    if request.method == 'GET':
        return render_to_response('polls/index.html', context_instance=RequestContext(request))
    else:
        del request.session['name']
        return render_to_response('polls/index.html', context_instance=RequestContext(request))

@check_login
def add(request):
    if request.method == "GET":
        return render_to_response('polls/add.html', context_instance=RequestContext(request))
    else:
        dir_name = request.POST.get('dir_name')
        phone_number = request.POST.get('phone_number')
        alt_number = request.POST.get('alt_number')
        address = request.POST.get('address')
        DirectoryHelp.add_to_dir(dir_name, phone_number, alt_number, address)
        #return render_to_response('directory', context_instance=RequestContext(request))
        return HttpResponseRedirect('/polls/directory')

@check_login
def directory(request):
    dir_list = DirectoryHelp.get_details()
    return render_to_response('polls/directory.html', { 'dir_list' : dir_list },context_instance=RequestContext(request))

@check_login
def delete(request):
    if request.POST:
        id = request.POST.get('id')
        DirectoryHelp.delete(id)
        res = {'status': True, 'msg': "Deleted entry."}
        return HttpResponse(json.dumps(res))

@check_login
def edit(request):
    print "in /polls/edit"
    print request.method
    '''if request.GET:
        entry = DirectoryHelp.get_entry_details(id)
        t = loader.get_template("edit_entry.html")
        e = {'entry' : entry}
        return HttpResponse(t.render(e, request))
    else:'''
    if request.POST:
        print "here"
        id = request.POST.get('id')
        entry = DirectoryHelp.get_entry_details(id)
        ename = entry.dir_name
        ephone_number = entry.phone_number
        ealt_number = entry.alt_number
        eaddress = entry.address
        DirectoryHelp.update(id, ename, ephone_number, ealt_number, eaddress)
        res = {'status': True, 'msg': "Deleted entry."}
        return HttpResponse(json.dumps(res))

        '''result = {'ename': ename, 'ealt_number': ealt_number, 'ephone_number': ephone_number, 'eaddress': eaddress}
        return HttpResponse(json.dumps(result))
        return render_to_response('polls/edit_entry.html', {'entry': entry}, context_instance=RequestContext(request))'''

def get_details(request, id=None):
    if request.method == "GET":
        obj = DirectoryHelp.get_details(id)
        t = loader.get_template('edit_entry.html')
        e = {'entry': obj}
        return HttpResponse(t.render(e, request))
    else:
        id = request.POST.get('id')
        ename = request.POST.get('ename')
        phone_no = request.POST.get('phone_no')
        alt_no = request.POST.get('alt_no')
        addrs = request.POST.get('addrs')
        status, msg = DirectoryHelp.update(id, ename, phone_no, alt_no, addrs)
        return HttpResponse(json.dumps({'status': status, 'msg': msg}))


