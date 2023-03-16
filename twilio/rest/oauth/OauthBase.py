r"""
  This code was generated by
  ___ _ _ _ _ _    _ ____    ____ ____ _    ____ ____ _  _ ____ ____ ____ ___ __   __
   |  | | | | |    | |  | __ |  | |__| | __ | __ |___ |\ | |___ |__/ |__|  | |  | |__/
   |  |_|_| | |___ | |__|    |__| |  | |    |__] |___ | \| |___ |  \ |  |  | |__| |  \

  NOTE: This class is auto generated by OpenAPI Generator.
  https://openapi-generator.tech
  Do not edit the class manually.
"""

from twilio.base.domain import Domain
from twilio.rest.oauth.v1 import V1


class OauthBase(Domain):
    def __init__(self, twilio):
        """
        Initialize the Oauth Domain

        :returns: Domain for Oauth
        :rtype: twilio.rest.oauth.Oauth
        """
        super().__init__(twilio)
        self.base_url = "https://oauth.twilio.com"
        self._v1 = None

    @property
    def v1(self):
        """
        :returns: Versions v1 of Oauth
        :rtype: twilio.rest.oauth.v1.V1
        """
        if self._v1 is None:
            self._v1 = V1(self)
        return self._v1

    def __repr__(self):
        """
        Provide a friendly representation
        :returns: Machine friendly representation
        :rtype: str
        """
        return "<Twilio.Oauth>"
