"""
    This code was generated by
   ___ _ _ _ _ _    _ ____    ____ ____ _    ____ ____ _  _ ____ ____ ____ ___ __   __
    |  | | | | |    | |  | __ |  | |__| | __ | __ |___ |\ | |___ |__/ |__|  | |  | |__/
    |  |_|_| | |___ | |__|    |__| |  | |    |__] |___ | \| |___ |  \ |  |  | |__| |  \

    Twilio - Api
    This is the public Twilio REST API.

    NOTE: This class is auto generated by OpenAPI Generator.
    https://openapi-generator.tech
    Do not edit the class manually.
"""


from twilio.base import deserialize
from twilio.base import serialize
from twilio.base import values

from twilio.base.instance_resource import InstanceResource
from twilio.base.list_resource import ListResource
from twilio.base.version import Version



class FeedbackList(ListResource):

    def __init__(self, version: Version, account_sid: str, message_sid: str):
        """
        Initialize the FeedbackList

        :param Version version: Version that contains the resource
        :param account_sid: The SID of the [Account](https://www.twilio.com/docs/iam/api/account) that will create the resource.
        :param message_sid: The SID of the Message resource for which the feedback was provided.
        
        :returns: twilio.rest.api.v2010.account.message.feedback.FeedbackList
        :rtype: twilio.rest.api.v2010.account.message.feedback.FeedbackList
        """
        super().__init__(version)

        # Path Solution
        self._solution = { 'account_sid': account_sid, 'message_sid': message_sid,  }
        self._uri = '/Accounts/{account_sid}/Messages/{message_sid}/Feedback.json'.format(**self._solution)
        
        
    
    def create(self, outcome=values.unset):
        """
        Create the FeedbackInstance

        :param MessageFeedbackOutcome outcome: 
        
        :returns: The created FeedbackInstance
        :rtype: twilio.rest.api.v2010.account.message.feedback.FeedbackInstance
        """
        data = values.of({ 
            'Outcome': outcome,
        })
        
        payload = self._version.create(method='POST', uri=self._uri, data=data,)

        return FeedbackInstance(self._version, payload, account_sid=self._solution['account_sid'], message_sid=self._solution['message_sid'])
    


    def __repr__(self):
        """
        Provide a friendly representation
        :returns: Machine friendly representation
        :rtype: str
        """
        return '<Twilio.Api.V2010.FeedbackList>'


class FeedbackInstance(InstanceResource):

    def __init__(self, version, payload, account_sid: str, message_sid: str):
        """
        Initialize the FeedbackInstance
        :returns: twilio.rest.api.v2010.account.message.feedback.FeedbackInstance
        :rtype: twilio.rest.api.v2010.account.message.feedback.FeedbackInstance
        """
        super().__init__(version)

        self._properties = { 
            'account_sid': payload.get('account_sid'),
            'message_sid': payload.get('message_sid'),
            'outcome': payload.get('outcome'),
            'date_created': deserialize.rfc2822_datetime(payload.get('date_created')),
            'date_updated': deserialize.rfc2822_datetime(payload.get('date_updated')),
            'uri': payload.get('uri'),
        }

        self._context = None
        self._solution = { 'account_sid': account_sid, 'message_sid': message_sid,  }
    
    
    @property
    def account_sid(self):
        """
        :returns: The SID of the [Account](https://www.twilio.com/docs/iam/api/account) that created the MessageFeedback resource.
        :rtype: str
        """
        return self._properties['account_sid']
    
    @property
    def message_sid(self):
        """
        :returns: The SID of the Message resource for which the feedback was provided.
        :rtype: str
        """
        return self._properties['message_sid']
    
    @property
    def outcome(self):
        """
        :returns: 
        :rtype: MessageFeedbackOutcome
        """
        return self._properties['outcome']
    
    @property
    def date_created(self):
        """
        :returns: The date and time in GMT that the resource was created specified in [RFC 2822](https://www.ietf.org/rfc/rfc2822.txt) format.
        :rtype: datetime
        """
        return self._properties['date_created']
    
    @property
    def date_updated(self):
        """
        :returns: The date and time in GMT that the resource was last updated specified in [RFC 2822](https://www.ietf.org/rfc/rfc2822.txt) format.
        :rtype: datetime
        """
        return self._properties['date_updated']
    
    @property
    def uri(self):
        """
        :returns: The URI of the resource, relative to `https://api.twilio.com`.
        :rtype: str
        """
        return self._properties['uri']
    
    def __repr__(self):
        """
        Provide a friendly representation
        :returns: Machine friendly representation
        :rtype: str
        """
        context = ' '.join('{}={}'.format(k, v) for k, v in self._solution.items())
        return '<Twilio.Api.V2010.FeedbackInstance {}>'.format(context)


