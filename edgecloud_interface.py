#!/usr/bin/env python3
# -*- coding: utf-8 -*-
##
# Copyright 2025-present by Software Networks Area, i2CAT.
# All rights reserved.
#
# This file is part of the Federation SDK
# Unauthorized copying of this file, via any medium is strictly prohibited.
#
# Contributors:
#   - Adrián Pino (adrian.pino@i2cat.net)
##

from abc import ABC, abstractmethod
from typing import List, Dict, Optional

class EdgeApplicationManagementInterface(ABC):
    """
    Abstract Base Class for Edge Application Management.
    """

    @abstractmethod
    def onboard_app(self, app_manifest: Dict) -> Dict:
        """
        Onboards an app, submitting application metadata to the Edge Cloud Provider.
        
        :param app_manifest: Application metadata in dictionary format.
        :return: Dictionary containing created application details.
        """
        pass

    @abstractmethod
    def get_onboarded_apps(self) -> List[Dict]:
        """
        Retrieves a list of onboarded applications.
        
        :return: List of application metadata dictionaries.
        """
        pass

    @abstractmethod
    def get_onboarded_app(self, app_id: str) -> Dict:
        """
        Retrieves information of a specific onboarded application.
        
        :param app_id: Unique identifier of the application.
        :return: Dictionary with application details.
        """
        pass

    @abstractmethod
    def delete_onboarded_app(self, app_id: str) -> None:
        """
        Deletes an application onboarded from the Edge Cloud Provider.
        
        :param app_id: Unique identifier of the application.
        """
        pass

    @abstractmethod
    def create_app_instance(self, app_id: str, app_zones: List[Dict]) -> Dict:
        """
        Requests the instantiation of an application instance.
        
        :param app_id: Unique identifier of the application.
        :param app_zones: List of Edge Cloud Zones where the app should be instantiated.
        :return: Dictionary with instance details.
        """
        pass

    @abstractmethod
    def get_app_instances(
        self, app_id: Optional[str] = None, app_instance_id: Optional[str] = None, region: Optional[str] = None
    ) -> List[Dict]:
        """
        Retrieves information of application instances.

        :param app_id: Filter by application ID.
        :param app_instance_id: Filter by instance ID.
        :param region: Filter by Edge Cloud region.
        :return: List of application instance details.
        """
        pass

    @abstractmethod
    def delete_app_instance(self, app_instance_id: str) -> None:
        """
        Terminates a specific application instance.

        :param app_instance_id: Unique identifier of the application instance.
        """
        pass

    @abstractmethod
    def get_edge_cloud_zones(self, region: Optional[str] = None, status: Optional[str] = None) -> List[Dict]:
        """
        Retrieves a list of available Edge Cloud Zones.

        :param region: Filter by geographical region.
        :param status: Filter by status (active, inactive, unknown).
        :return: List of Edge Cloud Zones.
        """
        pass
