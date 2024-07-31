# -*- coding: utf-8 -*-
# Part of Odoo. See LICENSE file for full copyright and licensing details.

from odoo import _, api, fields, models
from odoo.exceptions import ValidationError


class Vehiculo(models.Model):
    _name = 'fleetx.vehiculo'
    _description = 'Definir un Vehiculo'
    _rec_name = 'display_name'

    matricula = fields.Char(
        string='Matricula',
        required=True
    )
    fecha_matriculacion = fields.Date(
        string='Fecha de Matriculación',
        default=fields.date.today()
    )
    tipo = fields.Selection(
        string='Tipo',
        selection=[('camion', 'camion'), ('remolque', 'remolque')],
        default='camion'
    )
    conductor_id = fields.Many2one('res.partner', string='Conductor')
    anotaciones = fields.Text(string='Notas')
    display_name = fields.Char(
        compute='_compute_display_name', store=True, string='Vehículo'
    )

    @api.constrains('matricula')
    def check_matricula(self):
        if self.matricula and self.matricula != '':
            matriculas = self.env['fleetx.vehiculo'].search([('matricula','=',self.matricula)])
            if len(matriculas) > 1:
                raise ValidationError('Ya existen vehiculos con la  matricula %s'%(self.matricula))
    
    @api.depends('matricula', 'tipo')
    def _compute_display_name(self):        
        for vehiculo in self:
            vehiculo.display_name = f"{vehiculo.tipo.capitalize()} - {vehiculo.matricula}"        
        
