# Regions

## Overview

Regions of interest within a file.

### Available Operations

* [list_for_file](#list_for_file) - Get Regions For File
* [create](#create) - Create Regions In File
* [delete](#delete) - Delete Regions

## list_for_file

Get the regions for a file

### Example Usage

<!-- UsageSnippet language="python" operationID="regions_list_for_file" method="get" path="/regions/for-file/{file_id}" -->
```python
from flypix import FlyPix
from uuid import UUID


with FlyPix(
    bearer_auth="<YOUR_BEARER_TOKEN_HERE>",
) as fly_pix:

    res = fly_pix.regions.list_for_file(file_id=UUID("123e4567-e89b-12d3-a456-426614174000"))

    # Handle response
    print(res)

```

### Parameters

| Parameter                                                           | Type                                                                | Required                                                            | Description                                                         | Example                                                             |
| ------------------------------------------------------------------- | ------------------------------------------------------------------- | ------------------------------------------------------------------- | ------------------------------------------------------------------- | ------------------------------------------------------------------- |
| `file_id`                                                           | *UUID*                                                              | :heavy_check_mark:                                                  | N/A                                                                 | 123e4567-e89b-12d3-a456-426614174000                                |
| `retries`                                                           | [Optional[utils.RetryConfig]](../../models/utils/retryconfig.md)    | :heavy_minus_sign:                                                  | Configuration to override the default retry behavior of the client. |                                                                     |

### Response

**[List[models.RegionResponse]](../../models/.md)**

### Errors

| Error Type                | Status Code               | Content Type              |
| ------------------------- | ------------------------- | ------------------------- |
| errors.FlyPixDefaultError | 4XX, 5XX                  | \*/\*                     |

## create

Create regions in the file. The region payload format is similar to the one obtained
for vector features. Example:
```json
{
    "region_payloads": [
        {
            "inference_behavior": "IGNORE",
            "metadata": {
                "color": "2196f3",
                "description": null,
                "name": null
            },
            "polygon": "AQMAAAABAAAABQAAAJdcNM9GL5lAuuo2W2H6kMBS+DDvW9KbQLrqNlth+pDAUvgw71vSm0A/IBELcieVwJdcNM9GL5lAPyARC3InlcCXXDTPRi+ZQLrqNlth+pDA",
            "training_behavior": "TRAINING"
        }
    ]
}
```

### Example Usage

<!-- UsageSnippet language="python" operationID="regions_create" method="post" path="/regions/{file_id}" -->
```python
from flypix import FlyPix
from uuid import UUID


with FlyPix(
    bearer_auth="<YOUR_BEARER_TOKEN_HERE>",
) as fly_pix:

    res = fly_pix.regions.create(file_id=UUID("123e4567-e89b-12d3-a456-426614174000"), region_payloads=[
        {
            "polygon": "<value>",
            "metadata": {
                "color": "FF0000",
                "name": "New String",
                "description": "New String",
            },
            "training_behavior": "VALIDATION",
            "inference_behavior": "USE",
        },
    ])

    # Handle response
    print(res)

```

### Parameters

| Parameter                                                               | Type                                                                    | Required                                                                | Description                                                             | Example                                                                 |
| ----------------------------------------------------------------------- | ----------------------------------------------------------------------- | ----------------------------------------------------------------------- | ----------------------------------------------------------------------- | ----------------------------------------------------------------------- |
| `file_id`                                                               | *UUID*                                                                  | :heavy_check_mark:                                                      | N/A                                                                     | 123e4567-e89b-12d3-a456-426614174000                                    |
| `region_payloads`                                                       | List[[models.CreateRegionPayload](../../models/createregionpayload.md)] | :heavy_check_mark:                                                      | N/A                                                                     |                                                                         |
| `retries`                                                               | [Optional[utils.RetryConfig]](../../models/utils/retryconfig.md)        | :heavy_minus_sign:                                                      | Configuration to override the default retry behavior of the client.     |                                                                         |

### Response

**[List[models.RegionResponse]](../../models/.md)**

### Errors

| Error Type                | Status Code               | Content Type              |
| ------------------------- | ------------------------- | ------------------------- |
| errors.FlyPixDefaultError | 4XX, 5XX                  | \*/\*                     |

## delete

Delete regions

### Example Usage

<!-- UsageSnippet language="python" operationID="regions_delete" method="delete" path="/regions/" -->
```python
from flypix import FlyPix
from uuid import UUID


with FlyPix(
    bearer_auth="<YOUR_BEARER_TOKEN_HERE>",
) as fly_pix:

    res = fly_pix.regions.delete(request=[
        UUID("123e4567-e89b-12d3-a456-426614174000"),
    ])

    # Handle response
    print(res)

```

### Parameters

| Parameter                                                           | Type                                                                | Required                                                            | Description                                                         |
| ------------------------------------------------------------------- | ------------------------------------------------------------------- | ------------------------------------------------------------------- | ------------------------------------------------------------------- |
| `request`                                                           | [List[UUID]](../../models/.md)                                      | :heavy_check_mark:                                                  | The request object to use for the request.                          |
| `retries`                                                           | [Optional[utils.RetryConfig]](../../models/utils/retryconfig.md)    | :heavy_minus_sign:                                                  | Configuration to override the default retry behavior of the client. |

### Response

**[Any](../../models/.md)**

### Errors

| Error Type                | Status Code               | Content Type              |
| ------------------------- | ------------------------- | ------------------------- |
| errors.FlyPixDefaultError | 4XX, 5XX                  | \*/\*                     |