# Projects

## Overview

### Available Operations

* [create_project](#create_project) - Create project
* [get_projects_for_tenant](#get_projects_for_tenant) - List projects for tenant
* [delete_project](#delete_project) - Delete project

## create_project

Creates a new empty project.

### Example Usage

<!-- UsageSnippet language="python" operationID="create-project" method="post" path="/v2/projects/" -->
```python
from flypix import Flypix, models


with Flypix(
    security=models.Security(
        api_key="<YOUR_API_KEY_HERE>",
    ),
) as f_client:

    res = f_client.projects.create_project(name="<value>", tenant_id="<id>")

    # Handle response
    print(res)

```

### Parameters

| Parameter                                                           | Type                                                                | Required                                                            | Description                                                         |
| ------------------------------------------------------------------- | ------------------------------------------------------------------- | ------------------------------------------------------------------- | ------------------------------------------------------------------- |
| `name`                                                              | *str*                                                               | :heavy_check_mark:                                                  | N/A                                                                 |
| `tenant_id`                                                         | *str*                                                               | :heavy_check_mark:                                                  | N/A                                                                 |
| `retries`                                                           | [Optional[utils.RetryConfig]](../../models/utils/retryconfig.md)    | :heavy_minus_sign:                                                  | Configuration to override the default retry behavior of the client. |

### Response

**[models.CreateProjectResponse](../../models/createprojectresponse.md)**

### Errors

| Error Type                | Status Code               | Content Type              |
| ------------------------- | ------------------------- | ------------------------- |
| errors.FlyPixDefaultError | 4XX, 5XX                  | \*/\*                     |

## get_projects_for_tenant

Lists a tenant's projects.

### Example Usage

<!-- UsageSnippet language="python" operationID="get-projects-for-tenant" method="get" path="/v2/projects/for-tenant/{tenant_id}" -->
```python
from flypix import Flypix, models


with Flypix(
    security=models.Security(
        api_key="<YOUR_API_KEY_HERE>",
    ),
) as f_client:

    res = f_client.projects.get_projects_for_tenant(tenant_id="<id>")

    # Handle response
    print(res)

```

### Parameters

| Parameter                                                           | Type                                                                | Required                                                            | Description                                                         |
| ------------------------------------------------------------------- | ------------------------------------------------------------------- | ------------------------------------------------------------------- | ------------------------------------------------------------------- |
| `tenant_id`                                                         | *str*                                                               | :heavy_check_mark:                                                  | N/A                                                                 |
| `retries`                                                           | [Optional[utils.RetryConfig]](../../models/utils/retryconfig.md)    | :heavy_minus_sign:                                                  | Configuration to override the default retry behavior of the client. |

### Response

**[models.GetProjectsForTenantResponse](../../models/getprojectsfortenantresponse.md)**

### Errors

| Error Type                | Status Code               | Content Type              |
| ------------------------- | ------------------------- | ------------------------- |
| errors.FlyPixDefaultError | 4XX, 5XX                  | \*/\*                     |

## delete_project

Deletes a project and everything under it, recursively. This cannot be undone.

### Example Usage

<!-- UsageSnippet language="python" operationID="delete-project" method="delete" path="/v2/projects/{project_id}" -->
```python
from flypix import Flypix, models


with Flypix(
    security=models.Security(
        api_key="<YOUR_API_KEY_HERE>",
    ),
) as f_client:

    res = f_client.projects.delete_project(project_id="<id>")

    # Handle response
    print(res)

```

### Parameters

| Parameter                                                           | Type                                                                | Required                                                            | Description                                                         |
| ------------------------------------------------------------------- | ------------------------------------------------------------------- | ------------------------------------------------------------------- | ------------------------------------------------------------------- |
| `project_id`                                                        | *str*                                                               | :heavy_check_mark:                                                  | N/A                                                                 |
| `retries`                                                           | [Optional[utils.RetryConfig]](../../models/utils/retryconfig.md)    | :heavy_minus_sign:                                                  | Configuration to override the default retry behavior of the client. |

### Response

**[models.DeleteProjectResponse](../../models/deleteprojectresponse.md)**

### Errors

| Error Type                | Status Code               | Content Type              |
| ------------------------- | ------------------------- | ------------------------- |
| errors.FlyPixDefaultError | 4XX, 5XX                  | \*/\*                     |