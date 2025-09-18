from odoo import api, fields, models


class SaleOrderLine(models.Model):
    _inherit = 'sale.order.line'

    worker_id = fields.Many2one('hr.employee', string="Worker")
    assign_id = fields.Many2one('hr.employee', string="Assign")
