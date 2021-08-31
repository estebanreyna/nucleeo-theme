# -*- coding: utf-8 -*-
# from odoo import http


# class Nucleeo-theme(http.Controller):
#     @http.route('/nucleeo-theme/nucleeo-theme/', auth='public')
#     def index(self, **kw):
#         return "Hello, world"

#     @http.route('/nucleeo-theme/nucleeo-theme/objects/', auth='public')
#     def list(self, **kw):
#         return http.request.render('nucleeo-theme.listing', {
#             'root': '/nucleeo-theme/nucleeo-theme',
#             'objects': http.request.env['nucleeo-theme.nucleeo-theme'].search([]),
#         })

#     @http.route('/nucleeo-theme/nucleeo-theme/objects/<model("nucleeo-theme.nucleeo-theme"):obj>/', auth='public')
#     def object(self, obj, **kw):
#         return http.request.render('nucleeo-theme.object', {
#             'object': obj
#         })
