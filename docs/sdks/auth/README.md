# Auth

## Overview

### Available Operations

* [login_with_password](#login_with_password) - Login with password
* [refresh_token](#refresh_token) - Refresh token

## login_with_password

Exchanges a username and password for a token. Not available when the tenant's identity provider is DESP.

### Example Usage

<!-- UsageSnippet language="python" operationID="login-with-password" method="post" path="/v2/auth/login/password" -->
```python
from flypix import Flypix


with Flypix() as f_client:

    res = f_client.auth.login_with_password(password="N_EG18c_GGYVFM4", username="William_Kulas")

    # Handle response
    print(res)

```

### Parameters

| Parameter                                                           | Type                                                                | Required                                                            | Description                                                         |
| ------------------------------------------------------------------- | ------------------------------------------------------------------- | ------------------------------------------------------------------- | ------------------------------------------------------------------- |
| `password`                                                          | *str*                                                               | :heavy_check_mark:                                                  | N/A                                                                 |
| `username`                                                          | *str*                                                               | :heavy_check_mark:                                                  | N/A                                                                 |
| `retries`                                                           | [Optional[utils.RetryConfig]](../../models/utils/retryconfig.md)    | :heavy_minus_sign:                                                  | Configuration to override the default retry behavior of the client. |

### Response

**[models.LoginWithPasswordResponse](../../models/loginwithpasswordresponse.md)**

### Errors

| Error Type                | Status Code               | Content Type              |
| ------------------------- | ------------------------- | ------------------------- |
| errors.FlyPixDefaultError | 4XX, 5XX                  | \*/\*                     |

## refresh_token

Exchanges a refresh token for a new token. Not available when the tenant's identity provider is DESP.

### Example Usage

<!-- UsageSnippet language="python" operationID="refresh-token" method="post" path="/v2/auth/refresh" -->
```python
from flypix import Flypix


with Flypix() as f_client:

    res = f_client.auth.refresh_token(refresh_token="<value>")

    # Handle response
    print(res)

```

### Parameters

| Parameter                                                           | Type                                                                | Required                                                            | Description                                                         |
| ------------------------------------------------------------------- | ------------------------------------------------------------------- | ------------------------------------------------------------------- | ------------------------------------------------------------------- |
| `refresh_token`                                                     | *str*                                                               | :heavy_check_mark:                                                  | N/A                                                                 |
| `retries`                                                           | [Optional[utils.RetryConfig]](../../models/utils/retryconfig.md)    | :heavy_minus_sign:                                                  | Configuration to override the default retry behavior of the client. |

### Response

**[models.RefreshTokenResponse](../../models/refreshtokenresponse.md)**

### Errors

| Error Type                | Status Code               | Content Type              |
| ------------------------- | ------------------------- | ------------------------- |
| errors.FlyPixDefaultError | 4XX, 5XX                  | \*/\*                     |