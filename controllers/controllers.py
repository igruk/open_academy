from odoo import http
from odoo.http import request


class AddNewLeadController(http.Controller):

    @http.route('/add_new_lead', type='http', auth="public", methods=['POST'], website=True, csrf=False)
    def add_new_lead(self, **post):
        client_name = post.get('client_name')
        client_email = post.get('client_email')
        client_phone = post.get('client_phone')
        subject = post.get('subject')

        # Create new lead record
        lead = request.env['crm.lead']
        lead_data = {
            'name': client_name,
            'email_from': client_email,
            'phone': client_phone,
            'description': subject,
        }
        new_lead = lead.create(lead_data)

        return "Lead Created Successfully"

