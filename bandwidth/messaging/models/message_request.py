# -*- coding: utf-8 -*-

"""
bandwidth

This file was automatically generated by APIMATIC v3.0 (
 https://www.apimatic.io ).
"""


class MessageRequest(object):

    """Implementation of the 'MessageRequest' model.

    TODO: type model description here.

    Attributes:
        application_id (string): The ID of the Application your from number is
            associated with in the Bandwidth Phone Number Dashboard.
        to (list of string): The phone number(s) the message should be sent to
            in E164 format
        mfrom (string): One of your telephone numbers the message should come
            from in E164 format
        text (string): The contents of the text message. Must be 2048
            characters or less.
        media (list of string): A list of URLs to include as media attachments
            as part of the message.
        tag (string): A custom string that will be included in callback events
            of the message. Max 1024 characters
        priority (PriorityEnum): The message's priority, currently for
            toll-free or short code SMS only. Messages with a priority value
            of `"high"` are given preference over your other traffic.

    """

    # Create a mapping from Model property names to API property names
    _names = {
        "application_id": 'applicationId',
        "to": 'to',
        "mfrom": 'from',
        "text": 'text',
        "media": 'media',
        "tag": 'tag',
        "priority": 'priority'
    }

    def __init__(self,
                 application_id=None,
                 to=None,
                 mfrom=None,
                 text=None,
                 media=None,
                 tag=None,
                 priority=None):
        """Constructor for the MessageRequest class"""

        # Initialize members of the class
        self.application_id = application_id
        self.to = to
        self.mfrom = mfrom
        self.text = text
        self.media = media
        self.tag = tag
        self.priority = priority

    @classmethod
    def from_dictionary(cls,
                        dictionary):
        """Creates an instance of this model from a dictionary

        Args:
            dictionary (dictionary): A dictionary representation of the object
            as obtained from the deserialization of the server's response. The
            keys MUST match property names in the API description.

        Returns:
            object: An instance of this structure class.

        """
        if dictionary is None:
            return None

        # Extract variables from the dictionary
        application_id = dictionary.get('applicationId')
        to = dictionary.get('to')
        mfrom = dictionary.get('from')
        text = dictionary.get('text')
        media = dictionary.get('media')
        tag = dictionary.get('tag')
        priority = dictionary.get('priority')

        # Return an object of this model
        return cls(application_id,
                   to,
                   mfrom,
                   text,
                   media,
                   tag,
                   priority)
