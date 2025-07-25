```python
import logging
from django.http import JsonResponse
from django.utils.deprecation import MiddlewareMixin

logger = logging.getLogger(__name__)

class HealthCheckMiddleware(MiddlewareMixin):
    """
    Middleware to check the health of the application on each request.
    """
    def process_request(self, request):
        if request.path == "/health/":
            return JsonResponse({"status": "healthy", "message": "Application is running smoothly."})

class PerformanceMonitoringMiddleware(MiddlewareMixin):
    """
    Middleware to monitor and log the performance of each request.
    """
    def process_request(self, request):
        request.start_time = time.time()

    def process_response(self, request, response):
        if hasattr(request, 'start_time'):
            duration = time.time() - request.start_time
            logger.info(f"Request to {request.path} took {duration:.2f} seconds.")
        return response

def setup_logging():
    """
    Sets up logging for the application.
    """
    logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')

def monitor_application():
    """
    Sets up application monitoring tools and middleware.
    """
    setup_logging()
    # Additional monitoring tools like Prometheus, New Relic, or Sentry can be configured here.

# Example usage in Django settings:
# MIDDLEWARE += ['src.monitoring.HealthCheckMiddleware', 'src.monitoring.PerformanceMonitoringMiddleware']
```