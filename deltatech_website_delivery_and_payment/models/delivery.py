# ©  2008-2021 Deltatech
# See README.rst file on addons root folder for license details


from odoo import fields, models


class DeliveryCarrier(models.Model):
    _inherit = "delivery.carrier"

    acquirer_allowed_ids = fields.Many2many("payment.acquirer", string="Payments Acquirer Allowed")

    weight_min = fields.Float()
    weight_max = fields.Float()
    logo = fields.Image()
