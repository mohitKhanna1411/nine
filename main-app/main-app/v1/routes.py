# -*- coding: utf-8 -*-

###
### DO NOT CHANGE THIS FILE
### 
### The code is auto generated, your change will be overwritten by 
### code generating.
###
from __future__ import absolute_import

from .api.auth_login import AuthLogin
from .api.auth_signup import AuthSignup
from .api.article import Article
from .api.article_articleId import ArticleArticleid
from .api.tags_tagName_date import TagsTagnameDate


routes = [
    dict(resource=AuthLogin, urls=['/auth/login'], endpoint='auth_login'),
    dict(resource=AuthSignup, urls=['/auth/signup'], endpoint='auth_signup'),
    dict(resource=Article, urls=['/article/'], endpoint='article'),
    dict(resource=ArticleArticleid, urls=['/article/<int:articleId>'], endpoint='article_articleId'),
    dict(resource=TagsTagnameDate, urls=['/tags/<tagName>/<date>'], endpoint='tags_tagName_date'),
]