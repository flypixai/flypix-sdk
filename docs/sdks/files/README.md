# Files

## Overview

Upload, download, list, and delete files.

### Available Operations

* [list_for_project](#list_for_project) - Get Files For Project Root
* [list_for_folder](#list_for_folder) - Get For Folder
* [get](#get) - Get File
* [delete](#delete) - Delete File
* [get_visible_raster](#get_visible_raster) - Get Visible Raster Of File
* [get_download_link](#get_download_link) - Get File Download Link
* [get_by_ids](#get_by_ids) - Get Files By Ids
* [get_storage_usage](#get_storage_usage) - Get Storage Usage
* [~~upload~~](#upload) - Upload File :warning: **Deprecated**

## list_for_project

Get files in the project root. This will ONLY get the files in the specified
project root (it is not recursive)

### Example Usage

<!-- UsageSnippet language="python" operationID="files_list_for_project" method="get" path="/files/for-project/{project_id}" -->
```python
from flypix import Flypix, models


with Flypix(
    security=models.Security(
        api_key="<YOUR_API_KEY_HERE>",
    ),
) as f_client:

    res = f_client.files.list_for_project(project_id="123e4567-e89b-12d3-a456-426614174000")

    # Handle response
    print(res)

```

### Parameters

| Parameter                                                           | Type                                                                | Required                                                            | Description                                                         | Example                                                             |
| ------------------------------------------------------------------- | ------------------------------------------------------------------- | ------------------------------------------------------------------- | ------------------------------------------------------------------- | ------------------------------------------------------------------- |
| `project_id`                                                        | *str*                                                               | :heavy_check_mark:                                                  | N/A                                                                 | 123e4567-e89b-12d3-a456-426614174000                                |
| `retries`                                                           | [Optional[utils.RetryConfig]](../../models/utils/retryconfig.md)    | :heavy_minus_sign:                                                  | Configuration to override the default retry behavior of the client. |                                                                     |

### Response

**[List[models.FileResponse]](../../models/.md)**

### Errors

| Error Type                                                       | Status Code                                                      | Content Type                                                     |
| ---------------------------------------------------------------- | ---------------------------------------------------------------- | ---------------------------------------------------------------- |
| errors.FilesListForProjectBadRequestErrorResponseSchema          | 400                                                              | application/json                                                 |
| errors.FilesListForProjectForbiddenErrorResponseSchema           | 403                                                              | application/json                                                 |
| errors.FilesListForProjectNotFoundErrorResponseSchema            | 404                                                              | application/json                                                 |
| errors.FilesListForProjectInternalServerErrorErrorResponseSchema | 500                                                              | application/json                                                 |
| errors.FlyPixDefaultError                                        | 4XX, 5XX                                                         | \*/\*                                                            |

## list_for_folder

Get the files in the specified folder. To get the files in the project root,
use the /for-project/ endpoint. This will ONLY get the files in the specified
folder (it is not recursive)

### Example Usage

<!-- UsageSnippet language="python" operationID="files_list_for_folder" method="get" path="/files/for-folder/{folder_id}" -->
```python
from flypix import Flypix, models


with Flypix(
    security=models.Security(
        api_key="<YOUR_API_KEY_HERE>",
    ),
) as f_client:

    res = f_client.files.list_for_folder(folder_id="123e4567-e89b-12d3-a456-426614174000")

    # Handle response
    print(res)

```

### Parameters

| Parameter                                                           | Type                                                                | Required                                                            | Description                                                         | Example                                                             |
| ------------------------------------------------------------------- | ------------------------------------------------------------------- | ------------------------------------------------------------------- | ------------------------------------------------------------------- | ------------------------------------------------------------------- |
| `folder_id`                                                         | *str*                                                               | :heavy_check_mark:                                                  | N/A                                                                 | 123e4567-e89b-12d3-a456-426614174000                                |
| `retries`                                                           | [Optional[utils.RetryConfig]](../../models/utils/retryconfig.md)    | :heavy_minus_sign:                                                  | Configuration to override the default retry behavior of the client. |                                                                     |

### Response

**[List[models.FileResponse]](../../models/.md)**

### Errors

| Error Type                                                      | Status Code                                                     | Content Type                                                    |
| --------------------------------------------------------------- | --------------------------------------------------------------- | --------------------------------------------------------------- |
| errors.FilesListForFolderBadRequestErrorResponseSchema          | 400                                                             | application/json                                                |
| errors.FilesListForFolderForbiddenErrorResponseSchema           | 403                                                             | application/json                                                |
| errors.FilesListForFolderNotFoundErrorResponseSchema            | 404                                                             | application/json                                                |
| errors.FilesListForFolderInternalServerErrorErrorResponseSchema | 500                                                             | application/json                                                |
| errors.FlyPixDefaultError                                       | 4XX, 5XX                                                        | \*/\*                                                           |

## get

Get file details. To download the file, use the download endpoint

### Example Usage

<!-- UsageSnippet language="python" operationID="files_get" method="get" path="/files/{file_id}" -->
```python
from flypix import Flypix, models


with Flypix(
    security=models.Security(
        api_key="<YOUR_API_KEY_HERE>",
    ),
) as f_client:

    res = f_client.files.get(file_id="123e4567-e89b-12d3-a456-426614174000")

    # Handle response
    print(res)

```

### Parameters

| Parameter                                                           | Type                                                                | Required                                                            | Description                                                         | Example                                                             |
| ------------------------------------------------------------------- | ------------------------------------------------------------------- | ------------------------------------------------------------------- | ------------------------------------------------------------------- | ------------------------------------------------------------------- |
| `file_id`                                                           | *str*                                                               | :heavy_check_mark:                                                  | N/A                                                                 | 123e4567-e89b-12d3-a456-426614174000                                |
| `retries`                                                           | [Optional[utils.RetryConfig]](../../models/utils/retryconfig.md)    | :heavy_minus_sign:                                                  | Configuration to override the default retry behavior of the client. |                                                                     |

### Response

**[models.FileResponse](../../models/fileresponse.md)**

### Errors

| Error Type                                            | Status Code                                           | Content Type                                          |
| ----------------------------------------------------- | ----------------------------------------------------- | ----------------------------------------------------- |
| errors.FilesGetBadRequestErrorResponseSchema          | 400                                                   | application/json                                      |
| errors.FilesGetForbiddenErrorResponseSchema           | 403                                                   | application/json                                      |
| errors.FilesGetNotFoundErrorResponseSchema            | 404                                                   | application/json                                      |
| errors.FilesGetInternalServerErrorErrorResponseSchema | 500                                                   | application/json                                      |
| errors.FlyPixDefaultError                             | 4XX, 5XX                                              | \*/\*                                                 |

## delete

Delete a file. This operation cannot be undone

### Example Usage

<!-- UsageSnippet language="python" operationID="files_delete" method="delete" path="/files/{file_id}" -->
```python
from flypix import Flypix, models


with Flypix(
    security=models.Security(
        api_key="<YOUR_API_KEY_HERE>",
    ),
) as f_client:

    res = f_client.files.delete(file_id="123e4567-e89b-12d3-a456-426614174000")

    # Handle response
    print(res)

```

### Parameters

| Parameter                                                           | Type                                                                | Required                                                            | Description                                                         | Example                                                             |
| ------------------------------------------------------------------- | ------------------------------------------------------------------- | ------------------------------------------------------------------- | ------------------------------------------------------------------- | ------------------------------------------------------------------- |
| `file_id`                                                           | *str*                                                               | :heavy_check_mark:                                                  | N/A                                                                 | 123e4567-e89b-12d3-a456-426614174000                                |
| `retries`                                                           | [Optional[utils.RetryConfig]](../../models/utils/retryconfig.md)    | :heavy_minus_sign:                                                  | Configuration to override the default retry behavior of the client. |                                                                     |

### Response

**[models.EntityDeletionResponse](../../models/entitydeletionresponse.md)**

### Errors

| Error Type                                               | Status Code                                              | Content Type                                             |
| -------------------------------------------------------- | -------------------------------------------------------- | -------------------------------------------------------- |
| errors.FilesDeleteBadRequestErrorResponseSchema          | 400                                                      | application/json                                         |
| errors.FilesDeleteForbiddenErrorResponseSchema           | 403                                                      | application/json                                         |
| errors.FilesDeleteNotFoundErrorResponseSchema            | 404                                                      | application/json                                         |
| errors.FilesDeleteInternalServerErrorErrorResponseSchema | 500                                                      | application/json                                         |
| errors.FlyPixDefaultError                                | 4XX, 5XX                                                 | \*/\*                                                    |

## get_visible_raster

Gets the visible raster for the specified file.
Upload files are processed into a visible raster that is shown in the application.
This endpoints retrieves the same file that the application would display.
Note that a file may not have a visible raster because it hasn't been processed yet

### Example Usage

<!-- UsageSnippet language="python" operationID="files_get_visible_raster" method="get" path="/files/{file_id}/visible" -->
```python
from flypix import Flypix, models


with Flypix(
    security=models.Security(
        api_key="<YOUR_API_KEY_HERE>",
    ),
) as f_client:

    res = f_client.files.get_visible_raster(file_id="123e4567-e89b-12d3-a456-426614174000")

    # Handle response
    print(res)

```

### Parameters

| Parameter                                                           | Type                                                                | Required                                                            | Description                                                         | Example                                                             |
| ------------------------------------------------------------------- | ------------------------------------------------------------------- | ------------------------------------------------------------------- | ------------------------------------------------------------------- | ------------------------------------------------------------------- |
| `file_id`                                                           | *str*                                                               | :heavy_check_mark:                                                  | N/A                                                                 | 123e4567-e89b-12d3-a456-426614174000                                |
| `retries`                                                           | [Optional[utils.RetryConfig]](../../models/utils/retryconfig.md)    | :heavy_minus_sign:                                                  | Configuration to override the default retry behavior of the client. |                                                                     |

### Response

**[models.FileLinkResponse](../../models/filelinkresponse.md)**

### Errors

| Error Type                                                         | Status Code                                                        | Content Type                                                       |
| ------------------------------------------------------------------ | ------------------------------------------------------------------ | ------------------------------------------------------------------ |
| errors.FilesGetVisibleRasterBadRequestErrorResponseSchema          | 400                                                                | application/json                                                   |
| errors.FilesGetVisibleRasterForbiddenErrorResponseSchema           | 403                                                                | application/json                                                   |
| errors.FilesGetVisibleRasterNotFoundErrorResponseSchema            | 404                                                                | application/json                                                   |
| errors.FilesGetVisibleRasterInternalServerErrorErrorResponseSchema | 500                                                                | application/json                                                   |
| errors.FlyPixDefaultError                                          | 4XX, 5XX                                                           | \*/\*                                                              |

## get_download_link

Get file download link. The link will be valid for a limited amount of time.

### Example Usage

<!-- UsageSnippet language="python" operationID="files_get_download_link" method="get" path="/files/{file_id}/download" -->
```python
from flypix import Flypix, models


with Flypix(
    security=models.Security(
        api_key="<YOUR_API_KEY_HERE>",
    ),
) as f_client:

    res = f_client.files.get_download_link(file_id="123e4567-e89b-12d3-a456-426614174000")

    # Handle response
    print(res)

```

### Parameters

| Parameter                                                           | Type                                                                | Required                                                            | Description                                                         | Example                                                             |
| ------------------------------------------------------------------- | ------------------------------------------------------------------- | ------------------------------------------------------------------- | ------------------------------------------------------------------- | ------------------------------------------------------------------- |
| `file_id`                                                           | *str*                                                               | :heavy_check_mark:                                                  | N/A                                                                 | 123e4567-e89b-12d3-a456-426614174000                                |
| `retries`                                                           | [Optional[utils.RetryConfig]](../../models/utils/retryconfig.md)    | :heavy_minus_sign:                                                  | Configuration to override the default retry behavior of the client. |                                                                     |

### Response

**[models.FileLinkResponse](../../models/filelinkresponse.md)**

### Errors

| Error Type                                                        | Status Code                                                       | Content Type                                                      |
| ----------------------------------------------------------------- | ----------------------------------------------------------------- | ----------------------------------------------------------------- |
| errors.FilesGetDownloadLinkBadRequestErrorResponseSchema          | 400                                                               | application/json                                                  |
| errors.FilesGetDownloadLinkForbiddenErrorResponseSchema           | 403                                                               | application/json                                                  |
| errors.FilesGetDownloadLinkNotFoundErrorResponseSchema            | 404                                                               | application/json                                                  |
| errors.FilesGetDownloadLinkInternalServerErrorErrorResponseSchema | 500                                                               | application/json                                                  |
| errors.FlyPixDefaultError                                         | 4XX, 5XX                                                          | \*/\*                                                             |

## get_by_ids

Get file details for many files

### Example Usage

<!-- UsageSnippet language="python" operationID="files_get_by_ids" method="post" path="/files/by-ids" -->
```python
from flypix import Flypix, models


with Flypix(
    security=models.Security(
        api_key="<YOUR_API_KEY_HERE>",
    ),
) as f_client:

    res = f_client.files.get_by_ids(request=[
        "123e4567-e89b-12d3-a456-426614174000",
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

**[List[models.FileResponse]](../../models/.md)**

### Errors

| Error Type                                                 | Status Code                                                | Content Type                                               |
| ---------------------------------------------------------- | ---------------------------------------------------------- | ---------------------------------------------------------- |
| errors.FilesGetByIdsBadRequestErrorResponseSchema          | 400                                                        | application/json                                           |
| errors.FilesGetByIdsForbiddenErrorResponseSchema           | 403                                                        | application/json                                           |
| errors.FilesGetByIdsNotFoundErrorResponseSchema            | 404                                                        | application/json                                           |
| errors.FilesGetByIdsInternalServerErrorErrorResponseSchema | 500                                                        | application/json                                           |
| errors.FlyPixDefaultError                                  | 4XX, 5XX                                                   | \*/\*                                                      |

## get_storage_usage

Get files in the project root. This will ONLY get the files in the specified
project root (it is not recursive)

### Example Usage

<!-- UsageSnippet language="python" operationID="files_get_storage_usage" method="get" path="/files/usage/{tenant_id}" -->
```python
from flypix import Flypix, models


with Flypix(
    security=models.Security(
        api_key="<YOUR_API_KEY_HERE>",
    ),
) as f_client:

    res = f_client.files.get_storage_usage(tenant_id="123e4567-e89b-12d3-a456-426614174000")

    # Handle response
    print(res)

```

### Parameters

| Parameter                                                           | Type                                                                | Required                                                            | Description                                                         | Example                                                             |
| ------------------------------------------------------------------- | ------------------------------------------------------------------- | ------------------------------------------------------------------- | ------------------------------------------------------------------- | ------------------------------------------------------------------- |
| `tenant_id`                                                         | *str*                                                               | :heavy_check_mark:                                                  | N/A                                                                 | 123e4567-e89b-12d3-a456-426614174000                                |
| `retries`                                                           | [Optional[utils.RetryConfig]](../../models/utils/retryconfig.md)    | :heavy_minus_sign:                                                  | Configuration to override the default retry behavior of the client. |                                                                     |

### Response

**[models.UsageResponse](../../models/usageresponse.md)**

### Errors

| Error Type                                                        | Status Code                                                       | Content Type                                                      |
| ----------------------------------------------------------------- | ----------------------------------------------------------------- | ----------------------------------------------------------------- |
| errors.FilesGetStorageUsageBadRequestErrorResponseSchema          | 400                                                               | application/json                                                  |
| errors.FilesGetStorageUsageForbiddenErrorResponseSchema           | 403                                                               | application/json                                                  |
| errors.FilesGetStorageUsageNotFoundErrorResponseSchema            | 404                                                               | application/json                                                  |
| errors.FilesGetStorageUsageInternalServerErrorErrorResponseSchema | 500                                                               | application/json                                                  |
| errors.FlyPixDefaultError                                         | 4XX, 5XX                                                          | \*/\*                                                             |

## ~~upload~~

**DEPRECATED**: This endpoint is deprecated and has been removed from the V1 API.
Please use the V2 API instead.

> :warning: **DEPRECATED**: This will be removed in a future release, please migrate away from it as soon as possible.

### Example Usage

<!-- UsageSnippet language="python" operationID="files_upload" method="post" path="/files/upload" -->
```python
from flypix import Flypix, models


with Flypix(
    security=models.Security(
        api_key="<YOUR_API_KEY_HERE>",
    ),
) as f_client:

    res = f_client.files.upload(request=open("example.file", "rb"))

    # Handle response
    print(res)

```

### Parameters

| Parameter                                                           | Type                                                                | Required                                                            | Description                                                         |
| ------------------------------------------------------------------- | ------------------------------------------------------------------- | ------------------------------------------------------------------- | ------------------------------------------------------------------- |
| `request`                                                           | [Union[bytes, IO[bytes], io.IOBase]](../../models/.md)              | :heavy_check_mark:                                                  | The request object to use for the request.                          |
| `retries`                                                           | [Optional[utils.RetryConfig]](../../models/utils/retryconfig.md)    | :heavy_minus_sign:                                                  | Configuration to override the default retry behavior of the client. |

### Response

**[Any](../../models/.md)**

### Errors

| Error Type                                               | Status Code                                              | Content Type                                             |
| -------------------------------------------------------- | -------------------------------------------------------- | -------------------------------------------------------- |
| errors.FilesUploadBadRequestErrorResponseSchema          | 400                                                      | application/json                                         |
| errors.FilesUploadForbiddenErrorResponseSchema           | 403                                                      | application/json                                         |
| errors.FilesUploadNotFoundErrorResponseSchema            | 404                                                      | application/json                                         |
| errors.FilesUploadInternalServerErrorErrorResponseSchema | 500                                                      | application/json                                         |
| errors.FlyPixDefaultError                                | 4XX, 5XX                                                 | \*/\*                                                    |