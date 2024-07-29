# -*- coding: utf-8 -*-
# Part of Odoo. See LICENSE file for full copyright and licensing details.

from odoo import _, api, fields, models
from odoo.exceptions import ValidationError


class Multa(models.Model):
    _name = 'fleetx.multa'
    _description = 'Definir una multa'

    referencia = fields.Char(
        string='referencia',
        required=True
    )
    fecha = fields.Date(
        string='Fecha',
        default=fields.date.today()
    )
    tipo = fields.Selection(
        string='Tipo',
        selection=[('altura', 'Altura'), ('peso', 'Peso'),('radar', 'Radar')],
        default='radar'
    )
    estado = fields.Selection(
        string='Tipo',
        selection=[('borrador', 'Borrador'), ('validada', 'Validada'),('pagada', 'Pagada'),('recurrida', 'Recurrida')],
        default='borrador'
    )
    importe = fields.Float('importe')
    vehiculo_id = fields.Many2one('fleetx.vehiculo', string='Vehiculo')
    conductor_id = fields.Many2one('res.partner', string='Conductor')

    @api.constrains('referencia')
    def check_referencia(self):
        if self.referencia and self.referencia != '':
            multas = self.env['fleetx.multa'].search([('referencia','=',self.referencia)])
            if len(multas) > 1:
                raise ValidationError('Ya existen multas con la referencia %s'%(self.referencia))
    
    
    @api.onchange('vehiculo_id')
    def _onchange_vehiculo_id(self):        
        self.conductor_id = 4
        

    
    def name_get(self):
        res = []
        for record in self:
            name = record.referencia            
            res.append((record.id, name))
        return res