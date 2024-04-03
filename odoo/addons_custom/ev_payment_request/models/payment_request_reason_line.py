from odoo import models, fields

class paymentrequestreasonline(models.Model):
    _name = 'payment.request.reason.line'
    _description = 'Payment Request Reason Line'

    reason_id = fields.Many2one('payment.request.reason', string='Reason')
    document_id = fields.Many2one('payment.document', string='Document', required=True)
    required = fields.Boolean(string='Required', default=False)
    sequence = fields.Integer(string='ST', compute='_compute_sequence', store=True)

    # Hàm tính toán để tính số thứ tự
    def _compute_sequence(self):
        for index, record in enumerate(self, start=1):
            record.sequence = index
