"""
    This code was generated by
   ___ _ _ _ _ _    _ ____    ____ ____ _    ____ ____ _  _ ____ ____ ____ ___ __   __
    |  | | | | |    | |  | __ |  | |__| | __ | __ |___ |\ | |___ |__/ |__|  | |  | |__/
    |  |_|_| | |___ | |__|    |__| |  | |    |__] |___ | \| |___ |  \ |  |  | |__| |  \

    Twilio - Insights
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


class ParticipantList(ListResource):

    def __init__(self, version: Version, room_sid: str):
        """
        Initialize the ParticipantList

        :param Version version: Version that contains the resource
        :param room_sid: The SID of the Room resource.
        
        :returns: twilio.rest.insights.v1.room.participant.ParticipantList
        :rtype: twilio.rest.insights.v1.room.participant.ParticipantList
        """
        super().__init__(version)

        # Path Solution
        self._solution = { 'room_sid': room_sid,  }
        self._uri = '/Video/Rooms/{room_sid}/Participants'.format(**self._solution)
        
        
    
    
    def stream(self, limit=None, page_size=None):
        """
        Streams ParticipantInstance records from the API as a generator stream.
        This operation lazily loads records as efficiently as possible until the limit
        is reached.
        The results are returned as a generator, so this operation is memory efficient.
        
        :param int limit: Upper limit for the number of records to return. stream()
                          guarantees to never return more than limit.  Default is no limit
        :param int page_size: Number of records to fetch per request, when not set will use
                              the default value of 50 records.  If no page_size is defined
                              but a limit is defined, stream() will attempt to read the
                              limit with the most efficient page size, i.e. min(limit, 1000)

        :returns: Generator that will yield up to limit results
        :rtype: list[twilio.rest.insights.v1.room.participant.ParticipantInstance]
        """
        limits = self._version.read_limits(limit, page_size)
        page = self.page(
            page_size=limits['page_size']
        )

        return self._version.stream(page, limits['limit'])

    def list(self, limit=None, page_size=None):
        """
        Lists ParticipantInstance records from the API as a list.
        Unlike stream(), this operation is eager and will load `limit` records into
        memory before returning.
        
        :param int limit: Upper limit for the number of records to return. list() guarantees
                          never to return more than limit.  Default is no limit
        :param int page_size: Number of records to fetch per request, when not set will use
                              the default value of 50 records.  If no page_size is defined
                              but a limit is defined, list() will attempt to read the limit
                              with the most efficient page size, i.e. min(limit, 1000)

        :returns: Generator that will yield up to limit results
        :rtype: list[twilio.rest.insights.v1.room.participant.ParticipantInstance]
        """
        return list(self.stream(
            limit=limit,
            page_size=page_size,
        ))

    def page(self, page_token=values.unset, page_number=values.unset, page_size=values.unset):
        """
        Retrieve a single page of ParticipantInstance records from the API.
        Request is executed immediately
        
        :param str page_token: PageToken provided by the API
        :param int page_number: Page Number, this value is simply for client state
        :param int page_size: Number of records to return, defaults to 50

        :returns: Page of ParticipantInstance
        :rtype: twilio.rest.insights.v1.room.participant.ParticipantPage
        """
        data = values.of({ 
            'PageToken': page_token,
            'Page': page_number,
            'PageSize': page_size,
        })

        response = self._version.page(method='GET', uri=self._uri, params=data)
        return ParticipantPage(self._version, response, self._solution)

    def get_page(self, target_url):
        """
        Retrieve a specific page of ParticipantInstance records from the API.
        Request is executed immediately

        :param str target_url: API-generated URL for the requested results page

        :returns: Page of ParticipantInstance
        :rtype: twilio.rest.insights.v1.room.participant.ParticipantPage
        """
        response = self._version.domain.twilio.request(
            'GET',
            target_url
        )
        return ParticipantPage(self._version, response, self._solution)


    def get(self, participant_sid):
        """
        Constructs a ParticipantContext
        
        :param participant_sid: The SID of the Participant resource.
        
        :returns: twilio.rest.insights.v1.room.participant.ParticipantContext
        :rtype: twilio.rest.insights.v1.room.participant.ParticipantContext
        """
        return ParticipantContext(self._version, room_sid=self._solution['room_sid'], participant_sid=participant_sid)

    def __call__(self, participant_sid):
        """
        Constructs a ParticipantContext
        
        :param participant_sid: The SID of the Participant resource.
        
        :returns: twilio.rest.insights.v1.room.participant.ParticipantContext
        :rtype: twilio.rest.insights.v1.room.participant.ParticipantContext
        """
        return ParticipantContext(self._version, room_sid=self._solution['room_sid'], participant_sid=participant_sid)

    def __repr__(self):
        """
        Provide a friendly representation
        :returns: Machine friendly representation
        :rtype: str
        """
        return '<Twilio.Insights.V1.ParticipantList>'




class ParticipantPage(Page):

    def __init__(self, version, response, solution):
        """
        Initialize the ParticipantPage

        :param Version version: Version that contains the resource
        :param Response response: Response from the API

        :returns: twilio.rest.insights.v1.room.participant.ParticipantPage
        :rtype: twilio.rest.insights.v1.room.participant.ParticipantPage
        """
        super().__init__(version, response)

        # Path solution
        self._solution = solution

    def get_instance(self, payload):
        """
        Build an instance of ParticipantInstance

        :param dict payload: Payload response from the API

        :returns: twilio.rest.insights.v1.room.participant.ParticipantInstance
        :rtype: twilio.rest.insights.v1.room.participant.ParticipantInstance
        """
        return ParticipantInstance(self._version, payload, room_sid=self._solution['room_sid'])

    def __repr__(self):
        """
        Provide a friendly representation

        :returns: Machine friendly representation
        :rtype: str
        """
        return '<Twilio.Insights.V1.ParticipantPage>'




class ParticipantContext(InstanceContext):

    def __init__(self, version: Version, room_sid: str, participant_sid: str):
        """
        Initialize the ParticipantContext

        :param Version version: Version that contains the resource
        :param room_sid: The SID of the Room resource.:param participant_sid: The SID of the Participant resource.

        :returns: twilio.rest.insights.v1.room.participant.ParticipantContext
        :rtype: twilio.rest.insights.v1.room.participant.ParticipantContext
        """
        super().__init__(version)

        # Path Solution
        self._solution = { 
            'room_sid': room_sid,
            'participant_sid': participant_sid,
        }
        self._uri = '/Video/Rooms/{room_sid}/Participants/{participant_sid}'.format(**self._solution)
        
    
    def fetch(self):
        """
        Fetch the ParticipantInstance
        

        :returns: The fetched ParticipantInstance
        :rtype: twilio.rest.insights.v1.room.participant.ParticipantInstance
        """
        
        payload = self._version.fetch(method='GET', uri=self._uri, )

        return ParticipantInstance(
            self._version,
            payload,
            room_sid=self._solution['room_sid'],
            participant_sid=self._solution['participant_sid'],
            
        )
        
    
    def __repr__(self):
        """
        Provide a friendly representation
        :returns: Machine friendly representation
        :rtype: str
        """
        context = ' '.join('{}={}'.format(k, v) for k, v in self._solution.items())
        return '<Twilio.Insights.V1.ParticipantContext {}>'.format(context)

class ParticipantInstance(InstanceResource):

    def __init__(self, version, payload, room_sid: str, participant_sid: str=None):
        """
        Initialize the ParticipantInstance
        :returns: twilio.rest.insights.v1.room.participant.ParticipantInstance
        :rtype: twilio.rest.insights.v1.room.participant.ParticipantInstance
        """
        super().__init__(version)

        self._properties = { 
            'participant_sid': payload.get('participant_sid'),
            'participant_identity': payload.get('participant_identity'),
            'join_time': deserialize.iso8601_datetime(payload.get('join_time')),
            'leave_time': deserialize.iso8601_datetime(payload.get('leave_time')),
            'duration_sec': payload.get('duration_sec'),
            'account_sid': payload.get('account_sid'),
            'room_sid': payload.get('room_sid'),
            'status': payload.get('status'),
            'codecs': payload.get('codecs'),
            'end_reason': payload.get('end_reason'),
            'error_code': deserialize.integer(payload.get('error_code')),
            'error_code_url': payload.get('error_code_url'),
            'media_region': payload.get('media_region'),
            'properties': payload.get('properties'),
            'edge_location': payload.get('edge_location'),
            'publisher_info': payload.get('publisher_info'),
            'url': payload.get('url'),
        }

        self._context = None
        self._solution = { 'room_sid': room_sid, 'participant_sid': participant_sid or self._properties['participant_sid'],  }
    
    @property
    def _proxy(self):
        """
        Generate an instance context for the instance, the context is capable of
        performing various actions. All instance actions are proxied to the context

        :returns: ParticipantContext for this ParticipantInstance
        :rtype: twilio.rest.insights.v1.room.participant.ParticipantContext
        """
        if self._context is None:
            self._context = ParticipantContext(self._version, room_sid=self._solution['room_sid'], participant_sid=self._solution['participant_sid'],)
        return self._context
    
    @property
    def participant_sid(self):
        """
        :returns: Unique identifier for the participant.
        :rtype: str
        """
        return self._properties['participant_sid']
    
    @property
    def participant_identity(self):
        """
        :returns: The application-defined string that uniquely identifies the participant within a Room.
        :rtype: str
        """
        return self._properties['participant_identity']
    
    @property
    def join_time(self):
        """
        :returns: When the participant joined the room.
        :rtype: datetime
        """
        return self._properties['join_time']
    
    @property
    def leave_time(self):
        """
        :returns: When the participant left the room.
        :rtype: datetime
        """
        return self._properties['leave_time']
    
    @property
    def duration_sec(self):
        """
        :returns: Amount of time in seconds the participant was in the room.
        :rtype: int
        """
        return self._properties['duration_sec']
    
    @property
    def account_sid(self):
        """
        :returns: Account SID associated with the room.
        :rtype: str
        """
        return self._properties['account_sid']
    
    @property
    def room_sid(self):
        """
        :returns: Unique identifier for the room.
        :rtype: str
        """
        return self._properties['room_sid']
    
    @property
    def status(self):
        """
        :returns: 
        :rtype: VideoParticipantSummaryRoomStatus
        """
        return self._properties['status']
    
    @property
    def codecs(self):
        """
        :returns: Codecs detected from the participant. Can be `VP8`, `H264`, or `VP9`.
        :rtype: list[VideoParticipantSummaryCodec]
        """
        return self._properties['codecs']
    
    @property
    def end_reason(self):
        """
        :returns: Reason the participant left the room. See [the list of possible values here](https://www.twilio.com/docs/video/video-log-analyzer/video-log-analyzer-api#end_reason).
        :rtype: str
        """
        return self._properties['end_reason']
    
    @property
    def error_code(self):
        """
        :returns: Errors encountered by the participant.
        :rtype: int
        """
        return self._properties['error_code']
    
    @property
    def error_code_url(self):
        """
        :returns: Twilio error code dictionary link.
        :rtype: str
        """
        return self._properties['error_code_url']
    
    @property
    def media_region(self):
        """
        :returns: 
        :rtype: VideoParticipantSummaryTwilioRealm
        """
        return self._properties['media_region']
    
    @property
    def properties(self):
        """
        :returns: Object containing information about the participant's data from the room. See [below](https://www.twilio.com/docs/video/video-log-analyzer/video-log-analyzer-api#properties) for more information.
        :rtype: dict
        """
        return self._properties['properties']
    
    @property
    def edge_location(self):
        """
        :returns: 
        :rtype: VideoParticipantSummaryEdgeLocation
        """
        return self._properties['edge_location']
    
    @property
    def publisher_info(self):
        """
        :returns: Object containing information about the SDK name and version. See [below](https://www.twilio.com/docs/video/video-log-analyzer/video-log-analyzer-api#publisher_info) for more information.
        :rtype: dict
        """
        return self._properties['publisher_info']
    
    @property
    def url(self):
        """
        :returns: URL of the participant resource.
        :rtype: str
        """
        return self._properties['url']
    
    def fetch(self):
        """
        Fetch the ParticipantInstance
        

        :returns: The fetched ParticipantInstance
        :rtype: twilio.rest.insights.v1.room.participant.ParticipantInstance
        """
        return self._proxy.fetch()
    
    def __repr__(self):
        """
        Provide a friendly representation
        :returns: Machine friendly representation
        :rtype: str
        """
        context = ' '.join('{}={}'.format(k, v) for k, v in self._solution.items())
        return '<Twilio.Insights.V1.ParticipantInstance {}>'.format(context)


