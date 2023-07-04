from odoo import models, fields, api, _

class CrmLead(models.Model):
    _inherit = 'crm.lead'
    
    analytic_account_id = fields.Many2one('account.analytic.account','Analytic Account', copy=False)
    
    
    def action_sale_quotations_new(self):    
        action = super().action_sale_quotations_new()
        action['context']['default_analytic_account_id'] = self.analytic_account_id.id
        return action

