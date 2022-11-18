from aiohttp import web
import aiohttp_jinja2
import jinja2


app = web.Application()
routes = web.RouteTableDef()


@routes.get('/')
@aiohttp_jinja2.template('index.html')
async def handler_get(request):
    name = request.rel_url.query['name']
    message = request.rel_url.query['message']
    info = f'{name}, {message}'
    return info 


@routes.post('/')
async def handler_post(request):
    data = await request.json()
    name = data['name']
    message = data['message']
    return web.Response(text=f"Hello {name}, {message}")


def main():
    app.add_routes(routes)
    web.run_app(app, host='https://dandev0.github.io/test_task_rekruto/', port=8080)


if __name__ == '__main__':
    main()
