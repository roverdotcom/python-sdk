# -*- coding: utf-8 -*-

"""
bandwidth

This file was automatically generated by APIMATIC v3.0 (
 https://www.apimatic.io ).
"""


class Session(object):

    """Implementation of the 'Session' model.

    A session object

    Attributes:
        id (string): Unique id of the session
        tag (string): User defined tag to associate with the session

    """

    # Create a mapping from Model property names to API property names
    _names = {
        "id": 'id',
        "tag": 'tag'
    }

    def __init__(self,
                 id=None,
                 tag=None):
        """Constructor for the Session class"""

        # Initialize members of the class
        self.id = id
        self.tag = tag

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
        id = dictionary.get('id')
        tag = dictionary.get('tag')

        # Return an object of this model
        return cls(id,
                   tag)
