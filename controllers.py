# -*- coding: utf-8 -*-
from openerp import http

class Webdemo(http.Controller):
    @http.route('/webdemo/',auth='public')
    def index(self):
        return http.request.render('demo_website.index',{
            'employees': ["giovanni capalbo","stefan rinjhart","holger brunn" ,"lara freeke" ,"anne sedee","ronald portier","hans van dijk"],
        })

