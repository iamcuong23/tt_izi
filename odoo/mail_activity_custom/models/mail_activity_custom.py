from odoo import models, fields, api, exceptions
from datetime import timedelta
import datetime


class mailActivityCustom(models.Model):
    _inherit = 'mail.activity'

    estimate_time = fields.Float(string='Estimate Time', required=True)
    density = fields.Float(string='Density', required=True)

    @api.constrains('date_deadline', 'density')
    def _check_weekly_density(self):
        for activity in self:
            if activity.date_deadline:
                # Tính toán ngày đầu tiên và cuối cùng trong tuần
                week_start = activity.date_deadline - timedelta(days=activity.date_deadline.weekday())
                week_end = week_start + timedelta(days=6)
                # Tìm tất cả các hoạt động trong tuần
                activities_in_week = self.search([
                    ('user_id', '=', activity.user_id.id),
                    ('date_deadline', '>=', week_start),
                    ('date_deadline', '<=', week_end)
                ])
                # Tính tổng density của các hoạt động trong tuần
                total_density_in_week = sum(activities_in_week.mapped('density'))
                # Kiểm tra xem tổng density có vượt quá 100% không
                if total_density_in_week > 100:
                    raise exceptions.ValidationError("Density for this week has exceeded 100%.")