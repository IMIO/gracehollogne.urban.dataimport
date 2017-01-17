# -*- coding: utf-8 -*-

from zope.interface import implements

from imio.urban.dataimport.agorawin.importer import AgorawinDataImporter
from gracehollogne.urban.dataimport.interfaces import IGracehollogneDataImporter


class GracehollogneDataImporter(AgorawinDataImporter):
    """ """

    implements(IGracehollogneDataImporter)
