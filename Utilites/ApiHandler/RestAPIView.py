from rest_framework.response import Response
from rest_framework.views import APIView


class RestAPIView(APIView):
    """
    """
    @staticmethod
    def getResKeyValue(key, data):
        """
        :param key:
        :param data:
        :return:
        """
        return Response({
            "success": True,
            key: data
        }, 200)

    @staticmethod
    def getFailureResponse(key, data):
        """
        :param key:
        :param data:
        :return:
        """
        return Response({
            "success": False,
            key: data
        }, 200)

    @staticmethod
    def getFailureWithData(data, response_code=200):
        """
        :param data:
        :param response_code:
        :return:
        """
        data.update({"success": False})
        return Response(
            data,
            response_code
        )

    @staticmethod
    def getResWithData(data, response_code=200):
        """
        :param data:
        :param response_code:
        :return:
        """
        data.update({"success": True})
        return Response(data, response_code)

    def getPhoneFromSession(self):
        """
        :return:
        """
        try:
            return str(self.request.session["phone"])[3:13]
        except KeyError as e:
            e.message = self.getKeyErrorMessage(
                e, "Could not fetch phone exists in session")
            raise e

    def getUserFromSession(self):
        """
        :return:
        """
        try:
            return self.request.session["user_id"]
        except KeyError as e:
            e.message = self.getKeyErrorMessage(
                e, "Yor are not registered user")
            raise e

    @staticmethod
    def getKeyErrorMessage(e, msg="Ops Somethings Went Wrong "):
        """
        :param e:
        :param msg:
        :return:
        """
        return {
            "error": {
                "message": msg,
                "code": 4004,
                "status_code": 400,
                "developer_message": f"Key error {str(e)}",
            },
            "success": False,
        }

    def setJsonEncodedBody(self):
        """
        :return:
        """
        try:
            pass
        except Exception as e:
            e.message = self.getKeyErrorMessage(str(e))
            raise e

    def getConsumerFromSession(self):
        """
        :return:
        """
        try:
            return self.request.session["user_context"]["consumer_id"]
        except KeyError as e:
            e.message = self.getKeyErrorMessage(
                e, "Yor are not registered")
            raise e

    def getAgentFromSession(self):
        """
        :return:
        """
        try:
            return self.request.session["user_context"]["agent_id"]
        except KeyError as e:
            e.message = self.getKeyErrorMessage(
                e, "Yor are not registered as Reseller")
            raise e

    def getRequestHeaderData(self):
        """
        :return:
        """
        meta_data = self.request.META
        device_id = meta_data.get('HTTP_UNIQUE_ID', '')
        if 'HTTP_APP_CLIENT' in meta_data and 'HTTP_APP_VERSION' in meta_data:
            return {'app_client': meta_data['HTTP_APP_CLIENT'], 'app_version': meta_data['HTTP_APP_VERSION'],
                    'device_id': device_id}
        else:
            return {'app_client': '', 'app_version': '0', 'device_id': device_id}

    def get_access_token(self):
        """
        :return:
        """
        try:
            return self.request.session["access_token"]
        except KeyError as e:
            e.message = self.getKeyErrorMessage(
                e, "access_token not found in session")
            raise e
