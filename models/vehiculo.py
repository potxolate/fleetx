# -*- coding: utf-8 -*-
# Part of Odoo. See LICENSE file for full copyright and licensing details.

from odoo import _, api, fields, models
from odoo.exceptions import ValidationError


class Vehiculo(models.Model):
    _name = 'gestion_flota.vehiculo'
    _description = 'Definir un Vehiculo'

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

    @api.constrains('matricula')
    def check_matricula(self):
        if self.matricula and self.matricula != '':
            matriculas = self.env['gestion_flota.vehiculo'].search([('matricula','=',self.matricula)])
            if len(matriculas) > 1:
                raise ValidationError('Ya existen vehiculos con la  matricula %s'%(self.matricula))
    
    def name_get(self):
        res = []
        for record in self:
            name = record.matricula            
            res.append((record.id, name))
        return res
