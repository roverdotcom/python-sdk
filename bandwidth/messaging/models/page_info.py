# -*- coding: utf-8 -*-

"""
bandwidth

This file was automatically generated by APIMATIC v2.0 ( https://apimatic.io ).
"""


class PageInfo(object):

    """Implementation of the 'PageInfo' model.

    TODO: type model description here.

    Attributes:
        prev_page (string): The link to the previous page for pagination
        next_page (string): The link to the next page for pagination
        prev_page_token (string): The isolated pagination token for the
            previous page
        next_page_token (string): The isolated pagination token for the next
            page

    """

    # Create a mapping from Model property names to API property names
    _names = {
        "prev_page": 'prevPage',
        "next_page": 'nextPage',
        "prev_page_token": 'prevPageToken',
        "next_page_token": 'nextPageToken'
    }

    def __init__(self,
                 prev_page=None,
                 next_page=None,
                 prev_page_token=None,
                 next_page_token=None):
        """Constructor for the PageInfo class"""

        # Initialize members of the class
        self.prev_page = prev_page
        self.next_page = next_page
        self.prev_page_token = prev_page_token
        self.next_page_token = next_page_token

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
        prev_page = dictionary.get('prevPage')
        next_page = dictionary.get('nextPage')
        prev_page_token = dictionary.get('prevPageToken')
        next_page_token = dictionary.get('nextPageToken')

        # Return an object of this model
        return cls(prev_page,
                   next_page,
                   prev_page_token,
                   next_page_token)
