from utils.app import app
from routes.ClientsRoutes import RoutesV1
import os
app.register_blueprint(RoutesV1, url_prefix='/')

@app.route('/')
def index():
    return 'Testing Purpose'

BASE_PREFIX = ''


@app.route(BASE_PREFIX+'/health')
def health():
    return 'Health Check'

@app.route(BASE_PREFIX+'/healthz')
def healthz():
    return 'Health Check'

@app.route(BASE_PREFIX+'/health')
def health2():
    return 'Health Check'

@app.route(BASE_PREFIX+'/healthz')
def healthz2():
    return 'Health Check'