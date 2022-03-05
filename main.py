from fastapi import FastAPI


app = FastAPI()


fake_items_db = [{"blog_title": "Foo"}, {"blog_title": "Bar"}, {"blog_title": "Baz"}]

@app.get('/')
async def index():
	return {'hello':'world'}


@app.get('/blogs/')
async def blogs(skip:int = 0, limit:int = 10):
	return fake_items_db[skip: skip+limit]


@app.get('/about')
async def about():
	return {'data':{'name':'koushik','title':'hait'}}