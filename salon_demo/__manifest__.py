{
    'name': 'Salon Demo',
    'version': '17.0.1.0.0',
    'summary': 'Demo: Default calendar view and quick create for sale orders',
    'category': 'Sales',
    'website': '',
    'depends': ['sale','hr'],
    'data': [
        'security/ir.model.access.csv',
        'views/sale_order.xml',
        'wizard/assign_worker_wizard.xml',
],
    'installable': True,
    'application': False,
    'license': 'LGPL-3',
}
