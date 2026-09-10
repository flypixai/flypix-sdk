# Models

## Overview

### Available Operations

* [apply_change_detection](#apply_change_detection) - Apply change detection
* [get_models_for_project](#get_models_for_project) - List project models
* [get_models_for_tenant](#get_models_for_tenant) - List tenant models
* [get_models_by_ids](#get_models_by_ids) - Get models by ids
* [get_inference_status](#get_inference_status) - Get inference status
* [get_official_models](#get_official_models) - List official models
* [delete_model](#delete_model) - Delete model
* [apply_model_on_raster](#apply_model_on_raster) - Apply model to raster
* [estimate_model_application_on_file](#estimate_model_application_on_file) - Estimate model application cost

## apply_change_detection

Triggers asynchronous change-detection inference between two rasters.

### Example Usage

<!-- UsageSnippet language="python" operationID="apply-change-detection" method="post" path="/v2/models/change-detection/apply" -->
```python
from flypix import Flypix, models


with Flypix(
    security=models.Security(
        api_key="<YOUR_API_KEY_HERE>",
    ),
) as f_client:

    res = f_client.models.apply_change_detection(raster_id_a="<value>", raster_id_b="<value>")

    # Handle response
    print(res)

```

### Parameters

| Parameter                                                           | Type                                                                | Required                                                            | Description                                                         |
| ------------------------------------------------------------------- | ------------------------------------------------------------------- | ------------------------------------------------------------------- | ------------------------------------------------------------------- |
| `raster_id_a`                                                       | *str*                                                               | :heavy_check_mark:                                                  | N/A                                                                 |
| `raster_id_b`                                                       | *str*                                                               | :heavy_check_mark:                                                  | N/A                                                                 |
| `retries`                                                           | [Optional[utils.RetryConfig]](../../models/utils/retryconfig.md)    | :heavy_minus_sign:                                                  | Configuration to override the default retry behavior of the client. |

### Response

**[models.ApplyChangeDetectionResponse](../../models/applychangedetectionresponse.md)**

### Errors

| Error Type                | Status Code               | Content Type              |
| ------------------------- | ------------------------- | ------------------------- |
| errors.FlyPixDefaultError | 4XX, 5XX                  | \*/\*                     |

## get_models_for_project

Lists the models available to be applied on any file in a project.

### Example Usage

<!-- UsageSnippet language="python" operationID="get-models-for-project" method="get" path="/v2/models/for-project/{project_id}" -->
```python
from flypix import Flypix, models


with Flypix(
    security=models.Security(
        api_key="<YOUR_API_KEY_HERE>",
    ),
) as f_client:

    res = f_client.models.get_models_for_project(project_id="<id>", offset=0, limit=200)

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

**[models.GetModelsForProjectResponse](../../models/getmodelsforprojectresponse.md)**

### Errors

| Error Type                | Status Code               | Content Type              |
| ------------------------- | ------------------------- | ------------------------- |
| errors.FlyPixDefaultError | 4XX, 5XX                  | \*/\*                     |

## get_models_for_tenant

Lists the models available in a tenant.

### Example Usage

<!-- UsageSnippet language="python" operationID="get-models-for-tenant" method="get" path="/v2/models/for-tenant/{tenant_id}" -->
```python
from flypix import Flypix, models


with Flypix(
    security=models.Security(
        api_key="<YOUR_API_KEY_HERE>",
    ),
) as f_client:

    res = f_client.models.get_models_for_tenant(tenant_id="<id>", offset=0, limit=200)

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

**[models.GetModelsForTenantResponse](../../models/getmodelsfortenantresponse.md)**

### Errors

| Error Type                | Status Code               | Content Type              |
| ------------------------- | ------------------------- | ------------------------- |
| errors.FlyPixDefaultError | 4XX, 5XX                  | \*/\*                     |

## get_models_by_ids

Returns the models matching the given ids, in one call.

### Example Usage

<!-- UsageSnippet language="python" operationID="get-models-by-ids" method="post" path="/v2/models/get-by-ids" -->
```python
from flypix import Flypix, models


with Flypix(
    security=models.Security(
        api_key="<YOUR_API_KEY_HERE>",
    ),
) as f_client:

    res = f_client.models.get_models_by_ids(request=[
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

**[models.GetModelsByIdsResponse](../../models/getmodelsbyidsresponse.md)**

### Errors

| Error Type                | Status Code               | Content Type              |
| ------------------------- | ------------------------- | ------------------------- |
| errors.FlyPixDefaultError | 4XX, 5XX                  | \*/\*                     |

## get_inference_status

Returns the current status of an inference from applying a model.

### Example Usage

<!-- UsageSnippet language="python" operationID="get-inference-status" method="get" path="/v2/models/inference/{inference_id}" -->
```python
from flypix import Flypix, models


with Flypix(
    security=models.Security(
        api_key="<YOUR_API_KEY_HERE>",
    ),
) as f_client:

    res = f_client.models.get_inference_status(inference_id="<id>")

    # Handle response
    print(res)

```

### Parameters

| Parameter                                                           | Type                                                                | Required                                                            | Description                                                         |
| ------------------------------------------------------------------- | ------------------------------------------------------------------- | ------------------------------------------------------------------- | ------------------------------------------------------------------- |
| `inference_id`                                                      | *str*                                                               | :heavy_check_mark:                                                  | N/A                                                                 |
| `retries`                                                           | [Optional[utils.RetryConfig]](../../models/utils/retryconfig.md)    | :heavy_minus_sign:                                                  | Configuration to override the default retry behavior of the client. |

### Response

**[models.GetInferenceStatusResponse](../../models/getinferencestatusresponse.md)**

### Errors

| Error Type                | Status Code               | Content Type              |
| ------------------------- | ------------------------- | ------------------------- |
| errors.FlyPixDefaultError | 4XX, 5XX                  | \*/\*                     |

## get_official_models

Lists official models, available to be applied on any file in any project.

### Example Usage

<!-- UsageSnippet language="python" operationID="get-official-models" method="get" path="/v2/models/official" -->
```python
from flypix import Flypix, models


with Flypix(
    security=models.Security(
        api_key="<YOUR_API_KEY_HERE>",
    ),
) as f_client:

    res = f_client.models.get_official_models()

    # Handle response
    print(res)

```

### Parameters

| Parameter                                                           | Type                                                                | Required                                                            | Description                                                         |
| ------------------------------------------------------------------- | ------------------------------------------------------------------- | ------------------------------------------------------------------- | ------------------------------------------------------------------- |
| `retries`                                                           | [Optional[utils.RetryConfig]](../../models/utils/retryconfig.md)    | :heavy_minus_sign:                                                  | Configuration to override the default retry behavior of the client. |

### Response

**[models.GetOfficialModelsResponse](../../models/getofficialmodelsresponse.md)**

### Errors

| Error Type                | Status Code               | Content Type              |
| ------------------------- | ------------------------- | ------------------------- |
| errors.FlyPixDefaultError | 4XX, 5XX                  | \*/\*                     |

## delete_model

Deletes an already-trained model. This cannot be undone.

### Example Usage

<!-- UsageSnippet language="python" operationID="delete-model" method="delete" path="/v2/models/{model_id}" -->
```python
from flypix import Flypix, models


with Flypix(
    security=models.Security(
        api_key="<YOUR_API_KEY_HERE>",
    ),
) as f_client:

    res = f_client.models.delete_model(model_id="<id>")

    # Handle response
    print(res)

```

### Parameters

| Parameter                                                           | Type                                                                | Required                                                            | Description                                                         |
| ------------------------------------------------------------------- | ------------------------------------------------------------------- | ------------------------------------------------------------------- | ------------------------------------------------------------------- |
| `model_id`                                                          | *str*                                                               | :heavy_check_mark:                                                  | N/A                                                                 |
| `retries`                                                           | [Optional[utils.RetryConfig]](../../models/utils/retryconfig.md)    | :heavy_minus_sign:                                                  | Configuration to override the default retry behavior of the client. |

### Response

**[models.DeleteModelResponse](../../models/deletemodelresponse.md)**

### Errors

| Error Type                | Status Code               | Content Type              |
| ------------------------- | ------------------------- | ------------------------- |
| errors.FlyPixDefaultError | 4XX, 5XX                  | \*/\*                     |

## apply_model_on_raster

Triggers asynchronous inference of a model on a raster. Returns 402 if the estimated cost exceeds the tenant's balance, unless its subscription grants unlimited credits.

### Example Usage

<!-- UsageSnippet language="python" operationID="apply-model-on-raster" method="post" path="/v2/models/{model_id}/apply" -->
```python
from flypix import Flypix, models


with Flypix(
    security=models.Security(
        api_key="<YOUR_API_KEY_HERE>",
    ),
) as f_client:

    res = f_client.models.apply_model_on_raster(model_id="<id>", raster_id="<id>")

    # Handle response
    print(res)

```

### Parameters

| Parameter                                                           | Type                                                                | Required                                                            | Description                                                         |
| ------------------------------------------------------------------- | ------------------------------------------------------------------- | ------------------------------------------------------------------- | ------------------------------------------------------------------- |
| `model_id`                                                          | *str*                                                               | :heavy_check_mark:                                                  | N/A                                                                 |
| `raster_id`                                                         | *str*                                                               | :heavy_check_mark:                                                  | N/A                                                                 |
| `retries`                                                           | [Optional[utils.RetryConfig]](../../models/utils/retryconfig.md)    | :heavy_minus_sign:                                                  | Configuration to override the default retry behavior of the client. |

### Response

**[models.ApplyModelOnRasterResponse](../../models/applymodelonrasterresponse.md)**

### Errors

| Error Type                | Status Code               | Content Type              |
| ------------------------- | ------------------------- | ------------------------- |
| errors.FlyPixDefaultError | 4XX, 5XX                  | \*/\*                     |

## estimate_model_application_on_file

Calculates the credit cost to apply a model on a raster, without triggering it.

### Example Usage

<!-- UsageSnippet language="python" operationID="estimate-model-application-on-file" method="post" path="/v2/models/{model_id}/apply/estimate" -->
```python
from flypix import Flypix, models


with Flypix(
    security=models.Security(
        api_key="<YOUR_API_KEY_HERE>",
    ),
) as f_client:

    res = f_client.models.estimate_model_application_on_file(model_id="<id>", raster_id="<id>")

    # Handle response
    print(res)

```

### Parameters

| Parameter                                                           | Type                                                                | Required                                                            | Description                                                         |
| ------------------------------------------------------------------- | ------------------------------------------------------------------- | ------------------------------------------------------------------- | ------------------------------------------------------------------- |
| `model_id`                                                          | *str*                                                               | :heavy_check_mark:                                                  | N/A                                                                 |
| `raster_id`                                                         | *str*                                                               | :heavy_check_mark:                                                  | N/A                                                                 |
| `retries`                                                           | [Optional[utils.RetryConfig]](../../models/utils/retryconfig.md)    | :heavy_minus_sign:                                                  | Configuration to override the default retry behavior of the client. |

### Response

**[models.EstimateModelApplicationOnFileResponse](../../models/estimatemodelapplicationonfileresponse.md)**

### Errors

| Error Type                | Status Code               | Content Type              |
| ------------------------- | ------------------------- | ------------------------- |
| errors.FlyPixDefaultError | 4XX, 5XX                  | \*/\*                     |