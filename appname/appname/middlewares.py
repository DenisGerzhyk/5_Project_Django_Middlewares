import logging
import time
from datetime import datetime


class LogMiddleware:
    def __init__(self, get_response):
        self.get_response = get_response
        logging.basicConfig(level=logging.DEBUG)
        self.logger = logging.getLogger('LogMiddleware')

    def __call__(self, request):
        start_time = time.time()
        response = self.get_response(request)
        finish_time = time.time() - start_time

        log_str = f"{datetime.now()} - {request.method} - {request.path} - {response.status_code} - {finish_time}"
        self.logger.info(log_str)

        return response
