# Projects

## Overview

Manage projects within a tenant.

### Available Operations

* [list_for_tenant](#list_for_tenant) - Get Projects For Tenant
* [delete](#delete) - Delete Project
* [create](#create) - Create Project

## list_for_tenant

Get projects in a tenant

### Example Usage

<!-- UsageSnippet language="python" operationID="projects_list_for_tenant" method="get" path="/projects/for-tenant/{tenant_id}" -->
```python
from flypix import Flypix, models


with Flypix(
    security=models.Security(
        api_key="<YOUR_API_KEY_HERE>",
    ),
) as f_client:

    res = f_client.projects.list_for_tenant(tenant_id="123e4567-e89b-12d3-a456-426614174000")

    # Handle response
    print(res)

```

### Parameters

| Parameter                                                           | Type                                                                | Required                                                            | Description                                                         | Example                                                             |
| ------------------------------------------------------------------- | ------------------------------------------------------------------- | ------------------------------------------------------------------- | ------------------------------------------------------------------- | ------------------------------------------------------------------- |
| `tenant_id`                                                         | *str*                                                               | :heavy_check_mark:                                                  | N/A                                                                 | 123e4567-e89b-12d3-a456-426614174000                                |
| `retries`                                                           | [Optional[utils.RetryConfig]](../../models/utils/retryconfig.md)    | :heavy_minus_sign:                                                  | Configuration to override the default retry behavior of the client. |                                                                     |

### Response

**[List[models.ProjectResponse]](../../models/.md)**

### Errors

| Error Type                | Status Code               | Content Type              |
| ------------------------- | ------------------------- | ------------------------- |
| errors.FlyPixDefaultError | 4XX, 5XX                  | \*/\*                     |

## delete

Delete the specified project. This will recursively delete any files
as well as folders contained in the specified project.
This operation cannot be undone

### Example Usage

<!-- UsageSnippet language="python" operationID="projects_delete" method="delete" path="/projects/{project_id}" -->
```python
from flypix import Flypix, models


with Flypix(
    security=models.Security(
        api_key="<YOUR_API_KEY_HERE>",
    ),
) as f_client:

    res = f_client.projects.delete(project_id="123e4567-e89b-12d3-a456-426614174000")

    # Handle response
    print(res)

```

### Parameters

| Parameter                                                           | Type                                                                | Required                                                            | Description                                                         | Example                                                             |
| ------------------------------------------------------------------- | ------------------------------------------------------------------- | ------------------------------------------------------------------- | ------------------------------------------------------------------- | ------------------------------------------------------------------- |
| `project_id`                                                        | *str*                                                               | :heavy_check_mark:                                                  | N/A                                                                 | 123e4567-e89b-12d3-a456-426614174000                                |
| `retries`                                                           | [Optional[utils.RetryConfig]](../../models/utils/retryconfig.md)    | :heavy_minus_sign:                                                  | Configuration to override the default retry behavior of the client. |                                                                     |

### Response

**[models.EntityDeletionResponse](../../models/entitydeletionresponse.md)**

### Errors

| Error Type                | Status Code               | Content Type              |
| ------------------------- | ------------------------- | ------------------------- |
| errors.FlyPixDefaultError | 4XX, 5XX                  | \*/\*                     |

## create

Create a new empty project

### Example Usage

<!-- UsageSnippet language="python" operationID="projects_create" method="post" path="/projects/" -->
```python
from flypix import Flypix, models


with Flypix(
    security=models.Security(
        api_key="<YOUR_API_KEY_HERE>",
    ),
) as f_client:

    res = f_client.projects.create(tenant_id="123e4567-e89b-12d3-a456-426614174000", name="<value>")

    # Handle response
    print(res)

```

### Parameters

| Parameter                                                           | Type                                                                | Required                                                            | Description                                                         | Example                                                             |
| ------------------------------------------------------------------- | ------------------------------------------------------------------- | ------------------------------------------------------------------- | ------------------------------------------------------------------- | ------------------------------------------------------------------- |
| `tenant_id`                                                         | *str*                                                               | :heavy_check_mark:                                                  | A string in UUID format                                             | 123e4567-e89b-12d3-a456-426614174000                                |
| `name`                                                              | *str*                                                               | :heavy_check_mark:                                                  | N/A                                                                 |                                                                     |
| `retries`                                                           | [Optional[utils.RetryConfig]](../../models/utils/retryconfig.md)    | :heavy_minus_sign:                                                  | Configuration to override the default retry behavior of the client. |                                                                     |

### Response

**[models.ProjectResponse](../../models/projectresponse.md)**

### Errors

| Error Type                | Status Code               | Content Type              |
| ------------------------- | ------------------------- | ------------------------- |
| errors.FlyPixDefaultError | 4XX, 5XX                  | \*/\*                     |