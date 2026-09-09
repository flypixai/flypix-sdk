# Users

## Overview

User account details and tenant membership.

### Available Operations

* [list_tenants](#list_tenants) - Get Tenants For User

## list_tenants

List the tenants available for the user

### Example Usage

<!-- UsageSnippet language="python" operationID="users_list_tenants" method="get" path="/users/tenants/for-user/" -->
```python
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

### Parameters

| Parameter                                                           | Type                                                                | Required                                                            | Description                                                         |
| ------------------------------------------------------------------- | ------------------------------------------------------------------- | ------------------------------------------------------------------- | ------------------------------------------------------------------- |
| `retries`                                                           | [Optional[utils.RetryConfig]](../../models/utils/retryconfig.md)    | :heavy_minus_sign:                                                  | Configuration to override the default retry behavior of the client. |

### Response

**[List[models.TenantResponse]](../../models/.md)**

### Errors

| Error Type                                                    | Status Code                                                   | Content Type                                                  |
| ------------------------------------------------------------- | ------------------------------------------------------------- | ------------------------------------------------------------- |
| errors.UsersListTenantsBadRequestErrorResponseSchema          | 400                                                           | application/json                                              |
| errors.UsersListTenantsForbiddenErrorResponseSchema           | 403                                                           | application/json                                              |
| errors.UsersListTenantsNotFoundErrorResponseSchema            | 404                                                           | application/json                                              |
| errors.UsersListTenantsInternalServerErrorErrorResponseSchema | 500                                                           | application/json                                              |
| errors.FlyPixDefaultError                                     | 4XX, 5XX                                                      | \*/\*                                                         |