#coding:utf-8
from django.shortcuts import render
from django.http import HttpResponse
from django.http import HttpResponseRedirect
from django.shortcuts import render_to_response
from django.template import TemplateDoesNotExist, RequestContext
from django.views.decorators.csrf import csrf_exempt
from django.core.urlresolvers import reverse
from django.core import serializers
import ldap
import json
import models
from cmcc_dao import CMCCProjectDao
cmcc = CMCCProjectDao()

def index(request):
    string = u"我在自强学堂学习Django，用它来建网站"
    return render(request, 'home.html', {'string': string})

def login(request):
    if request.method == 'GET':
        
        return render_to_response("login.html", {}, RequestContext(request))
    elif request.method == 'POST':
        # print 'login post '
        return render(request, 'login.html')

def add(request):
    a = request.GET.get('a', 0)
    b = request.GET.get('b', 10)
    c = int(a)+int(b)
    return HttpResponse(str(c))

def add2(request, a, b):
    c = int(a) + int(b)
    print 'c is %s', c
    return HttpResponse(str(c))

def old_add2_redirect(request, a, b):
    print a
    return HttpResponseRedirect(
        reverse('add2', args=(a, b))
    )


def user_login(request):
    if request.method == 'GET':
        
        return render_to_response("login.html", {}, RequestContext(request))
    else:
        print 'login post '
        response = HttpResponse()
        name = request.POST.get('name')
        pw = request.POST.get('pw')
        request.session['username'] = name
        print login_validate(name, pw)
        if login_validate(name, pw):
            json_data = json.dumps({"status":200,"data":"","message":"login success!"})
            return HttpResponse(json_data, content_type="application/json")
        else:
            return json.dumps({"status":500,"data":"","message":"username or password error"})

def get_chip_name(request):
    chipdata = models.CmccProjectChip.objects.values("chip_name")
    print chipdata
    print request.session.get('username', False)
    chhiplist = []
    for chip in chipdata:
        chhiplist.append(chip['chip_name'])
    
    json_data = json.dumps({"status":200,"data":chhiplist,"message":"login success!"})
    return HttpResponse(json_data, content_type="application/json")

def cmcc_project_gethome_project_info(request):
    
    result = dict(state=200, data="", message="")
    search_data = {
                    'cust_name':request.GET.get('cust_name', ""),
                    'chip_name':request.GET.get('chip_name', ""),
                    'project_status':request.GET.get('status', ""),
                    'offset':request.GET.get('offset', 0),
                    'limit':request.GET.get('limit', 10),
                    'test_round':request.GET.get('test_round', ""),
                    'passed_round':request.GET.get('passed_round', ""),
                    'send_test_type':request.GET.get('send_test_type', ""),
                    'submiter': request.session['username']
                    }
    result_data,total = cmcc.get_my_project(search_data)
    project_result = {}
    project_result['rows'] = result_data
    project_result['total'] = total
    result['data'] = project_result
    # print project_result
    return HttpResponse(json.dumps(project_result), content_type="application/json")#json.dumps(result['data'])

def getproject_basic_info_by_all(request):
    result = dict(state=200, data="", message="")
    search_data = {
                    'cust_name':request.GET.get('cust_name', ""),
                    'chip_name':request.GET.get('chip_name', ""),
                    'project_status':request.GET.get('status', ""),
                    'offset':request.GET.get('offset', 0),
                    'limit':request.GET.get('limit', 10),
                    'test_round':request.GET.get('test_round', ""),
                    'passed_round':request.GET.get('passed_round', ""),
                    'send_test_type':request.GET.get('send_test_type', ""),
                    'submiter': request.session['username']
                    }
    search_data['project_status'] = search_data['project_status'].split(',')
    result_data,total = cmcc.get_all_project(search_data)
    all_result = {}
    all_result['rows'] = result_data
    all_result['total'] = total
    result['data'] = all_result        

def login_validate(username,password):
    # try:

    # if config.current_env != config.INTERNAL:
    username += "@spreadtrum.com"
    # else:
    #     username += "@sprd.com"

    con = ldap.initialize("ldap://spreadtrum.com")
    con.set_option(ldap.OPT_REFERRALS, 0)
    con.simple_bind_s(username,password)
    return True