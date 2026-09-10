<!-- Start SDK Example Usage [usage] -->
```python
# Synchronous Example
from flypix import Flypix


with Flypix() as f_client:

    res = f_client.system.health()

    # Handle response
    print(res)
```

</br>

The same SDK client can also be used to make asynchronous requests by importing asyncio.

```python
# Asynchronous Example
import asyncio
from flypix import Flypix

async def main():

    async with Flypix() as f_client:

        res = await f_client.system.health_async()

        # Handle response
        print(res)

asyncio.run(main())
```
<!-- End SDK Example Usage [usage] -->