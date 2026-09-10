# Files

## Overview

### Available Operations

* [upload_v2](#upload_v2) - Upload a file
* [upload_from_url](#upload_from_url) - Upload a file from a URL
* [get_storage_usage](#get_storage_usage) - Get storage usage
* [get_file_download_link](#get_file_download_link) - Get file download link

## upload_v2

Uploads a file directly, streamed from the request body. Rejected if it would push the tenant over its subscription's storage quota.

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
| `folder_id`                                                         | *Optional[str]*                                                     | :heavy_minus_sign:                                                  | N/A                                                                 |
| `content_length`                                                    | *Optional[str]*                                                     | :heavy_minus_sign:                                                  | N/A                                                                 |
| `retries`                                                           | [Optional[utils.RetryConfig]](../../models/utils/retryconfig.md)    | :heavy_minus_sign:                                                  | Configuration to override the default retry behavior of the client. |

### Response

**[models.FilesUploadV2Response](../../models/filesuploadv2response.md)**

### Errors

| Error Type                | Status Code               | Content Type              |
| ------------------------- | ------------------------- | ------------------------- |
| errors.FlyPixDefaultError | 4XX, 5XX                  | \*/\*                     |

## upload_from_url

Uploads a file by fetching it from a remote URL; the download is streamed straight into the upload, never buffered.

### Example Usage

<!-- UsageSnippet language="python" operationID="files_upload_from_url" method="post" path="/v2/files/upload-from-url" -->
```python
from flypix import Flypix, models


with Flypix(
    security=models.Security(
        api_key="<YOUR_API_KEY_HERE>",
    ),
) as f_client:

    res = f_client.files.upload_from_url(tenant_id="d614acda-2db6-4aed-a3d4-98b2a079ff2c", project_id="fa7c54bc-4f6d-40d6-8993-8da199e7586e", filename="example.file", file_url="dad272e1-d759-4787-8080-c3c21fce440f")

    # Handle response
    print(res)

```

### Parameters

| Parameter                                                           | Type                                                                | Required                                                            | Description                                                         |
| ------------------------------------------------------------------- | ------------------------------------------------------------------- | ------------------------------------------------------------------- | ------------------------------------------------------------------- |
| `tenant_id`                                                         | *str*                                                               | :heavy_check_mark:                                                  | N/A                                                                 |
| `project_id`                                                        | *str*                                                               | :heavy_check_mark:                                                  | N/A                                                                 |
| `filename`                                                          | *str*                                                               | :heavy_check_mark:                                                  | N/A                                                                 |
| `file_url`                                                          | *str*                                                               | :heavy_check_mark:                                                  | N/A                                                                 |
| `folder_id`                                                         | *Optional[str]*                                                     | :heavy_minus_sign:                                                  | N/A                                                                 |
| `content_length`                                                    | *Optional[str]*                                                     | :heavy_minus_sign:                                                  | N/A                                                                 |
| `retries`                                                           | [Optional[utils.RetryConfig]](../../models/utils/retryconfig.md)    | :heavy_minus_sign:                                                  | Configuration to override the default retry behavior of the client. |

### Response

**[models.FilesUploadFromURLResponse](../../models/filesuploadfromurlresponse.md)**

### Errors

| Error Type                | Status Code               | Content Type              |
| ------------------------- | ------------------------- | ------------------------- |
| errors.FlyPixDefaultError | 4XX, 5XX                  | \*/\*                     |

## get_storage_usage

Returns a tenant's storage usage against its subscription quota.

### Example Usage

<!-- UsageSnippet language="python" operationID="get-storage-usage" method="get" path="/v2/files/usage/{tenant_id}" -->
```python
from flypix import Flypix, models


with Flypix(
    security=models.Security(
        api_key="<YOUR_API_KEY_HERE>",
    ),
) as f_client:

    res = f_client.files.get_storage_usage(tenant_id="<id>")

    # Handle response
    print(res)

```

### Parameters

| Parameter                                                           | Type                                                                | Required                                                            | Description                                                         |
| ------------------------------------------------------------------- | ------------------------------------------------------------------- | ------------------------------------------------------------------- | ------------------------------------------------------------------- |
| `tenant_id`                                                         | *str*                                                               | :heavy_check_mark:                                                  | N/A                                                                 |
| `retries`                                                           | [Optional[utils.RetryConfig]](../../models/utils/retryconfig.md)    | :heavy_minus_sign:                                                  | Configuration to override the default retry behavior of the client. |

### Response

**[models.GetStorageUsageResponse](../../models/getstorageusageresponse.md)**

### Errors

| Error Type                | Status Code               | Content Type              |
| ------------------------- | ------------------------- | ------------------------- |
| errors.FlyPixDefaultError | 4XX, 5XX                  | \*/\*                     |

## get_file_download_link

Returns a time-limited download link for a file.

### Example Usage

<!-- UsageSnippet language="python" operationID="get-file-download-link" method="get" path="/v2/files/{file_id}/download" -->
```python
from flypix import Flypix, models


with Flypix(
    security=models.Security(
        api_key="<YOUR_API_KEY_HERE>",
    ),
) as f_client:

    res = f_client.files.get_file_download_link(file_id="<id>")

    # Handle response
    print(res)

```

### Parameters

| Parameter                                                           | Type                                                                | Required                                                            | Description                                                         |
| ------------------------------------------------------------------- | ------------------------------------------------------------------- | ------------------------------------------------------------------- | ------------------------------------------------------------------- |
| `file_id`                                                           | *str*                                                               | :heavy_check_mark:                                                  | N/A                                                                 |
| `retries`                                                           | [Optional[utils.RetryConfig]](../../models/utils/retryconfig.md)    | :heavy_minus_sign:                                                  | Configuration to override the default retry behavior of the client. |

### Response

**[models.GetFileDownloadLinkResponse](../../models/getfiledownloadlinkresponse.md)**

### Errors

| Error Type                | Status Code               | Content Type              |
| ------------------------- | ------------------------- | ------------------------- |
| errors.FlyPixDefaultError | 4XX, 5XX                  | \*/\*                     |