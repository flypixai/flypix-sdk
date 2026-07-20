# Folders

## Overview

Organize files into folders within a project.

### Available Operations

* [list_for_folder](#list_for_folder) - Get Folders For Folder
* [list_for_project](#list_for_project) - Get Folders In Project Root
* [delete](#delete) - Delete Folder
* [create](#create) - Create Folder

## list_for_folder

Get the folders in the specified folder. To get the folders in the project root,
use the /for-project/ endpoint. This will ONLY get the folders in the specified
folder (it is not recursive)

### Example Usage

<!-- UsageSnippet language="python" operationID="folders_list_for_folder" method="get" path="/folders/for-folder/{folder_id}" -->
```python
from flypix import FlyPix, models


with FlyPix(
    security=models.Security(
        bearer_auth="<YOUR_BEARER_TOKEN_HERE>",
    ),
) as fly_pix:

    res = fly_pix.folders.list_for_folder(folder_id="123e4567-e89b-12d3-a456-426614174000")

    # Handle response
    print(res)

```

### Parameters

| Parameter                                                           | Type                                                                | Required                                                            | Description                                                         | Example                                                             |
| ------------------------------------------------------------------- | ------------------------------------------------------------------- | ------------------------------------------------------------------- | ------------------------------------------------------------------- | ------------------------------------------------------------------- |
| `folder_id`                                                         | *str*                                                               | :heavy_check_mark:                                                  | N/A                                                                 | 123e4567-e89b-12d3-a456-426614174000                                |
| `retries`                                                           | [Optional[utils.RetryConfig]](../../models/utils/retryconfig.md)    | :heavy_minus_sign:                                                  | Configuration to override the default retry behavior of the client. |                                                                     |

### Response

**[List[models.FolderResponse]](../../models/.md)**

### Errors

| Error Type                | Status Code               | Content Type              |
| ------------------------- | ------------------------- | ------------------------- |
| errors.FlyPixDefaultError | 4XX, 5XX                  | \*/\*                     |

## list_for_project

Get folders in the project root. This will ONLY get the folders in the specified
project root (it is not recursive)

### Example Usage

<!-- UsageSnippet language="python" operationID="folders_list_for_project" method="get" path="/folders/for-project/{project_id}" -->
```python
from flypix import FlyPix, models


with FlyPix(
    security=models.Security(
        bearer_auth="<YOUR_BEARER_TOKEN_HERE>",
    ),
) as fly_pix:

    res = fly_pix.folders.list_for_project(project_id="123e4567-e89b-12d3-a456-426614174000")

    # Handle response
    print(res)

```

### Parameters

| Parameter                                                           | Type                                                                | Required                                                            | Description                                                         | Example                                                             |
| ------------------------------------------------------------------- | ------------------------------------------------------------------- | ------------------------------------------------------------------- | ------------------------------------------------------------------- | ------------------------------------------------------------------- |
| `project_id`                                                        | *str*                                                               | :heavy_check_mark:                                                  | N/A                                                                 | 123e4567-e89b-12d3-a456-426614174000                                |
| `retries`                                                           | [Optional[utils.RetryConfig]](../../models/utils/retryconfig.md)    | :heavy_minus_sign:                                                  | Configuration to override the default retry behavior of the client. |                                                                     |

### Response

**[List[models.FolderResponse]](../../models/.md)**

### Errors

| Error Type                | Status Code               | Content Type              |
| ------------------------- | ------------------------- | ------------------------- |
| errors.FlyPixDefaultError | 4XX, 5XX                  | \*/\*                     |

## delete

Delete the specified folder. This will recursively delete any files
as well as folders contained in the specified folder.
This operation cannot be undone

### Example Usage

<!-- UsageSnippet language="python" operationID="folders_delete" method="delete" path="/folders/{folder_id}" -->
```python
from flypix import FlyPix, models


with FlyPix(
    security=models.Security(
        bearer_auth="<YOUR_BEARER_TOKEN_HERE>",
    ),
) as fly_pix:

    res = fly_pix.folders.delete(folder_id="123e4567-e89b-12d3-a456-426614174000")

    # Handle response
    print(res)

```

### Parameters

| Parameter                                                           | Type                                                                | Required                                                            | Description                                                         | Example                                                             |
| ------------------------------------------------------------------- | ------------------------------------------------------------------- | ------------------------------------------------------------------- | ------------------------------------------------------------------- | ------------------------------------------------------------------- |
| `folder_id`                                                         | *str*                                                               | :heavy_check_mark:                                                  | N/A                                                                 | 123e4567-e89b-12d3-a456-426614174000                                |
| `retries`                                                           | [Optional[utils.RetryConfig]](../../models/utils/retryconfig.md)    | :heavy_minus_sign:                                                  | Configuration to override the default retry behavior of the client. |                                                                     |

### Response

**[models.EntityDeletionResponse](../../models/entitydeletionresponse.md)**

### Errors

| Error Type                | Status Code               | Content Type              |
| ------------------------- | ------------------------- | ------------------------- |
| errors.FlyPixDefaultError | 4XX, 5XX                  | \*/\*                     |

## create

Create a folder. Use parent_id to create it inside another folder
in the project, or skip it to create it in the project root.

### Example Usage

<!-- UsageSnippet language="python" operationID="folders_create" method="post" path="/folders/" -->
```python
from flypix import FlyPix, models


with FlyPix(
    security=models.Security(
        bearer_auth="<YOUR_BEARER_TOKEN_HERE>",
    ),
) as fly_pix:

    res = fly_pix.folders.create(tenant_id="123e4567-e89b-12d3-a456-426614174000", project_id="123e4567-e89b-12d3-a456-426614174000", parent_id="123e4567-e89b-12d3-a456-426614174000", name="<value>")

    # Handle response
    print(res)

```

### Parameters

| Parameter                                                           | Type                                                                | Required                                                            | Description                                                         | Example                                                             |
| ------------------------------------------------------------------- | ------------------------------------------------------------------- | ------------------------------------------------------------------- | ------------------------------------------------------------------- | ------------------------------------------------------------------- |
| `tenant_id`                                                         | *str*                                                               | :heavy_check_mark:                                                  | A string in UUID format                                             | 123e4567-e89b-12d3-a456-426614174000                                |
| `project_id`                                                        | *str*                                                               | :heavy_check_mark:                                                  | A string in UUID format                                             | 123e4567-e89b-12d3-a456-426614174000                                |
| `parent_id`                                                         | *Nullable[str]*                                                     | :heavy_check_mark:                                                  | N/A                                                                 | 123e4567-e89b-12d3-a456-426614174000                                |
| `name`                                                              | *str*                                                               | :heavy_check_mark:                                                  | N/A                                                                 |                                                                     |
| `retries`                                                           | [Optional[utils.RetryConfig]](../../models/utils/retryconfig.md)    | :heavy_minus_sign:                                                  | Configuration to override the default retry behavior of the client. |                                                                     |

### Response

**[models.FolderResponse](../../models/folderresponse.md)**

### Errors

| Error Type                | Status Code               | Content Type              |
| ------------------------- | ------------------------- | ------------------------- |
| errors.FlyPixDefaultError | 4XX, 5XX                  | \*/\*                     |