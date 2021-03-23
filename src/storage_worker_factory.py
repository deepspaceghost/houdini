from storage_worker import Storage_Worker

class Storage_Worker_Factory():

    worker_types = ["JSON"]

    def __init__(self):
        """
        """

        pass
        # print("Storage Worker factory object created.")

    def build_worker(self, worker_type):
        """
        """

        if worker_type.upper() in self.worker_types:
            if worker_type.upper() == "JSON":
                return Storage_Worker()

        return None
