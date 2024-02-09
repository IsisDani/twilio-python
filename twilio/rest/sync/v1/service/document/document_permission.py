r"""
    This code was generated by
   ___ _ _ _ _ _    _ ____    ____ ____ _    ____ ____ _  _ ____ ____ ____ ___ __   __
    |  | | | | |    | |  | __ |  | |__| | __ | __ |___ |\ | |___ |__/ |__|  | |  | |__/
    |  |_|_| | |___ | |__|    |__| |  | |    |__] |___ | \| |___ |  \ |  |  | |__| |  \

    Twilio - Sync
    This is the public Twilio REST API.

    NOTE: This class is auto generated by OpenAPI Generator.
    https://openapi-generator.tech
    Do not edit the class manually.
"""

from typing import Any, Dict, List, Optional, Union, Iterator, AsyncIterator
from twilio.base import values
from twilio.base.instance_context import InstanceContext
from twilio.base.instance_resource import InstanceResource
from twilio.base.list_resource import ListResource
from twilio.base.version import Version
from twilio.base.page import Page


class DocumentPermissionInstance(InstanceResource):
    """
    :ivar account_sid: The SID of the [Account](https://www.twilio.com/docs/iam/api/account) that created the Document Permission resource.
    :ivar service_sid: The SID of the [Sync Service](https://www.twilio.com/docs/sync/api/service) the resource is associated with.
    :ivar document_sid: The SID of the Sync Document to which the Document Permission applies.
    :ivar identity: The application-defined string that uniquely identifies the resource's User within the Service to an FPA token.
    :ivar read: Whether the identity can read the Sync Document.
    :ivar write: Whether the identity can update the Sync Document.
    :ivar manage: Whether the identity can delete the Sync Document.
    :ivar url: The absolute URL of the Sync Document Permission resource.
    """

    def __init__(
        self,
        version: Version,
        payload: Dict[str, Any],
        service_sid: str,
        document_sid: str,
        identity: Optional[str] = None,
    ):
        super().__init__(version)

        self.account_sid: Optional[str] = payload.get("account_sid")
        self.service_sid: Optional[str] = payload.get("service_sid")
        self.document_sid: Optional[str] = payload.get("document_sid")
        self.identity: Optional[str] = payload.get("identity")
        self.read: Optional[bool] = payload.get("read")
        self.write: Optional[bool] = payload.get("write")
        self.manage: Optional[bool] = payload.get("manage")
        self.url: Optional[str] = payload.get("url")

        self._solution = {
            "service_sid": service_sid,
            "document_sid": document_sid,
            "identity": identity or self.identity,
        }
        self._context: Optional[DocumentPermissionContext] = None

    @property
    def _proxy(self) -> "DocumentPermissionContext":
        """
        Generate an instance context for the instance, the context is capable of
        performing various actions. All instance actions are proxied to the context

        :returns: DocumentPermissionContext for this DocumentPermissionInstance
        """
        if self._context is None:
            self._context = DocumentPermissionContext(
                self._version,
                service_sid=self._solution["service_sid"],
                document_sid=self._solution["document_sid"],
                identity=self._solution["identity"],
            )
        return self._context

    def delete(self) -> bool:
        """
        Deletes the DocumentPermissionInstance


        :returns: True if delete succeeds, False otherwise
        """
        return self._proxy.delete()

    async def delete_async(self) -> bool:
        """
        Asynchronous coroutine that deletes the DocumentPermissionInstance


        :returns: True if delete succeeds, False otherwise
        """
        return await self._proxy.delete_async()

    def fetch(self) -> "DocumentPermissionInstance":
        """
        Fetch the DocumentPermissionInstance


        :returns: The fetched DocumentPermissionInstance
        """
        return self._proxy.fetch()

    async def fetch_async(self) -> "DocumentPermissionInstance":
        """
        Asynchronous coroutine to fetch the DocumentPermissionInstance


        :returns: The fetched DocumentPermissionInstance
        """
        return await self._proxy.fetch_async()

    def update(
        self, read: bool, write: bool, manage: bool
    ) -> "DocumentPermissionInstance":
        """
        Update the DocumentPermissionInstance

        :param read: Whether the identity can read the Sync Document. Default value is `false`.
        :param write: Whether the identity can update the Sync Document. Default value is `false`.
        :param manage: Whether the identity can delete the Sync Document. Default value is `false`.

        :returns: The updated DocumentPermissionInstance
        """
        return self._proxy.update(
            read=read,
            write=write,
            manage=manage,
        )

    async def update_async(
        self, read: bool, write: bool, manage: bool
    ) -> "DocumentPermissionInstance":
        """
        Asynchronous coroutine to update the DocumentPermissionInstance

        :param read: Whether the identity can read the Sync Document. Default value is `false`.
        :param write: Whether the identity can update the Sync Document. Default value is `false`.
        :param manage: Whether the identity can delete the Sync Document. Default value is `false`.

        :returns: The updated DocumentPermissionInstance
        """
        return await self._proxy.update_async(
            read=read,
            write=write,
            manage=manage,
        )

    def __repr__(self) -> str:
        """
        Provide a friendly representation

        :returns: Machine friendly representation
        """
        context = " ".join("{}={}".format(k, v) for k, v in self._solution.items())
        return "<Twilio.Sync.V1.DocumentPermissionInstance {}>".format(context)


