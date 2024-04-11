from odoo import models, fields


class mailActivityCustom(models.Model):
    _inherit = 'mail.activity'

    estimate_time = fields.Float(string='Estimate Time', required=True)
    density = fields.Float(string='Density', required=True)
