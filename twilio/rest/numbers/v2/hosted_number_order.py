r"""
    This code was generated by
   ___ _ _ _ _ _    _ ____    ____ ____ _    ____ ____ _  _ ____ ____ ____ ___ __   __
    |  | | | | |    | |  | __ |  | |__| | __ | __ |___ |\ | |___ |__/ |__|  | |  | |__/
    |  |_|_| | |___ | |__|    |__| |  | |    |__] |___ | \| |___ |  \ |  |  | |__| |  \

    Twilio - Numbers
    This is the public Twilio REST API.

    NOTE: This class is auto generated by OpenAPI Generator.
    https://openapi-generator.tech
    Do not edit the class manually.
"""

from datetime import datetime
from typing import Any, Dict, List, Optional, Union, Iterator, AsyncIterator
from twilio.base import deserialize, serialize, values
from twilio.base.instance_context import InstanceContext
from twilio.base.instance_resource import InstanceResource
from twilio.base.list_resource import ListResource
from twilio.base.version import Version
from twilio.base.page import Page


class HostedNumberOrderInstance(InstanceResource):

    class Status(object):
        RECEIVED = "received"
        VERIFIED = "verified"
        PENDING_LOA = "pending-loa"
        CARRIER_PROCESSING = "carrier-processing"
        COMPLETED = "completed"
        FAILED = "failed"
        ACTION_REQUIRED = "action-required"

    """
    :ivar sid: A 34 character string that uniquely identifies this HostedNumberOrder.
    :ivar account_sid: A 34 character string that uniquely identifies the account.
    :ivar incoming_phone_number_sid: A 34 character string that uniquely identifies the [IncomingPhoneNumber](https://www.twilio.com/docs/phone-numbers/api/incomingphonenumber-resource) resource that represents the phone number being hosted.
    :ivar address_sid: A 34 character string that uniquely identifies the Address resource that represents the address of the owner of this phone number.
    :ivar signing_document_sid: A 34 character string that uniquely identifies the [Authorization Document](https://www.twilio.com/docs/phone-numbers/hosted-numbers/hosted-numbers-api/authorization-document-resource) the user needs to sign.
    :ivar phone_number: Phone number to be hosted. This must be in [E.164](https://en.wikipedia.org/wiki/E.164) format, e.g., +16175551212
    :ivar capabilities: 
    :ivar friendly_name: A 128 character string that is a human-readable text that describes this resource.
    :ivar status: 
    :ivar failure_reason: A message that explains why a hosted_number_order went to status \"action-required\"
    :ivar date_created: The date this resource was created, given as [GMT RFC 2822](http://www.ietf.org/rfc/rfc2822.txt) format.
    :ivar date_updated: The date that this resource was updated, given as [GMT RFC 2822](http://www.ietf.org/rfc/rfc2822.txt) format.
    :ivar email: Email of the owner of this phone number that is being hosted.
    :ivar cc_emails: A list of emails that LOA document for this HostedNumberOrder will be carbon copied to.
    :ivar url: The URL of this HostedNumberOrder.
    :ivar contact_title: The title of the person authorized to sign the Authorization Document for this phone number.
    :ivar contact_phone_number: The contact phone number of the person authorized to sign the Authorization Document.
    :ivar bulk_hosting_request_sid: A 34 character string that uniquely identifies the bulk hosting request associated with this HostedNumberOrder.
    :ivar next_step: The next step you need to take to complete the hosted number order and request it successfully.
    """

    def __init__(
        self, version: Version, payload: Dict[str, Any], sid: Optional[str] = None
    ):
        super().__init__(version)

        self.sid: Optional[str] = payload.get("sid")
        self.account_sid: Optional[str] = payload.get("account_sid")
        self.incoming_phone_number_sid: Optional[str] = payload.get(
            "incoming_phone_number_sid"
        )
        self.address_sid: Optional[str] = payload.get("address_sid")
        self.signing_document_sid: Optional[str] = payload.get("signing_document_sid")
        self.phone_number: Optional[str] = payload.get("phone_number")
        self.capabilities: Optional[str] = payload.get("capabilities")
        self.friendly_name: Optional[str] = payload.get("friendly_name")
        self.status: Optional["HostedNumberOrderInstance.Status"] = payload.get(
            "status"
        )
        self.failure_reason: Optional[str] = payload.get("failure_reason")
        self.date_created: Optional[datetime] = deserialize.iso8601_datetime(
            payload.get("date_created")
        )
        self.date_updated: Optional[datetime] = deserialize.iso8601_datetime(
            payload.get("date_updated")
        )
        self.email: Optional[str] = payload.get("email")
        self.cc_emails: Optional[List[str]] = payload.get("cc_emails")
        self.url: Optional[str] = payload.get("url")
        self.contact_title: Optional[str] = payload.get("contact_title")
        self.contact_phone_number: Optional[str] = payload.get("contact_phone_number")
        self.bulk_hosting_request_sid: Optional[str] = payload.get(
            "bulk_hosting_request_sid"
        )
        self.next_step: Optional[str] = payload.get("next_step")

        self._solution = {
            "sid": sid or self.sid,
        }
        self._context: Optional[HostedNumberOrderContext] = None

    @property
    def _proxy(self) -> "HostedNumberOrderContext":
        """
        Generate an instance context for the instance, the context is capable of
        performing various actions. All instance actions are proxied to the context

        :returns: HostedNumberOrderContext for this HostedNumberOrderInstance
        """
        if self._context is None:
            self._context = HostedNumberOrderContext(
                self._version,
                sid=self._solution["sid"],
            )
        return self._context

    def delete(self) -> bool:
        """
        Deletes the HostedNumberOrderInstance


        :returns: True if delete succeeds, False otherwise
        """
        return self._proxy.delete()

    async def delete_async(self) -> bool:
        """
        Asynchronous coroutine that deletes the HostedNumberOrderInstance


        :returns: True if delete succeeds, False otherwise
        """
        return await self._proxy.delete_async()

    def fetch(self) -> "HostedNumberOrderInstance":
        """
        Fetch the HostedNumberOrderInstance


        :returns: The fetched HostedNumberOrderInstance
        """
        return self._proxy.fetch()

    async def fetch_async(self) -> "HostedNumberOrderInstance":
        """
        Asynchronous coroutine to fetch the HostedNumberOrderInstance


        :returns: The fetched HostedNumberOrderInstance
        """
        return await self._proxy.fetch_async()

    def __repr__(self) -> str:
        """
        Provide a friendly representation

        :returns: Machine friendly representation
        """
        context = " ".join("{}={}".format(k, v) for k, v in self._solution.items())
        return "<Twilio.Numbers.V2.HostedNumberOrderInstance {}>".format(context)


