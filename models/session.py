from odoo import models, fields, api
from odoo.exceptions import ValidationError


class Session(models.Model):
    _name = 'open_academy.session'
    _description = 'Session'

    name = fields.Char(required=True)
    start_date = fields.Date(default=lambda self: fields.Date.today())
    duration = fields.Float()
    seats = fields.Integer()
    instructor_id = fields.Many2one('res.partner', string='Instructor', domain=[('instructor', '=', False)])
    course_id = fields.Many2one('open_academy.course', string='Course', required=True)
    attendee_ids = fields.Many2many('res.partner', string='Attendees')
    taken_seats = fields.Float(compute='_compute_taken_seats', store=True)
    active = fields.Boolean(default=True)

    @api.depends('seats', 'attendee_ids')
    def _compute_taken_seats(self):
        for session in self:
            if session.seats > 0:
                session.taken_seats = (len(session.attendee_ids) / session.seats) * 100
            else:
                session.taken_seats = 0

    @api.onchange('seats', 'attendee_ids')
    def _onchange_seats_attendees(self):
        if self.seats < 0:
            return {
                'warning': {
                    'title': "Warning!",
                    'message': "Number of seats cannot be negative.",
                }
            }
        if len(self.attendee_ids) > self.seats:
            return {
                'warning': {
                    'title': "Warning!",
                    'message': "Number of participants cannot exceed the number of seats.",
                }
            }

    @api.constrains('instructor_id', attendee_ids)
    def _check_instructor_not_attendee(self):
        for session in self:
            if session.instructor_id and session.instructor_id in session.attendee_ids:
                raise ValidationError('The instructor cannot be an attendee of their own session.')

    @api.constrains('seats', 'attendee_ids')
    def _check_attendee_limit(self):
        for session in self:
            if len(session.attendee_ids) > session.seats:
                raise ValidationError("Number of participants cannot exceed the number of seats.")
