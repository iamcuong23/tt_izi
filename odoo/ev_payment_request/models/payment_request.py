from odoo import models, fields, api, _
from datetime import datetime

class paymentrequest(models.Model):
    _name = 'payment.request'
    _inherit = 'payment.request.reason'
    _description = 'Payment Request'

    name = fields.Char(string="Name", readonly=True, default='New')

    employee_id = fields.Many2one('hr.employee')
    department_id = fields.Many2one('hr.department', default='_compute_creator_department')
    manager_id = fields.Many2one('hr.employee')
    request_date = fields.Date(string="Request Date", defautl=fields.Date.today())
    reason_id = fields.Many2one('payment.request.reason.line')
    purchase_id = fields.Many2one('purchase.order', string='Purchase Order', domain="[('state', 'in', ('purchase', 'done'))]")
    sale_id = fields.Many2one('sale.order')
    invoice_id = fields.Many2one('account.move')
    contract_id = fields.Many2one('economic.contract')
    partner_id = fields.Many2one('res.partner')
    request_amount = fields.Float(string='Request Amount')
    paid_amount = fields.Float(string='Paid Amount')
    remain_amount = fields.Float(string='Remain Amount')
    paid_deadline = fields.Date(string="Date", defautl=fields.Date.today())
    bank_account_number = fields.Many2one('res.partner.bank')
    bank_account_name = fields.Char(string='Bank Account Name',related='bank_account_number.acc_holder_name', readonly=True)
    bank_id = fields.Many2one('res.bank')
    payments = fields.Selection([('cash', 'Cash'), ('personal', 'Personal'), ('company', 'Company')])
    delivery_date = fields.Date(string='Delivery Date', default=fields.Date.today())
    is_delivered = fields.Boolean(string='Delivered', default=False)
    is_vat = fields.Boolean(string='VAT', default=False)
    paid_date = fields.Datetime(string='Paid Date',defautl=fields.Date.today())
    late_day = fields.Float(string='Late Day', compute='_compute_late_day', store=True, readonly=True)

    state = fields.Selection([
        ('draft', 'Draft'),
        ('wait_manager', 'Waiting for Manager Approval'),
        ('wait_account_check', 'Waiting for Accounting Check'),
        ('wait_accountant', 'Waiting for Accountant Approval'),
        ('wait_vice', 'Waiting for Vice Approval'),
        ('wait_payment', 'Waiting for Payment'),
        ('reimbursement', 'Reimbursement'),
        ('done', 'Done'),
        ('cancel', 'Cancelled'),
        ('denied', 'Denied'),
    ], string='Status', default='draft')

    line_ids = fields.One2many('payment.request.line', 'request_id')

    slection_id = fields.Many2one('payment.request.reason')
    purchase_required = fields.Selection(related='slection_id.purchase_condition', string='Purchase Required')
    sale_required = fields.Selection(related='slection_id.sale_condition', string='Sale Required')

    #Onchange khi chọn số tài khoản ngân hàng thì sẽ hiện ra tên chủ TKNH
    @api.onchange('bank_account_number')
    def onchange_bank_account_number(self):
        if self.bank_account_number:
            self.bank_account_name = self.bank_account_number.bank_name
        else:
            self.bank_account_name = False

    #state
    def action_draft(selfs):
        selfs.state = 'draft'

    def action_wait_manager(selfs):
        selfs.state = 'wait_manager'

    def action_wait_account_check(selfs):
        selfs.state = 'wait_account_check'

    def action_wait_accountant(selfs):
        selfs.state = 'wait_accountant'

    def action_wait_accountant(selfs):
        selfs.state = 'wait_accountant'

    def action_wait_payment(selfs):
        selfs.state = 'wait_payment'

    def action_reimbursement(selfs):
        selfs.state = 'reimbursement'

    def action_done(selfs):
        selfs.state = 'done'

    def action_cancel(selfs):
        selfs.state = 'cancel'

    def action_denied(selfs):
        selfs.state = 'denied'

    def _compute_late_day(self):
        for record in self:
            if record.state == 'done':
                if record.paid_amount <= 0:
                    record.late_day = 0
                elif record.paid_date:
                    record.late_day = (record.paid_date - record.delivery_date).days
                else:
                    record.late_day = (datetime.now().date() - record.delivery_date).days

    # @api.model
    # def create(self, vals):
    #     if vals.get('name', 'New') == 'New':
    #         # Chuyển đổi chuỗi ngày tháng sang đối tượng ngày tháng
    #         date = fields.Date.from_string(vals.get('date'))
    #         # Lấy tháng và chuyển đổi thành chuỗi với định dạng 2 chữ số
    #         month = str(date.month).zfill(2)
    #         # Lấy năm và chuyển đổi thành chuỗi
    #         year = str(date.year)
    #         sequence = self.env['ir.sequence'].next_by_code('payment.request.sequence') or '/'
    #         vals['name'] = 'DNTT/{}/{}/{}'.format(year, month, sequence)
    #     return super(paymentrequest, self).create(vals)
    #
    # @api.model
    # # tự dộng điền người tạo yêu cầu
    # def default_get(self, fields):
    #     defaults = super(paymentrequest, self).default_get(fields)
    #     defaults['request_id'] = self.env.user.id
    #     return defaults
    #
    # @api.depends('request_id')
    # # chọn người phê duyệt tự động chọn phòng ban
    # def _compute_creator_department(self):
    #     for record in self:
    #         creator = record.request_id
    #         if creator:
    #             record.department_id = creator.department_id
    #
    # @api.onchange('department_id')
    # # chọn phòng ban tự động chọn quản lý phòng ban đó
    # def _onchange_department_id(self):
    #     if self.department_id:
    #         approver = self.env['res.users'].search([('department_id', '=', self.department_id.id)], limit=1)
    #         if approver:
    #             self.approver_id = approver.id
    #         else:
    #             self.approver_id = False