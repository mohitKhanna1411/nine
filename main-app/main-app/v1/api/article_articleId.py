# -*- coding: utf-8 -*-
from __future__ import absolute_import, print_function

from flask import request, g
from ..models import Articles, Tags, TagNames
from ..helpers import authorize

from . import Resource
from .. import schemas


class ArticleArticleid(Resource):

    def get(self, articleId):
        authorize(g.headers)
        try:
            article = Articles.select().where(Articles.id == articleId).dicts().get()
        except Articles.DoesNotExist:
            return {"message": "Article not found"}, 404, None

        res = TagNames.select(TagNames.name).join(Tags).where(
            Tags.article_id == articleId)
        res = [t.name for t in res]
        return {'title': article['title'], 'date': article['date'], 'body': article['body'], 'tags': res}, 200, None
