# -*- coding: utf-8 -*-
# Part of Odoo. See LICENSE file for full copyright and licensing details.

from odoo import fields, models


class Conductor(models.Model):
    _inherit = 'res.partner'

    # Add a new column to the res.partner model, DNI
    dni = fields.Char(
        string='DNI',
        required=True
    )
    alta_contrato = fields.Date(
        string='Alta Contrato Laboral',
        required=True,
        default=fields.date.today()
    )
    caducidad_dni = fields.Date(
        string='Caducidad DNI',
        required=True,
        default=fields.date.today()
    )
    fechas_carnet_conducir = fields.Date(
        string='Fechas carnet de conducir',
        required=True,
        default=fields.date.today()
    )
    caducidad_carnet_conducir = fields.Date(
        string='Caducidad C.Conducir',
        required=True,
        default=fields.date.today()
    )
    cap_fechas = fields.Date(
        string='CAP fechas',
        required=True,
        default=fields.date.today()
    )
    reconocimiento_medico = fields.Date(
        string='Reconocimiento medico',
        required=True,
        default=fields.date.today()
    )
    fecha_caducidad_tacografo = fields.Date(
        string='F. caducidad tacografo',
        required=True,
        default=fields.date.today()
    )