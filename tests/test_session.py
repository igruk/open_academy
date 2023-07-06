import datetime

from odoo.tests.common import TransactionCase
from odoo.exceptions import ValidationError


class TestSession(TransactionCase):
    def setUp(self):
        super().setUp()
        self.Session = self.env['open_academy.session']
        self.Partner = self.env['res.partner']

    def test_create_session(self):
        session = self.Session.create({
            'name': 'Test Session',
            'start_date': '2023-07-06',
            'duration': 2,
            'seats': 10,
            'instructor_id': self.env.ref('base.partner_admin').id,
            'course_id': self.env.ref('open_academy.course_1').id,
        })
        self.assertEqual(session.name, 'Test Session')
        self.assertEqual(session.start_date, datetime.date(2023, 7, 6))
        self.assertEqual(session.duration, 2)
        self.assertEqual(session.seats, 10)
        self.assertEqual(session.instructor_id, self.env.ref('base.partner_admin'))
        self.assertEqual(session.course_id, self.env.ref('open_academy.course_1'))

    def test_taken_seats(self):
        session = self.Session.create({
            'name': 'Test Session',
            'duration': 2,
            'seats': 10,
            'instructor_id': self.env.ref('base.partner_admin').id,
            'course_id': self.env.ref('open_academy.course_1').id,
        })

        self.assertEqual(session.taken_seats, 0)

        attendee1 = self.Partner.create({'name': 'Attendee 1'})
        attendee2 = self.Partner.create({'name': 'Attendee 2'})

        session.write({'attendee_ids': [(4, attendee1.id)]})

        self.assertEqual(session.taken_seats, 10)

        session.write({'attendee_ids': [(4, attendee2.id)]})

        self.assertEqual(session.taken_seats, 20)

    def test_invalid_seats(self):
        with self.assertRaises(ValidationError):
            session = self.env['open_academy.session'].create({
                'name': 'Test Session',
                'duration': 2,
                'seats': -1,
                'instructor_id': self.env.ref('base.partner_admin').id,
                'course_id': self.env.ref('open_academy.course_1').id,
            })

    def test_check_attendee_limit(self):
        session = self.env['open_academy.session'].create({
            'name': 'Test Session',
            'duration': 2,
            'seats': 1,
            'instructor_id': self.env.ref('base.partner_admin').id,
            'course_id': self.env.ref('open_academy.course_1').id,
        })

        attendee1 = self.Partner.create({'name': 'Attendee 1'})
        attendee2 = self.Partner.create({'name': 'Attendee 2'})

        session.write({'attendee_ids': [(4, attendee1.id)]})

        with self.assertRaises(ValidationError):
            session.write({'attendee_ids': [(4, attendee2.id)]})

    def test_check_instructor_not_attendee(self):
        instructor = self.Partner.create({'name': 'Instructor'})
        session = self.Session.create({
            'name': 'Test Session',
            'duration': 2,
            'seats': 10,
            'instructor_id': instructor.id,
            'course_id': self.env.ref('open_academy.course_1').id
        })

        with self.assertRaises(ValidationError):
            session.write({'attendee_ids': [(4, instructor.id)]})
            session._check_instructor_not_attendee()
