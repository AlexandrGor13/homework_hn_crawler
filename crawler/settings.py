from dotenv import load_dotenv
import os

load_dotenv()

base_url = os.getenv("BASE_URL")
crawl_interval = int(os.getenv("CRAWL_INTERVAL"))
request_timeout = int(os.getenv("REQUEST_TIMEOUT"))
request_delay = int(os.getenv("REQUEST_DELAY"))
max_concurrent_requests = int(os.getenv("MAX_CONCURRENT_REQUESTS"))
max_retries = int(os.getenv("MAX_RETRIES"))

