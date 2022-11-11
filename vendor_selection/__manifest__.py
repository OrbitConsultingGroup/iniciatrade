# -*- coding: utf-8 -*-
# Part of Odoo, Aktiv Software
# See LICENSE file for full copyright & licensing details.

# Author: Aktiv Software
# mail:   odoo@aktivsoftware.com
# Copyright (C) 2015-Present Aktiv Software
# Contributions:
#           Aktiv Software:
#              - Fatemi Lokhandwala
#              - Kinjal Lalani
#              - Surabh Yadav

{
    'name': 'Vendor Selection For Dropshipping',
    'summary': 'Customer will select vendor as per his choice.',
    'website': 'http://www.aktivsoftware.com',
    'description': 'Customer will select vendor as per his choice in sale order \
        when customer choose drop shipping scenario.',
    'license': 'AGPL-3',
    'author': 'Aktiv Software',
    'category': 'Purchases',
    'version': '15.0.1.0.0',
    'depends': ['sale_management', 'purchase', 'stock'],
    'data': [
        'views/sale_order.xml',
    ],
    'images': ['static/description/banner.jpg'],
    'auto_install': False,
    'installable': True,
    'application': False
}
