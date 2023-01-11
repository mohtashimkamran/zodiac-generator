import imp
from flask import Blueprint
from .v1_routes import V1RoutesDict, V1RoutesMethodsDict
import os
RoutesV1 = Blueprint('api', __name__)
BASE_PREFIX = ''
V1_API_PREFIX = 'v1'

for url, route in V1RoutesDict.items():
    RoutesV1.route(BASE_PREFIX + V1_API_PREFIX + url, methods=V1RoutesMethodsDict[route])(route)
