# Inferences

## Overview

Inference results across tenants, projects, and files.

### Available Operations

* [list_for_tenant](#list_for_tenant) - Get Inferences For Tenant
* [list_for_project](#list_for_project) - Get Inferences For Project
* [list_for_file](#list_for_file) - Get Inferences For File

## list_for_tenant

List the inferences in the tenant

### Example Usage

<!-- UsageSnippet language="python" operationID="inferences_list_for_tenant" method="get" path="/inferences/for-tenant/{tenant_id}" -->
```python
from flypix import FlyPix, models


with FlyPix(
    security=models.Security(
        bearer_auth="<YOUR_BEARER_TOKEN_HERE>",
    ),
) as fly_pix:

    res = fly_pix.inferences.list_for_tenant(tenant_id="123e4567-e89b-12d3-a456-426614174000")

    # Handle response
    print(res)

```

### Parameters

| Parameter                                                           | Type                                                                | Required                                                            | Description                                                         | Example                                                             |
| ------------------------------------------------------------------- | ------------------------------------------------------------------- | ------------------------------------------------------------------- | ------------------------------------------------------------------- | ------------------------------------------------------------------- |
| `tenant_id`                                                         | *str*                                                               | :heavy_check_mark:                                                  | N/A                                                                 | 123e4567-e89b-12d3-a456-426614174000                                |
| `retries`                                                           | [Optional[utils.RetryConfig]](../../models/utils/retryconfig.md)    | :heavy_minus_sign:                                                  | Configuration to override the default retry behavior of the client. |                                                                     |

### Response

**[List[models.InferenceResponse]](../../models/.md)**

### Errors

| Error Type                | Status Code               | Content Type              |
| ------------------------- | ------------------------- | ------------------------- |
| errors.FlyPixDefaultError | 4XX, 5XX                  | \*/\*                     |

## list_for_project

List the inferences in the project

### Example Usage

<!-- UsageSnippet language="python" operationID="inferences_list_for_project" method="get" path="/inferences/for-project/{project_id}" -->
```python
from flypix import FlyPix, models


with FlyPix(
    security=models.Security(
        bearer_auth="<YOUR_BEARER_TOKEN_HERE>",
    ),
) as fly_pix:

    res = fly_pix.inferences.list_for_project(project_id="123e4567-e89b-12d3-a456-426614174000")

    # Handle response
    print(res)

```

### Parameters

| Parameter                                                           | Type                                                                | Required                                                            | Description                                                         | Example                                                             |
| ------------------------------------------------------------------- | ------------------------------------------------------------------- | ------------------------------------------------------------------- | ------------------------------------------------------------------- | ------------------------------------------------------------------- |
| `project_id`                                                        | *str*                                                               | :heavy_check_mark:                                                  | N/A                                                                 | 123e4567-e89b-12d3-a456-426614174000                                |
| `retries`                                                           | [Optional[utils.RetryConfig]](../../models/utils/retryconfig.md)    | :heavy_minus_sign:                                                  | Configuration to override the default retry behavior of the client. |                                                                     |

### Response

**[List[models.InferenceResponse]](../../models/.md)**

### Errors

| Error Type                | Status Code               | Content Type              |
| ------------------------- | ------------------------- | ------------------------- |
| errors.FlyPixDefaultError | 4XX, 5XX                  | \*/\*                     |

## list_for_file

List the inferences for the file

### Example Usage

<!-- UsageSnippet language="python" operationID="inferences_list_for_file" method="get" path="/inferences/for-file/{file_id}" -->
```python
from flypix import FlyPix, models


with FlyPix(
    security=models.Security(
        bearer_auth="<YOUR_BEARER_TOKEN_HERE>",
    ),
) as fly_pix:

    res = fly_pix.inferences.list_for_file(file_id="123e4567-e89b-12d3-a456-426614174000")

    # Handle response
    print(res)

```

### Parameters

| Parameter                                                           | Type                                                                | Required                                                            | Description                                                         | Example                                                             |
| ------------------------------------------------------------------- | ------------------------------------------------------------------- | ------------------------------------------------------------------- | ------------------------------------------------------------------- | ------------------------------------------------------------------- |
| `file_id`                                                           | *str*                                                               | :heavy_check_mark:                                                  | N/A                                                                 | 123e4567-e89b-12d3-a456-426614174000                                |
| `retries`                                                           | [Optional[utils.RetryConfig]](../../models/utils/retryconfig.md)    | :heavy_minus_sign:                                                  | Configuration to override the default retry behavior of the client. |                                                                     |

### Response

**[List[models.InferenceResponse]](../../models/.md)**

### Errors

| Error Type                | Status Code               | Content Type              |
| ------------------------- | ------------------------- | ------------------------- |
| errors.FlyPixDefaultError | 4XX, 5XX                  | \*/\*                     |