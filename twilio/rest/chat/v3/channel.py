r"""
    This code was generated by
   ___ _ _ _ _ _    _ ____    ____ ____ _    ____ ____ _  _ ____ ____ ____ ___ __   __
    |  | | | | |    | |  | __ |  | |__| | __ | __ |___ |\ | |___ |__/ |__|  | |  | |__/
    |  |_|_| | |___ | |__|    |__| |  | |    |__] |___ | \| |___ |  \ |  |  | |__| |  \

    Twilio - Chat
    This is the public Twilio REST API.

    NOTE: This class is auto generated by OpenAPI Generator.
    https://openapi-generator.tech
    Do not edit the class manually.
"""

from datetime import datetime
from typing import Any, Dict, Optional, Union
from twilio.base import deserialize, values
from twilio.base.instance_context import InstanceContext
from twilio.base.instance_resource import InstanceResource
from twilio.base.list_resource import ListResource
from twilio.base.version import Version


class ChannelInstance(InstanceResource):

    class ChannelType(object):
        PUBLIC = "public"
        PRIVATE = "private"

    class WebhookEnabledType(object):
        TRUE = "true"
        FALSE = "false"

    """
    :ivar sid: The unique string that we created to identify the Channel resource.
    :ivar account_sid: The SID of the [Account](https://www.twilio.com/docs/iam/api/account) that created the Channel resource.
    :ivar service_sid: The SID of the [Service](https://www.twilio.com/docs/chat/rest/service-resource) the Channel resource is associated with.
    :ivar friendly_name: The string that you assigned to describe the resource.
    :ivar unique_name: An application-defined string that uniquely identifies the resource. It can be used to address the resource in place of the resource's `sid` in the URL.
    :ivar attributes: The JSON string that stores application-specific data. If attributes have not been set, `{}` is returned.
    :ivar type: 
    :ivar date_created: The date and time in GMT when the resource was created specified in [ISO 8601](https://en.wikipedia.org/wiki/ISO_8601) format.
    :ivar date_updated: The date and time in GMT when the resource was last updated specified in [ISO 8601](https://en.wikipedia.org/wiki/ISO_8601) format.
    :ivar created_by: The `identity` of the User that created the channel. If the Channel was created by using the API, the value is `system`.
    :ivar members_count: The number of Members in the Channel.
    :ivar messages_count: The number of Messages that have been passed in the Channel.
    :ivar messaging_service_sid: The unique ID of the [Messaging Service](https://www.twilio.com/docs/messaging/api/service-resource) this channel belongs to.
    :ivar url: The absolute URL of the Channel resource.
    """

    def __init__(
        self,
        version: Version,
        payload: Dict[str, Any],
        service_sid: Optional[str] = None,
        sid: Optional[str] = None,
    ):
        super().__init__(version)

        self.sid: Optional[str] = payload.get("sid")
        self.account_sid: Optional[str] = payload.get("account_sid")
        self.service_sid: Optional[str] = payload.get("service_sid")
        self.friendly_name: Optional[str] = payload.get("friendly_name")
        self.unique_name: Optional[str] = payload.get("unique_name")
        self.attributes: Optional[str] = payload.get("attributes")
        self.type: Optional["ChannelInstance.ChannelType"] = payload.get("type")
        self.date_created: Optional[datetime] = deserialize.iso8601_datetime(
            payload.get("date_created")
        )
        self.date_updated: Optional[datetime] = deserialize.iso8601_datetime(
            payload.get("date_updated")
        )
        self.created_by: Optional[str] = payload.get("created_by")
        self.members_count: Optional[int] = deserialize.integer(
            payload.get("members_count")
        )
        self.messages_count: Optional[int] = deserialize.integer(
            payload.get("messages_count")
        )
        self.messaging_service_sid: Optional[str] = payload.get("messaging_service_sid")
        self.url: Optional[str] = payload.get("url")

        self._solution = {
            "service_sid": service_sid or self.service_sid,
            "sid": sid or self.sid,
        }
        self._context: Optional[ChannelContext] = None

    @property
    def _proxy(self) -> "ChannelContext":
        """
        Generate an instance context for the instance, the context is capable of
        performing various actions. All instance actions are proxied to the context

        :returns: ChannelContext for this ChannelInstance
        """
        if self._context is None:
            self._context = ChannelContext(
                self._version,
                service_sid=self._solution["service_sid"],
                sid=self._solution["sid"],
            )
        return self._context

    def update(
        self,
        x_twilio_webhook_enabled: Union[
            "ChannelInstance.WebhookEnabledType", object
        ] = values.unset,
        type: Union["ChannelInstance.ChannelType", object] = values.unset,
        messaging_service_sid: Union[str, object] = values.unset,
    ) -> "ChannelInstance":
        """
        Update the ChannelInstance

        :param x_twilio_webhook_enabled: The X-Twilio-Webhook-Enabled HTTP request header
        :param type:
        :param messaging_service_sid: The unique ID of the [Messaging Service](https://www.twilio.com/docs/messaging/api/service-resource) this channel belongs to.

        :returns: The updated ChannelInstance
        """
        return self._proxy.update(
            x_twilio_webhook_enabled=x_twilio_webhook_enabled,
            type=type,
            messaging_service_sid=messaging_service_sid,
        )

    async def update_async(
        self,
        x_twilio_webhook_enabled: Union[
            "ChannelInstance.WebhookEnabledType", object
        ] = values.unset,
        type: Union["ChannelInstance.ChannelType", object] = values.unset,
        messaging_service_sid: Union[str, object] = values.unset,
    ) -> "ChannelInstance":
        """
        Asynchronous coroutine to update the ChannelInstance

        :param x_twilio_webhook_enabled: The X-Twilio-Webhook-Enabled HTTP request header
        :param type:
        :param messaging_service_sid: The unique ID of the [Messaging Service](https://www.twilio.com/docs/messaging/api/service-resource) this channel belongs to.

        :returns: The updated ChannelInstance
        """
        return await self._proxy.update_async(
            x_twilio_webhook_enabled=x_twilio_webhook_enabled,
            type=type,
            messaging_service_sid=messaging_service_sid,
        )

    def __repr__(self) -> str:
        """
        Provide a friendly representation

        :returns: Machine friendly representation
        """
        context = " ".join("{}={}".format(k, v) for k, v in self._solution.items())
        return "<Twilio.Chat.V3.ChannelInstance {}>".format(context)


