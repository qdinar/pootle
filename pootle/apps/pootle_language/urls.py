#!/usr/bin/env python
# -*- coding: utf-8 -*-
#
# Copyright 2008-2014 Zuza Software Foundation
# Copyright 2013 Evernote Corporation
#
# This file is part of Pootle.
#
# Pootle is free software; you can redistribute it and/or modify it under the
# terms of the GNU General Public License as published by the Free Software
# Foundation; either version 2 of the License, or (at your option) any later
# version.
#
# Pootle is distributed in the hope that it will be useful, but WITHOUT ANY
# WARRANTY; without even the implied warranty of MERCHANTABILITY or FITNESS FOR
# A PARTICULAR PURPOSE. See the GNU General Public License for more details.
#
# You should have received a copy of the GNU General Public License along with
# Pootle; if not, see <http://www.gnu.org/licenses/>.

from django.conf.urls import patterns, url


urlpatterns = patterns('pootle_language.views',
    url(r'^(?P<language_code>[^/]*)/$',
        'overview',
        name='pootle-language-overview'),

    url(r'^(?P<language_code>[^/]*)/translate/$',
        'translate',
        name='pootle-language-translate'),

    # Admin
    url(r'^(?P<language_code>[^/]*)/admin/settings/$',
        'language_settings_edit',
        name='pootle-language-admin-settings'),
    url(r'^(?P<language_code>[^/]*)/admin/permissions/$',
        'language_admin',
        name='pootle-language-admin-permissions'),
)
