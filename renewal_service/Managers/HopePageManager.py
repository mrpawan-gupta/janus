import json

from renewal_service.Store.HomePageStore import ServiceDataInfo


class ServiceInfoManager:

    def __init__(self):
        """
        """
        super(ServiceInfoManager, self).__init__()
        self.service_data_store = ServiceDataInfo()

    def get_service_data(self, service_id: str) -> dict:
        """
        function to get all service data
        :return: Node
        """
        if service_id:
            return self.service_data_store.get_service_using_id(service_id=service_id)
        else:
            return self.service_data_store.get_active_service_info()
    
    def insert_service_information(self, description, amount, name):
        """
        function to insert infomation of services
        @return: 
        """
        self.service_data_store.insert_service(name=name, amount=amount, description=description)
        

