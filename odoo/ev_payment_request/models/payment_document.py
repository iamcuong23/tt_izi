from odoo import models, fields


class paymentdocument(models.Model):
    _name = 'payment.document'
    _description = 'Payment Document'

    document = fields.Char(string='Name Document', required=True)
    active = fields.Boolean(string='Active', default=True)
