# -*- coding: utf-8 -*-
from __future__ import absolute_import, print_function

from flask import request, g

from . import Resource
from .. import schemas


class Article(Resource):

    def post(self):
        print(g.json)
        print(g.headers)

        return {'title': 'something', 'date': 'something', 'body': 'something', 'tags': []}, 200, None