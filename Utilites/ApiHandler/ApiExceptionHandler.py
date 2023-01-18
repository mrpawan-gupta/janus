class ThirdPartyApiException(Exception):
    def __init__(self, satus_code, msg="Ops Something went Wrong."):
        message = {
            "error": {
                "message": msg,
                "code": 4037,
                "developer_message": "",
                "status_code": satus_code
            },
            "success": False,
        }
        self.message = message

    def __str__(self):
        return repr(self.message)


class AuthException(Exception):
    def __init__(self, exception):
        message = {
            "success": False,
            "message": f"Authentication Failed by server {str(exception)}",
        }
        self.message = message

    def __str__(self):
        return repr(self.message)


class DefaultException(Exception):
    def __init__(self, msg):
        message = {
            "error": {
                "message": msg,
                "code": 4055,
                "status_code": 400,
                "developer_message": msg
            },
            "success": False}

        self.message = message


class CantCreateUser(Exception):
    def __init__(self, message="Unable to Create User"):
        message = {
            "error": {
                "message": message,
                "code": 4016,
                "developer_message": "Unable To create User",
                "status_code": 400
            },
            "success": False
        }
        self.message = message


class InvalidOtp(Exception):
    def __init__(self, message="Unable to Create User"):
        message = {
            "error": {
                "message": message,
                "code": 4016,
                "developer_message": "Unable To create User",
                "status_code": 400
            },
            "success": False
        }
        self.message = message


class PermissionException(Exception):
    def __init__(self, msg="Authorization failes"):
        message = {"success": False,
                   "error": {
                       "message": msg,
                       "code": 4037,
                       "developer_message": "",
                       "status_code": 403}
                   }
        self.message = message

    def __str__(self):
        return repr(self.message)


class TimeConversionException(Exception):
    def __init__(self, exception):
        message = {
            "error": {
                "message": "Time Conversion Exception ",
                "code": 4033,
                "developer_message": str(exception),
                "status_code": 503
            },
            "success": False}
        self.message = message

    def __str__(self):
        return repr(self.message)
