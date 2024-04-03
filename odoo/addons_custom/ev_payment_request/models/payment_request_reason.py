from odoo import models, fields, api

class paymentrequestreason(models.Model):
    _name = 'payment.request.reason'
    _description = 'Payment Request Reason'

    name = fields.Char(string='Reason Name', required=True)
    is_advance = fields.Boolean(string='Is Advance Payment', default=True)
    invoice_condition = fields.Selection([('required', 'Required'), ('no-required', 'No-required'), ('none', 'None')],
                                         string="Invoice", default='none')
    purchase_condition = fields.Selection([('required', 'Required'), ('no-required', 'No-required'), ('none', 'None')],
                                          string="Purchase Order", default='none')
    contact_condition = fields.Selection([('required', 'Required'), ('no-required', 'No-required'), ('none', 'None')],
                                         string="Contract", default='none')
    sale_condition = fields.Selection([('required', 'Required'), ('no-required', 'No-required'), ('none', 'None')],
                                      string="Sales Order", default='none')
    supplier_condition = fields.Selection([('required', 'Required'), ('no-required', 'No-required'), ('none', 'None')],
                                          string="Supplier", default='none')

    active = fields.Boolean(string='Active', default=True)
    line_ids = fields.One2many('payment.request.reason.line', 'reason_id')
