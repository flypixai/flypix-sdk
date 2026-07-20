# Payments

## Overview

Billing and tenant balance.

### Available Operations

* [get_balance](#get_balance) - Get Tenant Balance

## get_balance

Get current balance and list of transactions for the specified tenant.

### Example Usage

<!-- UsageSnippet language="python" operationID="payments_get_balance" method="get" path="/payments/balance/{tenant_id}" -->
```python
from flypix import FlyPix, models


with FlyPix(
    security=models.Security(
        bearer_auth="<YOUR_BEARER_TOKEN_HERE>",
    ),
) as fly_pix:

    res = fly_pix.payments.get_balance(tenant_id="123e4567-e89b-12d3-a456-426614174000")

    # Handle response
    print(res)

```

### Parameters

| Parameter                                                           | Type                                                                | Required                                                            | Description                                                         | Example                                                             |
| ------------------------------------------------------------------- | ------------------------------------------------------------------- | ------------------------------------------------------------------- | ------------------------------------------------------------------- | ------------------------------------------------------------------- |
| `tenant_id`                                                         | *str*                                                               | :heavy_check_mark:                                                  | N/A                                                                 | 123e4567-e89b-12d3-a456-426614174000                                |
| `retries`                                                           | [Optional[utils.RetryConfig]](../../models/utils/retryconfig.md)    | :heavy_minus_sign:                                                  | Configuration to override the default retry behavior of the client. |                                                                     |

### Response

**[models.BalanceResponse](../../models/balanceresponse.md)**

### Errors

| Error Type                | Status Code               | Content Type              |
| ------------------------- | ------------------------- | ------------------------- |
| errors.FlyPixDefaultError | 4XX, 5XX                  | \*/\*                     |