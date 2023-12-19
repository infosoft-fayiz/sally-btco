from odoo import models, fields

class SaleOrderLine(models.Model):
    _inherit = 'sale.order.line'

    def _get_domain_for_flower_products(self):
        return [('is_flower', '=', True)]

    product_id = fields.Many2one(domain=_get_domain_for_flower_products)
