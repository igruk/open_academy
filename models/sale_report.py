from odoo import fields, models, api


class SaleReport(models.Model):
    _inherit = 'sale.report'

    subcontractor_id = fields.Many2one('res.partner', string="Subcontractor", readonly=True)
    expenses = fields.Float(string="Expenses", readonly=True)
    profit = fields.Float(string="Profit", readonly=True)

    def _group_by_sale(self, groupby=''):
        res = super()._group_by_sale(groupby)
        res += """,l.subcontractor_id, l.expenses, l.profit"""
        return res

    def _select_additional_fields(self, fields):
        fields['subcontractor_id'] = ", l.subcontractor_id as subcontractor_id"
        fields['expenses'] = ", l.expenses as expenses"
        fields['profit'] = ", l.profit as profit"
        return super()._select_additional_fields(fields)
