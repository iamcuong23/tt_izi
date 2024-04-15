from odoo import models, fields, api, tools


class crm_activity_report_custom(models.Model):
    _inherit = 'crm.activity.report'

    estimate_time = fields.Float(string='Estimate Time', required=True)
    density = fields.Float(string='Density', required=True)

    def _select(self):
        select_query = super(crm_activity_report_custom, self)._select()
        select_query += ", m.estimate_time, m.density"
        return select_query

    def init(self):
        tools.drop_view_if_exists(self._cr, self._table)
        self._cr.execute("""
        CREATE OR REPLACE VIEW mail_activity_custom AS
            SELECT
                m.id,
                l.create_date AS lead_create_date,
                l.date_conversion,
                l.date_deadline,
                l.date_closed,
                m.subtype_id,
                m.mail_activity_type_id,
                m.author_id,
                m.date,
                m.body,
                l.id as lead_id,
                l.user_id,
                l.team_id,
                l.country_id,
                l.company_id,
                l.stage_id,
                l.partner_id,
                l.type as lead_type,
                l.active

            FROM mail_message AS m
            
            JOIN crm_lead AS l ON m.res_id = l.id
            WHERE
                m.model = 'crm.lead' AND (m.mail_activity_type_id IS NOT NULL)


            UNION ALL

            SELECT
                m.id,
                l.create_date AS lead_create_date,
                l.date_conversion,
                l.date_deadline,
                l.date_closed,
                m.subtype_id,
                m.mail_activity_type_id,
                m.author_id,
                m.date,
                m.body,
                l.id as lead_id,
                l.user_id,
                l.team_id,
                l.country_id,
                l.company_id,
                l.stage_id,
                l.partner_id,
                l.type as lead_type,
                l.active

            FROM mail_activity AS m
            JOIN crm_lead AS l ON m.res_id = l.id
            WHERE
                m.res_model = 'crm.lead' AND (m.activity_type_id IS NOT NULL)
            """
        )