class DocumentPermissionContext(InstanceContext):

    def __init__(
        self, version: Version, service_sid: str, document_sid: str, identity: str
    ):
        """
        Initialize the DocumentPermissionContext

        :param version: Version that contains the resource
        :param service_sid: The SID of the [Sync Service](https://www.twilio.com/docs/sync/api/service) with the Document Permission resource to update.
        :param document_sid: The SID of the Sync Document with the Document Permission resource to update. Can be the Document resource's `sid` or its `unique_name`.
        :param identity: The application-defined string that uniquely identifies the User's Document Permission resource to update.
        """
        super().__init__(version)

        # Path Solution
        self._solution = {
            "service_sid": service_sid,
            "document_sid": document_sid,
            "identity": identity,
        }
        self._uri = "/Services/{service_sid}/Documents/{document_sid}/Permissions/{identity}".format(
            **self._solution
        )

    def delete(self) -> bool:
        """
        Deletes the DocumentPermissionInstance


        :returns: True if delete succeeds, False otherwise
        """
        return self._version.delete(
            method="DELETE",
            uri=self._uri,
        )

    async def delete_async(self) -> bool:
        """
        Asynchronous coroutine that deletes the DocumentPermissionInstance


        :returns: True if delete succeeds, False otherwise
        """
        return await self._version.delete_async(
            method="DELETE",
            uri=self._uri,
        )

    def fetch(self) -> DocumentPermissionInstance:
        """
        Fetch the DocumentPermissionInstance


        :returns: The fetched DocumentPermissionInstance
        """

        payload = self._version.fetch(
            method="GET",
            uri=self._uri,
        )

        return DocumentPermissionInstance(
            self._version,
            payload,
            service_sid=self._solution["service_sid"],
            document_sid=self._solution["document_sid"],
            identity=self._solution["identity"],
        )

    async def fetch_async(self) -> DocumentPermissionInstance:
        """
        Asynchronous coroutine to fetch the DocumentPermissionInstance


        :returns: The fetched DocumentPermissionInstance
        """

        payload = await self._version.fetch_async(
            method="GET",
            uri=self._uri,
        )

        return DocumentPermissionInstance(
            self._version,
            payload,
            service_sid=self._solution["service_sid"],
            document_sid=self._solution["document_sid"],
            identity=self._solution["identity"],
        )

    def update(
        self, read: bool, write: bool, manage: bool
    ) -> DocumentPermissionInstance:
        """
        Update the DocumentPermissionInstance

        :param read: Whether the identity can read the Sync Document. Default value is `false`.
        :param write: Whether the identity can update the Sync Document. Default value is `false`.
        :param manage: Whether the identity can delete the Sync Document. Default value is `false`.

        :returns: The updated DocumentPermissionInstance
        """
        data = values.of(
            {
                "Read": read,
                "Write": write,
                "Manage": manage,
            }
        )

        payload = self._version.update(
            method="POST",
            uri=self._uri,
            data=data,
        )

        return DocumentPermissionInstance(
            self._version,
            payload,
            service_sid=self._solution["service_sid"],
            document_sid=self._solution["document_sid"],
            identity=self._solution["identity"],
        )

    async def update_async(
        self, read: bool, write: bool, manage: bool
    ) -> DocumentPermissionInstance:
        """
        Asynchronous coroutine to update the DocumentPermissionInstance

        :param read: Whether the identity can read the Sync Document. Default value is `false`.
        :param write: Whether the identity can update the Sync Document. Default value is `false`.
        :param manage: Whether the identity can delete the Sync Document. Default value is `false`.

        :returns: The updated DocumentPermissionInstance
        """
        data = values.of(
            {
                "Read": read,
                "Write": write,
                "Manage": manage,
            }
        )

        payload = await self._version.update_async(
            method="POST",
            uri=self._uri,
            data=data,
        )

        return DocumentPermissionInstance(
            self._version,
            payload,
            service_sid=self._solution["service_sid"],
            document_sid=self._solution["document_sid"],
            identity=self._solution["identity"],
        )

    def __repr__(self) -> str:
        """
        Provide a friendly representation

        :returns: Machine friendly representation
        """
        context = " ".join("{}={}".format(k, v) for k, v in self._solution.items())
        return "<Twilio.Sync.V1.DocumentPermissionContext {}>".format(context)


