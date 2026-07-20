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
* [upload_v2](#upload_v2) - Upload File
* [upload_from_url](#upload_from_url) - Upload File From Url

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

| Error Type                | Status Code               | Content Type              |
| ------------------------- | ------------------------- | ------------------------- |
| errors.FlyPixDefaultError | 4XX, 5XX                  | \*/\*                     |

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

| Error Type                | Status Code               | Content Type              |
| ------------------------- | ------------------------- | ------------------------- |
| errors.FlyPixDefaultError | 4XX, 5XX                  | \*/\*                     |

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

| Error Type                | Status Code               | Content Type              |
| ------------------------- | ------------------------- | ------------------------- |
| errors.FlyPixDefaultError | 4XX, 5XX                  | \*/\*                     |

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

| Error Type                | Status Code               | Content Type              |
| ------------------------- | ------------------------- | ------------------------- |
| errors.FlyPixDefaultError | 4XX, 5XX                  | \*/\*                     |

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

| Error Type                | Status Code               | Content Type              |
| ------------------------- | ------------------------- | ------------------------- |
| errors.FlyPixDefaultError | 4XX, 5XX                  | \*/\*                     |

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

| Error Type                | Status Code               | Content Type              |
| ------------------------- | ------------------------- | ------------------------- |
| errors.FlyPixDefaultError | 4XX, 5XX                  | \*/\*                     |

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

| Error Type                | Status Code               | Content Type              |
| ------------------------- | ------------------------- | ------------------------- |
| errors.FlyPixDefaultError | 4XX, 5XX                  | \*/\*                     |

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

| Error Type                | Status Code               | Content Type              |
| ------------------------- | ------------------------- | ------------------------- |
| errors.FlyPixDefaultError | 4XX, 5XX                  | \*/\*                     |

## ~~upload~~

**DEPRECATED**: This endpoint is deprecated and will be removed in a future version, use
[v2/files/upload](/#/operations/upload_file_v2) instead.

Upload a raster file to the specified folder. If folder_id is not included,
the file will be uploaded to the project root.
Valid file formats: TIFF.
Example:
```bash
curl -X 'POST' '(...)/files/upload  \
    -H 'accept: application/json' \
    -H 'Content-Type: application/octet-stream' \
    -H 'Authorization: Bearer eyJ... \
    --url-query tenant_id=34f67787-dc22-4894-8fa8-74b450c44f6f \
    --url-query project_id=db7642d5-8b11-4057-b1be-b5a554c227c9 \
    --url-query filename=rgba.tiff \
    --data-binary @sentinel-2-data-2024-12-16.tiff 
```

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

    res = f_client.files.upload(tenant_id="95d06de1-31d8-4dc6-a134-b591889f9c67", project_id="334fb3cb-5f26-4e97-a2b7-e97b6de6064d", filename="example.file", body=open("example.file", "rb"))

    # Handle response
    print(res)

```

### Parameters

| Parameter                                                           | Type                                                                | Required                                                            | Description                                                         |
| ------------------------------------------------------------------- | ------------------------------------------------------------------- | ------------------------------------------------------------------- | ------------------------------------------------------------------- |
| `tenant_id`                                                         | *str*                                                               | :heavy_check_mark:                                                  | N/A                                                                 |
| `project_id`                                                        | *str*                                                               | :heavy_check_mark:                                                  | N/A                                                                 |
| `filename`                                                          | *str*                                                               | :heavy_check_mark:                                                  | N/A                                                                 |
| `body`                                                              | *Union[bytes, IO[bytes], io.IOBase]*                                | :heavy_check_mark:                                                  | N/A                                                                 |
| `folder_id`                                                         | *OptionalNullable[str]*                                             | :heavy_minus_sign:                                                  | N/A                                                                 |
| `retries`                                                           | [Optional[utils.RetryConfig]](../../models/utils/retryconfig.md)    | :heavy_minus_sign:                                                  | Configuration to override the default retry behavior of the client. |

### Response

**[Any](../../models/.md)**

### Errors

| Error Type                | Status Code               | Content Type              |
| ------------------------- | ------------------------- | ------------------------- |
| errors.FlyPixDefaultError | 4XX, 5XX                  | \*/\*                     |

## upload_v2

NOTE: This endpoint cannot be triggered directly from this UI
Upload a raster file to the specified folder. If folder_id is not included,
the file will be uploaded to the project root.
Valid file formats: TIFF.
Example:
```bash
curl -X 'POST' '(...)/v2/files/upload  \
    -H 'accept: application/json' \
    -H 'Content-Type: application/octet-stream' \
    -H 'Authorization: Bearer eyJ... \
    --url-query tenant_id=34f67787-dc22-4894-8fa8-74b450c44f6f \
    --url-query project_id=db7642d5-8b11-4057-b1be-b5a554c227c9 \
    --url-query filename=rgba.tiff \
    --data-binary @sentinel-2-data-2024-12-16.tiff 
```

### Example Usage

<!-- UsageSnippet language="python" operationID="files_upload_v2" method="post" path="/v2/files/upload" -->
```python
from flypix import Flypix, models


with Flypix(
    security=models.Security(
        api_key="<YOUR_API_KEY_HERE>",
    ),
) as f_client:

    res = f_client.files.upload_v2(tenant_id="170b602d-192c-4e40-a031-f5892fa57f45", project_id="55299aef-34b1-4aaa-a1aa-cbeca6dd058b", filename="example.file", body=open("example.file", "rb"))

    # Handle response
    print(res)

```

### Parameters

| Parameter                                                           | Type                                                                | Required                                                            | Description                                                         |
| ------------------------------------------------------------------- | ------------------------------------------------------------------- | ------------------------------------------------------------------- | ------------------------------------------------------------------- |
| `tenant_id`                                                         | *str*                                                               | :heavy_check_mark:                                                  | N/A                                                                 |
| `project_id`                                                        | *str*                                                               | :heavy_check_mark:                                                  | N/A                                                                 |
| `filename`                                                          | *str*                                                               | :heavy_check_mark:                                                  | N/A                                                                 |
| `body`                                                              | *Union[bytes, IO[bytes], io.IOBase]*                                | :heavy_check_mark:                                                  | N/A                                                                 |
| `folder_id`                                                         | *OptionalNullable[str]*                                             | :heavy_minus_sign:                                                  | N/A                                                                 |
| `retries`                                                           | [Optional[utils.RetryConfig]](../../models/utils/retryconfig.md)    | :heavy_minus_sign:                                                  | Configuration to override the default retry behavior of the client. |

### Response

**[models.UploadFileResponseStatus](../../models/uploadfileresponsestatus.md)**

### Errors

| Error Type                | Status Code               | Content Type              |
| ------------------------- | ------------------------- | ------------------------- |
| errors.FlyPixDefaultError | 4XX, 5XX                  | \*/\*                     |

## upload_from_url

NOTE: This endpoint cannot be triggered directly from this UI
Upload the raster file in the specified url to the specified folder.
If folder_id is not included, the file will be uploaded to the project root.
Valid file formats: TIFF.
Example:
```bash
curl -X 'POST' '(...)/v2/files/upload-from-url  \
    -H 'accept: application/json' \
    -H 'Content-Type: application/json' \
    -H 'Authorization: Bearer eyJ... \
    --url-query tenant_id=34f67787-dc22-4894-8fa8-74b450c44f6f \
    --url-query project_id=db7642d5-8b11-4057-b1be-b5a554c227c9 \
    --url-query filename=myfile.tiff \
    --url-query file_url=https://(...)/at3_1m4_01.tif \
```

### Example Usage

<!-- UsageSnippet language="python" operationID="files_upload_from_url" method="post" path="/v2/files/upload-from-url" -->
```python
from flypix import Flypix, models


with Flypix(
    security=models.Security(
        api_key="<YOUR_API_KEY_HERE>",
    ),
) as f_client:

    res = f_client.files.upload_from_url(file_url="dad272e1-d759-4787-8080-c3c21fce440f", tenant_id="d614acda-2db6-4aed-a3d4-98b2a079ff2c", project_id="fa7c54bc-4f6d-40d6-8993-8da199e7586e", filename="example.file")

    # Handle response
    print(res)

```

### Parameters

| Parameter                                                           | Type                                                                | Required                                                            | Description                                                         |
| ------------------------------------------------------------------- | ------------------------------------------------------------------- | ------------------------------------------------------------------- | ------------------------------------------------------------------- |
| `file_url`                                                          | *str*                                                               | :heavy_check_mark:                                                  | N/A                                                                 |
| `tenant_id`                                                         | *str*                                                               | :heavy_check_mark:                                                  | N/A                                                                 |
| `project_id`                                                        | *str*                                                               | :heavy_check_mark:                                                  | N/A                                                                 |
| `filename`                                                          | *str*                                                               | :heavy_check_mark:                                                  | N/A                                                                 |
| `folder_id`                                                         | *OptionalNullable[str]*                                             | :heavy_minus_sign:                                                  | N/A                                                                 |
| `retries`                                                           | [Optional[utils.RetryConfig]](../../models/utils/retryconfig.md)    | :heavy_minus_sign:                                                  | Configuration to override the default retry behavior of the client. |

### Response

**[models.UploadFileResponseStatus](../../models/uploadfileresponsestatus.md)**

### Errors

| Error Type                | Status Code               | Content Type              |
| ------------------------- | ------------------------- | ------------------------- |
| errors.FlyPixDefaultError | 4XX, 5XX                  | \*/\*                     |