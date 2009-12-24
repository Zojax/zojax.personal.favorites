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
from zope import schema, interface
from zope.i18nmessageid import MessageFactory

from zojax.content.space.interfaces import IWorkspace, IWorkspaceFactory

_ = MessageFactory('zojax.personal.favorites')


class IFavorite(interface.Interface):
    """ favorite """

    title = schema.TextLine(
        title = _(u'Title'),
        description = _(u'Favorite title.'),
        default = u'',
        required = True)

    description = schema.Text(
        title = _(u'Description'),
        description = _(u'Favorite description.'),
        default = u'',
        required = False)


class IFavoriteType(interface.Interface):
    """ favorite type """


class IPersonalLink(IFavorite):
    """ personal link """

    url = schema.TextLine(
        title = _(u'URL'),
        description = _(u'Link URL.'),
        required = True)


class IPersonalLinkType(interface.Interface):
    """ personal link content type """


class IPersonalFavorites(interface.Interface):
    """ """

    allowOthers = schema.Bool(
        title = _(u'Allow others to view'),
        description = _(u'Allow other members view my favorites.'),
        default = True,
        required = True)


class IFavoriteStorage(interface.Interface):
    """ favorite storage """


class IFavoritesWorkspace(IFavoriteStorage, IWorkspace):
    """ favorites workspace """


class IFavoritesWorkspaceFactory(IWorkspaceFactory):
    """ favorites workspace factory """
