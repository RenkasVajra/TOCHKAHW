from aiohttp import web

async def echo_handler(request):
    data = await request.text()
    return web.Response(text=data)

async def headers_handler(request):
    headers = dict(request.headers)
    return web.json_response(headers)

async def hello_handler(request):
    return web.Response(text="Hello")

app = web.Application()
app.router.add_get('/echo', echo_handler)
app.router.add_get('/hello', hello_handler)
app.router.add_post('/echo', echo_handler)

if __name__ == '__main__':
    web.run_app(app)
