"""
    This code was generated by
   ___ _ _ _ _ _    _ ____    ____ ____ _    ____ ____ _  _ ____ ____ ____ ___ __   __
    |  | | | | |    | |  | __ |  | |__| | __ | __ |___ |\ | |___ |__/ |__|  | |  | |__/
    |  |_|_| | |___ | |__|    |__| |  | |    |__] |___ | \| |___ |  \ |  |  | |__| |  \

    Twilio - Notify
    This is the public Twilio REST API.

    NOTE: This class is auto generated by OpenAPI Generator.
    https://openapi-generator.tech
    Do not edit the class manually.
"""


from twilio.base import deserialize
from twilio.base import serialize
from twilio.base import values
from twilio.base.instance_context import InstanceContext
from twilio.base.instance_resource import InstanceResource
from twilio.base.list_resource import ListResource
from twilio.base.version import Version
from twilio.base.page import Page


class BindingList(ListResource):

    def __init__(self, version: Version, service_sid: str):
        """
        Initialize the BindingList

        :param Version version: Version that contains the resource
        :param service_sid: The SID of the [Service](https://www.twilio.com/docs/notify/api/service-resource) to read the resource from.
        
        :returns: twilio.rest.notify.v1.service.binding.BindingList
        :rtype: twilio.rest.notify.v1.service.binding.BindingList
        """
        super().__init__(version)

        # Path Solution
        self._solution = { 'service_sid': service_sid,  }
        self._uri = '/Services/{service_sid}/Bindings'.format(**self._solution)
        
        
    
    
    
    def create(self, identity, binding_type, address, tag=values.unset, notification_protocol_version=values.unset, credential_sid=values.unset, endpoint=values.unset):
        """
        Create the BindingInstance

        :param str identity: The `identity` value that uniquely identifies the new resource's [User](https://www.twilio.com/docs/chat/rest/user-resource) within the [Service](https://www.twilio.com/docs/notify/api/service-resource). Up to 20 Bindings can be created for the same Identity in a given Service.
        :param BindingBindingType binding_type: 
        :param str address: The channel-specific address. For APNS, the device token. For FCM and GCM, the registration token. For SMS, a phone number in E.164 format. For Facebook Messenger, the Messenger ID of the user or a phone number in E.164 format.
        :param list[str] tag: A tag that can be used to select the Bindings to notify. Repeat this parameter to specify more than one tag, up to a total of 20 tags.
        :param str notification_protocol_version: The protocol version to use to send the notification. This defaults to the value of `default_xxxx_notification_protocol_version` for the protocol in the [Service](https://www.twilio.com/docs/notify/api/service-resource). The current version is `\\\"3\\\"` for `apn`, `fcm`, and `gcm` type Bindings. The parameter is not applicable to `sms` and `facebook-messenger` type Bindings as the data format is fixed.
        :param str credential_sid: The SID of the [Credential](https://www.twilio.com/docs/notify/api/credential-resource) resource to be used to send notifications to this Binding. If present, this overrides the Credential specified in the Service resource. Applies to only `apn`, `fcm`, and `gcm` type Bindings.
        :param str endpoint: Deprecated.
        
        :returns: The created BindingInstance
        :rtype: twilio.rest.notify.v1.service.binding.BindingInstance
        """
        data = values.of({ 
            'Identity': identity,
            'BindingType': binding_type,
            'Address': address,
            'Tag': serialize.map(tag, lambda e: e),
            'NotificationProtocolVersion': notification_protocol_version,
            'CredentialSid': credential_sid,
            'Endpoint': endpoint,
        })
        
        payload = self._version.create(method='POST', uri=self._uri, data=data,)

        return BindingInstance(self._version, payload, service_sid=self._solution['service_sid'])
    
    
    def stream(self, start_date=values.unset, end_date=values.unset, identity=values.unset, tag=values.unset, limit=None, page_size=None):
        """
        Streams BindingInstance records from the API as a generator stream.
        This operation lazily loads records as efficiently as possible until the limit
        is reached.
        The results are returned as a generator, so this operation is memory efficient.
        
        :param date start_date: Only include usage that has occurred on or after this date. Specify the date in GMT and format as `YYYY-MM-DD`.
        :param date end_date: Only include usage that occurred on or before this date. Specify the date in GMT and format as `YYYY-MM-DD`.
        :param list[str] identity: The [User](https://www.twilio.com/docs/chat/rest/user-resource)'s `identity` value of the resources to read.
        :param list[str] tag: Only list Bindings that have all of the specified Tags. The following implicit tags are available: `all`, `apn`, `fcm`, `gcm`, `sms`, `facebook-messenger`. Up to 5 tags are allowed.
        :param int limit: Upper limit for the number of records to return. stream()
                          guarantees to never return more than limit.  Default is no limit
        :param int page_size: Number of records to fetch per request, when not set will use
                              the default value of 50 records.  If no page_size is defined
                              but a limit is defined, stream() will attempt to read the
                              limit with the most efficient page size, i.e. min(limit, 1000)

        :returns: Generator that will yield up to limit results
        :rtype: list[twilio.rest.notify.v1.service.binding.BindingInstance]
        """
        limits = self._version.read_limits(limit, page_size)
        page = self.page(
            start_date=start_date,
            end_date=end_date,
            identity=identity,
            tag=tag,
            page_size=limits['page_size']
        )

        return self._version.stream(page, limits['limit'])

    def list(self, start_date=values.unset, end_date=values.unset, identity=values.unset, tag=values.unset, limit=None, page_size=None):
        """
        Lists BindingInstance records from the API as a list.
        Unlike stream(), this operation is eager and will load `limit` records into
        memory before returning.
        
        :param date start_date: Only include usage that has occurred on or after this date. Specify the date in GMT and format as `YYYY-MM-DD`.
        :param date end_date: Only include usage that occurred on or before this date. Specify the date in GMT and format as `YYYY-MM-DD`.
        :param list[str] identity: The [User](https://www.twilio.com/docs/chat/rest/user-resource)'s `identity` value of the resources to read.
        :param list[str] tag: Only list Bindings that have all of the specified Tags. The following implicit tags are available: `all`, `apn`, `fcm`, `gcm`, `sms`, `facebook-messenger`. Up to 5 tags are allowed.
        :param int limit: Upper limit for the number of records to return. list() guarantees
                          never to return more than limit.  Default is no limit
        :param int page_size: Number of records to fetch per request, when not set will use
                              the default value of 50 records.  If no page_size is defined
                              but a limit is defined, list() will attempt to read the limit
                              with the most efficient page size, i.e. min(limit, 1000)

        :returns: Generator that will yield up to limit results
        :rtype: list[twilio.rest.notify.v1.service.binding.BindingInstance]
        """
        return list(self.stream(
            start_date=start_date,
            end_date=end_date,
            identity=identity,
            tag=tag,
            limit=limit,
            page_size=page_size,
        ))

    def page(self, start_date=values.unset, end_date=values.unset, identity=values.unset, tag=values.unset, page_token=values.unset, page_number=values.unset, page_size=values.unset):
        """
        Retrieve a single page of BindingInstance records from the API.
        Request is executed immediately
        
        :param date start_date: Only include usage that has occurred on or after this date. Specify the date in GMT and format as `YYYY-MM-DD`.
        :param date end_date: Only include usage that occurred on or before this date. Specify the date in GMT and format as `YYYY-MM-DD`.
        :param list[str] identity: The [User](https://www.twilio.com/docs/chat/rest/user-resource)'s `identity` value of the resources to read.
        :param list[str] tag: Only list Bindings that have all of the specified Tags. The following implicit tags are available: `all`, `apn`, `fcm`, `gcm`, `sms`, `facebook-messenger`. Up to 5 tags are allowed.
        :param str page_token: PageToken provided by the API
        :param int page_number: Page Number, this value is simply for client state
        :param int page_size: Number of records to return, defaults to 50

        :returns: Page of BindingInstance
        :rtype: twilio.rest.notify.v1.service.binding.BindingPage
        """
        data = values.of({ 
            'StartDate': serialize.iso8601_date(start_date),
            'EndDate': serialize.iso8601_date(end_date),
            'Identity': serialize.map(identity),
            'Tag': serialize.map(tag),
            'PageToken': page_token,
            'Page': page_number,
            'PageSize': page_size,
        })

        response = self._version.page(method='GET', uri=self._uri, params=data)
        return BindingPage(self._version, response, self._solution)

    def get_page(self, target_url):
        """
        Retrieve a specific page of BindingInstance records from the API.
        Request is executed immediately

        :param str target_url: API-generated URL for the requested results page

        :returns: Page of BindingInstance
        :rtype: twilio.rest.notify.v1.service.binding.BindingPage
        """
        response = self._version.domain.twilio.request(
            'GET',
            target_url
        )
        return BindingPage(self._version, response, self._solution)


    def get(self, sid):
        """
        Constructs a BindingContext
        
        :param sid: The Twilio-provided string that uniquely identifies the Binding resource to fetch.
        
        :returns: twilio.rest.notify.v1.service.binding.BindingContext
        :rtype: twilio.rest.notify.v1.service.binding.BindingContext
        """
        return BindingContext(self._version, service_sid=self._solution['service_sid'], sid=sid)

    def __call__(self, sid):
        """
        Constructs a BindingContext
        
        :param sid: The Twilio-provided string that uniquely identifies the Binding resource to fetch.
        
        :returns: twilio.rest.notify.v1.service.binding.BindingContext
        :rtype: twilio.rest.notify.v1.service.binding.BindingContext
        """
        return BindingContext(self._version, service_sid=self._solution['service_sid'], sid=sid)

    def __repr__(self):
        """
        Provide a friendly representation
        :returns: Machine friendly representation
        :rtype: str
        """
        return '<Twilio.Notify.V1.BindingList>'








