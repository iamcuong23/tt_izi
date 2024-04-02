from odoo import http
import json

class LeadAPI(http.Controller):

    @http.route('/create_lead', type='json', auth='public', methods=['POST'])
    def create_lead(self, **kwargs):
        Lead = http.request.env['crm.lead']
        CustomerRequest = http.request.env['crm.customer.request']

        data = json.loads(http.request.httprequest.data)
        customer_requests = data.pop('customer_requests', [])

        lead_vals = {
            'name': data.get('name'),
            'partner_id': data.get('partner_id'),
            'planned_revenue': data.get('planned_revenue'),
            'email_from': data.get('email_from'),
            'phone': data.get('phone'),
            'description': data.get('description')
        }
        new_lead = Lead.create(lead_vals)

        for req in customer_requests:
            req['opportunity_id'] = new_lead.id
            CustomerRequest.create(req)

        return {'success': True}
