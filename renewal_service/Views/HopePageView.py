from renewal_service.Managers.HopePageManager import ServiceInfoManager
from Utilites.ApiHandler.RestAPIView import RestAPIView
from decimal import Decimal


class ServiceWidgetView(RestAPIView):

    def get(self, request, version_id):
        """
        API to get Service Widget data for STNK Renewal
        :param request:
        :param version_id:
        :return: List of service info objects
        """
        service_id = request.GET.get('service_id', None)
        response = ServiceInfoManager().get_service_data(service_id=service_id)
        return self.getResWithData({"data": response})


class InsertServiceView(RestAPIView):

    def post(self, request, version_id):
        """
        :param request:
        :param version_id:
        :return:
        """
        name = request.data.get('name', '')
        amount = int(request.data.get('amount', 0))
        description = request.data.get('description', '')
        ServiceInfoManager().insert_service_information(name=name, amount=amount, description=description)
        return self.getResKeyValue("message", "inserted data ")