class BindingPage(Page):

    def __init__(self, version, response, solution):
        """
        Initialize the BindingPage

        :param Version version: Version that contains the resource
        :param Response response: Response from the API

        :returns: twilio.rest.notify.v1.service.binding.BindingPage
        :rtype: twilio.rest.notify.v1.service.binding.BindingPage
        """
        super().__init__(version, response)

        # Path solution
        self._solution = solution

    def get_instance(self, payload):
        """
        Build an instance of BindingInstance

        :param dict payload: Payload response from the API

        :returns: twilio.rest.notify.v1.service.binding.BindingInstance
        :rtype: twilio.rest.notify.v1.service.binding.BindingInstance
        """
        return BindingInstance(self._version, payload, service_sid=self._solution['service_sid'])

    def __repr__(self):
        """
        Provide a friendly representation

        :returns: Machine friendly representation
        :rtype: str
        """
        return '<Twilio.Notify.V1.BindingPage>'




class BindingContext(InstanceContext):

    def __init__(self, version: Version, service_sid: str, sid: str):
        """
        Initialize the BindingContext

        :param Version version: Version that contains the resource
        :param service_sid: The SID of the [Service](https://www.twilio.com/docs/notify/api/service-resource) to fetch the resource from.:param sid: The Twilio-provided string that uniquely identifies the Binding resource to fetch.

        :returns: twilio.rest.notify.v1.service.binding.BindingContext
        :rtype: twilio.rest.notify.v1.service.binding.BindingContext
        """
        super().__init__(version)

        # Path Solution
        self._solution = { 
            'service_sid': service_sid,
            'sid': sid,
        }
        self._uri = '/Services/{service_sid}/Bindings/{sid}'.format(**self._solution)
        
    
    def delete(self):
        """
        Deletes the BindingInstance

        
        :returns: True if delete succeeds, False otherwise
        :rtype: bool
        """
        return self._version.delete(method='DELETE', uri=self._uri,)
        
    def fetch(self):
        """
        Fetch the BindingInstance
        

        :returns: The fetched BindingInstance
        :rtype: twilio.rest.notify.v1.service.binding.BindingInstance
        """
        
        payload = self._version.fetch(method='GET', uri=self._uri, )

        return BindingInstance(
            self._version,
            payload,
            service_sid=self._solution['service_sid'],
            sid=self._solution['sid'],
            
        )
        
    
    def __repr__(self):
        """
        Provide a friendly representation
        :returns: Machine friendly representation
        :rtype: str
        """
        context = ' '.join('{}={}'.format(k, v) for k, v in self._solution.items())
        return '<Twilio.Notify.V1.BindingContext {}>'.format(context)

