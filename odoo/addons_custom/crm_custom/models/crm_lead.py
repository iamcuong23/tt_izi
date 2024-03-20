from odoo import models, fields, api

class customer(models.Model):
    _inherit = 'crm.lead'

    request_ids = fields.One2many('crm.customer.request', 'opportunity_id', string='Customer Requests')
    total_sales = fields.Float(compute='_compute_total_sales', string='Total Sales')
    expected_revenue = fields.Float(compute='_compute_expected_revenue', string='Expected Revenue')

    @api.depends('request_ids')
    def _compute_total_sales(self):
        for lead in self:
            lead.total_sales = sum(request.qty for request in lead.request_ids)

    @api.depends('request_ids')
    def _compute_expected_revenue(self):
        for lead in self:
            lead.expected_revenue = sum(request.qty * request.product_id.list_price for request in lead.request_ids)
