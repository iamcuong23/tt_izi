# -*- coding: utf-8 -*-
{
    'name': "mail_activity_custom",

    'summary': """""",

    'description': """""",
    'category': 'Uncategorized',
    'version': '0.1',
    # any module necessary for this one to work correctly
    'depends': ['base', 'purchase', 'crm'],
    # always loaded
    'data': [
        'views/mail_activity_custom.xml',
        'report/crm_activity_report_custom_view.xml',
    ],
}
