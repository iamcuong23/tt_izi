# -*- coding: utf-8 -*-
{
    'name': "ev_payment_request",

    'summary': """
        Short (1 phrase/line) summary of the module's purpose, used as
        subtitle on modules listing or apps.openerp.com""",

    'description': """
        Long description of module's purpose
    """,

    'author': "My Company",
    'website': "https://www.yourcompany.com",

    # Categories can be used to filter modules in modules listing
    # Check https://github.com/odoo/odoo/blob/16.0/odoo/addons/base/data/ir_module_category_data.xml
    # for the full list
    'category': 'Uncategorized',
    'version': '0.1',

    # any module necessary for this one to work correctly
    'depends': ['base',],

    # always loaded
    'data': [
        #'security/security.xml',
        'security/ir.model.access.csv',
        'views/payment_document_view.xml',
        'views/payment_request_menu.xml',
        'views/payment_request_reason_view.xml',
        'views/payment_request_reason_line_view.xml',
        'views/economic_contract_view.xml',

    ],
    # only loaded in demonstration mode
    'demo': [
        'demo/demo.xml',
    ],
}
