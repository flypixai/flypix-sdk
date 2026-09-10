# Users

## Overview

### Available Operations

* [get_tenants_for_user](#get_tenants_for_user) - List tenants for user

## get_tenants_for_user

Lists the tenants the authenticated user has access to.

### Example Usage

<!-- UsageSnippet language="python" operationID="get-tenants-for-user" method="get" path="/v2/users/tenants/for-user/" -->
```python
from flypix import Flypix, models


with Flypix(
    security=models.Security(
        api_key="<YOUR_API_KEY_HERE>",
    ),
) as f_client:

    res = f_client.users.get_tenants_for_user()

    # Handle response
    print(res)

```

### Parameters

| Parameter                                                           | Type                                                                | Required                                                            | Description                                                         |
| ------------------------------------------------------------------- | ------------------------------------------------------------------- | ------------------------------------------------------------------- | ------------------------------------------------------------------- |
| `retries`                                                           | [Optional[utils.RetryConfig]](../../models/utils/retryconfig.md)    | :heavy_minus_sign:                                                  | Configuration to override the default retry behavior of the client. |

### Response

**[models.GetTenantsForUserResponse](../../models/gettenantsforuserresponse.md)**

### Errors

| Error Type                | Status Code               | Content Type              |
| ------------------------- | ------------------------- | ------------------------- |
| errors.FlyPixDefaultError | 4XX, 5XX                  | \*/\*                     |