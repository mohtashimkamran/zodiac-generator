from Controllers import mombassador

V1RoutesDict ={
    '/test': mombassador.test,
}

V1RoutesMethodsDict = {
    mombassador.test: ['GET']
}