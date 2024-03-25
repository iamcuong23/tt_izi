# -*- coding: utf-8 -*-
{
    'name': 'CRM Customer Request',
    'summary': """""",
    'description': """""",
    'author': "By-Cuong",
    'category': 'Uncategorized',
    'version': '1.0',
    # any module necessary for this one to work correctly
    'depends': ['base','crm', 'product', 'sale_management'],
    # always loaded
    'data': [
        #'security\ir.model.access.csv',
        'views/customer_request_views.xml',
        'views/crm_lead_views.xml',
    ],
    # only loaded in demonstration mode
    'demo': [
        # 'demo/demo.xml',
    ],
}
