{
    "name": "Orbit Analytic Dropship",
    "version": "15.0.0.1",
    'author': "Orbit consulting, Dinaneo, Cristian Zea",
    "license": "Other proprietary",
    "category": "accounting",
    "description": """
    - Campo nuevo analytic_account_id en oportunidad.
    - El campo se propaga al presupuesto de venta creado desde la oportunidad.
    - Al confirmarse el presupuesto de venta, las líneas del pedido de compra generado (dropship) llevarán también la cuenta analítica.
    """,
    "depends": [
        "sale_crm",
        "stock_dropshipping",
    ],
    "data": [
        "views/crm_views.xml",
    ],
}