class HostedNumberOrderContext(InstanceContext):

    def __init__(self, version: Version, sid: str):
        """
        Initialize the HostedNumberOrderContext

        :param version: Version that contains the resource
        :param sid: A 34 character string that uniquely identifies this HostedNumberOrder.
        """
        super().__init__(version)

        # Path Solution
        self._solution = {
            "sid": sid,
        }
        self._uri = "/HostedNumber/Orders/{sid}".format(**self._solution)

    def delete(self) -> bool:
        """
        Deletes the HostedNumberOrderInstance


        :returns: True if delete succeeds, False otherwise
        """
        return self._version.delete(
            method="DELETE",
            uri=self._uri,
        )

    async def delete_async(self) -> bool:
        """
        Asynchronous coroutine that deletes the HostedNumberOrderInstance


        :returns: True if delete succeeds, False otherwise
        """
        return await self._version.delete_async(
            method="DELETE",
            uri=self._uri,
        )

    def fetch(self) -> HostedNumberOrderInstance:
        """
        Fetch the HostedNumberOrderInstance


        :returns: The fetched HostedNumberOrderInstance
        """

        payload = self._version.fetch(
            method="GET",
            uri=self._uri,
        )

        return HostedNumberOrderInstance(
            self._version,
            payload,
            sid=self._solution["sid"],
        )

    async def fetch_async(self) -> HostedNumberOrderInstance:
        """
        Asynchronous coroutine to fetch the HostedNumberOrderInstance


        :returns: The fetched HostedNumberOrderInstance
        """

        payload = await self._version.fetch_async(
            method="GET",
            uri=self._uri,
        )

        return HostedNumberOrderInstance(
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
        return "<Twilio.Numbers.V2.HostedNumberOrderContext {}>".format(context)


class HostedNumberOrderPage(Page):

    def get_instance(self, payload: Dict[str, Any]) -> HostedNumberOrderInstance:
        """
        Build an instance of HostedNumberOrderInstance

        :param payload: Payload response from the API
        """
        return HostedNumberOrderInstance(self._version, payload)

    def __repr__(self) -> str:
        """
        Provide a friendly representation

        :returns: Machine friendly representation
        """
        return "<Twilio.Numbers.V2.HostedNumberOrderPage>"


class HostedNumberOrderList(ListResource):

    def __init__(self, version: Version):
        """
        Initialize the HostedNumberOrderList

        :param version: Version that contains the resource

        """
        super().__init__(version)

        self._uri = "/HostedNumber/Orders"

    def create(
        self,
        phone_number: str,
        contact_phone_number: str,
        address_sid: str,
        email: str,
        account_sid: Union[str, object] = values.unset,
        friendly_name: Union[str, object] = values.unset,
        cc_emails: Union[List[str], object] = values.unset,
        sms_url: Union[str, object] = values.unset,
        sms_method: Union[str, object] = values.unset,
        sms_fallback_url: Union[str, object] = values.unset,
        sms_capability: Union[bool, object] = values.unset,
        sms_fallback_method: Union[str, object] = values.unset,
        status_callback_url: Union[str, object] = values.unset,
        status_callback_method: Union[str, object] = values.unset,
        sms_application_sid: Union[str, object] = values.unset,
        contact_title: Union[str, object] = values.unset,
    ) -> HostedNumberOrderInstance:
        """
        Create the HostedNumberOrderInstance

        :param phone_number: The number to host in [+E.164](https://en.wikipedia.org/wiki/E.164) format
        :param contact_phone_number: The contact phone number of the person authorized to sign the Authorization Document.
        :param address_sid: Optional. A 34 character string that uniquely identifies the Address resource that represents the address of the owner of this phone number.
        :param email: Optional. Email of the owner of this phone number that is being hosted.
        :param account_sid: This defaults to the AccountSid of the authorization the user is using. This can be provided to specify a subaccount to add the HostedNumberOrder to.
        :param friendly_name: A 128 character string that is a human readable text that describes this resource.
        :param cc_emails: Optional. A list of emails that the LOA document for this HostedNumberOrder will be carbon copied to.
        :param sms_url: The URL that Twilio should request when somebody sends an SMS to the phone number. This will be copied onto the IncomingPhoneNumber resource.
        :param sms_method: The HTTP method that should be used to request the SmsUrl. Must be either `GET` or `POST`.  This will be copied onto the IncomingPhoneNumber resource.
        :param sms_fallback_url: A URL that Twilio will request if an error occurs requesting or executing the TwiML defined by SmsUrl. This will be copied onto the IncomingPhoneNumber resource.
        :param sms_capability: Used to specify that the SMS capability will be hosted on Twilio's platform.
        :param sms_fallback_method: The HTTP method that should be used to request the SmsFallbackUrl. Must be either `GET` or `POST`. This will be copied onto the IncomingPhoneNumber resource.
        :param status_callback_url: Optional. The Status Callback URL attached to the IncomingPhoneNumber resource.
        :param status_callback_method: Optional. The Status Callback Method attached to the IncomingPhoneNumber resource.
        :param sms_application_sid: Optional. The 34 character sid of the application Twilio should use to handle SMS messages sent to this number. If a `SmsApplicationSid` is present, Twilio will ignore all of the SMS urls above and use those set on the application.
        :param contact_title: The title of the person authorized to sign the Authorization Document for this phone number.

        :returns: The created HostedNumberOrderInstance
        """

        data = values.of(
            {
                "PhoneNumber": phone_number,
                "ContactPhoneNumber": contact_phone_number,
                "AddressSid": address_sid,
                "Email": email,
                "AccountSid": account_sid,
                "FriendlyName": friendly_name,
                "CcEmails": serialize.map(cc_emails, lambda e: e),
                "SmsUrl": sms_url,
                "SmsMethod": sms_method,
                "SmsFallbackUrl": sms_fallback_url,
                "SmsCapability": sms_capability,
                "SmsFallbackMethod": sms_fallback_method,
                "StatusCallbackUrl": status_callback_url,
                "StatusCallbackMethod": status_callback_method,
                "SmsApplicationSid": sms_application_sid,
                "ContactTitle": contact_title,
            }
        )

        payload = self._version.create(
            method="POST",
            uri=self._uri,
            data=data,
        )

        return HostedNumberOrderInstance(self._version, payload)

    async def create_async(
        self,
        phone_number: str,
        contact_phone_number: str,
        address_sid: str,
        email: str,
        account_sid: Union[str, object] = values.unset,
        friendly_name: Union[str, object] = values.unset,
        cc_emails: Union[List[str], object] = values.unset,
        sms_url: Union[str, object] = values.unset,
        sms_method: Union[str, object] = values.unset,
        sms_fallback_url: Union[str, object] = values.unset,
        sms_capability: Union[bool, object] = values.unset,
        sms_fallback_method: Union[str, object] = values.unset,
        status_callback_url: Union[str, object] = values.unset,
        status_callback_method: Union[str, object] = values.unset,
        sms_application_sid: Union[str, object] = values.unset,
        contact_title: Union[str, object] = values.unset,
    ) -> HostedNumberOrderInstance:
        """
        Asynchronously create the HostedNumberOrderInstance

        :param phone_number: The number to host in [+E.164](https://en.wikipedia.org/wiki/E.164) format
        :param contact_phone_number: The contact phone number of the person authorized to sign the Authorization Document.
        :param address_sid: Optional. A 34 character string that uniquely identifies the Address resource that represents the address of the owner of this phone number.
        :param email: Optional. Email of the owner of this phone number that is being hosted.
        :param account_sid: This defaults to the AccountSid of the authorization the user is using. This can be provided to specify a subaccount to add the HostedNumberOrder to.
        :param friendly_name: A 128 character string that is a human readable text that describes this resource.
        :param cc_emails: Optional. A list of emails that the LOA document for this HostedNumberOrder will be carbon copied to.
        :param sms_url: The URL that Twilio should request when somebody sends an SMS to the phone number. This will be copied onto the IncomingPhoneNumber resource.
        :param sms_method: The HTTP method that should be used to request the SmsUrl. Must be either `GET` or `POST`.  This will be copied onto the IncomingPhoneNumber resource.
        :param sms_fallback_url: A URL that Twilio will request if an error occurs requesting or executing the TwiML defined by SmsUrl. This will be copied onto the IncomingPhoneNumber resource.
        :param sms_capability: Used to specify that the SMS capability will be hosted on Twilio's platform.
        :param sms_fallback_method: The HTTP method that should be used to request the SmsFallbackUrl. Must be either `GET` or `POST`. This will be copied onto the IncomingPhoneNumber resource.
        :param status_callback_url: Optional. The Status Callback URL attached to the IncomingPhoneNumber resource.
        :param status_callback_method: Optional. The Status Callback Method attached to the IncomingPhoneNumber resource.
        :param sms_application_sid: Optional. The 34 character sid of the application Twilio should use to handle SMS messages sent to this number. If a `SmsApplicationSid` is present, Twilio will ignore all of the SMS urls above and use those set on the application.
        :param contact_title: The title of the person authorized to sign the Authorization Document for this phone number.

        :returns: The created HostedNumberOrderInstance
        """

        data = values.of(
            {
                "PhoneNumber": phone_number,
                "ContactPhoneNumber": contact_phone_number,
                "AddressSid": address_sid,
                "Email": email,
                "AccountSid": account_sid,
                "FriendlyName": friendly_name,
                "CcEmails": serialize.map(cc_emails, lambda e: e),
                "SmsUrl": sms_url,
                "SmsMethod": sms_method,
                "SmsFallbackUrl": sms_fallback_url,
                "SmsCapability": sms_capability,
                "SmsFallbackMethod": sms_fallback_method,
                "StatusCallbackUrl": status_callback_url,
                "StatusCallbackMethod": status_callback_method,
                "SmsApplicationSid": sms_application_sid,
                "ContactTitle": contact_title,
            }
        )

        payload = await self._version.create_async(
            method="POST",
            uri=self._uri,
            data=data,
        )

        return HostedNumberOrderInstance(self._version, payload)

    def stream(
        self,
        status: Union["HostedNumberOrderInstance.Status", object] = values.unset,
        sms_capability: Union[bool, object] = values.unset,
        phone_number: Union[str, object] = values.unset,
        incoming_phone_number_sid: Union[str, object] = values.unset,
        friendly_name: Union[str, object] = values.unset,
        limit: Optional[int] = None,
        page_size: Optional[int] = None,
    ) -> Iterator[HostedNumberOrderInstance]:
        """
        Streams HostedNumberOrderInstance records from the API as a generator stream.
        This operation lazily loads records as efficiently as possible until the limit
        is reached.
        The results are returned as a generator, so this operation is memory efficient.

        :param &quot;HostedNumberOrderInstance.Status&quot; status: The Status of this HostedNumberOrder. One of `received`, `pending-verification`, `verified`, `pending-loa`, `carrier-processing`, `testing`, `completed`, `failed`, or `action-required`.
        :param bool sms_capability: Whether the SMS capability will be hosted on our platform. Can be `true` of `false`.
        :param str phone_number: An E164 formatted phone number hosted by this HostedNumberOrder.
        :param str incoming_phone_number_sid: A 34 character string that uniquely identifies the IncomingPhoneNumber resource created by this HostedNumberOrder.
        :param str friendly_name: A human readable description of this resource, up to 128 characters.
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
            status=status,
            sms_capability=sms_capability,
            phone_number=phone_number,
            incoming_phone_number_sid=incoming_phone_number_sid,
            friendly_name=friendly_name,
            page_size=limits["page_size"],
        )

        return self._version.stream(page, limits["limit"])

    async def stream_async(
        self,
        status: Union["HostedNumberOrderInstance.Status", object] = values.unset,
        sms_capability: Union[bool, object] = values.unset,
        phone_number: Union[str, object] = values.unset,
        incoming_phone_number_sid: Union[str, object] = values.unset,
        friendly_name: Union[str, object] = values.unset,
        limit: Optional[int] = None,
        page_size: Optional[int] = None,
    ) -> AsyncIterator[HostedNumberOrderInstance]:
        """
        Asynchronously streams HostedNumberOrderInstance records from the API as a generator stream.
        This operation lazily loads records as efficiently as possible until the limit
        is reached.
        The results are returned as a generator, so this operation is memory efficient.

        :param &quot;HostedNumberOrderInstance.Status&quot; status: The Status of this HostedNumberOrder. One of `received`, `pending-verification`, `verified`, `pending-loa`, `carrier-processing`, `testing`, `completed`, `failed`, or `action-required`.
        :param bool sms_capability: Whether the SMS capability will be hosted on our platform. Can be `true` of `false`.
        :param str phone_number: An E164 formatted phone number hosted by this HostedNumberOrder.
        :param str incoming_phone_number_sid: A 34 character string that uniquely identifies the IncomingPhoneNumber resource created by this HostedNumberOrder.
        :param str friendly_name: A human readable description of this resource, up to 128 characters.
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
            status=status,
            sms_capability=sms_capability,
            phone_number=phone_number,
            incoming_phone_number_sid=incoming_phone_number_sid,
            friendly_name=friendly_name,
            page_size=limits["page_size"],
        )

        return self._version.stream_async(page, limits["limit"])

    def list(
        self,
        status: Union["HostedNumberOrderInstance.Status", object] = values.unset,
        sms_capability: Union[bool, object] = values.unset,
        phone_number: Union[str, object] = values.unset,
        incoming_phone_number_sid: Union[str, object] = values.unset,
        friendly_name: Union[str, object] = values.unset,
        limit: Optional[int] = None,
        page_size: Optional[int] = None,
    ) -> List[HostedNumberOrderInstance]:
        """
        Lists HostedNumberOrderInstance records from the API as a list.
        Unlike stream(), this operation is eager and will load `limit` records into
        memory before returning.

        :param &quot;HostedNumberOrderInstance.Status&quot; status: The Status of this HostedNumberOrder. One of `received`, `pending-verification`, `verified`, `pending-loa`, `carrier-processing`, `testing`, `completed`, `failed`, or `action-required`.
        :param bool sms_capability: Whether the SMS capability will be hosted on our platform. Can be `true` of `false`.
        :param str phone_number: An E164 formatted phone number hosted by this HostedNumberOrder.
        :param str incoming_phone_number_sid: A 34 character string that uniquely identifies the IncomingPhoneNumber resource created by this HostedNumberOrder.
        :param str friendly_name: A human readable description of this resource, up to 128 characters.
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
                status=status,
                sms_capability=sms_capability,
                phone_number=phone_number,
                incoming_phone_number_sid=incoming_phone_number_sid,
                friendly_name=friendly_name,
                limit=limit,
                page_size=page_size,
            )
        )

    async def list_async(
        self,
        status: Union["HostedNumberOrderInstance.Status", object] = values.unset,
        sms_capability: Union[bool, object] = values.unset,
        phone_number: Union[str, object] = values.unset,
        incoming_phone_number_sid: Union[str, object] = values.unset,
        friendly_name: Union[str, object] = values.unset,
        limit: Optional[int] = None,
        page_size: Optional[int] = None,
    ) -> List[HostedNumberOrderInstance]:
        """
        Asynchronously lists HostedNumberOrderInstance records from the API as a list.
        Unlike stream(), this operation is eager and will load `limit` records into
        memory before returning.

        :param &quot;HostedNumberOrderInstance.Status&quot; status: The Status of this HostedNumberOrder. One of `received`, `pending-verification`, `verified`, `pending-loa`, `carrier-processing`, `testing`, `completed`, `failed`, or `action-required`.
        :param bool sms_capability: Whether the SMS capability will be hosted on our platform. Can be `true` of `false`.
        :param str phone_number: An E164 formatted phone number hosted by this HostedNumberOrder.
        :param str incoming_phone_number_sid: A 34 character string that uniquely identifies the IncomingPhoneNumber resource created by this HostedNumberOrder.
        :param str friendly_name: A human readable description of this resource, up to 128 characters.
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
                status=status,
                sms_capability=sms_capability,
                phone_number=phone_number,
                incoming_phone_number_sid=incoming_phone_number_sid,
                friendly_name=friendly_name,
                limit=limit,
                page_size=page_size,
            )
        ]

    def page(
        self,
        status: Union["HostedNumberOrderInstance.Status", object] = values.unset,
        sms_capability: Union[bool, object] = values.unset,
        phone_number: Union[str, object] = values.unset,
        incoming_phone_number_sid: Union[str, object] = values.unset,
        friendly_name: Union[str, object] = values.unset,
        page_token: Union[str, object] = values.unset,
        page_number: Union[int, object] = values.unset,
        page_size: Union[int, object] = values.unset,
    ) -> HostedNumberOrderPage:
        """
        Retrieve a single page of HostedNumberOrderInstance records from the API.
        Request is executed immediately

        :param status: The Status of this HostedNumberOrder. One of `received`, `pending-verification`, `verified`, `pending-loa`, `carrier-processing`, `testing`, `completed`, `failed`, or `action-required`.
        :param sms_capability: Whether the SMS capability will be hosted on our platform. Can be `true` of `false`.
        :param phone_number: An E164 formatted phone number hosted by this HostedNumberOrder.
        :param incoming_phone_number_sid: A 34 character string that uniquely identifies the IncomingPhoneNumber resource created by this HostedNumberOrder.
        :param friendly_name: A human readable description of this resource, up to 128 characters.
        :param page_token: PageToken provided by the API
        :param page_number: Page Number, this value is simply for client state
        :param page_size: Number of records to return, defaults to 50

        :returns: Page of HostedNumberOrderInstance
        """
        data = values.of(
            {
                "Status": status,
                "SmsCapability": sms_capability,
                "PhoneNumber": phone_number,
                "IncomingPhoneNumberSid": incoming_phone_number_sid,
                "FriendlyName": friendly_name,
                "PageToken": page_token,
                "Page": page_number,
                "PageSize": page_size,
            }
        )

        response = self._version.page(method="GET", uri=self._uri, params=data)
        return HostedNumberOrderPage(self._version, response)

    async def page_async(
        self,
        status: Union["HostedNumberOrderInstance.Status", object] = values.unset,
        sms_capability: Union[bool, object] = values.unset,
        phone_number: Union[str, object] = values.unset,
        incoming_phone_number_sid: Union[str, object] = values.unset,
        friendly_name: Union[str, object] = values.unset,
        page_token: Union[str, object] = values.unset,
        page_number: Union[int, object] = values.unset,
        page_size: Union[int, object] = values.unset,
    ) -> HostedNumberOrderPage:
        """
        Asynchronously retrieve a single page of HostedNumberOrderInstance records from the API.
        Request is executed immediately

        :param status: The Status of this HostedNumberOrder. One of `received`, `pending-verification`, `verified`, `pending-loa`, `carrier-processing`, `testing`, `completed`, `failed`, or `action-required`.
        :param sms_capability: Whether the SMS capability will be hosted on our platform. Can be `true` of `false`.
        :param phone_number: An E164 formatted phone number hosted by this HostedNumberOrder.
        :param incoming_phone_number_sid: A 34 character string that uniquely identifies the IncomingPhoneNumber resource created by this HostedNumberOrder.
        :param friendly_name: A human readable description of this resource, up to 128 characters.
        :param page_token: PageToken provided by the API
        :param page_number: Page Number, this value is simply for client state
        :param page_size: Number of records to return, defaults to 50

        :returns: Page of HostedNumberOrderInstance
        """
        data = values.of(
            {
                "Status": status,
                "SmsCapability": sms_capability,
                "PhoneNumber": phone_number,
                "IncomingPhoneNumberSid": incoming_phone_number_sid,
                "FriendlyName": friendly_name,
                "PageToken": page_token,
                "Page": page_number,
                "PageSize": page_size,
            }
        )

        response = await self._version.page_async(
            method="GET", uri=self._uri, params=data
        )
        return HostedNumberOrderPage(self._version, response)

    def get_page(self, target_url: str) -> HostedNumberOrderPage:
        """
        Retrieve a specific page of HostedNumberOrderInstance records from the API.
        Request is executed immediately

        :param target_url: API-generated URL for the requested results page

        :returns: Page of HostedNumberOrderInstance
        """
        response = self._version.domain.twilio.request("GET", target_url)
        return HostedNumberOrderPage(self._version, response)

    async def get_page_async(self, target_url: str) -> HostedNumberOrderPage:
        """
        Asynchronously retrieve a specific page of HostedNumberOrderInstance records from the API.
        Request is executed immediately

        :param target_url: API-generated URL for the requested results page

        :returns: Page of HostedNumberOrderInstance
        """
        response = await self._version.domain.twilio.request_async("GET", target_url)
        return HostedNumberOrderPage(self._version, response)

    def get(self, sid: str) -> HostedNumberOrderContext:
        """
        Constructs a HostedNumberOrderContext

        :param sid: A 34 character string that uniquely identifies this HostedNumberOrder.
        """
        return HostedNumberOrderContext(self._version, sid=sid)

    def __call__(self, sid: str) -> HostedNumberOrderContext:
        """
        Constructs a HostedNumberOrderContext

        :param sid: A 34 character string that uniquely identifies this HostedNumberOrder.
        """
        return HostedNumberOrderContext(self._version, sid=sid)

    def __repr__(self) -> str:
        """
        Provide a friendly representation

        :returns: Machine friendly representation
        """
        return "<Twilio.Numbers.V2.HostedNumberOrderList>"
