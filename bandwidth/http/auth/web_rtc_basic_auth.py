# -*- coding: utf-8 -*-

"""
bandwidth

This file was automatically generated by APIMATIC v2.0 ( https://apimatic.io ).
"""

import base64


class WebRtcBasicAuth:

    @staticmethod
    def apply(config, http_request):
        """ Add basic authentication to the request.

        Args:
            config (Configuration): The Configuration object which holds the
                authentication information.
            http_request (HttpRequest): The HttpRequest object to which
                authentication will be added.

        """
        username = config.web_rtc_basic_auth_user_name
        password = config.web_rtc_basic_auth_password
        joined = "{}:{}".format(username, password)
        encoded = base64.b64encode(str.encode(joined)).decode('iso-8859-1')
        header_value = "Basic {}".format(encoded)
        http_request.headers["Authorization"] = header_value
