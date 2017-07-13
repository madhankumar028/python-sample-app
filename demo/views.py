# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from django.views.generic import TemplateView
from django.shortcuts import render

from django.http import HttpResponse

from couchbase import Couchbase
from couchbase.bucket import Bucket
from couchbase.exceptions import *
from couchbase.views.params import Query

import models

class HomePageView(TemplateView):
    def get(self, request, **kwargs):
        return render(request, 'index.html', context=None)

class TableView(TemplateView):
    def get(self, request, **kwargs):
        return render(request, 'tables.html', context=None)

class AboutPageView(TemplateView):
    def get(self, request, **kwargs):
        bucketObject = models.CBModel.connect_cb_bucket()

        query_string = 'select hestia.* from hestia where `role`.role_id="poa"'

        nlql_request = bucketObject.n1ql_query(query_string)

        result = []

        for query_result in nlql_request:
            print query_result
            result.append(query_result)

        return render(request, 'about.html', {'result': result})

class GetHestiaAdmin(TemplateView):
    def get(self, request):
        bucketObject = models.CBModel.connect_cb_bucket()

        query_string = 'SELECT * FROM `hestia` WHERE email="admin@hestia.com"'

        nlql_request = bucketObject.n1ql_query(query_string)

        result = []

        for query_result in nlql_request:
            result.append(query_result)

        return HttpResponse(result)
