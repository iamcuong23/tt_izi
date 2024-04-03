from odoo import models, fields

class economiccontract(models.Model):
    _name = 'economic.contract'
    _description = 'Economic Contract'

    name = fields.Char(string='Contract ID',required=True)
    supplier_id = fields.Many2one('res.partner', string='Supplier',required=True)
    contract_date = fields.Date(string='Contract Date', default=fields.Date.today())
    value = fields.Float(string='Contract Value')
    state = fields.Selection([('draft','Draft'), ('validity', 'Validity'), ('invalidity', 'Invalidity')], string="State", default='draft', readonly=True)

    def action_draft(selfs):
        selfs.state = 'draft'

    def action_validity(self):
        self.state = 'validity'

    def action_invalidity(self):
        self.state = 'invalidity'

    def action_exit(self):
        pass

