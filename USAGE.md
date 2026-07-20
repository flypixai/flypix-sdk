<!-- Start SDK Example Usage [usage] -->
### List tenants for the current user

```python
# Synchronous Example
from flypix import Flypix, models


with Flypix(
    security=models.Security(
        api_key="<YOUR_API_KEY_HERE>",
    ),
) as f_client:

    res = f_client.users.list_tenants()

    # Handle response
    print(res)
```

</br>

The same SDK client can also be used to make asynchronous requests by importing asyncio.

```python
# Asynchronous Example
import asyncio
from flypix import Flypix, models

async def main():

    async with Flypix(
        security=models.Security(
            api_key="<YOUR_API_KEY_HERE>",
        ),
    ) as f_client:

        res = await f_client.users.list_tenants_async()

        # Handle response
        print(res)

asyncio.run(main())
```
<!-- End SDK Example Usage [usage] -->