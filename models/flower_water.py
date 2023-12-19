from odoo import models, fields, api

class FlowerWater(models.Model):
    _name = 'flower.water'
    _description = 'Flower Watering Record'

    flower_id = fields.Many2one('stock.lot', string='Flower Serial', required=True)
    last_watered_date = fields.Date(string='Last Watered On', required=True)

    @api.model
    def create(self, vals_list):
        if not self.env.user.has_group('flower_shop.group_gardener'):
            raise AccessError(_("Only users with the 'Gardener' role can perform this action."))
        return super(FlowerWater, self).create(vals_list)
    
    def _action_needs_watering(self):
        flowers = self.env["product.template"].search([("is_flower", "=", True)])
        serials = self.env["stock.lot"].search([("product_id", "in", flowers.ids)])
        lot_vals = defaultdict(bool)
        for serial in serials:
            if serial.water_ids:
                last_watered_date_x = serial.water_ids[0].date
                frequency = serial.product_id.flower_id.watering_frequency
                today = fields.Date.today()
                needs_watering = (today - last_watered_date_x).days >= frequency
                lot_vals[serial.product_id.id] |= needs_watering
            else:
                lot_vals[serial.product_id.id] = True
        for flower in flowers:
            flower.needs_watering = lot_vals[flower.id]