from odoo import models, fields

class economiccontract(models.Model):
    _name = 'economic.contract'
    _description = 'Economic Contract'

    name = fields.Char(string='Contract ID',required=True)
    supplier_id = fields.Many2one('res.partner', string='Supplier',required=True)
    contract_date = fields.Date(string='Contract Date', default=fields.Date.today())
    value = fields.Float(string='Contract Value')
    state = fields.Selection([('draft','Draft'), ('validity', 'Validity'), ('invalidity', 'Invalidity')], string="State", default='draft', readonly=True)

    def action_validate(self):
        self.state = 'validity'

    def action_invalidate(self):
        self.state = 'invalidity'

    def write(self, vals):
        if 'state' in vals and vals['state'] == 'validity':
            vals['readonly'] = True
        return super(economiccontract, self).write(vals)

    def write(self, vals):
        if 'state' in vals:
            if vals['state'] == 'validity':
                vals['readonly'] = True
            elif vals['state'] == 'invalidity':
                vals['readonly'] = False
        return super(economiccontract, self).write(vals)