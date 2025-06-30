To send data, you should use one of: ```POST``` (the more common), ```PUT```, ```DELETE``` or ```PATCH.```

Sending a body with a GET request has an undefined behavior in the specifications, nevertheless, it is supported by FastAPI, only for very complex/extreme use cases.

```Note```: As it is discouraged, the interactive docs with Swagger UI won't show the documentation for the body when using GET, and proxies in the middle might not support it.