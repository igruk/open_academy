from odoo import models, fields


class SessionWizard(models.TransientModel):
    _name = 'open_academy.session.wizard'
    _description = 'Session Wizard'

    session_ids = fields.Many2many('open_academy.session', string='Sessions')
    partner_ids = fields.Many2many('res.partner', string='Partners')

    def apply_changes(self):
        sessions = self.session_ids
        attendees = self.partner_ids

        for session in sessions:
            session.attendee_ids |= attendees

        return {
            'type': 'ir.actions.act_window_close'
        }
