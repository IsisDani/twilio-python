r"""
    This code was generated by
   ___ _ _ _ _ _    _ ____    ____ ____ _    ____ ____ _  _ ____ ____ ____ ___ __   __
    |  | | | | |    | |  | __ |  | |__| | __ | __ |___ |\ | |___ |__/ |__|  | |  | |__/
    |  |_|_| | |___ | |__|    |__| |  | |    |__] |___ | \| |___ |  \ |  |  | |__| |  \

    Twilio - Messaging
    This is the public Twilio REST API.

    NOTE: This class is auto generated by OpenAPI Generator.
    https://openapi-generator.tech
    Do not edit the class manually.
"""

from typing import Any, Dict, List, Optional, Union
from twilio.base import values

from twilio.base.instance_resource import InstanceResource
from twilio.base.list_resource import ListResource
from twilio.base.version import Version


class UsAppToPersonUsecaseInstance(InstanceResource):
    """
    :ivar us_app_to_person_usecases: Human readable name, code, description and post_approval_required (indicates whether or not post approval is required for this Use Case) of A2P Campaign Use Cases.
    """

    def __init__(
        self, version: Version, payload: Dict[str, Any], messaging_service_sid: str
    ):
        super().__init__(version)

        self.us_app_to_person_usecases: Optional[List[Dict[str, object]]] = payload.get(
            "us_app_to_person_usecases"
        )

        self._solution = {
            "messaging_service_sid": messaging_service_sid,
        }

    def __repr__(self) -> str:
        """
        Provide a friendly representation

        :returns: Machine friendly representation
        """
        context = " ".join("{}={}".format(k, v) for k, v in self._solution.items())
        return "<Twilio.Messaging.V1.UsAppToPersonUsecaseInstance {}>".format(context)


class UsAppToPersonUsecaseList(ListResource):

    def __init__(self, version: Version, messaging_service_sid: str):
        """
        Initialize the UsAppToPersonUsecaseList

        :param version: Version that contains the resource
        :param messaging_service_sid: The SID of the [Messaging Service](https://www.twilio.com/docs/messaging/api/service-resource) to fetch the resource from.

        """
        super().__init__(version)

        # Path Solution
        self._solution = {
            "messaging_service_sid": messaging_service_sid,
        }
        self._uri = (
            "/Services/{messaging_service_sid}/Compliance/Usa2p/Usecases".format(
                **self._solution
            )
        )

    def fetch(
        self, brand_registration_sid: Union[str, object] = values.unset
    ) -> UsAppToPersonUsecaseInstance:
        """
        Asynchronously fetch the UsAppToPersonUsecaseInstance

        :param brand_registration_sid: The unique string to identify the A2P brand.
        :returns: The fetched UsAppToPersonUsecaseInstance
        """

        params = values.of(
            {
                "BrandRegistrationSid": brand_registration_sid,
            }
        )
        payload = self._version.fetch(method="GET", uri=self._uri, params=params)

        return UsAppToPersonUsecaseInstance(
            self._version,
            payload,
            messaging_service_sid=self._solution["messaging_service_sid"],
        )

    async def fetch_async(
        self, brand_registration_sid: Union[str, object] = values.unset
    ) -> UsAppToPersonUsecaseInstance:
        """
        Asynchronously fetch the UsAppToPersonUsecaseInstance

        :param brand_registration_sid: The unique string to identify the A2P brand.
        :returns: The fetched UsAppToPersonUsecaseInstance
        """

        params = values.of(
            {
                "BrandRegistrationSid": brand_registration_sid,
            }
        )
        payload = await self._version.fetch_async(
            method="GET", uri=self._uri, params=params
        )

        return UsAppToPersonUsecaseInstance(
            self._version,
            payload,
            messaging_service_sid=self._solution["messaging_service_sid"],
        )

    def __repr__(self) -> str:
        """
        Provide a friendly representation

        :returns: Machine friendly representation
        """
        return "<Twilio.Messaging.V1.UsAppToPersonUsecaseList>"
