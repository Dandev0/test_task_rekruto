from aiohttp import web


app = web.Application()
routes = web.RouteTableDef()


@routes.get('/rekruto')
async def handler_get(request):
    name = request.rel_url.query['name']
    message = request.rel_url.query['message']
    return web.Response(text=f"Hello {name}, {message}")


@routes.post('/rekruto')
async def handler_post(request):
    data = await request.json()
    name = data['name']
    message = data['message']
    return web.Response(text=f"Hello {name}, {message}")


def main():
    app.add_routes(routes)
    web.run_app(app, host='127.0.1.3', port=8080)


if __name__ == '__main__':
    main()
