from odoo import models, fields, api

class paymentrequestreason(models.Model):
    _name = 'payment.request.reason'
    _description = 'Payment Request Reason'

    name = fields.Char(string='Reason Name', required=True)
    is_advance = fields.Boolean(string='Is Advance Payment', default=True)

    selection_required = [('required', 'Required'), ('no-required', 'No-required'), ('none', 'None')]

    invoice_condition = fields.Selection(selection_required,string="Invoice", default='none')
    purchase_condition = fields.Selection(selection_required,string="Purchase Order", default='none')
    contact_condition = fields.Selection(selection_required,string="Contract", default='none')
    sale_condition = fields.Selection(selection_required,string="Sales Order", default='none')
    supplier_condition = fields.Selection(selection_required,string="Supplier", default='none')

    active = fields.Boolean(string='Active', default=True)
    payment_request_reason_line_ids = fields.One2many('payment.request.reason.line', 'reason_id')
