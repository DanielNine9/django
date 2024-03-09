from rest_framework.response import Response
from rest_framework import status

# class CommonResponse(Response):
#     def __init__(self, data=None, status=None, message=None, errors=None, **kwargs):
#         response_data = {}
#         if data is not None:
#             response_data['data'] = data
#         if message is not None:
#             response_data['message'] = message
#         if errors is not None:
#             response_data['errors'] = errors
        
#         super().__init__(data=response_data, status=status, **kwargs)


class CommonResponse(Response):
    def __init__(self, data=None, status=status.HTTP_200_OK, message=None, errors=None, **kwargs):
        response_data = {
            "status": status,
            "error": True if status and status >= 400 else False,
            "data": [data] if data is not None and not isinstance(data, list) else [] if data is None else data,
            "message": message if message is not None else "",
            "errors": errors if errors is not None else {}
        }
        
        super().__init__(data=response_data, status=status, **kwargs)

