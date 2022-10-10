# -*- coding: utf-8 -*-
# from odoo import http


# class GestionFlota(http.Controller):
#     @http.route('/gestion_flota/gestion_flota', auth='public')
#     def index(self, **kw):
#         return "Hello, world"

#     @http.route('/gestion_flota/gestion_flota/objects', auth='public')
#     def list(self, **kw):
#         return http.request.render('gestion_flota.listing', {
#             'root': '/gestion_flota/gestion_flota',
#             'objects': http.request.env['gestion_flota.gestion_flota'].search([]),
#         })

#     @http.route('/gestion_flota/gestion_flota/objects/<model("gestion_flota.gestion_flota"):obj>', auth='public')
#     def object(self, obj, **kw):
#         return http.request.render('gestion_flota.object', {
#             'object': obj
#         })
