# -*- coding: utf-8 -*-
from __future__ import absolute_import, print_function

from flask import request, g

from . import Resource
from .. import schemas


class TagsTagnameDate(Resource):

    def get(self, tagName, date):
        print(g.headers)

        return {'tag': 'something', 'count': 9573, 'articles': [], 'related_tags': []}, 200, None