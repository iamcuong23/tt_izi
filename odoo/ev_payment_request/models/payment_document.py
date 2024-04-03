from odoo import models, fields

class paymentdocument(models.Model):
    _name = 'payment.document'
    _description = 'Payment Document'

    name = fields.Char(string='Name', required=True)
    active = fields.Boolean(string='Active', default=True)