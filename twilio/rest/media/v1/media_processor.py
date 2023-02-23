"""
    This code was generated by
   ___ _ _ _ _ _    _ ____    ____ ____ _    ____ ____ _  _ ____ ____ ____ ___ __   __
    |  | | | | |    | |  | __ |  | |__| | __ | __ |___ |\ | |___ |__/ |__|  | |  | |__/
    |  |_|_| | |___ | |__|    |__| |  | |    |__] |___ | \| |___ |  \ |  |  | |__| |  \

    Twilio - Media
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


class MediaProcessorList(ListResource):

    def __init__(self, version: Version):
        """
        Initialize the MediaProcessorList

        :param Version version: Version that contains the resource
        
        :returns: twilio.rest.media.v1.media_processor.MediaProcessorList
        :rtype: twilio.rest.media.v1.media_processor.MediaProcessorList
        """
        super().__init__(version)

        # Path Solution
        self._solution = {  }
        self._uri = '/MediaProcessors'.format(**self._solution)
        
        
    
    
    
    def create(self, extension, extension_context, extension_environment=values.unset, status_callback=values.unset, status_callback_method=values.unset, max_duration=values.unset):
        """
        Create the MediaProcessorInstance

        :param str extension: The [Media Extension](/docs/live/api/media-extensions-overview) name or URL. Ex: `video-composer-v2`
        :param str extension_context: The context of the Media Extension, represented as a JSON dictionary. See the documentation for the specific [Media Extension](/docs/live/api/media-extensions-overview) you are using for more information about the context to send.
        :param object extension_environment: User-defined environment variables for the Media Extension, represented as a JSON dictionary of key/value strings. See the documentation for the specific [Media Extension](/docs/live/api/media-extensions-overview) you are using for more information about whether you need to provide this.
        :param str status_callback: The URL to which Twilio will send asynchronous webhook requests for every MediaProcessor event. See [Status Callbacks](/docs/live/status-callbacks) for details.
        :param str status_callback_method: The HTTP method Twilio should use to call the `status_callback` URL. Can be `POST` or `GET` and the default is `POST`.
        :param int max_duration: The maximum time, in seconds, that the MediaProcessor can run before automatically ends. The default value is 300 seconds, and the maximum value is 90000 seconds. Once this maximum duration is reached, Twilio will end the MediaProcessor, regardless of whether media is still streaming.
        
        :returns: The created MediaProcessorInstance
        :rtype: twilio.rest.media.v1.media_processor.MediaProcessorInstance
        """
        data = values.of({ 
            'Extension': extension,
            'ExtensionContext': extension_context,
            'ExtensionEnvironment': serialize.object(extension_environment),
            'StatusCallback': status_callback,
            'StatusCallbackMethod': status_callback_method,
            'MaxDuration': max_duration,
        })
        
        payload = self._version.create(method='POST', uri=self._uri, data=data,)

        return MediaProcessorInstance(self._version, payload)
    
    
    def stream(self, order=values.unset, status=values.unset, limit=None, page_size=None):
        """
        Streams MediaProcessorInstance records from the API as a generator stream.
        This operation lazily loads records as efficiently as possible until the limit
        is reached.
        The results are returned as a generator, so this operation is memory efficient.
        
        :param MediaProcessorOrder order: The sort order of the list by `date_created`. Can be: `asc` (ascending) or `desc` (descending) with `desc` as the default.
        :param MediaProcessorStatus status: Status to filter by, with possible values `started`, `ended` or `failed`.
        :param int limit: Upper limit for the number of records to return. stream()
                          guarantees to never return more than limit.  Default is no limit
        :param int page_size: Number of records to fetch per request, when not set will use
                              the default value of 50 records.  If no page_size is defined
                              but a limit is defined, stream() will attempt to read the
                              limit with the most efficient page size, i.e. min(limit, 1000)

        :returns: Generator that will yield up to limit results
        :rtype: list[twilio.rest.media.v1.media_processor.MediaProcessorInstance]
        """
        limits = self._version.read_limits(limit, page_size)
        page = self.page(
            order=order,
            status=status,
            page_size=limits['page_size']
        )

        return self._version.stream(page, limits['limit'])

    def list(self, order=values.unset, status=values.unset, limit=None, page_size=None):
        """
        Lists MediaProcessorInstance records from the API as a list.
        Unlike stream(), this operation is eager and will load `limit` records into
        memory before returning.
        
        :param MediaProcessorOrder order: The sort order of the list by `date_created`. Can be: `asc` (ascending) or `desc` (descending) with `desc` as the default.
        :param MediaProcessorStatus status: Status to filter by, with possible values `started`, `ended` or `failed`.
        :param int limit: Upper limit for the number of records to return. list() guarantees
                          never to return more than limit.  Default is no limit
        :param int page_size: Number of records to fetch per request, when not set will use
                              the default value of 50 records.  If no page_size is defined
                              but a limit is defined, list() will attempt to read the limit
                              with the most efficient page size, i.e. min(limit, 1000)

        :returns: Generator that will yield up to limit results
        :rtype: list[twilio.rest.media.v1.media_processor.MediaProcessorInstance]
        """
        return list(self.stream(
            order=order,
            status=status,
            limit=limit,
            page_size=page_size,
        ))

    def page(self, order=values.unset, status=values.unset, page_token=values.unset, page_number=values.unset, page_size=values.unset):
        """
        Retrieve a single page of MediaProcessorInstance records from the API.
        Request is executed immediately
        
        :param MediaProcessorOrder order: The sort order of the list by `date_created`. Can be: `asc` (ascending) or `desc` (descending) with `desc` as the default.
        :param MediaProcessorStatus status: Status to filter by, with possible values `started`, `ended` or `failed`.
        :param str page_token: PageToken provided by the API
        :param int page_number: Page Number, this value is simply for client state
        :param int page_size: Number of records to return, defaults to 50

        :returns: Page of MediaProcessorInstance
        :rtype: twilio.rest.media.v1.media_processor.MediaProcessorPage
        """
        data = values.of({ 
            'Order': order,
            'Status': status,
            'PageToken': page_token,
            'Page': page_number,
            'PageSize': page_size,
        })

        response = self._version.page(method='GET', uri=self._uri, params=data)
        return MediaProcessorPage(self._version, response, self._solution)

    def get_page(self, target_url):
        """
        Retrieve a specific page of MediaProcessorInstance records from the API.
        Request is executed immediately

        :param str target_url: API-generated URL for the requested results page

        :returns: Page of MediaProcessorInstance
        :rtype: twilio.rest.media.v1.media_processor.MediaProcessorPage
        """
        response = self._version.domain.twilio.request(
            'GET',
            target_url
        )
        return MediaProcessorPage(self._version, response, self._solution)


    def get(self, sid):
        """
        Constructs a MediaProcessorContext
        
        :param sid: The SID of the MediaProcessor resource to update.
        
        :returns: twilio.rest.media.v1.media_processor.MediaProcessorContext
        :rtype: twilio.rest.media.v1.media_processor.MediaProcessorContext
        """
        return MediaProcessorContext(self._version, sid=sid)

    def __call__(self, sid):
        """
        Constructs a MediaProcessorContext
        
        :param sid: The SID of the MediaProcessor resource to update.
        
        :returns: twilio.rest.media.v1.media_processor.MediaProcessorContext
        :rtype: twilio.rest.media.v1.media_processor.MediaProcessorContext
        """
        return MediaProcessorContext(self._version, sid=sid)

    def __repr__(self):
        """
        Provide a friendly representation
        :returns: Machine friendly representation
        :rtype: str
        """
        return '<Twilio.Media.V1.MediaProcessorList>'








class MediaProcessorPage(Page):

    def __init__(self, version, response, solution):
        """
        Initialize the MediaProcessorPage

        :param Version version: Version that contains the resource
        :param Response response: Response from the API

        :returns: twilio.rest.media.v1.media_processor.MediaProcessorPage
        :rtype: twilio.rest.media.v1.media_processor.MediaProcessorPage
        """
        super().__init__(version, response)

        # Path solution
        self._solution = solution

    def get_instance(self, payload):
        """
        Build an instance of MediaProcessorInstance

        :param dict payload: Payload response from the API

        :returns: twilio.rest.media.v1.media_processor.MediaProcessorInstance
        :rtype: twilio.rest.media.v1.media_processor.MediaProcessorInstance
        """
        return MediaProcessorInstance(self._version, payload)

    def __repr__(self):
        """
        Provide a friendly representation

        :returns: Machine friendly representation
        :rtype: str
        """
        return '<Twilio.Media.V1.MediaProcessorPage>'




class MediaProcessorContext(InstanceContext):

    def __init__(self, version: Version, sid: str):
        """
        Initialize the MediaProcessorContext

        :param Version version: Version that contains the resource
        :param sid: The SID of the MediaProcessor resource to update.

        :returns: twilio.rest.media.v1.media_processor.MediaProcessorContext
        :rtype: twilio.rest.media.v1.media_processor.MediaProcessorContext
        """
        super().__init__(version)

        # Path Solution
        self._solution = { 
            'sid': sid,
        }
        self._uri = '/MediaProcessors/{sid}'.format(**self._solution)
        
    
    def fetch(self):
        """
        Fetch the MediaProcessorInstance
        

        :returns: The fetched MediaProcessorInstance
        :rtype: twilio.rest.media.v1.media_processor.MediaProcessorInstance
        """
        
        payload = self._version.fetch(method='GET', uri=self._uri, )

        return MediaProcessorInstance(
            self._version,
            payload,
            sid=self._solution['sid'],
            
        )
        
    def update(self, status):
        """
        Update the MediaProcessorInstance
        
        :params MediaProcessorUpdateStatus status: 

        :returns: The updated MediaProcessorInstance
        :rtype: twilio.rest.media.v1.media_processor.MediaProcessorInstance
        """
        data = values.of({ 
            'Status': status,
        })
        

        payload = self._version.update(method='POST', uri=self._uri, data=data,)

        return MediaProcessorInstance(
            self._version,
            payload,
            sid=self._solution['sid']
        )
        
    
    def __repr__(self):
        """
        Provide a friendly representation
        :returns: Machine friendly representation
        :rtype: str
        """
        context = ' '.join('{}={}'.format(k, v) for k, v in self._solution.items())
        return '<Twilio.Media.V1.MediaProcessorContext {}>'.format(context)

class MediaProcessorInstance(InstanceResource):

    def __init__(self, version, payload, sid: str=None):
        """
        Initialize the MediaProcessorInstance
        :returns: twilio.rest.media.v1.media_processor.MediaProcessorInstance
        :rtype: twilio.rest.media.v1.media_processor.MediaProcessorInstance
        """
        super().__init__(version)

        self._properties = { 
            'account_sid': payload.get('account_sid'),
            'sid': payload.get('sid'),
            'date_created': deserialize.iso8601_datetime(payload.get('date_created')),
            'date_updated': deserialize.iso8601_datetime(payload.get('date_updated')),
            'extension': payload.get('extension'),
            'extension_context': payload.get('extension_context'),
            'status': payload.get('status'),
            'url': payload.get('url'),
            'ended_reason': payload.get('ended_reason'),
            'status_callback': payload.get('status_callback'),
            'status_callback_method': payload.get('status_callback_method'),
            'max_duration': deserialize.integer(payload.get('max_duration')),
        }

        self._context = None
        self._solution = { 'sid': sid or self._properties['sid'],  }
    
    @property
    def _proxy(self):
        """
        Generate an instance context for the instance, the context is capable of
        performing various actions. All instance actions are proxied to the context

        :returns: MediaProcessorContext for this MediaProcessorInstance
        :rtype: twilio.rest.media.v1.media_processor.MediaProcessorContext
        """
        if self._context is None:
            self._context = MediaProcessorContext(self._version, sid=self._solution['sid'],)
        return self._context
    
    @property
    def account_sid(self):
        """
        :returns: The SID of the [Account](https://www.twilio.com/docs/iam/api/account) that created the MediaProcessor resource.
        :rtype: str
        """
        return self._properties['account_sid']
    
    @property
    def sid(self):
        """
        :returns: The unique string generated to identify the MediaProcessor resource.
        :rtype: str
        """
        return self._properties['sid']
    
    @property
    def date_created(self):
        """
        :returns: The date and time in GMT when the resource was created specified in [ISO 8601](https://en.wikipedia.org/wiki/ISO_8601) format.
        :rtype: datetime
        """
        return self._properties['date_created']
    
    @property
    def date_updated(self):
        """
        :returns: The date and time in GMT when the resource was last updated specified in [ISO 8601](https://en.wikipedia.org/wiki/ISO_8601) format.
        :rtype: datetime
        """
        return self._properties['date_updated']
    
    @property
    def extension(self):
        """
        :returns: The [Media Extension](/docs/live/api/media-extensions-overview) name or URL. Ex: `video-composer-v2`
        :rtype: str
        """
        return self._properties['extension']
    
    @property
    def extension_context(self):
        """
        :returns: The context of the Media Extension, represented as a JSON dictionary. See the documentation for the specific [Media Extension](/docs/live/api/media-extensions-overview) you are using for more information about the context to send.
        :rtype: str
        """
        return self._properties['extension_context']
    
    @property
    def status(self):
        """
        :returns: 
        :rtype: MediaProcessorStatus
        """
        return self._properties['status']
    
    @property
    def url(self):
        """
        :returns: The absolute URL of the resource.
        :rtype: str
        """
        return self._properties['url']
    
    @property
    def ended_reason(self):
        """
        :returns: The reason why a MediaProcessor ended. When a MediaProcessor is in progress, will be `null`. When a MediaProcessor is completed, can be `ended-via-api`, `max-duration-exceeded`, `error-loading-extension`, `error-streaming-media` or `internal-service-error`. See [ended reasons](/docs/live/api/mediaprocessors#mediaprocessor-ended-reason-values) for more details.
        :rtype: str
        """
        return self._properties['ended_reason']
    
    @property
    def status_callback(self):
        """
        :returns: The URL to which Twilio will send asynchronous webhook requests for every MediaProcessor event. See [Status Callbacks](/docs/live/status-callbacks) for details.
        :rtype: str
        """
        return self._properties['status_callback']
    
    @property
    def status_callback_method(self):
        """
        :returns: The HTTP method Twilio should use to call the `status_callback` URL. Can be `POST` or `GET` and the default is `POST`.
        :rtype: str
        """
        return self._properties['status_callback_method']
    
    @property
    def max_duration(self):
        """
        :returns: The maximum time, in seconds, that the MediaProcessor can run before automatically ends. The default value is 300 seconds, and the maximum value is 90000 seconds. Once this maximum duration is reached, Twilio will end the MediaProcessor, regardless of whether media is still streaming.
        :rtype: int
        """
        return self._properties['max_duration']
    
    def fetch(self):
        """
        Fetch the MediaProcessorInstance
        

        :returns: The fetched MediaProcessorInstance
        :rtype: twilio.rest.media.v1.media_processor.MediaProcessorInstance
        """
        return self._proxy.fetch()
    
    def update(self, status):
        """
        Update the MediaProcessorInstance
        
        :params MediaProcessorUpdateStatus status: 

        :returns: The updated MediaProcessorInstance
        :rtype: twilio.rest.media.v1.media_processor.MediaProcessorInstance
        """
        return self._proxy.update(status=status, )
    
    def __repr__(self):
        """
        Provide a friendly representation
        :returns: Machine friendly representation
        :rtype: str
        """
        context = ' '.join('{}={}'.format(k, v) for k, v in self._solution.items())
        return '<Twilio.Media.V1.MediaProcessorInstance {}>'.format(context)


