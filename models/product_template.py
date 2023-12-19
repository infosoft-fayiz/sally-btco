from odoo import fields, models

class ProductTemplate(models.Model):
    _inherit = 'product.template'

    is_flower = fields.Boolean(string='Is a Flower')
    flower_id= fields.Many2one("flower.shop")
