# -*- coding: utf-8 -*-
# License AGPL-3.0 or later (http://www.gnu.org/licenses/agpl.html).
{

    "name": "Gestion Flota",
    "summary": "Modulo para gestion de flotas comerciales",
    "description": "Control y monitorización eficaz de vehiculos, conductores y gastos",
    "author": "Marea Online",
    "license": "AGPL-3",
    "website": "https://mareaonline.com",
    "category": "Uncategorized",
    "version": "0.1",
    "depends": [
        "base",
        "account"
    ],
    "data": [
        "views/menus.xml",        
        "views/templates.xml",
        "views/orden_carga_views.xml",
        "views/vehiculo_views.xml",
        "views/gastos_vehiculo_views.xml",
        "views/multas_views.xml",
        "views/conductor_views.xml"
    ],
    # only loaded in demonstration mode
    "demo": ["demo/demo.xml"],
    "installable": True,
}