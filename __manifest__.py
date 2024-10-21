# -*- coding: utf-8 -*-

{
    'name': 'Expired orders in CRM',
    'version': '1.0',
    'author': 'Celestine Dabrowski',
    'category': 'Productivity',
    'description': """
Adds a button in CRM Lead that shows list of canceled quotes
    """,
    'depends': ['sale_management', 'crm'],
    'data': [
        'views/crm_lead_views.xml',
    ],
    'auto_install': False,
    'application': True,
    'license': 'OPL-1',
}
