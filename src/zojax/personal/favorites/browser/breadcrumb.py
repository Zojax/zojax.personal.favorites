##############################################################################
#
# Copyright (c) 2008 Zope Foundation and Contributors.
# All Rights Reserved.
#
# This software is subject to the provisions of the Zope Public License,
# Version 2.1 (ZPL).  A copy of the ZPL should accompany this distribution.
# THIS SOFTWARE IS PROVIDED "AS IS" AND ANY AND ALL EXPRESS OR IMPLIED
# WARRANTIES ARE DISCLAIMED, INCLUDING, BUT NOT LIMITED TO, THE IMPLIED
# WARRANTIES OF TITLE, MERCHANTABILITY, AGAINST INFRINGEMENT, AND FITNESS
# FOR A PARTICULAR PURPOSE.
#
##############################################################################
"""

$Id$
"""
from zope import component, interface
from zojax.content.browser.breadcrumb import ContentBreadcrumb
from zojax.principal.profile.interfaces import IPersonalProfile
from zojax.personal.favorites.interfaces import _, IFavoritesWorkspace


class FavoritesWorkspaceBreadcrumb(ContentBreadcrumb):
    component.adapts(IFavoritesWorkspace, interface.Interface)

    @property
    def name(self):
        principal = self.context.space.principal

        if principal.id == self.request.principal.id:
            return _(u'Your favorites')
        else:
            profile = IPersonalProfile(principal)
            return _("${user_title}'s favorites",
                     mapping={'user_title': profile.title.strip()})