class BindingInstance(InstanceResource):

    def __init__(self, version, payload, service_sid: str, sid: str=None):
        """
        Initialize the BindingInstance
        :returns: twilio.rest.notify.v1.service.binding.BindingInstance
        :rtype: twilio.rest.notify.v1.service.binding.BindingInstance
        """
        super().__init__(version)

        self._properties = { 
            'sid': payload.get('sid'),
            'account_sid': payload.get('account_sid'),
            'service_sid': payload.get('service_sid'),
            'credential_sid': payload.get('credential_sid'),
            'date_created': deserialize.iso8601_datetime(payload.get('date_created')),
            'date_updated': deserialize.iso8601_datetime(payload.get('date_updated')),
            'notification_protocol_version': payload.get('notification_protocol_version'),
            'endpoint': payload.get('endpoint'),
            'identity': payload.get('identity'),
            'binding_type': payload.get('binding_type'),
            'address': payload.get('address'),
            'tags': payload.get('tags'),
            'url': payload.get('url'),
            'links': payload.get('links'),
        }

        self._context = None
        self._solution = { 'service_sid': service_sid, 'sid': sid or self._properties['sid'],  }
    
    @property
    def _proxy(self):
        """
        Generate an instance context for the instance, the context is capable of
        performing various actions. All instance actions are proxied to the context

        :returns: BindingContext for this BindingInstance
        :rtype: twilio.rest.notify.v1.service.binding.BindingContext
        """
        if self._context is None:
            self._context = BindingContext(self._version, service_sid=self._solution['service_sid'], sid=self._solution['sid'],)
        return self._context
    
    @property
    def sid(self):
        """
        :returns: The unique string that we created to identify the Binding resource.
        :rtype: str
        """
        return self._properties['sid']
    
    @property
    def account_sid(self):
        """
        :returns: The SID of the [Account](https://www.twilio.com/docs/iam/api/account) that created the Binding resource.
        :rtype: str
        """
        return self._properties['account_sid']
    
    @property
    def service_sid(self):
        """
        :returns: The SID of the [Service](https://www.twilio.com/docs/notify/api/service-resource) the resource is associated with.
        :rtype: str
        """
        return self._properties['service_sid']
    
    @property
    def credential_sid(self):
        """
        :returns: The SID of the [Credential](https://www.twilio.com/docs/notify/api/credential-resource) resource to be used to send notifications to this Binding. If present, this overrides the Credential specified in the Service resource. Applicable only to `apn`, `fcm`, and `gcm` type Bindings.
        :rtype: str
        """
        return self._properties['credential_sid']
    
    @property
    def date_created(self):
        """
        :returns: The date and time in GMT when the resource was created specified in [RFC 2822](https://www.ietf.org/rfc/rfc2822.txt) format.
        :rtype: datetime
        """
        return self._properties['date_created']
    
    @property
    def date_updated(self):
        """
        :returns: The date and time in GMT when the resource was last updated specified in [RFC 2822](https://www.ietf.org/rfc/rfc2822.txt) format.
        :rtype: datetime
        """
        return self._properties['date_updated']
    
    @property
    def notification_protocol_version(self):
        """
        :returns: The protocol version to use to send the notification. This defaults to the value of `default_xxxx_notification_protocol_version` in the [Service](https://www.twilio.com/docs/notify/api/service-resource) for the protocol. The current version is `\"3\"` for `apn`, `fcm`, and `gcm` type Bindings. The parameter is not applicable to `sms` and `facebook-messenger` type Bindings as the data format is fixed.
        :rtype: str
        """
        return self._properties['notification_protocol_version']
    
    @property
    def endpoint(self):
        """
        :returns: Deprecated.
        :rtype: str
        """
        return self._properties['endpoint']
    
    @property
    def identity(self):
        """
        :returns: The `identity` value that uniquely identifies the resource's [User](https://www.twilio.com/docs/chat/rest/user-resource) within the [Service](https://www.twilio.com/docs/notify/api/service-resource). Up to 20 Bindings can be created for the same Identity in a given Service.
        :rtype: str
        """
        return self._properties['identity']
    
    @property
    def binding_type(self):
        """
        :returns: The transport technology to use for the Binding. Can be: `apn`, `fcm`, `gcm`, `sms`, or `facebook-messenger`.
        :rtype: str
        """
        return self._properties['binding_type']
    
    @property
    def address(self):
        """
        :returns: The channel-specific address. For APNS, the device token. For FCM and GCM, the registration token. For SMS, a phone number in E.164 format. For Facebook Messenger, the Messenger ID of the user or a phone number in E.164 format.
        :rtype: str
        """
        return self._properties['address']
    
    @property
    def tags(self):
        """
        :returns: The list of tags associated with this Binding. Tags can be used to select the Bindings to use when sending a notification. Maximum 20 tags are allowed.
        :rtype: list[str]
        """
        return self._properties['tags']
    
    @property
    def url(self):
        """
        :returns: The absolute URL of the Binding resource.
        :rtype: str
        """
        return self._properties['url']
    
    @property
    def links(self):
        """
        :returns: The URLs of related resources.
        :rtype: dict
        """
        return self._properties['links']
    
    def delete(self):
        """
        Deletes the BindingInstance
        

        :returns: True if delete succeeds, False otherwise
        :rtype: bool
        """
        return self._proxy.delete()
    
    def fetch(self):
        """
        Fetch the BindingInstance
        

        :returns: The fetched BindingInstance
        :rtype: twilio.rest.notify.v1.service.binding.BindingInstance
        """
        return self._proxy.fetch()
    
    def __repr__(self):
        """
        Provide a friendly representation
        :returns: Machine friendly representation
        :rtype: str
        """
        context = ' '.join('{}={}'.format(k, v) for k, v in self._solution.items())
        return '<Twilio.Notify.V1.BindingInstance {}>'.format(context)


