from odoo import models, fields, api, exceptions


class CrmLead(models.Model):
    _inherit = 'crm.lead'

    request_ids = fields.One2many('crm.customer.request', 'opportunity_id', string='Customer Requests')
    sale = fields.Float(string='Doanh số', compute='_compute_sale')
    expected_revenue = fields.Float(string='Doanh thu mong đợi', compute='_compute_expected_revenue')

    @api.depends('request_ids.qty')
    def _compute_sale(self):
        for lead in self:
            lead.sale = sum(lead.request_ids.mapped('qty'))

    @api.depends('request_ids')
    def _compute_expected_revenue(self):
        for lead in self:
            sale = sum(request.qty * request.product_id.list_price for request in lead.request_ids)
            lead.expected_revenue = sale

    # @api.constrains('request_ids')
    # def _check_request_ids_state(self):
    #     for lead in self:
    #         if lead.stage_id not in lead._get_new_stage_ids():
    #             raise exceptions.ValidationError("You cannot add, edit or delete customer requests in this stage.")

    def _get_new_stage_ids(self):
        # Define the stage IDs where adding, editing or deleting requests is allowed
        new_stage_ids = self.env['crm.stage'].search([]).filtered(lambda s: s.name == 'New').ids
        return new_stage_ids

    #
    