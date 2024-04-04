from odoo import models, fields

class paymentrequestline(models.Model):
    _name = 'payment.request.line'
    _description = 'Payment Request Line'

    request_id = fields.Many2one('payment.request', string='Request')
    document_id = fields.Many2one('payment.document')
    required = fields.Boolean(string='Required', default=True)
    file = fields.Text(string='File')