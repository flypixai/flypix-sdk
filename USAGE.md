<!-- Start SDK Example Usage [usage] -->
```python
# Synchronous Example
from flypix import FlyPix


with FlyPix() as fly_pix:

    res = fly_pix.auth.login_with_password(username="Allie.Hartmann", password="9ne8TpFJLsebftr")

    # Handle response
    print(res)
```

</br>

The same SDK client can also be used to make asynchronous requests by importing asyncio.

```python
# Asynchronous Example
import asyncio
from flypix import FlyPix

async def main():

    async with FlyPix() as fly_pix:

        res = await fly_pix.auth.login_with_password_async(username="Allie.Hartmann", password="9ne8TpFJLsebftr")

        # Handle response
        print(res)

asyncio.run(main())
```
<!-- End SDK Example Usage [usage] -->