class DocumentPermissionPage(Page):

    def get_instance(self, payload: Dict[str, Any]) -> DocumentPermissionInstance:
        """
        Build an instance of DocumentPermissionInstance

        :param payload: Payload response from the API
        """
        return DocumentPermissionInstance(
            self._version,
            payload,
            service_sid=self._solution["service_sid"],
            document_sid=self._solution["document_sid"],
        )

    def __repr__(self) -> str:
        """
        Provide a friendly representation

        :returns: Machine friendly representation
        """
        return "<Twilio.Sync.V1.DocumentPermissionPage>"


class DocumentPermissionList(ListResource):

    def __init__(self, version: Version, service_sid: str, document_sid: str):
        """
        Initialize the DocumentPermissionList

        :param version: Version that contains the resource
        :param service_sid: The SID of the [Sync Service](https://www.twilio.com/docs/sync/api/service) with the Document Permission resources to read.
        :param document_sid: The SID of the Sync Document with the Document Permission resources to read. Can be the Document resource's `sid` or its `unique_name`.

        """
        super().__init__(version)

        # Path Solution
        self._solution = {
            "service_sid": service_sid,
            "document_sid": document_sid,
        }
        self._uri = (
            "/Services/{service_sid}/Documents/{document_sid}/Permissions".format(
                **self._solution
            )
        )

    def stream(
        self,
        limit: Optional[int] = None,
        page_size: Optional[int] = None,
    ) -> Iterator[DocumentPermissionInstance]:
        """
        Streams DocumentPermissionInstance records from the API as a generator stream.
        This operation lazily loads records as efficiently as possible until the limit
        is reached.
        The results are returned as a generator, so this operation is memory efficient.

        :param limit: Upper limit for the number of records to return. stream()
                      guarantees to never return more than limit.  Default is no limit
        :param page_size: Number of records to fetch per request, when not set will use
                          the default value of 50 records.  If no page_size is defined
                          but a limit is defined, stream() will attempt to read the
                          limit with the most efficient page size, i.e. min(limit, 1000)

        :returns: Generator that will yield up to limit results
        """
        limits = self._version.read_limits(limit, page_size)
        page = self.page(page_size=limits["page_size"])

        return self._version.stream(page, limits["limit"])

    async def stream_async(
        self,
        limit: Optional[int] = None,
        page_size: Optional[int] = None,
    ) -> AsyncIterator[DocumentPermissionInstance]:
        """
        Asynchronously streams DocumentPermissionInstance records from the API as a generator stream.
        This operation lazily loads records as efficiently as possible until the limit
        is reached.
        The results are returned as a generator, so this operation is memory efficient.

        :param limit: Upper limit for the number of records to return. stream()
                      guarantees to never return more than limit.  Default is no limit
        :param page_size: Number of records to fetch per request, when not set will use
                          the default value of 50 records.  If no page_size is defined
                          but a limit is defined, stream() will attempt to read the
                          limit with the most efficient page size, i.e. min(limit, 1000)

        :returns: Generator that will yield up to limit results
        """
        limits = self._version.read_limits(limit, page_size)
        page = await self.page_async(page_size=limits["page_size"])

        return self._version.stream_async(page, limits["limit"])

    def list(
        self,
        limit: Optional[int] = None,
        page_size: Optional[int] = None,
    ) -> List[DocumentPermissionInstance]:
        """
        Lists DocumentPermissionInstance records from the API as a list.
        Unlike stream(), this operation is eager and will load `limit` records into
        memory before returning.

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
                limit=limit,
                page_size=page_size,
            )
        )

    async def list_async(
        self,
        limit: Optional[int] = None,
        page_size: Optional[int] = None,
    ) -> List[DocumentPermissionInstance]:
        """
        Asynchronously lists DocumentPermissionInstance records from the API as a list.
        Unlike stream(), this operation is eager and will load `limit` records into
        memory before returning.

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
                limit=limit,
                page_size=page_size,
            )
        ]

    def page(
        self,
        page_token: Union[str, object] = values.unset,
        page_number: Union[int, object] = values.unset,
        page_size: Union[int, object] = values.unset,
    ) -> DocumentPermissionPage:
        """
        Retrieve a single page of DocumentPermissionInstance records from the API.
        Request is executed immediately

        :param page_token: PageToken provided by the API
        :param page_number: Page Number, this value is simply for client state
        :param page_size: Number of records to return, defaults to 50

        :returns: Page of DocumentPermissionInstance
        """
        data = values.of(
            {
                "PageToken": page_token,
                "Page": page_number,
                "PageSize": page_size,
            }
        )

        response = self._version.page(method="GET", uri=self._uri, params=data)
        return DocumentPermissionPage(self._version, response, self._solution)

    async def page_async(
        self,
        page_token: Union[str, object] = values.unset,
        page_number: Union[int, object] = values.unset,
        page_size: Union[int, object] = values.unset,
    ) -> DocumentPermissionPage:
        """
        Asynchronously retrieve a single page of DocumentPermissionInstance records from the API.
        Request is executed immediately

        :param page_token: PageToken provided by the API
        :param page_number: Page Number, this value is simply for client state
        :param page_size: Number of records to return, defaults to 50

        :returns: Page of DocumentPermissionInstance
        """
        data = values.of(
            {
                "PageToken": page_token,
                "Page": page_number,
                "PageSize": page_size,
            }
        )

        response = await self._version.page_async(
            method="GET", uri=self._uri, params=data
        )
        return DocumentPermissionPage(self._version, response, self._solution)

    def get_page(self, target_url: str) -> DocumentPermissionPage:
        """
        Retrieve a specific page of DocumentPermissionInstance records from the API.
        Request is executed immediately

        :param target_url: API-generated URL for the requested results page

        :returns: Page of DocumentPermissionInstance
        """
        response = self._version.domain.twilio.request("GET", target_url)
        return DocumentPermissionPage(self._version, response, self._solution)

    async def get_page_async(self, target_url: str) -> DocumentPermissionPage:
        """
        Asynchronously retrieve a specific page of DocumentPermissionInstance records from the API.
        Request is executed immediately

        :param target_url: API-generated URL for the requested results page

        :returns: Page of DocumentPermissionInstance
        """
        response = await self._version.domain.twilio.request_async("GET", target_url)
        return DocumentPermissionPage(self._version, response, self._solution)

    def get(self, identity: str) -> DocumentPermissionContext:
        """
        Constructs a DocumentPermissionContext

        :param identity: The application-defined string that uniquely identifies the User's Document Permission resource to update.
        """
        return DocumentPermissionContext(
            self._version,
            service_sid=self._solution["service_sid"],
            document_sid=self._solution["document_sid"],
            identity=identity,
        )

    def __call__(self, identity: str) -> DocumentPermissionContext:
        """
        Constructs a DocumentPermissionContext

        :param identity: The application-defined string that uniquely identifies the User's Document Permission resource to update.
        """
        return DocumentPermissionContext(
            self._version,
            service_sid=self._solution["service_sid"],
            document_sid=self._solution["document_sid"],
            identity=identity,
        )

    def __repr__(self) -> str:
        """
        Provide a friendly representation

        :returns: Machine friendly representation
        """
        return "<Twilio.Sync.V1.DocumentPermissionList>"
