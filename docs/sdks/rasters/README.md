# Rasters

## Overview

### Available Operations

* [get_rasters_for_project](#get_rasters_for_project) - List project rasters
* [get_project_raster_tree](#get_project_raster_tree) - Get project raster tree
* [get_rasters_for_tenant](#get_rasters_for_tenant) - List tenant rasters
* [get_rasters_by_ids](#get_rasters_by_ids) - Get rasters by ids
* [delete_raster](#delete_raster) - Delete raster
* [get_raster](#get_raster) - Get raster details

## get_rasters_for_project

Lists the rasters in a project, optionally scoped to a single folder via `folder_id` ("root", a folder UUID, or omitted for all).

### Example Usage

<!-- UsageSnippet language="python" operationID="get-rasters-for-project" method="get" path="/v2/rasters/for-project/{project_id}" -->
```python
from flypix import Flypix, models


with Flypix(
    security=models.Security(
        api_key="<YOUR_API_KEY_HERE>",
    ),
) as f_client:

    res = f_client.rasters.get_rasters_for_project(project_id="<id>", offset=0, limit=200)

    # Handle response
    print(res)

```

### Parameters

| Parameter                                                                                       | Type                                                                                            | Required                                                                                        | Description                                                                                     |
| ----------------------------------------------------------------------------------------------- | ----------------------------------------------------------------------------------------------- | ----------------------------------------------------------------------------------------------- | ----------------------------------------------------------------------------------------------- |
| `project_id`                                                                                    | *str*                                                                                           | :heavy_check_mark:                                                                              | N/A                                                                                             |
| `folder_id`                                                                                     | *Optional[str]*                                                                                 | :heavy_minus_sign:                                                                              | A specific folder UUID or "root". Omit to list all rasters in the project regardless of folder. |
| `filter_`                                                                                       | *Optional[str]*                                                                                 | :heavy_minus_sign:                                                                              | Comma-separated field:operator:value clauses, e.g. status:eq:FAILED                             |
| `sort`                                                                                          | *Optional[str]*                                                                                 | :heavy_minus_sign:                                                                              | Comma-separated field:asc\|desc clauses, e.g. created_at:desc                                   |
| `offset`                                                                                        | *Optional[int]*                                                                                 | :heavy_minus_sign:                                                                              | N/A                                                                                             |
| `limit`                                                                                         | *Optional[int]*                                                                                 | :heavy_minus_sign:                                                                              | N/A                                                                                             |
| `retries`                                                                                       | [Optional[utils.RetryConfig]](../../models/utils/retryconfig.md)                                | :heavy_minus_sign:                                                                              | Configuration to override the default retry behavior of the client.                             |

### Response

**[models.GetRastersForProjectResponse](../../models/getrastersforprojectresponse.md)**

### Errors

| Error Type                | Status Code               | Content Type              |
| ------------------------- | ------------------------- | ------------------------- |
| errors.FlyPixDefaultError | 4XX, 5XX                  | \*/\*                     |

## get_project_raster_tree

Returns a project's full folder structure with the raster ids in each folder, in one call — used to build breadcrumbs/navigation without a separate listing call.

### Example Usage

<!-- UsageSnippet language="python" operationID="get-project-raster-tree" method="get" path="/v2/rasters/for-project/{project_id}/tree" -->
```python
from flypix import Flypix, models


with Flypix(
    security=models.Security(
        api_key="<YOUR_API_KEY_HERE>",
    ),
) as f_client:

    res = f_client.rasters.get_project_raster_tree(project_id="<id>")

    # Handle response
    print(res)

```

### Parameters

| Parameter                                                           | Type                                                                | Required                                                            | Description                                                         |
| ------------------------------------------------------------------- | ------------------------------------------------------------------- | ------------------------------------------------------------------- | ------------------------------------------------------------------- |
| `project_id`                                                        | *str*                                                               | :heavy_check_mark:                                                  | N/A                                                                 |
| `retries`                                                           | [Optional[utils.RetryConfig]](../../models/utils/retryconfig.md)    | :heavy_minus_sign:                                                  | Configuration to override the default retry behavior of the client. |

### Response

**[models.GetProjectRasterTreeResponse](../../models/getprojectrastertreeresponse.md)**

### Errors

| Error Type                | Status Code               | Content Type              |
| ------------------------- | ------------------------- | ------------------------- |
| errors.FlyPixDefaultError | 4XX, 5XX                  | \*/\*                     |

## get_rasters_for_tenant

Lists the rasters in a tenant.

### Example Usage

<!-- UsageSnippet language="python" operationID="get-rasters-for-tenant" method="get" path="/v2/rasters/for-tenant/{tenant_id}" -->
```python
from flypix import Flypix, models


with Flypix(
    security=models.Security(
        api_key="<YOUR_API_KEY_HERE>",
    ),
) as f_client:

    res = f_client.rasters.get_rasters_for_tenant(tenant_id="<id>", offset=0, limit=200)

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

**[models.GetRastersForTenantResponse](../../models/getrastersfortenantresponse.md)**

### Errors

| Error Type                | Status Code               | Content Type              |
| ------------------------- | ------------------------- | ------------------------- |
| errors.FlyPixDefaultError | 4XX, 5XX                  | \*/\*                     |

## get_rasters_by_ids

Returns the rasters matching the given ids, in one call.

### Example Usage

<!-- UsageSnippet language="python" operationID="get-rasters-by-ids" method="post" path="/v2/rasters/get-by-ids" -->
```python
from flypix import Flypix, models


with Flypix(
    security=models.Security(
        api_key="<YOUR_API_KEY_HERE>",
    ),
) as f_client:

    res = f_client.rasters.get_rasters_by_ids(request=[
        "<value 1>",
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

**[models.GetRastersByIdsResponse](../../models/getrastersbyidsresponse.md)**

### Errors

| Error Type                | Status Code               | Content Type              |
| ------------------------- | ------------------------- | ------------------------- |
| errors.FlyPixDefaultError | 4XX, 5XX                  | \*/\*                     |

## delete_raster

Deletes a raster, cascading to its backing file if it has one. This cannot be undone.

### Example Usage

<!-- UsageSnippet language="python" operationID="delete-raster" method="delete" path="/v2/rasters/{raster_id}" -->
```python
from flypix import Flypix, models


with Flypix(
    security=models.Security(
        api_key="<YOUR_API_KEY_HERE>",
    ),
) as f_client:

    res = f_client.rasters.delete_raster(raster_id="<id>")

    # Handle response
    print(res)

```

### Parameters

| Parameter                                                           | Type                                                                | Required                                                            | Description                                                         |
| ------------------------------------------------------------------- | ------------------------------------------------------------------- | ------------------------------------------------------------------- | ------------------------------------------------------------------- |
| `raster_id`                                                         | *str*                                                               | :heavy_check_mark:                                                  | N/A                                                                 |
| `retries`                                                           | [Optional[utils.RetryConfig]](../../models/utils/retryconfig.md)    | :heavy_minus_sign:                                                  | Configuration to override the default retry behavior of the client. |

### Response

**[models.DeleteRasterResponse](../../models/deleterasterresponse.md)**

### Errors

| Error Type                | Status Code               | Content Type              |
| ------------------------- | ------------------------- | ------------------------- |
| errors.FlyPixDefaultError | 4XX, 5XX                  | \*/\*                     |

## get_raster

Returns a raster's details, by id.

### Example Usage

<!-- UsageSnippet language="python" operationID="get-raster" method="get" path="/v2/rasters/{raster_id}" -->
```python
from flypix import Flypix, models


with Flypix(
    security=models.Security(
        api_key="<YOUR_API_KEY_HERE>",
    ),
) as f_client:

    res = f_client.rasters.get_raster(raster_id="<id>")

    # Handle response
    print(res)

```

### Parameters

| Parameter                                                           | Type                                                                | Required                                                            | Description                                                         |
| ------------------------------------------------------------------- | ------------------------------------------------------------------- | ------------------------------------------------------------------- | ------------------------------------------------------------------- |
| `raster_id`                                                         | *str*                                                               | :heavy_check_mark:                                                  | N/A                                                                 |
| `retries`                                                           | [Optional[utils.RetryConfig]](../../models/utils/retryconfig.md)    | :heavy_minus_sign:                                                  | Configuration to override the default retry behavior of the client. |

### Response

**[models.GetRasterResponse](../../models/getrasterresponse.md)**

### Errors

| Error Type                | Status Code               | Content Type              |
| ------------------------- | ------------------------- | ------------------------- |
| errors.FlyPixDefaultError | 4XX, 5XX                  | \*/\*                     |