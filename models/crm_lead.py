from dateutil.relativedelta import relativedelta

from odoo import fields, models, api, _

class CrmLead(models.Model):
    _inherit = 'crm.lead'

    quotation_count_ex = fields.Integer(compute='_compute_expired_data', string="Number of expired quotations")

    @api.depends('order_ids.state', 'order_ids.currency_id', 'order_ids.amount_untaxed', 'order_ids.date_order', 'order_ids.company_id')
    def _compute_expired_data(self):
        for lead in self:
            total = 0.0
            quotation_ex_cnt = 0
            sale_ex_cnt = 0
            company_currency = lead.company_currency or self.env.company.currency_id
            for order in lead.order_ids:
                if order.state in ('cancel'):
                    quotation_ex_cnt += 1
            lead.quotation_count_ex = quotation_ex_cnt

    def action_view_expired(self):
        action = self.env['ir.actions.actions']._for_xml_id("sale.action_orders")
        action['context'] = {
            'search_default_partner_id': self.partner_id.id,
            'default_partner_id': self.partner_id.id,
            'default_opportunity_id': self.id,
        }
        action['domain'] = [('opportunity_id', '=', self.id), ('state', '=', 'cancel')]
        orders = self.mapped('order_ids').filtered(lambda l: l.state in ('cancel'))
        if len(orders) == 1:
            action['views'] = [(self.env.ref('sale.view_order_form').id, 'form')]
            action['res_id'] = orders.id
        return action
        
                
    