# Payments

## Overview

Billing and tenant balance.

### Available Operations

* [get_balance](#get_balance) - Get Tenant Balance
* [get_tenant_transactions_payments_balance_tenant_id_transactions_get](#get_tenant_transactions_payments_balance_tenant_id_transactions_get) - Get Tenant Transactions

## get_balance

Get the current numerical credit balance for the specified tenant.

### Example Usage

<!-- UsageSnippet language="python" operationID="payments_get_balance" method="get" path="/payments/balance/{tenant_id}" -->
```python
from flypix import Flypix, models


with Flypix(
    security=models.Security(
        api_key="<YOUR_API_KEY_HERE>",
    ),
) as f_client:

    res = f_client.payments.get_balance(tenant_id="123e4567-e89b-12d3-a456-426614174000")

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

| Error Type                                                      | Status Code                                                     | Content Type                                                    |
| --------------------------------------------------------------- | --------------------------------------------------------------- | --------------------------------------------------------------- |
| errors.PaymentsGetBalanceBadRequestErrorResponseSchema          | 400                                                             | application/json                                                |
| errors.PaymentsGetBalanceForbiddenErrorResponseSchema           | 403                                                             | application/json                                                |
| errors.PaymentsGetBalanceNotFoundErrorResponseSchema            | 404                                                             | application/json                                                |
| errors.PaymentsGetBalanceInternalServerErrorErrorResponseSchema | 500                                                             | application/json                                                |
| errors.FlyPixDefaultError                                       | 4XX, 5XX                                                        | \*/\*                                                           |

## get_tenant_transactions_payments_balance_tenant_id_transactions_get

Get the paginated list of transactions for the specified tenant.

### Example Usage

<!-- UsageSnippet language="python" operationID="get_tenant_transactions_payments_balance__tenant_id__transactions_get" method="get" path="/payments/balance/{tenant_id}/transactions" -->
```python
from flypix import Flypix, models


with Flypix(
    security=models.Security(
        api_key="<YOUR_API_KEY_HERE>",
    ),
) as f_client:

    res = f_client.payments.get_tenant_transactions_payments_balance_tenant_id_transactions_get(tenant_id="123e4567-e89b-12d3-a456-426614174000", offset=0, limit=200)

    # Handle response
    print(res)

```

### Parameters

| Parameter                                                           | Type                                                                | Required                                                            | Description                                                         | Example                                                             |
| ------------------------------------------------------------------- | ------------------------------------------------------------------- | ------------------------------------------------------------------- | ------------------------------------------------------------------- | ------------------------------------------------------------------- |
| `tenant_id`                                                         | *str*                                                               | :heavy_check_mark:                                                  | N/A                                                                 | 123e4567-e89b-12d3-a456-426614174000                                |
| `offset`                                                            | *Optional[int]*                                                     | :heavy_minus_sign:                                                  | N/A                                                                 |                                                                     |
| `limit`                                                             | *Optional[int]*                                                     | :heavy_minus_sign:                                                  | N/A                                                                 |                                                                     |
| `retries`                                                           | [Optional[utils.RetryConfig]](../../models/utils/retryconfig.md)    | :heavy_minus_sign:                                                  | Configuration to override the default retry behavior of the client. |                                                                     |

### Response

**[List[models.TransactionResponse]](../../models/.md)**

### Errors

| Error Type                                                                                               | Status Code                                                                                              | Content Type                                                                                             |
| -------------------------------------------------------------------------------------------------------- | -------------------------------------------------------------------------------------------------------- | -------------------------------------------------------------------------------------------------------- |
| errors.GetTenantTransactionsPaymentsBalanceTenantIDTransactionsGetBadRequestErrorResponseSchema          | 400                                                                                                      | application/json                                                                                         |
| errors.GetTenantTransactionsPaymentsBalanceTenantIDTransactionsGetForbiddenErrorResponseSchema           | 403                                                                                                      | application/json                                                                                         |
| errors.GetTenantTransactionsPaymentsBalanceTenantIDTransactionsGetNotFoundErrorResponseSchema            | 404                                                                                                      | application/json                                                                                         |
| errors.GetTenantTransactionsPaymentsBalanceTenantIDTransactionsGetInternalServerErrorErrorResponseSchema | 500                                                                                                      | application/json                                                                                         |
| errors.FlyPixDefaultError                                                                                | 4XX, 5XX                                                                                                 | \*/\*                                                                                                    |