from odoo import models , fields

class SaleOrder(models.Model):
    _inherit = 'sale.order'

    worker_id = fields.Many2one('hr.employee', string="Worker", required=True)

    def action_assign_worker(self):
        return {
            'name': 'Assign Worker',
            'type': 'ir.actions.act_window',
            'res_model': 'assign.worker.wizard',
            'view_mode': 'form',
            'target': 'new',
            'context': {'default_worker_id': self.worker_id.id}
        }
