# -*- coding: utf-8 -*-

from odoo import fields, models


class ContractType(models.Model):
    _inherit = 'hr.contract.type'

    # With an active field the ORM leaves archived types out of every
    # hr.contract.type selection (Employee Category and Contract Type of
    # contracts, Employment Type of jobs...) and of the type_id default.
    # Imported before contract_type so the column exists when hr.contract's
    # required type_id fills empty rows with its default.
    active = fields.Boolean(default=True)
