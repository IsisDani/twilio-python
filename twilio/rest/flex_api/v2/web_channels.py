"""
    This code was generated by
   ___ _ _ _ _ _    _ ____    ____ ____ _    ____ ____ _  _ ____ ____ ____ ___ __   __
    |  | | | | |    | |  | __ |  | |__| | __ | __ |___ |\ | |___ |__/ |__|  | |  | |__/
    |  |_|_| | |___ | |__|    |__| |  | |    |__] |___ | \| |___ |  \ |  |  | |__| |  \

    Twilio - Flex
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



class WebChannelsList(ListResource):

    def __init__(self, version: Version):
        """
        Initialize the WebChannelsList

        :param Version version: Version that contains the resource
        
        :returns: twilio.rest.flex_api.v2.web_channels.WebChannelsList
        :rtype: twilio.rest.flex_api.v2.web_channels.WebChannelsList
        """
        super().__init__(version)

        # Path Solution
        self._solution = {  }
        self._uri = '/WebChats'.format(**self._solution)
        
        
    
    def create(self, address_sid, chat_friendly_name=values.unset, customer_friendly_name=values.unset, pre_engagement_data=values.unset):
        """
        Create the WebChannelsInstance

        :param str address_sid: The SID of the Conversations Address. See [Address Configuration Resource](https://www.twilio.com/docs/conversations/api/address-configuration-resource) for configuration details. When a conversation is created on the Flex backend, the callback URL will be set to the corresponding Studio Flow SID or webhook URL in your address configuration.
        :param str chat_friendly_name: The Conversation's friendly name. See the [Conversation resource](https://www.twilio.com/docs/conversations/api/conversation-resource) for an example.
        :param str customer_friendly_name: The Conversation participant's friendly name. See the [Conversation Participant Resource](https://www.twilio.com/docs/conversations/api/conversation-participant-resource) for an example.
        :param str pre_engagement_data: The pre-engagement data.
        
        :returns: The created WebChannelsInstance
        :rtype: twilio.rest.flex_api.v2.web_channels.WebChannelsInstance
        """
        data = values.of({ 
            'AddressSid': address_sid,
            'ChatFriendlyName': chat_friendly_name,
            'CustomerFriendlyName': customer_friendly_name,
            'PreEngagementData': pre_engagement_data,
        })
        
        payload = self._version.create(method='POST', uri=self._uri, data=data,)

        return WebChannelsInstance(self._version, payload)
    


    def __repr__(self):
        """
        Provide a friendly representation
        :returns: Machine friendly representation
        :rtype: str
        """
        return '<Twilio.FlexApi.V2.WebChannelsList>'


class WebChannelsInstance(InstanceResource):

    def __init__(self, version, payload):
        """
        Initialize the WebChannelsInstance
        :returns: twilio.rest.flex_api.v2.web_channels.WebChannelsInstance
        :rtype: twilio.rest.flex_api.v2.web_channels.WebChannelsInstance
        """
        super().__init__(version)

        self._properties = { 
            'conversation_sid': payload.get('conversation_sid'),
            'identity': payload.get('identity'),
        }

        self._context = None
        self._solution = {  }
    
    
    @property
    def conversation_sid(self):
        """
        :returns: The unique string representing the [Conversation resource](https://www.twilio.com/docs/conversations/api/conversation-resource) created.
        :rtype: str
        """
        return self._properties['conversation_sid']
    
    @property
    def identity(self):
        """
        :returns: The unique string representing the User created and should be authorized to participate in the Conversation. For more details, see [User Identity & Access Tokens](https://www.twilio.com/docs/conversations/identity).
        :rtype: str
        """
        return self._properties['identity']
    
    def __repr__(self):
        """
        Provide a friendly representation
        :returns: Machine friendly representation
        :rtype: str
        """
        context = ' '.join('{}={}'.format(k, v) for k, v in self._solution.items())
        return '<Twilio.FlexApi.V2.WebChannelsInstance {}>'.format(context)


