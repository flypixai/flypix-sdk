# System

## Overview

### Available Operations

* [health](#health) - Health check

## health

Reports whether the API is up. Does not check downstream backends.

### Example Usage

<!-- UsageSnippet language="python" operationID="health" method="get" path="/health" -->
```python
from flypix import Flypix


with Flypix() as f_client:

    res = f_client.system.health()

    # Handle response
    print(res)

```

### Parameters

| Parameter                                                           | Type                                                                | Required                                                            | Description                                                         |
| ------------------------------------------------------------------- | ------------------------------------------------------------------- | ------------------------------------------------------------------- | ------------------------------------------------------------------- |
| `retries`                                                           | [Optional[utils.RetryConfig]](../../models/utils/retryconfig.md)    | :heavy_minus_sign:                                                  | Configuration to override the default retry behavior of the client. |

### Response

**[models.HealthResponse](../../models/healthresponse.md)**

### Errors

| Error Type                | Status Code               | Content Type              |
| ------------------------- | ------------------------- | ------------------------- |
| errors.FlyPixDefaultError | 4XX, 5XX                  | \*/\*                     |