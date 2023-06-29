from odoo import models, fields, api


class Project(models.Model):
    _inherit = 'project.project'

    limit_time = fields.Float(string='Limit Time', digits=(6, 2))
    remaining_time = fields.Float(string='Remaining Time', compute='_compute_remaining_time', digits=(6, 2))

    @api.depends('limit_time', 'total_timesheet_time')
    def _compute_remaining_time(self):
        for project in self:
            project.remaining_time = project.limit_time - project.total_timesheet_time
