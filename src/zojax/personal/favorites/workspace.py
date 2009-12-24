##############################################################################
#
# Copyright (c) 2009 Zope Foundation and Contributors.
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
from zope.component import getAdapter
from zope.size import byteDisplay
from zope.size.interfaces import ISized
from zope.security.interfaces import IPrincipal

from zojax.catalog.catalog import queryCatalog
from zojax.content.type.container import ContentContainer
from zojax.content.space.workspace import WorkspaceFactory
from zojax.personal.space.interfaces import \
    IPersonalSpace, IPersonalWorkspaceDescription
from zojax.security.utils import checkPermissionForPrincipal

from interfaces import _, \
    IFavoriteStorage, IFavoriteType, \
    IFavoritesWorkspace, IFavoritesWorkspaceFactory


class FavoritesWorkspace(ContentContainer):
    interface.implements(IFavoritesWorkspace)

    title = _('Favorites')
    description = u''

    @property
    def space(self):
        return self.__parent__


class FavoritesWorkspaceFactory(WorkspaceFactory):
    component.adapts(IPersonalSpace)
    interface.implements(IFavoritesWorkspaceFactory)

    name = u'favorites'
    title = _('Favorites')
    description = _(u'Personal favorites.')
    weight = 1000
    factory = FavoritesWorkspace

    def isAvailable(self):
        principal = self.space.principal
        if principal is not None:
            return checkPermissionForPrincipal(
                principal, 'zojax.PersonalFavorites', self.space)
        else:
            return False


class FavoritesDescription(object):
    interface.implements(IPersonalWorkspaceDescription)

    name = 'favorites'
    title = _(u'Personal favorites.')
    description = u''

    def createTemp(self, context):
        ws = FavoritesWorkspace()
        ws.__parent__ = context
        return ws


@component.adapter(IPrincipal)
@interface.implementer(IFavoriteStorage)
def getFavoriteStorage(principal):
    space = IPersonalSpace(principal, None)
    if space is not None:
        return getAdapter(space, IFavoritesWorkspaceFactory, 'favorites').get()
