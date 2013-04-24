# -*- coding: utf-8 -*-
# Create your views here.
from django.http import HttpResponse
from django.shortcuts import render_to_response
from djtest.books.models import Book

def search_form(request):
    return render_to_response('search_form.html')

#def search(request):
    #if 'q' in request.GET:
        #message = 'You searched for: %r' % request.GET['q']
    #else:
        #message = 'You submitted an empty form.'
    #return HttpResponse(message)

# 直接通过地址访问/search/(没有GET数据)时，跳转至search_form.html而且不会有错误提示信息.
def search(request):
    errors = []
    error = False
    if 'q' in request.GET:
        q = request.GET['q']
        if not q:
            errors.append('Enter a search term.')
        elif len(q) > 20:
            errors.append('Please enter at most 20 characters.')
        else:
            books = Book.objects.filter(title__icontains=q)
            return render_to_response('search_results.html',
                    {'books': books, 'query': q})
    return render_to_response('search_form.html',
            {'errors': errors})
