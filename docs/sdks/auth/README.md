# Auth

## Overview

Obtain and refresh API access tokens.

### Available Operations

* [login_with_password](#login_with_password) - Login With Password
* [refresh_token](#refresh_token) - Refresh Token

## login_with_password

Retrieve a short lived auth token using your username and password.
Only accounts created directly in the app are supported, third party accounts (Google, Linkedin) are not supported

### Example Usage

<!-- UsageSnippet language="python" operationID="auth_login_with_password" method="post" path="/auth/login/password" -->
```python
from flypix import FlyPix


with FlyPix() as fly_pix:

    res = fly_pix.auth.login_with_password(username="Allie.Hartmann", password="9ne8TpFJLsebftr")

    # Handle response
    print(res)

```

### Parameters

| Parameter                                                           | Type                                                                | Required                                                            | Description                                                         |
| ------------------------------------------------------------------- | ------------------------------------------------------------------- | ------------------------------------------------------------------- | ------------------------------------------------------------------- |
| `username`                                                          | *str*                                                               | :heavy_check_mark:                                                  | N/A                                                                 |
| `password`                                                          | *str*                                                               | :heavy_check_mark:                                                  | N/A                                                                 |
| `retries`                                                           | [Optional[utils.RetryConfig]](../../models/utils/retryconfig.md)    | :heavy_minus_sign:                                                  | Configuration to override the default retry behavior of the client. |

### Response

**[models.LoginResponse](../../models/loginresponse.md)**

### Errors

| Error Type                | Status Code               | Content Type              |
| ------------------------- | ------------------------- | ------------------------- |
| errors.FlyPixDefaultError | 4XX, 5XX                  | \*/\*                     |

## refresh_token

Get a new short lived authentication token using the refresh token

### Example Usage

<!-- UsageSnippet language="python" operationID="auth_refresh_token" method="post" path="/auth/refresh" -->
```python
from flypix import FlyPix


with FlyPix(
    bearer_auth="<YOUR_BEARER_TOKEN_HERE>",
) as fly_pix:

    res = fly_pix.auth.refresh_token(refresh_token="<value>")

    # Handle response
    print(res)

```

### Parameters

| Parameter                                                           | Type                                                                | Required                                                            | Description                                                         |
| ------------------------------------------------------------------- | ------------------------------------------------------------------- | ------------------------------------------------------------------- | ------------------------------------------------------------------- |
| `refresh_token`                                                     | *str*                                                               | :heavy_check_mark:                                                  | N/A                                                                 |
| `retries`                                                           | [Optional[utils.RetryConfig]](../../models/utils/retryconfig.md)    | :heavy_minus_sign:                                                  | Configuration to override the default retry behavior of the client. |

### Response

**[models.LoginResponse](../../models/loginresponse.md)**

### Errors

| Error Type                | Status Code               | Content Type              |
| ------------------------- | ------------------------- | ------------------------- |
| errors.FlyPixDefaultError | 4XX, 5XX                  | \*/\*                     |