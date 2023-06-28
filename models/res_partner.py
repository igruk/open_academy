from odoo import models, fields


class Partner(models.Model):
    _inherit = 'res.partner'

    instructor = fields.Boolean(string='Is Instructor')
    session_ids = fields.Many2many('open_academy.session', string='Sessions')
