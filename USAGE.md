<!-- Start SDK Example Usage [usage] -->
### List tenants for the current user

```python
# Synchronous Example
from flypix import FlyPix, models


with FlyPix(
    security=models.Security(
        api_key="<YOUR_API_KEY_HERE>",
    ),
) as fly_pix:

    res = fly_pix.users.list_tenants()

    # Handle response
    print(res)
```

</br>

The same SDK client can also be used to make asynchronous requests by importing asyncio.

```python
# Asynchronous Example
import asyncio
from flypix import FlyPix, models

async def main():

    async with FlyPix(
        security=models.Security(
            api_key="<YOUR_API_KEY_HERE>",
        ),
    ) as fly_pix:

        res = await fly_pix.users.list_tenants_async()

        # Handle response
        print(res)

asyncio.run(main())
```
<!-- End SDK Example Usage [usage] -->