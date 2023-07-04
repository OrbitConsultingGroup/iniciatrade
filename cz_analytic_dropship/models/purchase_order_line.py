from odoo import models, fields, api, _

class PurchaseOrderLine(models.Model):
    _inherit = 'purchase.order.line'
    
    
    @api.model
    def _prepare_purchase_order_line_from_procurement(self, product_id, product_qty, product_uom, company_id, values, po):
        res = super()._prepare_purchase_order_line_from_procurement(product_id, product_qty, product_uom, company_id, values, po)
        if res['sale_line_id']:
            sale_line_id = self.env['sale.order.line'].browse(res['sale_line_id'])
            if sale_line_id:
                res['account_analytic_id'] = sale_line_id.order_id.analytic_account_id.id
        return res
    
