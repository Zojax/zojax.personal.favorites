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
from zope.component import getUtility, getUtilitiesFor
from zope.traversing.browser import absoluteURL
from zope.security.proxy import removeSecurityProxy

from zojax.personal.space.interfaces import IPersonalSpace

from zojax.personal.favorites.interfaces import \
    _, IFavoriteStorage, IFavoriteType


class YourFavoritesPortlet(object):
    """ VERY IMPORTANT! We need caching for this view """

    view = None
    container_url = None
    container = None
    favorites = None
    space = None

    def isAvailable(self):
        if self.container is None:
            return False
        if self.favorites is None:
            return False
        return bool(self.favorites)

    def update(self):
        space = self.context
        while space is not None and not IPersonalSpace.providedBy(space):
            space = space.__parent__
        self.space = space

        if space is not None:
            self.container = IFavoriteStorage(space.principal, None)
            if self.container is not None:
                if space.principal.id != self.request.principal.id:
                    self.title = _(u"${title}'s links",
                                   mapping=dict(title=space.principal.title))
                    self.container_url = '%s/%s/'%(
                        absoluteURL(space, self.request),
                        self.container.__name__)
        else:
            self.container = IFavoriteStorage(self.request.principal, None)

        self.favorites = self.listFavorites()

        super(YourFavoritesPortlet, self).update()

    def listFavorites(self):
        if self.container is None:
            return []
        return removeSecurityProxy(self.container).values()
