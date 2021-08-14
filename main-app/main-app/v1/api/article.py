# -*- coding: utf-8 -*-
from __future__ import absolute_import, print_function

from flask import request, g
from ..helpers import authorize
from ..models import Articles, Tags, TagNames
import uuid

from . import Resource
from .. import schemas


class Article(Resource):

    def post(self):

        user = authorize(g.headers)
        data = request.get_json()
        unique_uuid = str(uuid.uuid4())
        Articles.create(
            title=data.get('title'),
            uuid=unique_uuid,
            body=data.get('body'),
            date=data.get('date'),
            user_id=user.get('id'),
        )
        article = Articles.select().where(Articles.uuid == unique_uuid).dicts().get()
        tags_arr = []
        for tag in data.get('tags'):
            try:
                t = TagNames.select().where(TagNames.name == tag.lower()).dicts().get()

            except TagNames.DoesNotExist:
                TagNames.create(
                    name=tag.lower()
                )
                t = TagNames.select().where(TagNames.name == tag).dicts().get()
            tags_arr.append(t['name'])
            Tags.create(
                tag_id=t['id'],
                article_id=article['id']
            )

        return {'title': article['title'], 'date': article['date'], 'body': article['body'], 'tags': tags_arr}, 200, None
