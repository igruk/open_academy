# -*- coding: utf-8 -*-
# noinspection PyStatementEffect
{
    'name': "OpenAcademy",

    'summary': """
        Short summary
    """,

    'description': """
        Long description of module's purpose
    """,

    'author': "My Company",
    'website': "http://github.com",

    # Categories can be used to filter modules in modules listing
    # Check https://github.com/odoo/odoo/blob/15.0/odoo/addons/base/data/ir_module_category_data.xml
    # for the full list
    'category': 'Uncategorized',
    'version': '0.1',

    # any module necessary for this one to work correctly
    'depends': ['base', 'board', 'project', 'sale', 'website', 'contacts'],

    # always loaded
    'data': [
        'security/ir.model.access.csv',
        'security/security.xml',
        'wizard/wizard_view.xml',
        'wizard/contact_wizard_views.xml',
        'views/course.xml',
        'views/session.xml',
        'views/partner.xml',
        'views/dashboard.xml',
        'views/project_views.xml',
        'views/currency_form_view.xml',
        'views/telegram_views.xml',
        'views/sale_views.xml',
        'views/menu.xml',
        'views/website_sale_view.xml',
        'report/report.xml',
        'report/report_session.xml',
    ],
    # only loaded in demonstration mode
    'demo': [
        'demo/data.xml',
    ],

    'application': True,
    'sequence': 0,
}
