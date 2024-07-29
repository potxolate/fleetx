# -*- coding: utf-8 -*-
# Part of Odoo. See LICENSE file for full copyright and licensing details.

from odoo import fields, models


class OrdenCarga(models.Model):
    _name = 'fleetx.orden_carga'
    _description = 'Orden de Carga'

    conductor1_id = fields.Many2one('res.partner', string='Conductor 1')
    vehiculo1_id = fields.Many2one('fleetx.vehiculo', string='Vehiculo 1')
    conductor2_id = fields.Many2one('res.partner', string='Conductor 2')
    vehiculo2_id = fields.Many2one('fleetx.vehiculo', string='Vehiculo 2')
    fecha_carga = fields.Date(string='Fecha de carga', default=fields.date.today())
    lugar_carga = fields.Char(related='conductor1_id.street', string='Dirección Carga')    
    fecha_descarga = fields.Date(string='Fecha descarga', default=fields.date.today())
    lugar_descarga = fields.Char(related='conductor2_id.street', string='Dirección Descarga')
    ref_factura = fields.Char(string='Ref Factura', required=True)
    ref_logistica = fields.Char(string='Ref Logist', required=True)
    observaciones = fields.Text(string='Observaciones')
    precio = fields.Float('precio')
