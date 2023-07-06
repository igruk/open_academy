import re

from odoo import models, fields, api
from odoo.exceptions import ValidationError


class Partner(models.Model):
    _inherit = 'res.partner'

    instructor = fields.Boolean(string='Is Instructor')
    session_ids = fields.Many2many('open_academy.session', string='Sessions')

    @api.constrains('mobile', 'phone')
    def check_duplicate_phone_number(self):
        for partner in self:
            phone = re.sub(r'\D', '', partner.phone) if partner.phone else False
            mobile = re.sub(r'\D', '', partner.mobile) if partner.mobile else False

            if phone:
                domain = [('id', '!=', partner.id), '|', ('phone', '=', phone), ('mobile', '=', phone)]
                duplicate_partner = self.search(domain, limit=1)
                if duplicate_partner:
                    raise ValidationError('Warning: Duplicate phone number found!')

            if mobile:
                domain = [('id', '!=', partner.id), '|', ('phone', '=', mobile), ('mobile', '=', mobile)]
                duplicate_partner = self.search(domain, limit=1)
                if duplicate_partner:
                    raise ValidationError('Warning: Duplicate mobile number found!')
