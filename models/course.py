from odoo import models, fields, api, tools


class Course(models.Model):
    _name = 'open_academy.course'
    _description = 'Course'
    _rec_name = 'title'

    title = fields.Char(required=True)
    description = fields.Text()
    responsible_user_id = fields.Many2one('res.users', string='Responsible User')
    session_id = fields.One2many('open_academy.session', 'course_id', string='Session')
    picture = fields.Binary(string='Picture')

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

    @api.model
    def create(self, vals):
        if 'picture' in vals:
            image = tools.ImageProcess(vals['picture'])
            resize_image = image.resize(250, 250)
            resize_image_b64 = resize_image.image_base64()
            vals['picture'] = resize_image_b64
        obj = super(Course, self).create(vals)
        return obj

    def write(self, vals):
        if 'picture' in vals:
            image = tools.ImageProcess(vals['picture'])
            resize_image = image.resize(250, 250)
            resize_image_b64 = resize_image.image_base64()
            vals['picture'] = resize_image_b64
        obj = super(Course, self).write(vals)
        return obj
