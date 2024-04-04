# -*- coding: utf-8 -*-
{
    'name': "ev_payment_request",

    'summary': """""",

    'description': """""",

    'author': "My Company",
    'website': "https://www.yourcompany.com",


    # for the full list
    'category': 'Uncategorized',
    'version': '0.1',

    # any module necessary for this one to work correctly
    'depends': ['base', 'account', 'hr', 'sale', 'purchase', 'payment'],

    # always loaded
    'data': [
        'security/ir.model.access.csv',
        'views/payment_request_menu.xml',
        'data/payment_request_sequence.xml',
        'views/payment_document_view.xml',
        'views/payment_request_reason_view.xml',
        'views/payment_request_reason_line_view.xml',
        'views/economic_contract_view.xml',
        'views/payment_request_view.xml',
        'views/payment_request_line_view.xml',
        'data/payment_request_sequence.xml',
    ],
}
