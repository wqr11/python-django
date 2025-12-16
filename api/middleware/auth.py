from django.http import HttpRequest, HttpResponseNotAllowed


class AuthMiddleware:
    def __init__(self, get_response):
        self.get_response = get_response
        # Configuration

    def __call__(self, req: HttpRequest):
        try: 

            headers = req.headers.get("Authorization")

            if not headers: 
                return HttpResponseNotAllowed("No Authorization header was provided!")

            secret = headers.split(" ")[1]

            if secret != 'test':
                return HttpResponseNotAllowed("Secret is not valid")

            response = self.get_response(req)

            return response
        except:
            return HttpResponseNotAllowed("Unexpected error")