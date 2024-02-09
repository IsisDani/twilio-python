r"""
    This code was generated by
   ___ _ _ _ _ _    _ ____    ____ ____ _    ____ ____ _  _ ____ ____ ____ ___ __   __
    |  | | | | |    | |  | __ |  | |__| | __ | __ |___ |\ | |___ |__/ |__|  | |  | |__/
    |  |_|_| | |___ | |__|    |__| |  | |    |__] |___ | \| |___ |  \ |  |  | |__| |  \

    Twilio - Wireless
    This is the public Twilio REST API.

    NOTE: This class is auto generated by OpenAPI Generator.
    https://openapi-generator.tech
    Do not edit the class manually.
"""

from datetime import datetime
from typing import Any, Dict, List, Optional, Union, Iterator, AsyncIterator
from twilio.base import deserialize, values
from twilio.base.instance_context import InstanceContext
from twilio.base.instance_resource import InstanceResource
from twilio.base.list_resource import ListResource
from twilio.base.version import Version
from twilio.base.page import Page


class CommandInstance(InstanceResource):

    class CommandMode(object):
        TEXT = "text"
        BINARY = "binary"

    class Direction(object):
        FROM_SIM = "from_sim"
        TO_SIM = "to_sim"

    class Status(object):
        QUEUED = "queued"
        SENT = "sent"
        DELIVERED = "delivered"
        RECEIVED = "received"
        FAILED = "failed"

    class Transport(object):
        SMS = "sms"
        IP = "ip"

    """
    :ivar sid: The unique string that we created to identify the Command resource.
    :ivar account_sid: The SID of the [Account](https://www.twilio.com/docs/iam/api/account) that created the Command resource.
    :ivar sim_sid: The SID of the [Sim resource](https://www.twilio.com/docs/iot/wireless/api/sim-resource) that the Command was sent to or from.
    :ivar command: The message being sent to or from the SIM. For text mode messages, this can be up to 160 characters. For binary mode messages, this is a series of up to 140 bytes of data encoded using base64.
    :ivar command_mode: 
    :ivar transport: 
    :ivar delivery_receipt_requested: Whether to request a delivery receipt.
    :ivar status: 
    :ivar direction: 
    :ivar date_created: The date and time in GMT when the resource was created specified in [ISO 8601](https://www.iso.org/iso-8601-date-and-time-format.html) format.
    :ivar date_updated: The date and time in GMT when the resource was last updated specified in [ISO 8601](https://www.iso.org/iso-8601-date-and-time-format.html) format.
    :ivar url: The absolute URL of the resource.
    """

    def __init__(
        self, version: Version, payload: Dict[str, Any], sid: Optional[str] = None
    ):
        super().__init__(version)

        self.sid: Optional[str] = payload.get("sid")
        self.account_sid: Optional[str] = payload.get("account_sid")
        self.sim_sid: Optional[str] = payload.get("sim_sid")
        self.command: Optional[str] = payload.get("command")
        self.command_mode: Optional["CommandInstance.CommandMode"] = payload.get(
            "command_mode"
        )
        self.transport: Optional["CommandInstance.Transport"] = payload.get("transport")
        self.delivery_receipt_requested: Optional[bool] = payload.get(
            "delivery_receipt_requested"
        )
        self.status: Optional["CommandInstance.Status"] = payload.get("status")
        self.direction: Optional["CommandInstance.Direction"] = payload.get("direction")
        self.date_created: Optional[datetime] = deserialize.iso8601_datetime(
            payload.get("date_created")
        )
        self.date_updated: Optional[datetime] = deserialize.iso8601_datetime(
            payload.get("date_updated")
        )
        self.url: Optional[str] = payload.get("url")

        self._solution = {
            "sid": sid or self.sid,
        }
        self._context: Optional[CommandContext] = None

    @property
    def _proxy(self) -> "CommandContext":
        """
        Generate an instance context for the instance, the context is capable of
        performing various actions. All instance actions are proxied to the context

        :returns: CommandContext for this CommandInstance
        """
        if self._context is None:
            self._context = CommandContext(
                self._version,
                sid=self._solution["sid"],
            )
        return self._context

    def delete(self) -> bool:
        """
        Deletes the CommandInstance


        :returns: True if delete succeeds, False otherwise
        """
        return self._proxy.delete()

    async def delete_async(self) -> bool:
        """
        Asynchronous coroutine that deletes the CommandInstance


        :returns: True if delete succeeds, False otherwise
        """
        return await self._proxy.delete_async()

    def fetch(self) -> "CommandInstance":
        """
        Fetch the CommandInstance


        :returns: The fetched CommandInstance
        """
        return self._proxy.fetch()

    async def fetch_async(self) -> "CommandInstance":
        """
        Asynchronous coroutine to fetch the CommandInstance


        :returns: The fetched CommandInstance
        """
        return await self._proxy.fetch_async()

    def __repr__(self) -> str:
        """
        Provide a friendly representation

        :returns: Machine friendly representation
        """
        context = " ".join("{}={}".format(k, v) for k, v in self._solution.items())
        return "<Twilio.Wireless.V1.CommandInstance {}>".format(context)


