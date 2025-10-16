from django.utils.deprecation import MiddlewareMixin
import time

class TimeMiddleware(MiddlewareMixin):
    def process_view(self, request, view_func, view_args, view_kwargs):
        pass

    def process_request(self, request):
        print('middleware start')
        request.start = time.time()

    def process_response(self, request, response):
        print('middleware done')

        if request.path == '/':
            total = time.time() - request.start
            print(f"total time:, {total} seconds")

        return response