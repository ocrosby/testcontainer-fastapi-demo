# Security


## Flows

## The ```password``` flow

The ```password``` flow is one of the ways ("flows") defined in OAuth2, to handle security authentication.

OAuth2 was designed so that the backend or API could be independent of the server that authenticates the user.

But in this case, the same FastAPI application will handle the API and the authentication.

Let's review:

* The user types the ```username``` and ```password``` in the frontend, and hits Enter.
* The frontend (running in the user's browser) sends that ```username``` and ```password``` to a specific URL in our API (declared with tokenUrl="token").
* The API checks that the ```username``` and ```password``` are correct, and responds with a "token".
  - A "token" is just a string with some content that we can use later to verify this user.
  - Normally, a token is set to expire after some time.
    * So, the user will have ot log in again at some point later.
    * And if the token is stolen, the risk is less.  It is not like a permanent key that will work forever (in most cases).
* The frontend stores that "token" temporarily somewhere.
* The user clicks in the frontend to go to another section of the frontend web app.
* The frontend needs to fetch some more data from the API.
  - But it needs authentication for that specific endpoint.
  - So, to authenticate with our API, it sends a header ```Authorization``` with a value of ```Bearer <token>```
  - If the token contains ```foobar```, the header will be ```Authorization``` header would be: ```Bearer foobar```.

### FastAPI's ```OAuth2PasswordBearer```

**FastAPI** provides several tools, at different levels of abstraction, to implement these security features.

```Python
from typing import Annotated

from fastapi import Depends, FastAPI
from fastapi.security import OAuth2PasswordBearer

app = FastAPI()

oauth2_scheme = OAuth2PasswordBearer(tokenUrl="token")
    
@app.get("/items/")
async def read_items(token: str = Depends(oauth2_scheme)):
    return {"token": token}
```

Here ```tokenUrl="token"``` refers to a relative URL ```token``` that we haven't created yet. As it's a relative URL, it's
equivalent to ```./token.```.

Because we are using a relative URL, if your API was located at ```https://example.com/```, then it would refer to ```https://example.com/token```. 
But if yoru API was located at ```https://example.com/api/v1```, then it would refer to ```https://example.com/api/v1/token```.



## References

- [Fast API Security](https://fastapi.tiangolo.com/tutorial/security/)