from abc import ABCMeta, abstractmethod
from flask.blueprints import Blueprint
from plugins.reflection.activator import Activator
from plugins.reflection.module import Module
from flask import Blueprint
from flask.app import Flask
from plugins.collections.generic import DictionaryC, KeyValuePair
from plugins.reflection.type import typeof


class RouteAPI(metaclass=ABCMeta):
    @abstractmethod
    def resister_route() -> Blueprint:
        """ resister route
        @returns: name of the module: provede `Blueprint(__name__,__name__)`
        """
        return


class Router:
    # static
    __routes = DictionaryC[str, Blueprint]()

    @staticmethod
    def all_routes():
        """ Returns all routes
        """
        return Router.__routes

    @staticmethod
    def activate_all_routes(app: Flask):
        """ Resister all routes
        """

        # Write all route module to resister
        rootAPI = typeof(RouteAPI).TypeInfo
        types =\
            Module\
            .GetModules("api")\
            .Select(lambda module: module.GetTypes().Where(lambda t: t.BaseType == rootAPI).First())\
            .NotNone()
        for t in types:
            if t is not None:
                method = t.GetMethod("resister_route")
                if method is not None:
                    bp: Blueprint =\
                        method.Invoke(Activator.CreateInstance(t))
                    Router.__routes.AddKP(KeyValuePair(bp.name, bp))
                    app.register_blueprint(bp)
