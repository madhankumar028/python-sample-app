# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models

from couchbase import Couchbase
from couchbase.bucket import Bucket
from couchbase.exceptions import *
from couchbase.views.params import Query

class CBModel:

    @staticmethod
    def connect_cb_bucket():
        db = Bucket('couchbase://192.168.244.202/hestia')
        return db

    def getUserByAdmin():
        bucketObject = connect_cb_bucket()
        print 'model has been invoked'
        query_string = 'SELECT * FROM `hestia` WHERE email="admin@hestia.com"'
        nlql_request = bucketObject.n1ql_query(query_string)
        result = []
        for query_result in nlql_request:
            result.append(query_result)
        return result
