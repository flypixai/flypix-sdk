# Regions

## Overview

### Available Operations

* [delete_regions](#delete_regions) - Delete regions
* [get_regions_for_raster](#get_regions_for_raster) - List raster regions
* [get_regions_by_ids](#get_regions_by_ids) - Get regions by ids
* [create_regions_in_raster](#create_regions_in_raster) - Create regions on a raster

## delete_regions

Deletes many regions at once.

### Example Usage

<!-- UsageSnippet language="python" operationID="delete-regions" method="delete" path="/v2/regions/" -->
```python
from flypix import Flypix, models


with Flypix(
    security=models.Security(
        api_key="<YOUR_API_KEY_HERE>",
    ),
) as f_client:

    res = f_client.regions.delete_regions(request=[])

    # Handle response
    print(res)

```

### Parameters

| Parameter                                                           | Type                                                                | Required                                                            | Description                                                         |
| ------------------------------------------------------------------- | ------------------------------------------------------------------- | ------------------------------------------------------------------- | ------------------------------------------------------------------- |
| `request`                                                           | [List[str]](../../models/.md)                                       | :heavy_check_mark:                                                  | The request object to use for the request.                          |
| `retries`                                                           | [Optional[utils.RetryConfig]](../../models/utils/retryconfig.md)    | :heavy_minus_sign:                                                  | Configuration to override the default retry behavior of the client. |

### Response

**[models.DeleteRegionsResponse](../../models/deleteregionsresponse.md)**

### Errors

| Error Type                | Status Code               | Content Type              |
| ------------------------- | ------------------------- | ------------------------- |
| errors.FlyPixDefaultError | 4XX, 5XX                  | \*/\*                     |

## get_regions_for_raster

Lists the regions for a raster.

### Example Usage

<!-- UsageSnippet language="python" operationID="get-regions-for-raster" method="get" path="/v2/regions/for-raster/{raster_id}" -->
```python
from flypix import Flypix, models


with Flypix(
    security=models.Security(
        api_key="<YOUR_API_KEY_HERE>",
    ),
) as f_client:

    res = f_client.regions.get_regions_for_raster(raster_id="<id>")

    # Handle response
    print(res)

```

### Parameters

| Parameter                                                           | Type                                                                | Required                                                            | Description                                                         |
| ------------------------------------------------------------------- | ------------------------------------------------------------------- | ------------------------------------------------------------------- | ------------------------------------------------------------------- |
| `raster_id`                                                         | *str*                                                               | :heavy_check_mark:                                                  | N/A                                                                 |
| `retries`                                                           | [Optional[utils.RetryConfig]](../../models/utils/retryconfig.md)    | :heavy_minus_sign:                                                  | Configuration to override the default retry behavior of the client. |

### Response

**[models.GetRegionsForRasterResponse](../../models/getregionsforrasterresponse.md)**

### Errors

| Error Type                | Status Code               | Content Type              |
| ------------------------- | ------------------------- | ------------------------- |
| errors.FlyPixDefaultError | 4XX, 5XX                  | \*/\*                     |

## get_regions_by_ids

Returns the regions matching the given ids, in one call.

### Example Usage

<!-- UsageSnippet language="python" operationID="get-regions-by-ids" method="post" path="/v2/regions/get-by-ids" -->
```python
from flypix import Flypix, models


with Flypix(
    security=models.Security(
        api_key="<YOUR_API_KEY_HERE>",
    ),
) as f_client:

    res = f_client.regions.get_regions_by_ids(request=[
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

**[models.GetRegionsByIdsResponse](../../models/getregionsbyidsresponse.md)**

### Errors

| Error Type                | Status Code               | Content Type              |
| ------------------------- | ------------------------- | ------------------------- |
| errors.FlyPixDefaultError | 4XX, 5XX                  | \*/\*                     |

## create_regions_in_raster

Creates regions on a raster. Region payloads use the same shape as vector features.

### Example Usage

<!-- UsageSnippet language="python" operationID="create-regions-in-raster" method="post" path="/v2/regions/{raster_id}" -->
```python
from flypix import Flypix, models


with Flypix(
    security=models.Security(
        api_key="<YOUR_API_KEY_HERE>",
    ),
) as f_client:

    res = f_client.regions.create_regions_in_raster(raster_id="<id>", region_payloads=[
        {
            "inference_behavior": "IGNORE",
            "metadata": {
                "color": "gold",
            },
            "polygon": "<value>",
            "training_behavior": "TRAINING",
        },
    ])

    # Handle response
    print(res)

```

### Parameters

| Parameter                                                             | Type                                                                  | Required                                                              | Description                                                           |
| --------------------------------------------------------------------- | --------------------------------------------------------------------- | --------------------------------------------------------------------- | --------------------------------------------------------------------- |
| `raster_id`                                                           | *str*                                                                 | :heavy_check_mark:                                                    | N/A                                                                   |
| `region_payloads`                                                     | List[[models.RegionPayloadInput](../../models/regionpayloadinput.md)] | :heavy_check_mark:                                                    | N/A                                                                   |
| `retries`                                                             | [Optional[utils.RetryConfig]](../../models/utils/retryconfig.md)      | :heavy_minus_sign:                                                    | Configuration to override the default retry behavior of the client.   |

### Response

**[models.CreateRegionsInRasterResponse](../../models/createregionsinrasterresponse.md)**

### Errors

| Error Type                | Status Code               | Content Type              |
| ------------------------- | ------------------------- | ------------------------- |
| errors.FlyPixDefaultError | 4XX, 5XX                  | \*/\*                     |