class ChannelContext(InstanceContext):

    def __init__(self, version: Version, service_sid: str, sid: str):
        """
        Initialize the ChannelContext

        :param version: Version that contains the resource
        :param service_sid: The unique SID identifier of the Service.
        :param sid: A 34 character string that uniquely identifies this Channel.
        """
        super().__init__(version)

        # Path Solution
        self._solution = {
            "service_sid": service_sid,
            "sid": sid,
        }
        self._uri = "/Services/{service_sid}/Channels/{sid}".format(**self._solution)

    def update(
        self,
        x_twilio_webhook_enabled: Union[
            "ChannelInstance.WebhookEnabledType", object
        ] = values.unset,
        type: Union["ChannelInstance.ChannelType", object] = values.unset,
        messaging_service_sid: Union[str, object] = values.unset,
    ) -> ChannelInstance:
        """
        Update the ChannelInstance

        :param x_twilio_webhook_enabled: The X-Twilio-Webhook-Enabled HTTP request header
        :param type:
        :param messaging_service_sid: The unique ID of the [Messaging Service](https://www.twilio.com/docs/messaging/api/service-resource) this channel belongs to.

        :returns: The updated ChannelInstance
        """
        data = values.of(
            {
                "Type": type,
                "MessagingServiceSid": messaging_service_sid,
            }
        )
        headers = values.of(
            {
                "X-Twilio-Webhook-Enabled": x_twilio_webhook_enabled,
            }
        )

        payload = self._version.update(
            method="POST", uri=self._uri, data=data, headers=headers
        )

        return ChannelInstance(
            self._version,
            payload,
            service_sid=self._solution["service_sid"],
            sid=self._solution["sid"],
        )

    async def update_async(
        self,
        x_twilio_webhook_enabled: Union[
            "ChannelInstance.WebhookEnabledType", object
        ] = values.unset,
        type: Union["ChannelInstance.ChannelType", object] = values.unset,
        messaging_service_sid: Union[str, object] = values.unset,
    ) -> ChannelInstance:
        """
        Asynchronous coroutine to update the ChannelInstance

        :param x_twilio_webhook_enabled: The X-Twilio-Webhook-Enabled HTTP request header
        :param type:
        :param messaging_service_sid: The unique ID of the [Messaging Service](https://www.twilio.com/docs/messaging/api/service-resource) this channel belongs to.

        :returns: The updated ChannelInstance
        """
        data = values.of(
            {
                "Type": type,
                "MessagingServiceSid": messaging_service_sid,
            }
        )
        headers = values.of(
            {
                "X-Twilio-Webhook-Enabled": x_twilio_webhook_enabled,
            }
        )

        payload = await self._version.update_async(
            method="POST", uri=self._uri, data=data, headers=headers
        )

        return ChannelInstance(
            self._version,
            payload,
            service_sid=self._solution["service_sid"],
            sid=self._solution["sid"],
        )

    def __repr__(self) -> str:
        """
        Provide a friendly representation

        :returns: Machine friendly representation
        """
        context = " ".join("{}={}".format(k, v) for k, v in self._solution.items())
        return "<Twilio.Chat.V3.ChannelContext {}>".format(context)


class ChannelList(ListResource):

    def __init__(self, version: Version):
        """
        Initialize the ChannelList

        :param version: Version that contains the resource

        """
        super().__init__(version)

    def get(self, service_sid: str, sid: str) -> ChannelContext:
        """
        Constructs a ChannelContext

        :param service_sid: The unique SID identifier of the Service.
        :param sid: A 34 character string that uniquely identifies this Channel.
        """
        return ChannelContext(self._version, service_sid=service_sid, sid=sid)

    def __call__(self, service_sid: str, sid: str) -> ChannelContext:
        """
        Constructs a ChannelContext

        :param service_sid: The unique SID identifier of the Service.
        :param sid: A 34 character string that uniquely identifies this Channel.
        """
        return ChannelContext(self._version, service_sid=service_sid, sid=sid)

    def __repr__(self) -> str:
        """
        Provide a friendly representation

        :returns: Machine friendly representation
        """
        return "<Twilio.Chat.V3.ChannelList>"
