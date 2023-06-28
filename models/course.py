from odoo import models, fields


class Course(models.Model):
    _name = 'open_academy.course'
    _description = 'Course'
    _rec_name = 'title'

    title = fields.Char(required=True)
    description = fields.Text()
    responsible_user_id = fields.Many2one('res.users', string='Responsible User')
    session_id = fields.One2many('open_academy.session', 'course_id', string='Session')

    _sql_constraints = [
        ('title_description', 'CHECK (title <> description)',
         'The course title and description must be different.'),
        ('title_unique', 'UNIQUE (title)', 'The course title must be unique.')
    ]

    def copy(self, default=None):
        self.ensure_one()
        if default is None:
            default = {}
        default['title'] = f"Copy of {self.title}"
        return super(Course, self).copy(default)
