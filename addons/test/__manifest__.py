# -*- coding: utf-8 -*-
{
    'name': "Test",

    'summary': """
        Test module for an accomplishment the course Odoo
        """,

    'description': """
        Test module tasks:
            - to create Test menu
            - to create 'Tests' and 'Test session' submenus
            - to add calender filter for next 30 days
    """,

    'author': "Ievgen Synchyshyn",
    'website': "http://www.yourcompany.com",

    # Categories can be used to filter modules in modules listing
    # Check https://github.com/odoo/odoo/blob/master/odoo/addons/base/module/module_data.xml
    # for the full list
    'category': 'Test',
    'version': '0.1',

    # any module necessary for this one to work correctly
    'depends': ['base'],

    # always loaded
    'data': [
        # 'security/ir.model.access.csv',
        # 'views/views.xml',
        'views/templates.xml',
        'views/test.xml',
    ],
    # only loaded in demonstration mode
    'demo': [
        'demo/demo.xml',
    ],
}
