# Models

## Overview

List, apply, and manage detection models.

### Available Operations

* [list_for_tenant](#list_for_tenant) - Get Models For Tenant
* [list_for_project](#list_for_project) - Get Models For Project
* [list_official](#list_official) - Get Official Models
* [apply](#apply) - Apply Model On File
* [estimate_application](#estimate_application) - Estimate Model Application On File
* [get_inference_status](#get_inference_status) - Get Inference Status
* [delete](#delete) - Delete Model

## list_for_tenant

List the models available in the tenant

### Example Usage

<!-- UsageSnippet language="python" operationID="models_list_for_tenant" method="get" path="/models/for-tenant/{tenant_id}" -->
```python
from flypix import FlyPix, models


with FlyPix(
    security=models.Security(
        bearer_auth="<YOUR_BEARER_TOKEN_HERE>",
    ),
) as fly_pix:

    res = fly_pix.models.list_for_tenant(tenant_id="123e4567-e89b-12d3-a456-426614174000")

    # Handle response
    print(res)

```

### Parameters

| Parameter                                                           | Type                                                                | Required                                                            | Description                                                         | Example                                                             |
| ------------------------------------------------------------------- | ------------------------------------------------------------------- | ------------------------------------------------------------------- | ------------------------------------------------------------------- | ------------------------------------------------------------------- |
| `tenant_id`                                                         | *str*                                                               | :heavy_check_mark:                                                  | N/A                                                                 | 123e4567-e89b-12d3-a456-426614174000                                |
| `retries`                                                           | [Optional[utils.RetryConfig]](../../models/utils/retryconfig.md)    | :heavy_minus_sign:                                                  | Configuration to override the default retry behavior of the client. |                                                                     |

### Response

**[List[models.PrivateModelResponse]](../../models/.md)**

### Errors

| Error Type                | Status Code               | Content Type              |
| ------------------------- | ------------------------- | ------------------------- |
| errors.FlyPixDefaultError | 4XX, 5XX                  | \*/\*                     |

## list_for_project

List the models available to be applied in any file in the project

### Example Usage

<!-- UsageSnippet language="python" operationID="models_list_for_project" method="get" path="/models/for-project/{project_id}" -->
```python
from flypix import FlyPix, models


with FlyPix(
    security=models.Security(
        bearer_auth="<YOUR_BEARER_TOKEN_HERE>",
    ),
) as fly_pix:

    res = fly_pix.models.list_for_project(project_id="123e4567-e89b-12d3-a456-426614174000")

    # Handle response
    print(res)

```

### Parameters

| Parameter                                                           | Type                                                                | Required                                                            | Description                                                         | Example                                                             |
| ------------------------------------------------------------------- | ------------------------------------------------------------------- | ------------------------------------------------------------------- | ------------------------------------------------------------------- | ------------------------------------------------------------------- |
| `project_id`                                                        | *str*                                                               | :heavy_check_mark:                                                  | N/A                                                                 | 123e4567-e89b-12d3-a456-426614174000                                |
| `retries`                                                           | [Optional[utils.RetryConfig]](../../models/utils/retryconfig.md)    | :heavy_minus_sign:                                                  | Configuration to override the default retry behavior of the client. |                                                                     |

### Response

**[List[models.PrivateModelResponse]](../../models/.md)**

### Errors

| Error Type                | Status Code               | Content Type              |
| ------------------------- | ------------------------- | ------------------------- |
| errors.FlyPixDefaultError | 4XX, 5XX                  | \*/\*                     |

## list_official

List official models, available to be applied on any file in any project

### Example Usage

<!-- UsageSnippet language="python" operationID="models_list_official" method="get" path="/models/official" -->
```python
from flypix import FlyPix, models


with FlyPix(
    security=models.Security(
        bearer_auth="<YOUR_BEARER_TOKEN_HERE>",
    ),
) as fly_pix:

    res = fly_pix.models.list_official()

    # Handle response
    print(res)

```

### Parameters

| Parameter                                                           | Type                                                                | Required                                                            | Description                                                         |
| ------------------------------------------------------------------- | ------------------------------------------------------------------- | ------------------------------------------------------------------- | ------------------------------------------------------------------- |
| `retries`                                                           | [Optional[utils.RetryConfig]](../../models/utils/retryconfig.md)    | :heavy_minus_sign:                                                  | Configuration to override the default retry behavior of the client. |

### Response

**[List[models.OfficialModelResponse]](../../models/.md)**

### Errors

| Error Type                | Status Code               | Content Type              |
| ------------------------- | ------------------------- | ------------------------- |
| errors.FlyPixDefaultError | 4XX, 5XX                  | \*/\*                     |

## apply

Trigger the inference of a model on a file.
Note that inference is applied asynchronously so this won't return the
vector features

### Example Usage

<!-- UsageSnippet language="python" operationID="models_apply" method="post" path="/models/{model_id}/apply" -->
```python
from flypix import FlyPix, models


with FlyPix(
    security=models.Security(
        bearer_auth="<YOUR_BEARER_TOKEN_HERE>",
    ),
) as fly_pix:

    res = fly_pix.models.apply(model_id="123e4567-e89b-12d3-a456-426614174000", file_id="123e4567-e89b-12d3-a456-426614174000")

    # Handle response
    print(res)

```

### Parameters

| Parameter                                                           | Type                                                                | Required                                                            | Description                                                         | Example                                                             |
| ------------------------------------------------------------------- | ------------------------------------------------------------------- | ------------------------------------------------------------------- | ------------------------------------------------------------------- | ------------------------------------------------------------------- |
| `model_id`                                                          | *str*                                                               | :heavy_check_mark:                                                  | N/A                                                                 | 123e4567-e89b-12d3-a456-426614174000                                |
| `file_id`                                                           | *str*                                                               | :heavy_check_mark:                                                  | A string in UUID format                                             | 123e4567-e89b-12d3-a456-426614174000                                |
| `retries`                                                           | [Optional[utils.RetryConfig]](../../models/utils/retryconfig.md)    | :heavy_minus_sign:                                                  | Configuration to override the default retry behavior of the client. |                                                                     |

### Response

**[models.ApplyModelResponse](../../models/applymodelresponse.md)**

### Errors

| Error Type                | Status Code               | Content Type              |
| ------------------------- | ------------------------- | ------------------------- |
| errors.FlyPixDefaultError | 4XX, 5XX                  | \*/\*                     |

## estimate_application

Calculate the cost in credits to apply a model.

### Example Usage

<!-- UsageSnippet language="python" operationID="models_estimate_application" method="post" path="/models/{model_id}/apply/estimate" -->
```python
from flypix import FlyPix, models


with FlyPix(
    security=models.Security(
        bearer_auth="<YOUR_BEARER_TOKEN_HERE>",
    ),
) as fly_pix:

    res = fly_pix.models.estimate_application(model_id="123e4567-e89b-12d3-a456-426614174000", file_id="123e4567-e89b-12d3-a456-426614174000")

    # Handle response
    print(res)

```

### Parameters

| Parameter                                                           | Type                                                                | Required                                                            | Description                                                         | Example                                                             |
| ------------------------------------------------------------------- | ------------------------------------------------------------------- | ------------------------------------------------------------------- | ------------------------------------------------------------------- | ------------------------------------------------------------------- |
| `model_id`                                                          | *str*                                                               | :heavy_check_mark:                                                  | N/A                                                                 | 123e4567-e89b-12d3-a456-426614174000                                |
| `file_id`                                                           | *str*                                                               | :heavy_check_mark:                                                  | A string in UUID format                                             | 123e4567-e89b-12d3-a456-426614174000                                |
| `retries`                                                           | [Optional[utils.RetryConfig]](../../models/utils/retryconfig.md)    | :heavy_minus_sign:                                                  | Configuration to override the default retry behavior of the client. |                                                                     |

### Response

**[models.EstimateModelResponse](../../models/estimatemodelresponse.md)**

### Errors

| Error Type                | Status Code               | Content Type              |
| ------------------------- | ------------------------- | ------------------------- |
| errors.FlyPixDefaultError | 4XX, 5XX                  | \*/\*                     |

## get_inference_status

Get the current status of an inference from applying a model

### Example Usage

<!-- UsageSnippet language="python" operationID="models_get_inference_status" method="get" path="/models/inference/{inference_id}" -->
```python
from flypix import FlyPix, models


with FlyPix(
    security=models.Security(
        bearer_auth="<YOUR_BEARER_TOKEN_HERE>",
    ),
) as fly_pix:

    res = fly_pix.models.get_inference_status(inference_id="123e4567-e89b-12d3-a456-426614174000")

    # Handle response
    print(res)

```

### Parameters

| Parameter                                                           | Type                                                                | Required                                                            | Description                                                         | Example                                                             |
| ------------------------------------------------------------------- | ------------------------------------------------------------------- | ------------------------------------------------------------------- | ------------------------------------------------------------------- | ------------------------------------------------------------------- |
| `inference_id`                                                      | *str*                                                               | :heavy_check_mark:                                                  | N/A                                                                 | 123e4567-e89b-12d3-a456-426614174000                                |
| `retries`                                                           | [Optional[utils.RetryConfig]](../../models/utils/retryconfig.md)    | :heavy_minus_sign:                                                  | Configuration to override the default retry behavior of the client. |                                                                     |

### Response

**[models.ApplyModelResponse](../../models/applymodelresponse.md)**

### Errors

| Error Type                | Status Code               | Content Type              |
| ------------------------- | ------------------------- | ------------------------- |
| errors.FlyPixDefaultError | 4XX, 5XX                  | \*/\*                     |

## delete

Delete an already trained model. This operation cannot be undone

### Example Usage

<!-- UsageSnippet language="python" operationID="models_delete" method="delete" path="/models/{model_id}" -->
```python
from flypix import FlyPix, models


with FlyPix(
    security=models.Security(
        bearer_auth="<YOUR_BEARER_TOKEN_HERE>",
    ),
) as fly_pix:

    res = fly_pix.models.delete(model_id="123e4567-e89b-12d3-a456-426614174000")

    # Handle response
    print(res)

```

### Parameters

| Parameter                                                           | Type                                                                | Required                                                            | Description                                                         | Example                                                             |
| ------------------------------------------------------------------- | ------------------------------------------------------------------- | ------------------------------------------------------------------- | ------------------------------------------------------------------- | ------------------------------------------------------------------- |
| `model_id`                                                          | *str*                                                               | :heavy_check_mark:                                                  | N/A                                                                 | 123e4567-e89b-12d3-a456-426614174000                                |
| `retries`                                                           | [Optional[utils.RetryConfig]](../../models/utils/retryconfig.md)    | :heavy_minus_sign:                                                  | Configuration to override the default retry behavior of the client. |                                                                     |

### Response

**[models.EntityDeletionResponse](../../models/entitydeletionresponse.md)**

### Errors

| Error Type                | Status Code               | Content Type              |
| ------------------------- | ------------------------- | ------------------------- |
| errors.FlyPixDefaultError | 4XX, 5XX                  | \*/\*                     |