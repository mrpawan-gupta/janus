from renewal_service.models import Service


class ServiceDataInfo:
    """
    """
    def __init__(self):
        """
        """

    @staticmethod
    def get_service_using_id(service_id):
        """
        function to get all active service provided by using id
        :return: dict of information
        """
        return Service.objects.filter(id=service_id).values('id', 'name', 'amount')


    @staticmethod
    def get_active_service_info():
        """
        function to get all active service provided by us
        :return: dict of information
        """
        return Service.objects.values('id', 'name', 'amount')

    @staticmethod
    def insert_service(name, amount, description):
        """
        fucntion to insert the service info into databases
        @param name:
        @param amount:
        @param description:
        @return:
        """
        if data := Service.objects.filter(name=name):
            data.update(amount=amount)
            data.update(description=description)
        else:
            Service.objects.create(name=name, amount=amount, description=description)
