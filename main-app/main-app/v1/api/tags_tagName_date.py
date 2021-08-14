# -*- coding: utf-8 -*-
from __future__ import absolute_import, print_function

from flask import request, g
from ..models import Articles, Tags, TagNames

from . import Resource
from .. import schemas


class TagsTagnameDate(Resource):

    def get(self, tagName, date):
        print(g.headers)
        date = date[:4] + '-' + date[4:6] + '-' + date[6:]
        print(date, flush=True)
        try:
            article_ids_1 = Articles.select(Articles.id).where(
                Articles.date == date)
            article_ids_1 = [a.id for a in article_ids_1]

            article_ids_2 = Tags.select(Tags.article_id).join(TagNames).where(
                TagNames.name == tagName.lower())
            article_ids_2 = [t.article_id.id for t in article_ids_2]
            # intersection
            ids = list(set(article_ids_1) & set(article_ids_2))
            if not ids:
                return {"message": "Article not found"}, 404, None
        except Articles.DoesNotExist:
            return {"message": "Article not found"}, 404, None

        res = Tags.select(Tags.tag_id).where(Tags.article_id.in_(ids))
        res = [r.tag_id.id for r in res]

        related_tags = TagNames.select(
            TagNames.name).distinct().where(TagNames.id.in_(res))
        related_tags = [r.name for r in related_tags]
        related_tags.remove(tagName)

        return {'tag': tagName, 'count': len(res), 'articles': ids[:10], 'related_tags': related_tags}, 200, None
