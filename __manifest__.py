# -*- coding: utf-8 -*-
{
    'name': 'Flower Shop',
    'version': '1.0',
    'summary': 'flower shop for btco',
    'depends': ['base','sale','website_sale','stock','mail'],
    'data': [
        'security/ir.model.access.csv',
        'views/flower_views.xml',
        'views/product_template_views.xml',
        'views/web_store_flower_views.xml',
        'views/stock_lot_action.xml',
        'data/flower_order_paperformat.xml',
        'reports/sales_order_report.xml',
        'views/sales_report_action.xml',
        'security/flower_shop_security.xml',
        'data/weather_api.xml',
        'data/ir_cron.xml',
    ],
    'installable': True,
    'application': True,

    'author': "Fayiz Asad",
    'website': "https://www.infosoft.ae",

    # Categories can be used to filter modules in modules listing
    # Check https://github.com/odoo/odoo/blob/16.0/odoo/addons/base/data/ir_module_category_data.xml
    # for the full list
    'category': 'Uncategorized',

    # only loaded in demonstration mode
    'demo': [
        'demo/demo.xml',
    ],
}
