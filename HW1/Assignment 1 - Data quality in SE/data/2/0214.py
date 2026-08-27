import tornado
import copy


class DjangoHandler(tornado.web.RequestHandler):
    async def reroute(self):
        http = tornado.httpclient.AsyncHTTPClient()

        new_request = copy.deepcopy(self.request)
        url_obj = copy.urlparse(new_request.url)
        new_request.url = f"{url_obj.scheme}://localhost:9000{url_obj.path}"

        return await http.fetch(new_request)

    get = reroute
    post = reroute


application = tornado.web.Application([
    # (r'/chat', WebsocketChatHandler),
    (r'/', DjangoHandler),
])
application.listen(80)

tornado.ioloop.IOLoop.current().start()
