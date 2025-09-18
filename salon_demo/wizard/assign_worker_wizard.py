from odoo import models, fields, api

class AssignWorkerWizard(models.TransientModel):
    _name = 'assign.worker.wizard'
    _description = 'Assign Worker Wizard'

    worker_id = fields.Many2one('hr.employee', string="Worker", required=True)

    def action_apply(self):
        active_id = self.env.context.get('active_id')
        if active_id and self.worker_id:
            order = self.env['sale.order'].browse(active_id)
            # Filter lines with empty worker_id only
            empty_lines = order.order_line.filtered(lambda l: not l.worker_id)
            empty_lines.write({'worker_id': self.worker_id.id})
        return {'type': 'ir.actions.act_window_close'}
