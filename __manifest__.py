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
    'depends': ['base'],

    # always loaded
    'data': [
        'security/ir.model.access.csv',
        # 'views/views.xml',
        # 'views/templates.xml',
        'views/course.xml',
        'views/session.xml',
        'views/partner.xml',
        'views/menu.xml',
    ],
    # only loaded in demonstration mode
    'demo': [
        'demo/data.xml',
    ],

    'application': True,
    'sequence': 0,
}
