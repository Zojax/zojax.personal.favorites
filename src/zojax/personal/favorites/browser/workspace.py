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
from zope import interface, component
from zope.component import getUtility, getUtilitiesFor
from zope.security.proxy import removeSecurityProxy

from zojax.table.table import Table
from zojax.principal.profile.interfaces import IPersonalProfile

from zojax.personal.favorites.interfaces import \
    _, IFavoriteType, IFavoritesWorkspace

from interfaces import IPersonalFavoritesTable


class WorkspaceView(object):

    def label(self):
        if self.principal_title is None:
            return _(u'Your Latest Favorites')
        else:
            return _("${user_title}'s Latest Favorites",
                     mapping={'user_title': self.principal_title})

    def description(self):
        if self.principal_title is None:
            return _(u'Below is a list of favorites you created.')
        else:
            return _(u'Below is a list of favorites ${user_title} created.',
                     mapping={'user_title': self.principal_title})

    def update(self):
        request = self.request
        principal = self.context.space.principal
        if principal.id == self.request.principal.id:
            self.principal_title = None
        else:
            self.principal_title = IPersonalProfile(principal).title


class PersonalFavoritesTable(Table):
    interface.implements(IPersonalFavoritesTable)
    component.adapts(
        IFavoritesWorkspace, interface.Interface, interface.Interface)

    title = _('Personal favorites')
    msgEmptyTable = _(u'You do not have favorites yet.')

    pageSize = 15
    enabledColumns = ('typeicon', 'title', 'tags', 'modified')

    def initDataset(self):
        self.dataset = removeSecurityProxy(self.context).values()

    @property
    def msgEmptyTable(self):
        principal = self.context.__parent__.principal

        if principal.id == self.request.principal.id:
            return _(u'You do not have favorites yet.')
        else:
            return _(u'He/she does not have favorites yet.')
