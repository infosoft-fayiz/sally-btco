# -*- coding: utf-8 -*-
# from odoo import http


# class Flower(http.Controller):
#     @http.route('/flower/flower', auth='public')
#     def index(self, **kw):
#         return "Hello, world"

#     @http.route('/flower/flower/objects', auth='public')
#     def list(self, **kw):
#         return http.request.render('flower.listing', {
#             'root': '/flower/flower',
#             'objects': http.request.env['flower.flower'].search([]),
#         })

#     @http.route('/flower/flower/objects/<model("flower.flower"):obj>', auth='public')
#     def object(self, obj, **kw):
#         return http.request.render('flower.object', {
#             'object': obj
#         })
