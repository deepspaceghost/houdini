class Storage_Worker():
    """
    """

    storage_type = None

    def __init__(self, storage_type):
        """
        """

        self.storage_type = storage_type

    def store(self, file_name, data):
        """
        """

        if self.storage_type.upper() == "JSON":
            pass

            # convert the dict to JSON and store it in a file

    def retrieve(self, file_name):
        """
        """

        if self.storage_type.upper() == "JSON":
            pass

            # read the JSON file from the file system
            # convert it to a python dict
            # return dict
