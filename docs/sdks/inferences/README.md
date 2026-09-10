# Inferences

## Overview

### Available Operations

* [get_inferences_for_project](#get_inferences_for_project) - List project inferences
* [get_inferences_for_raster](#get_inferences_for_raster) - List raster inferences
* [get_inferences_for_tenant](#get_inferences_for_tenant) - List tenant inferences
* [get_inferences_by_ids](#get_inferences_by_ids) - Get inferences by ids

## get_inferences_for_project

Lists the inferences in a project.

### Example Usage

<!-- UsageSnippet language="python" operationID="get-inferences-for-project" method="get" path="/v2/inferences/for-project/{project_id}" -->
```python
from flypix import Flypix, models


with Flypix(
    security=models.Security(
        api_key="<YOUR_API_KEY_HERE>",
    ),
) as f_client:

    res = f_client.inferences.get_inferences_for_project(project_id="<id>", offset=0, limit=200)

    # Handle response
    print(res)

```

### Parameters

| Parameter                                                           | Type                                                                | Required                                                            | Description                                                         |
| ------------------------------------------------------------------- | ------------------------------------------------------------------- | ------------------------------------------------------------------- | ------------------------------------------------------------------- |
| `project_id`                                                        | *str*                                                               | :heavy_check_mark:                                                  | N/A                                                                 |
| `filter_`                                                           | *Optional[str]*                                                     | :heavy_minus_sign:                                                  | Comma-separated field:operator:value clauses, e.g. status:eq:FAILED |
| `sort`                                                              | *Optional[str]*                                                     | :heavy_minus_sign:                                                  | Comma-separated field:asc\|desc clauses, e.g. created_at:desc       |
| `offset`                                                            | *Optional[int]*                                                     | :heavy_minus_sign:                                                  | N/A                                                                 |
| `limit`                                                             | *Optional[int]*                                                     | :heavy_minus_sign:                                                  | N/A                                                                 |
| `retries`                                                           | [Optional[utils.RetryConfig]](../../models/utils/retryconfig.md)    | :heavy_minus_sign:                                                  | Configuration to override the default retry behavior of the client. |

### Response

**[models.GetInferencesForProjectResponse](../../models/getinferencesforprojectresponse.md)**

### Errors

| Error Type                | Status Code               | Content Type              |
| ------------------------- | ------------------------- | ------------------------- |
| errors.FlyPixDefaultError | 4XX, 5XX                  | \*/\*                     |

## get_inferences_for_raster

Lists the inferences for a raster.

### Example Usage

<!-- UsageSnippet language="python" operationID="get-inferences-for-raster" method="get" path="/v2/inferences/for-raster/{raster_id}" -->
```python
from flypix import Flypix, models


with Flypix(
    security=models.Security(
        api_key="<YOUR_API_KEY_HERE>",
    ),
) as f_client:

    res = f_client.inferences.get_inferences_for_raster(raster_id="<id>")

    # Handle response
    print(res)

```

### Parameters

| Parameter                                                           | Type                                                                | Required                                                            | Description                                                         |
| ------------------------------------------------------------------- | ------------------------------------------------------------------- | ------------------------------------------------------------------- | ------------------------------------------------------------------- |
| `raster_id`                                                         | *str*                                                               | :heavy_check_mark:                                                  | N/A                                                                 |
| `retries`                                                           | [Optional[utils.RetryConfig]](../../models/utils/retryconfig.md)    | :heavy_minus_sign:                                                  | Configuration to override the default retry behavior of the client. |

### Response

**[models.GetInferencesForRasterResponse](../../models/getinferencesforrasterresponse.md)**

### Errors

| Error Type                | Status Code               | Content Type              |
| ------------------------- | ------------------------- | ------------------------- |
| errors.FlyPixDefaultError | 4XX, 5XX                  | \*/\*                     |

## get_inferences_for_tenant

Lists the inferences in a tenant.

### Example Usage

<!-- UsageSnippet language="python" operationID="get-inferences-for-tenant" method="get" path="/v2/inferences/for-tenant/{tenant_id}" -->
```python
from flypix import Flypix, models


with Flypix(
    security=models.Security(
        api_key="<YOUR_API_KEY_HERE>",
    ),
) as f_client:

    res = f_client.inferences.get_inferences_for_tenant(tenant_id="<id>", offset=0, limit=200)

    # Handle response
    print(res)

```

### Parameters

| Parameter                                                           | Type                                                                | Required                                                            | Description                                                         |
| ------------------------------------------------------------------- | ------------------------------------------------------------------- | ------------------------------------------------------------------- | ------------------------------------------------------------------- |
| `tenant_id`                                                         | *str*                                                               | :heavy_check_mark:                                                  | N/A                                                                 |
| `filter_`                                                           | *Optional[str]*                                                     | :heavy_minus_sign:                                                  | Comma-separated field:operator:value clauses, e.g. status:eq:FAILED |
| `sort`                                                              | *Optional[str]*                                                     | :heavy_minus_sign:                                                  | Comma-separated field:asc\|desc clauses, e.g. created_at:desc       |
| `offset`                                                            | *Optional[int]*                                                     | :heavy_minus_sign:                                                  | N/A                                                                 |
| `limit`                                                             | *Optional[int]*                                                     | :heavy_minus_sign:                                                  | N/A                                                                 |
| `retries`                                                           | [Optional[utils.RetryConfig]](../../models/utils/retryconfig.md)    | :heavy_minus_sign:                                                  | Configuration to override the default retry behavior of the client. |

### Response

**[models.GetInferencesForTenantResponse](../../models/getinferencesfortenantresponse.md)**

### Errors

| Error Type                | Status Code               | Content Type              |
| ------------------------- | ------------------------- | ------------------------- |
| errors.FlyPixDefaultError | 4XX, 5XX                  | \*/\*                     |

## get_inferences_by_ids

Returns the inferences matching the given ids, in one call.

### Example Usage

<!-- UsageSnippet language="python" operationID="get-inferences-by-ids" method="post" path="/v2/inferences/get-by-ids" -->
```python
from flypix import Flypix, models


with Flypix(
    security=models.Security(
        api_key="<YOUR_API_KEY_HERE>",
    ),
) as f_client:

    res = f_client.inferences.get_inferences_by_ids(request=[
        "<value 1>",
        "<value 2>",
        "<value 3>",
    ])

    # Handle response
    print(res)

```

### Parameters

| Parameter                                                           | Type                                                                | Required                                                            | Description                                                         |
| ------------------------------------------------------------------- | ------------------------------------------------------------------- | ------------------------------------------------------------------- | ------------------------------------------------------------------- |
| `request`                                                           | [List[str]](../../models/.md)                                       | :heavy_check_mark:                                                  | The request object to use for the request.                          |
| `retries`                                                           | [Optional[utils.RetryConfig]](../../models/utils/retryconfig.md)    | :heavy_minus_sign:                                                  | Configuration to override the default retry behavior of the client. |

### Response

**[models.GetInferencesByIdsResponse](../../models/getinferencesbyidsresponse.md)**

### Errors

| Error Type                | Status Code               | Content Type              |
| ------------------------- | ------------------------- | ------------------------- |
| errors.FlyPixDefaultError | 4XX, 5XX                  | \*/\*                     |