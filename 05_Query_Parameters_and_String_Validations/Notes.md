FastAPI will know that the value of q is not required because of the default value = None.

Having str | None will allow your editor to give you better support and detect errors.

```Annotated``` is used like this:

```bash
Annotated[type, metadata]
```