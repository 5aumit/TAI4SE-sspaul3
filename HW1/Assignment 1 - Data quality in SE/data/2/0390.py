#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import tornado.web

from sqlalchemy import desc
from sqlalchemy.orm import contains_eager

from main_app.models.post import Post
from main_app.models.thread import PostThread, User2Thread

from main_app.handlers.base_handler import BaseHandler


class API_Comments(BaseHandler):

    def post(self):
        '''
            add comment to a post

            example:
                POST /comment
                    body: post_id, text

            returns:
                200 - the comment created
                406 - incorrect data
        '''
        arg_comment = self.get_argument('comment')
        try:
            post_id = int(arg_comment['post_id'])
            text = str(arg_comment['text'])
        except KeyError, ValueError:
            raise tornado.web.HTTPError(406)
        if not text:
            # the comment text is empty
            raise tornado.web.HTTPError(406)
        # get post + thread + User2Thread
        post = self.db.query(Post).\
            join(
                PostThread, Post.thread_id == PostThread.id
            ).join(
                User2Thread
            ).options(
                contains_eager(PostThread.user2thread)
            ).filter(
                Post.id == post_id
            ).filter(
                User2Thread.user_id.in_(DEFAULT_USER_ID, self.current_user),
            ).filter(
                User2Thread.is_current()
            ).filter(
                User2Thread.allow_add_posts == True
            ).order_by(
                desc(User2Thread.user_id)
            ).first()