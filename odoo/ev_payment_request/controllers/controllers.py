# -*- coding: utf-8 -*-
# from odoo import http


# class EvPaymentRequest(http.Controller):
#     @http.route('/ev_payment_request/ev_payment_request', auth='public')
#     def index(self, **kw):
#         return "Hello, world"

#     @http.route('/ev_payment_request/ev_payment_request/objects', auth='public')
#     def list(self, **kw):
#         return http.request.render('ev_payment_request.listing', {
#             'root': '/ev_payment_request/ev_payment_request',
#             'objects': http.request.env['ev_payment_request.ev_payment_request'].search([]),
#         })

#     @http.route('/ev_payment_request/ev_payment_request/objects/<model("ev_payment_request.ev_payment_request"):obj>', auth='public')
#     def object(self, obj, **kw):
#         return http.request.render('ev_payment_request.object', {
#             'object': obj
#         })
