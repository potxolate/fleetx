# -*- coding: utf-8 -*-
# Part of Odoo. See LICENSE file for full copyright and licensing details.

from odoo import _, api, fields, models


class GastosVehiculo(models.Model):
    _name = 'fleetx.gastos.vehiculo'
    _description = 'Gastos Vehiculo'

    invoice_id = fields.Many2one('account.move', string='Invoice',
        ondelete='cascade', index=True)
    tipo_gasto = fields.Selection(
        string='Tipo de Gasto',
        selection=[('taller', 'Parte de taller'), ('ruedas', 'Cambio de ruedas')],
        default='taller'
    )
    descripcion = fields.Text(string='Descripción')
    vehiculo_id = fields.Many2one('fleetx.vehiculo', string='Vehiculo')