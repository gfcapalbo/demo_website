# -*- coding: utf-8 -*-
from openerp import http

class Webdemo(http.Controller):
    @http.route('/webdemo/',auth='public')
    def index(self):
        return "Hello, world!"

