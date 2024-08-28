from sqlalchemy.sql.functions import current_timefrom locale import format_string

# Middleware


```Python
from fastapi import FastAPI, Request
import random
import string

app = FastAPI()

@app.middleware("http")
async def request_id_logging(request: Request, call_next):
    """
    Middleware that generates a random string of 60 characters and logs it.
    """
    response = await call_next(request)
    random_letters = ''.join(random.choices(string.ascii_letters + string.digits, k=6) for _ in range(10))
    print(f"Log: {random_letters}")
    response.headers["X-Request-ID"] = random_letters
    
    return response


@app.get("/")
async def read_root():
    """
    Root endpoint that returns a simple JSON response.
    """
    return {"Hello": "World"}
```

## Rate Limiting

Rate limiting is a technique used to control the rate of requests sent to a server. This can be useful to prevent abuse of the server and to ensure that the server remains responsive to legitimate users. FastAPI provides a built-in rate limiting middleware that can be used to limit the number of requests that a client can make to the server within a specified time period.


[Rate Limiting Middleware](https://www.youtube.com/watch?v=2-exKF2Vszg)
```Python
from fastapi import FastAPI, Request, Response
from starlette.middleware.base import BaseHTTPMiddleware
import time
from collections import defaultdict
from typing import Dict

app = FastAPI()

class AdvancedMiddleware(BaseHTTPMiddleware):
    def __init__(self, app):
        super().__init__(app)
        self.rate_limit_records: Dict[str, float] = defaultdict(float)
    
    async def log_message(self, message: str):
        print(message)
        
    async def dispatch(self, request: Request, call_next):
        """
        Middleware that limits the number of requests a client can make to the server.
        """
        client_ip = request.client.host
        current_time = time.time()
        
        if current_time - self.rate_limit_records[client_ip] < 1:  # 1 request per second limit            
            return Response("Rate limit exceeded", status_code=429)
        
        self.rate_limit_records[client_ip] = current_time
        path = request.url.path
        await self.log_message(f"Client {client_ip} accessed {path}")

        # Process the request
        start_time = time.time()
        response = await call_next(request)
        process_time = time.time() - start_time

        # Add custom headers without modifying the original headers object
        custom_headers = {"X-Process-Time": str(process_time)}
        for header, value in custom_headers.items():
            response.headers.append(header, value)

# Add the advanced middleware to the application            
app.add_middleware(AdvancedMiddleware)
```

Good Channel        
https://www.youtube.com/@codingwithroby
