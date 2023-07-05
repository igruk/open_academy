from odoo import fields, models, api


class SaleOrderLine(models.Model):
    _inherit = 'sale.order.line'

    subcontractor_id = fields.Many2one('res.partner', string="Subcontractor")
    expenses = fields.Float(string="Expenses")
    profit = fields.Float(compute='_compute_profit', string="Profit", store=True)

    @api.depends('price_subtotal', 'expenses')
    def _compute_profit(self):
        for record in self:
            record.profit = record.price_subtotal - record.expenses
