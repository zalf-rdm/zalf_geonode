# -*- coding: utf-8 -*-
#########################################################################
#
# Copyright (C) 2018 OSGeo
#
# This program is free software: you can redistribute it and/or modify
# it under the terms of the GNU General Public License as published by
# the Free Software Foundation, either version 3 of the License, or
# (at your option) any later version.
#
# This program is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE. See the
# GNU General Public License for more details.
#
# You should have received a copy of the GNU General Public License
# along with this program. If not, see <http://www.gnu.org/licenses/>.
#
#########################################################################

import os
from django.apps import AppConfig as BaseAppConfig
from django.db import models
from django.utils.translation import ugettext_lazy as _

def run_setup_hooks(*args, **kwargs):
    from django.conf import settings
    from .celeryapp import app as celeryapp

    LOCAL_ROOT = os.path.abspath(os.path.dirname(__file__))
    settings.TEMPLATES[0]["DIRS"].insert(0, os.path.join(LOCAL_ROOT, "templates"))

    if celeryapp not in settings.INSTALLED_APPS:
        settings.INSTALLED_APPS += (celeryapp,)

class AppConfig(BaseAppConfig):

    name = "zalf_geonode"
    label = "zalf_geonode"

    def patch_resource_base(self, cls):
        
        datacite_json_help_text = _(
            'a German title is required for each dataset.')
        datacite_json = models.CharField(
            ('title_de'),
            max_length=102400,
            default="",
            help_text=datacite_json_help_text)
        cls.add_to_class('datacite_json', datacite_json)


    def ready(self):
        super(AppConfig, self).ready()
        run_setup_hooks()

        from geonode.base.models import ResourceBase
        self.patch_resource_base(ResourceBase)
