# -*- coding: utf-8 -*-
"""Setup/installation tests for this package."""

from gracehollogne.urban.dataimport.testing import IntegrationTestCase
from plone import api


class TestInstall(IntegrationTestCase):
    """Test installation of gracehollogne.urban.dataimport into Plone."""

    def setUp(self):
        """Custom shared utility setup for tests."""
        self.portal = self.layer['portal']
        self.installer = api.portal.get_tool('portal_quickinstaller')

    def test_product_installed(self):
        """Test if gracehollogne.urban.dataimport is installed with portal_quickinstaller."""
        self.assertTrue(self.installer.isProductInstalled('gracehollogne.urban.dataimport'))

    def test_uninstall(self):
        """Test if gracehollogne.urban.dataimport is cleanly uninstalled."""
        self.installer.uninstallProducts(['gracehollogne.urban.dataimport'])
        self.assertFalse(self.installer.isProductInstalled('gracehollogne.urban.dataimport'))

    # browserlayer.xml
    def test_browserlayer(self):
        """Test that IGracehollogneUrbanDataimportLayer is registered."""
        from gracehollogne.urban.dataimport.interfaces import IGracehollogneUrbanDataimportLayer
        from plone.browserlayer import utils
        self.failUnless(IGracehollogneUrbanDataimportLayer in utils.registered_layers())