class CommandContext(InstanceContext):

    def __init__(self, version: Version, sid: str):
        """
        Initialize the CommandContext

        :param version: Version that contains the resource
        :param sid: The SID of the Command resource to fetch.
        """
        super().__init__(version)

        # Path Solution
        self._solution = {
            "sid": sid,
        }
        self._uri = "/Commands/{sid}".format(**self._solution)

    def delete(self) -> bool:
        """
        Deletes the CommandInstance


        :returns: True if delete succeeds, False otherwise
        """
        return self._version.delete(
            method="DELETE",
            uri=self._uri,
        )

    async def delete_async(self) -> bool:
        """
        Asynchronous coroutine that deletes the CommandInstance


        :returns: True if delete succeeds, False otherwise
        """
        return await self._version.delete_async(
            method="DELETE",
            uri=self._uri,
        )

    def fetch(self) -> CommandInstance:
        """
        Fetch the CommandInstance


        :returns: The fetched CommandInstance
        """

        payload = self._version.fetch(
            method="GET",
            uri=self._uri,
        )

        return CommandInstance(
            self._version,
            payload,
            sid=self._solution["sid"],
        )

    async def fetch_async(self) -> CommandInstance:
        """
        Asynchronous coroutine to fetch the CommandInstance


        :returns: The fetched CommandInstance
        """

        payload = await self._version.fetch_async(
            method="GET",
            uri=self._uri,
        )

        return CommandInstance(
            self._version,
            payload,
            sid=self._solution["sid"],
        )

    def __repr__(self) -> str:
        """
        Provide a friendly representation

        :returns: Machine friendly representation
        """
        context = " ".join("{}={}".format(k, v) for k, v in self._solution.items())
        return "<Twilio.Wireless.V1.CommandContext {}>".format(context)


class CommandPage(Page):

    def get_instance(self, payload: Dict[str, Any]) -> CommandInstance:
        """
        Build an instance of CommandInstance

        :param payload: Payload response from the API
        """
        return CommandInstance(self._version, payload)

    def __repr__(self) -> str:
        """
        Provide a friendly representation

        :returns: Machine friendly representation
        """
        return "<Twilio.Wireless.V1.CommandPage>"


