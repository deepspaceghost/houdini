import os
import pprint

from storage_worker_factory import Storage_Worker_Factory

class JSON_Historian():

    execution_record = {}
    execution_history = {}
    storage_worker = None

    def __init__(self):
        """
        """

        pass
        # print("JSON_Historian object created.")

    def ammend_execution_history(self):
        """
        self.execution_history
        referrence the execution_history key
        append self.execution_record
        """

    def create_execution_history(self):
        """
        add a key to self.execution_history
        execution_history = []
        """

    def create_execution_record(self, timestamp, input1, output1):
        """
        """

        self.execution_record["timestamp"] = timestamp
        self.execution_record["input"] = input1
        self.execution_record["output"] = output1

    def is_execution_history(self, file_name):
        """
        look in the file system for a file called execution_history.json
        if found, return true
        if not, return false
        """

        file = "execution_history.json"
        dir_path = os.path.dirname(os.path.realpath(__file__))
        for root, dirs, files in os.walk(dir_path):
            if file in files:
                return True

            else:
                return False

    def print_execution_record(self):
        """
        """

        pprint.pprint(self.execution_record, width=1)

    def print_execution_history(self):
        """
        """

        pass

    def read_execution_history(self):
        """
        read the contents of execution_history.json
        convert to python dictionary
        store in self.execution_history
        """

        if not self.storage_worker:
            storage_worker_factory = Storage_Worker_Factory()
            self.storage_worker = storage_worker_factory.build_worker("JSON")

        execution_history = self.storage_worker.retrieve("execution_history.json")
        return execution_history

    # def write_execution_history(self):
    #     """
    #     """

    #     if is_execution_history():
    #         read_execution_history()

    #     else:
    #         create_execution_history()

    #     ammend_execution_history()

    #     take self.execution_history
    #     convert to JSON
    #     write to execution_history.json

        if not self.storage_worker:
            storage_worker_factory = Storage_Worker_Factory()
            self.storage_worker = storage_worker_factory.build_worker("JSON")

        self.storage_worker.store("execution_history.json", execution_history)
