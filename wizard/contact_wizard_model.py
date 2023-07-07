import io
import base64
import pandas as pd

from odoo import models, fields, api


class ContactWizard(models.TransientModel):
    _name = 'contacts.wizard'
    _description = 'Contact Wizard'

    excel_file = fields.Binary(string='Excel File')

    def create_contacts(self):
        excel_data = base64.b64decode(self.excel_file)
        df = pd.read_excel(io.BytesIO(excel_data))

        partner = self.env['res.partner']

        for index, row in df.iterrows():
            name = row['Name']
            phone = row['Phone']
            email = row['Email']

            existing_contact = partner.search(['|', ('phone', '=', phone), ('email', '=', email)])

            if not existing_contact:
                values = {
                    'name': name,
                    'phone': phone,
                    'email': email,
                }

                partner.create(values)

        return {'type': 'ir.actions.act_window_close'}