class CommandList(ListResource):

    def __init__(self, version: Version):
        """
        Initialize the CommandList

        :param version: Version that contains the resource

        """
        super().__init__(version)

        self._uri = "/Commands"

    def create(
        self,
        command: str,
        sim: Union[str, object] = values.unset,
        callback_method: Union[str, object] = values.unset,
        callback_url: Union[str, object] = values.unset,
        command_mode: Union["CommandInstance.CommandMode", object] = values.unset,
        include_sid: Union[str, object] = values.unset,
        delivery_receipt_requested: Union[bool, object] = values.unset,
    ) -> CommandInstance:
        """
        Create the CommandInstance

        :param command: The message body of the Command. Can be plain text in text mode or a Base64 encoded byte string in binary mode.
        :param sim: The `sid` or `unique_name` of the [SIM](https://www.twilio.com/docs/iot/wireless/api/sim-resource) to send the Command to.
        :param callback_method: The HTTP method we use to call `callback_url`. Can be: `POST` or `GET`, and the default is `POST`.
        :param callback_url: The URL we call using the `callback_url` when the Command has finished sending, whether the command was delivered or it failed.
        :param command_mode:
        :param include_sid: Whether to include the SID of the command in the message body. Can be: `none`, `start`, or `end`, and the default behavior is `none`. When sending a Command to a SIM in text mode, we can automatically include the SID of the Command in the message body, which could be used to ensure that the device does not process the same Command more than once.  A value of `start` will prepend the message with the Command SID, and `end` will append it to the end, separating the Command SID from the message body with a space. The length of the Command SID is included in the 160 character limit so the SMS body must be 128 characters or less before the Command SID is included.
        :param delivery_receipt_requested: Whether to request delivery receipt from the recipient. For Commands that request delivery receipt, the Command state transitions to 'delivered' once the server has received a delivery receipt from the device. The default value is `true`.

        :returns: The created CommandInstance
        """

        data = values.of(
            {
                "Command": command,
                "Sim": sim,
                "CallbackMethod": callback_method,
                "CallbackUrl": callback_url,
                "CommandMode": command_mode,
                "IncludeSid": include_sid,
                "DeliveryReceiptRequested": delivery_receipt_requested,
            }
        )

        payload = self._version.create(
            method="POST",
            uri=self._uri,
            data=data,
        )

        return CommandInstance(self._version, payload)

    async def create_async(
        self,
        command: str,
        sim: Union[str, object] = values.unset,
        callback_method: Union[str, object] = values.unset,
        callback_url: Union[str, object] = values.unset,
        command_mode: Union["CommandInstance.CommandMode", object] = values.unset,
        include_sid: Union[str, object] = values.unset,
        delivery_receipt_requested: Union[bool, object] = values.unset,
    ) -> CommandInstance:
        """
        Asynchronously create the CommandInstance

        :param command: The message body of the Command. Can be plain text in text mode or a Base64 encoded byte string in binary mode.
        :param sim: The `sid` or `unique_name` of the [SIM](https://www.twilio.com/docs/iot/wireless/api/sim-resource) to send the Command to.
        :param callback_method: The HTTP method we use to call `callback_url`. Can be: `POST` or `GET`, and the default is `POST`.
        :param callback_url: The URL we call using the `callback_url` when the Command has finished sending, whether the command was delivered or it failed.
        :param command_mode:
        :param include_sid: Whether to include the SID of the command in the message body. Can be: `none`, `start`, or `end`, and the default behavior is `none`. When sending a Command to a SIM in text mode, we can automatically include the SID of the Command in the message body, which could be used to ensure that the device does not process the same Command more than once.  A value of `start` will prepend the message with the Command SID, and `end` will append it to the end, separating the Command SID from the message body with a space. The length of the Command SID is included in the 160 character limit so the SMS body must be 128 characters or less before the Command SID is included.
        :param delivery_receipt_requested: Whether to request delivery receipt from the recipient. For Commands that request delivery receipt, the Command state transitions to 'delivered' once the server has received a delivery receipt from the device. The default value is `true`.

        :returns: The created CommandInstance
        """

        data = values.of(
            {
                "Command": command,
                "Sim": sim,
                "CallbackMethod": callback_method,
                "CallbackUrl": callback_url,
                "CommandMode": command_mode,
                "IncludeSid": include_sid,
                "DeliveryReceiptRequested": delivery_receipt_requested,
            }
        )

        payload = await self._version.create_async(
            method="POST",
            uri=self._uri,
            data=data,
        )

        return CommandInstance(self._version, payload)

    def stream(
        self,
        sim: Union[str, object] = values.unset,
        status: Union["CommandInstance.Status", object] = values.unset,
        direction: Union["CommandInstance.Direction", object] = values.unset,
        transport: Union["CommandInstance.Transport", object] = values.unset,
        limit: Optional[int] = None,
        page_size: Optional[int] = None,
    ) -> Iterator[CommandInstance]:
        """
        Streams CommandInstance records from the API as a generator stream.
        This operation lazily loads records as efficiently as possible until the limit
        is reached.
        The results are returned as a generator, so this operation is memory efficient.

        :param str sim: The `sid` or `unique_name` of the [Sim resources](https://www.twilio.com/docs/iot/wireless/api/sim-resource) to read.
        :param &quot;CommandInstance.Status&quot; status: The status of the resources to read. Can be: `queued`, `sent`, `delivered`, `received`, or `failed`.
        :param &quot;CommandInstance.Direction&quot; direction: Only return Commands with this direction value.
        :param &quot;CommandInstance.Transport&quot; transport: Only return Commands with this transport value. Can be: `sms` or `ip`.
        :param limit: Upper limit for the number of records to return. stream()
                      guarantees to never return more than limit.  Default is no limit
        :param page_size: Number of records to fetch per request, when not set will use
                          the default value of 50 records.  If no page_size is defined
                          but a limit is defined, stream() will attempt to read the
                          limit with the most efficient page size, i.e. min(limit, 1000)

        :returns: Generator that will yield up to limit results
        """
        limits = self._version.read_limits(limit, page_size)
        page = self.page(
            sim=sim,
            status=status,
            direction=direction,
            transport=transport,
            page_size=limits["page_size"],
        )

        return self._version.stream(page, limits["limit"])

    async def stream_async(
        self,
        sim: Union[str, object] = values.unset,
        status: Union["CommandInstance.Status", object] = values.unset,
        direction: Union["CommandInstance.Direction", object] = values.unset,
        transport: Union["CommandInstance.Transport", object] = values.unset,
        limit: Optional[int] = None,
        page_size: Optional[int] = None,
    ) -> AsyncIterator[CommandInstance]:
        """
        Asynchronously streams CommandInstance records from the API as a generator stream.
        This operation lazily loads records as efficiently as possible until the limit
        is reached.
        The results are returned as a generator, so this operation is memory efficient.

        :param str sim: The `sid` or `unique_name` of the [Sim resources](https://www.twilio.com/docs/iot/wireless/api/sim-resource) to read.
        :param &quot;CommandInstance.Status&quot; status: The status of the resources to read. Can be: `queued`, `sent`, `delivered`, `received`, or `failed`.
        :param &quot;CommandInstance.Direction&quot; direction: Only return Commands with this direction value.
        :param &quot;CommandInstance.Transport&quot; transport: Only return Commands with this transport value. Can be: `sms` or `ip`.
        :param limit: Upper limit for the number of records to return. stream()
                      guarantees to never return more than limit.  Default is no limit
        :param page_size: Number of records to fetch per request, when not set will use
                          the default value of 50 records.  If no page_size is defined
                          but a limit is defined, stream() will attempt to read the
                          limit with the most efficient page size, i.e. min(limit, 1000)

        :returns: Generator that will yield up to limit results
        """
        limits = self._version.read_limits(limit, page_size)
        page = await self.page_async(
            sim=sim,
            status=status,
            direction=direction,
            transport=transport,
            page_size=limits["page_size"],
        )

        return self._version.stream_async(page, limits["limit"])

    def list(
        self,
        sim: Union[str, object] = values.unset,
        status: Union["CommandInstance.Status", object] = values.unset,
        direction: Union["CommandInstance.Direction", object] = values.unset,
        transport: Union["CommandInstance.Transport", object] = values.unset,
        limit: Optional[int] = None,
        page_size: Optional[int] = None,
    ) -> List[CommandInstance]:
        """
        Lists CommandInstance records from the API as a list.
        Unlike stream(), this operation is eager and will load `limit` records into
        memory before returning.

        :param str sim: The `sid` or `unique_name` of the [Sim resources](https://www.twilio.com/docs/iot/wireless/api/sim-resource) to read.
        :param &quot;CommandInstance.Status&quot; status: The status of the resources to read. Can be: `queued`, `sent`, `delivered`, `received`, or `failed`.
        :param &quot;CommandInstance.Direction&quot; direction: Only return Commands with this direction value.
        :param &quot;CommandInstance.Transport&quot; transport: Only return Commands with this transport value. Can be: `sms` or `ip`.
        :param limit: Upper limit for the number of records to return. list() guarantees
                      never to return more than limit.  Default is no limit
        :param page_size: Number of records to fetch per request, when not set will use
                          the default value of 50 records.  If no page_size is defined
                          but a limit is defined, list() will attempt to read the limit
                          with the most efficient page size, i.e. min(limit, 1000)

        :returns: list that will contain up to limit results
        """
        return list(
            self.stream(
                sim=sim,
                status=status,
                direction=direction,
                transport=transport,
                limit=limit,
                page_size=page_size,
            )
        )

    async def list_async(
        self,
        sim: Union[str, object] = values.unset,
        status: Union["CommandInstance.Status", object] = values.unset,
        direction: Union["CommandInstance.Direction", object] = values.unset,
        transport: Union["CommandInstance.Transport", object] = values.unset,
        limit: Optional[int] = None,
        page_size: Optional[int] = None,
    ) -> List[CommandInstance]:
        """
        Asynchronously lists CommandInstance records from the API as a list.
        Unlike stream(), this operation is eager and will load `limit` records into
        memory before returning.

        :param str sim: The `sid` or `unique_name` of the [Sim resources](https://www.twilio.com/docs/iot/wireless/api/sim-resource) to read.
        :param &quot;CommandInstance.Status&quot; status: The status of the resources to read. Can be: `queued`, `sent`, `delivered`, `received`, or `failed`.
        :param &quot;CommandInstance.Direction&quot; direction: Only return Commands with this direction value.
        :param &quot;CommandInstance.Transport&quot; transport: Only return Commands with this transport value. Can be: `sms` or `ip`.
        :param limit: Upper limit for the number of records to return. list() guarantees
                      never to return more than limit.  Default is no limit
        :param page_size: Number of records to fetch per request, when not set will use
                          the default value of 50 records.  If no page_size is defined
                          but a limit is defined, list() will attempt to read the limit
                          with the most efficient page size, i.e. min(limit, 1000)

        :returns: list that will contain up to limit results
        """
        return [
            record
            async for record in await self.stream_async(
                sim=sim,
                status=status,
                direction=direction,
                transport=transport,
                limit=limit,
                page_size=page_size,
            )
        ]

    def page(
        self,
        sim: Union[str, object] = values.unset,
        status: Union["CommandInstance.Status", object] = values.unset,
        direction: Union["CommandInstance.Direction", object] = values.unset,
        transport: Union["CommandInstance.Transport", object] = values.unset,
        page_token: Union[str, object] = values.unset,
        page_number: Union[int, object] = values.unset,
        page_size: Union[int, object] = values.unset,
    ) -> CommandPage:
        """
        Retrieve a single page of CommandInstance records from the API.
        Request is executed immediately

        :param sim: The `sid` or `unique_name` of the [Sim resources](https://www.twilio.com/docs/iot/wireless/api/sim-resource) to read.
        :param status: The status of the resources to read. Can be: `queued`, `sent`, `delivered`, `received`, or `failed`.
        :param direction: Only return Commands with this direction value.
        :param transport: Only return Commands with this transport value. Can be: `sms` or `ip`.
        :param page_token: PageToken provided by the API
        :param page_number: Page Number, this value is simply for client state
        :param page_size: Number of records to return, defaults to 50

        :returns: Page of CommandInstance
        """
        data = values.of(
            {
                "Sim": sim,
                "Status": status,
                "Direction": direction,
                "Transport": transport,
                "PageToken": page_token,
                "Page": page_number,
                "PageSize": page_size,
            }
        )

        response = self._version.page(method="GET", uri=self._uri, params=data)
        return CommandPage(self._version, response)

    async def page_async(
        self,
        sim: Union[str, object] = values.unset,
        status: Union["CommandInstance.Status", object] = values.unset,
        direction: Union["CommandInstance.Direction", object] = values.unset,
        transport: Union["CommandInstance.Transport", object] = values.unset,
        page_token: Union[str, object] = values.unset,
        page_number: Union[int, object] = values.unset,
        page_size: Union[int, object] = values.unset,
    ) -> CommandPage:
        """
        Asynchronously retrieve a single page of CommandInstance records from the API.
        Request is executed immediately

        :param sim: The `sid` or `unique_name` of the [Sim resources](https://www.twilio.com/docs/iot/wireless/api/sim-resource) to read.
        :param status: The status of the resources to read. Can be: `queued`, `sent`, `delivered`, `received`, or `failed`.
        :param direction: Only return Commands with this direction value.
        :param transport: Only return Commands with this transport value. Can be: `sms` or `ip`.
        :param page_token: PageToken provided by the API
        :param page_number: Page Number, this value is simply for client state
        :param page_size: Number of records to return, defaults to 50

        :returns: Page of CommandInstance
        """
        data = values.of(
            {
                "Sim": sim,
                "Status": status,
                "Direction": direction,
                "Transport": transport,
                "PageToken": page_token,
                "Page": page_number,
                "PageSize": page_size,
            }
        )

        response = await self._version.page_async(
            method="GET", uri=self._uri, params=data
        )
        return CommandPage(self._version, response)

    def get_page(self, target_url: str) -> CommandPage:
        """
        Retrieve a specific page of CommandInstance records from the API.
        Request is executed immediately

        :param target_url: API-generated URL for the requested results page

        :returns: Page of CommandInstance
        """
        response = self._version.domain.twilio.request("GET", target_url)
        return CommandPage(self._version, response)

    async def get_page_async(self, target_url: str) -> CommandPage:
        """
        Asynchronously retrieve a specific page of CommandInstance records from the API.
        Request is executed immediately

        :param target_url: API-generated URL for the requested results page

        :returns: Page of CommandInstance
        """
        response = await self._version.domain.twilio.request_async("GET", target_url)
        return CommandPage(self._version, response)

    def get(self, sid: str) -> CommandContext:
        """
        Constructs a CommandContext

        :param sid: The SID of the Command resource to fetch.
        """
        return CommandContext(self._version, sid=sid)

    def __call__(self, sid: str) -> CommandContext:
        """
        Constructs a CommandContext

        :param sid: The SID of the Command resource to fetch.
        """
        return CommandContext(self._version, sid=sid)

    def __repr__(self) -> str:
        """
        Provide a friendly representation

        :returns: Machine friendly representation
        """
        return "<Twilio.Wireless.V1.CommandList>"
