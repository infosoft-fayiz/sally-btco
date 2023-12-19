from odoo import models, fields, api
from odoo.exceptions import ValidationError
from datetime import timedelta

class StockLot(models.Model):
    _inherit = 'stock.lot'

    watering_ids = fields.One2many('flower.water', 'flower_id', string='Watering Records')

    def water_flower(self):
        """Button method to create a watering record."""
        self.ensure_one()
        last_watering = self.watering_ids.sorted('last_watered_date', reverse=True)[:1]
        if last_watering and (fields.Date.today() - last_watering.last_watered_date).days < self.product_id.product_tmpl_id.watering_frequency:
            raise ValidationError("It's too soon to water this flower again.")
        self.env['flower.water'].create({
            'flower_id': self.id,
            'last_watered_date': fields.Date.today()
        })

    def name_get(self):
        return [(flower.id, "{} ({})".format(flower.scientific_name, flower.common_name)) for flower in self]