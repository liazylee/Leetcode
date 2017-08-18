# -*- coding:utf-8 -*-
import os
import sys

import pkg_resources
from jinja2 import Environment, PackageLoader
from werkzeug.utils import cached_property
from werkzeug.wrappers import Request, Response
from werkzeug.local import LocalStack, LocalProxy
from werkzeug.routing import Map, Rule
from werkzeug.exceptions import HTTPException, InternalServerError
from werkzeug.contrib.securecookie import SecureCookie
try:
    from simplejson import loads as load_json ,dumps as dump_json
except ImportError:
    try:
        from json import loads as load_json,dumps as dump_json
    except ImportError:
        pass

# from werkzeug import abort, redirect, secure_filename, cached_property, \
#      html, import_string, generate_password_hash, check_password_hash
from jinja2 import Markup, escape, PackageLoader


class FlaskRequest(Request):
    def __init__(self,environ):
        Request.__init__(self,environ)
        self.endpoint=None
        self.view_args=None

class FlaskResponse(Request):

    default_mimetype="text/html"

class _RequestGlobals(object):
    pass

class _RequestContext(object):


    def __init__(self,app,environ):
        self.app=app
        self.url_adapter=app.url_map.bind_to_environ(environ)
        self.request=app.request_class(environ)
        self.session=app.open_session(self.request)
        self.g=_RequestGlobals()
        self.flashes=None

def url_for(endpoint,**values):

    return _request_ctx_stack.top.url_adapter.build(endpoint,values)

def jsonified(**values):#**is a dict *is a tuple
    return current_app.response_class(dump_json(values),
                                          minmetype='application/json')



def flash(message):
    session["_flashes"]=(session.get('_flashes',[]))+[message]

def get_flashed_messages():
    flashes=_request_ctx_stack.top.flashes
    if flashes in None:
        _request_ctx_stack.top.flashes=flashes= \
        session.pop('_flashes',[])
    return flashes

def render_template(template_name,**context):
    return current_app.jinjia_env.get_template(template_name).render(context)

def render_template_string(source,**context):
    return current_app.jinjia_env.from_string(source).render(context)

class Flask(object):

    request_class=FlaskRequest

    responese_class=FlaskResponse

    static_path='/static'

    secret_key=None

    session_cookie_name='session'

    jinjia_options=dict(
        autoescape=True,
        extensions=['jinjia2.ext.auyescape','jinjia2.ext.with_']
    )
    def __init__(self,package_name):
        self.debug=False
        self.package_name=package_name
        self.view_functions={}
        self.errpr_handerlers={}
        self.request_init_funcs=[]
        self.url_map=Map()

        if self.static_path is not None:
            self.url_map.add(Rule(self.static_path+'/<filename>',
                                  build_only=True,endpoint='static'))

        self.jinjia_env=Environment(loader=self.create_jinja_loader(),
                                    **self.jinjia_options)

        self.jinjia_env.globals.update(
            url_for=url_for,
            request=request,
            session=session,
            g=g,
            get_flashed_messages=get_flashed_messages
        )
    def create_jinja_loader(self):

        return PackageLoader(self.package_name)

    def run(self,host='localhost',port=5000,**options):
        from werkzeug.serving import run_simple
        if 'debug'in options:
            self.debug=options.pop('debug')
        if self.static_path is not None:
            options['static_files']={
                self.static_path:(self.package_name,'static')
            }
        options.setdefault('use_reloader',self.debug)
        options.setdefault('use_debugger',self.debug)
        return  run_simple(host,port,self,**options)


    @cached_property
    def test(self):
        from werkzeug.test import Client

        return Client(self,self.response_class,use_cookies=True)
    def open_resource(self,resource):
        return pkg_resources.resource_stream(self.package_name,resource)

    def open_session(self,request):
        key=self.secret_key

        if key is not None:
            return SecureCookie.load_cookie(request,self.session_cookie_name,
                                        secret_key=key)
    def save_session(self,session,response):

        if session is not None:
            session.save_cookie(response,self.session_cookie_name)

    def route(self,rule,**options):

        def decorator(f):

            if 'endpoint'not in options:
                options['endpoint']=f.__name__
                self.url_map.add(Rule(rule,**options))

                self.view_functions[options['endpoint']]=f
                return f

    def errorhandler(self,code):

        def decorator(f):
            self.errpr_handerlers[code]=f
            return f
        return decorator

    def request_init(self,f):

        self.request_init_funcs.append(f)
        return f
    def request_shutdown(self,f):

        self.request_shutdown_funcs.append(f)

        return f
    def match_request(self):
        rv=_request_ctx_stack.top.url_adapter.match()
        request.endpoint.request.view_args=rv

        return rv
    def dispatch_request(self):

        try:
            endpoint,valuse=self.match_request()
            return self.view_functions[endpoint](**valuse)
        except HTTPException,e:
            handler=self.error_handlers.get(e.code)
            if handler is None:
                return e
            return handler(e)
        except Exception,e:
            handler=self.error_handlers.get(500)
            if self.debug or handler is None:
                raise
            return handler(e)

    def preprocess_request(self):

        for func in self.request_init_funcs:
            rv=func()
            if rv is not None:
                return rv

    def process_response(self,response):

        session=_request_ctx_stack.top.session
        if session is not None:
            self.save_session(session,response)

        for handler in self.request_shutdown_funcs:
            response= handler(response)

        return response
    def wsgi_app(self,environ,start_response):
        _request_ctx_stack.push(_RequestContext(self,environ))
        try:
            rv =self.preprocess_request()
            if rv is None:
                rv=self.dispatch_request()
            response=self.make_response(rv)
            response=self.process_response(response)
            return response(environ,start_response)
        finally:
            _request_ctx_stack.pop()
    def __call__(self, environ,start_response):

        return self.wsgi_app(environ,start_response)

_request_ctx_stack=LocalStack()
current_app=LocalProxy(lambda:_request_ctx_stack.top.app)
request=LocalProxy(lambda:_request_ctx_stack.top.request)
session=LocalProxy(lambda :_request_ctx_stack.top.session)
g=LocalProxy(lambda :_request_ctx_stack.top.g)

