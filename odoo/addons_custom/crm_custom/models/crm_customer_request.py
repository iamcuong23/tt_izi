from odoo import models, fields

class Customer(models.Model):
    _name = 'crm.customer.request'
    _description = 'CRM Customer'

    product_id = fields.Many2one('product.template',string='Product', requied = True)
    opportunity_id = fields.Many2one('crm.lead',string='Opportunity', required = True)
    date = fields.Date(string='Date', required = True, default = fields.Date.today())
    description = fields.Text(string='Description')
    qty = fields.Float(string='QTY', default= True)
