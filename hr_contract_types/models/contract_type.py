# -*- coding: utf-8 -*-

from odoo import fields, models


class ContractInherit(models.Model):
    _inherit = 'hr.contract'

    # hr.contract.type is in Odoo itself since 15.0 (hr in 16.0+): its model,
    # views, menu and access rights come from there
    type_id = fields.Many2one('hr.contract.type', string="Employee Category",
                              required=True, help="Employee category",
                              default=lambda self: self.env['hr.contract.type'].search([], limit=1))
