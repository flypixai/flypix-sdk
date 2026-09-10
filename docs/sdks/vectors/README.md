# Vectors

## Overview

### Available Operations

* [create_empty_vector](#create_empty_vector) - Create empty vector layer
* [get_classes_for_project](#get_classes_for_project) - List project classes
* [get_vectors_for_raster](#get_vectors_for_raster) - List raster vector layers
* [get_vectors_by_ids](#get_vectors_by_ids) - Get vector layers by ids
* [create_class_in_project](#create_class_in_project) - Create project class
* [delete_vector](#delete_vector) - Delete vector
* [create_annotations_in_vector](#create_annotations_in_vector) - Create annotations in a vector
* [get_vector_features](#get_vector_features) - List vector annotations
* [upload_geojson](#upload_geojson) - Upload GeoJSON annotations
* [upload_geopkg](#upload_geopkg) - Upload GeoPackage annotations
* [upload_shapefile](#upload_shapefile) - Upload Shapefile annotations

## create_empty_vector

Creates a new empty vector layer on a raster, ready to receive annotations.

### Example Usage

<!-- UsageSnippet language="python" operationID="create-empty-vector" method="post" path="/v2/vectors/" -->
```python
from flypix import Flypix, models


with Flypix(
    security=models.Security(
        api_key="<YOUR_API_KEY_HERE>",
    ),
) as f_client:

    res = f_client.vectors.create_empty_vector(raster_id="<id>")

    # Handle response
    print(res)

```

### Parameters

| Parameter                                                           | Type                                                                | Required                                                            | Description                                                         |
| ------------------------------------------------------------------- | ------------------------------------------------------------------- | ------------------------------------------------------------------- | ------------------------------------------------------------------- |
| `raster_id`                                                         | *str*                                                               | :heavy_check_mark:                                                  | N/A                                                                 |
| `name`                                                              | *Optional[str]*                                                     | :heavy_minus_sign:                                                  | N/A                                                                 |
| `retries`                                                           | [Optional[utils.RetryConfig]](../../models/utils/retryconfig.md)    | :heavy_minus_sign:                                                  | Configuration to override the default retry behavior of the client. |

### Response

**[models.CreateEmptyVectorResponse](../../models/createemptyvectorresponse.md)**

### Errors

| Error Type                | Status Code               | Content Type              |
| ------------------------- | ------------------------- | ------------------------- |
| errors.FlyPixDefaultError | 4XX, 5XX                  | \*/\*                     |

## get_classes_for_project

Lists the classes for a project.

### Example Usage

<!-- UsageSnippet language="python" operationID="get-classes-for-project" method="get" path="/v2/vectors/classes/for-project/{project_id}" -->
```python
from flypix import Flypix, models


with Flypix(
    security=models.Security(
        api_key="<YOUR_API_KEY_HERE>",
    ),
) as f_client:

    res = f_client.vectors.get_classes_for_project(project_id="<id>")

    # Handle response
    print(res)

```

### Parameters

| Parameter                                                           | Type                                                                | Required                                                            | Description                                                         |
| ------------------------------------------------------------------- | ------------------------------------------------------------------- | ------------------------------------------------------------------- | ------------------------------------------------------------------- |
| `project_id`                                                        | *str*                                                               | :heavy_check_mark:                                                  | N/A                                                                 |
| `retries`                                                           | [Optional[utils.RetryConfig]](../../models/utils/retryconfig.md)    | :heavy_minus_sign:                                                  | Configuration to override the default retry behavior of the client. |

### Response

**[models.GetClassesForProjectResponse](../../models/getclassesforprojectresponse.md)**

### Errors

| Error Type                | Status Code               | Content Type              |
| ------------------------- | ------------------------- | ------------------------- |
| errors.FlyPixDefaultError | 4XX, 5XX                  | \*/\*                     |

## get_vectors_for_raster

Lists the vector layers for a raster. This won't return the vector features, just the names and identifiers of the vector layers.

### Example Usage

<!-- UsageSnippet language="python" operationID="get-vectors-for-raster" method="get" path="/v2/vectors/for-raster/{raster_id}" -->
```python
from flypix import Flypix, models


with Flypix(
    security=models.Security(
        api_key="<YOUR_API_KEY_HERE>",
    ),
) as f_client:

    res = f_client.vectors.get_vectors_for_raster(raster_id="<id>")

    # Handle response
    print(res)

```

### Parameters

| Parameter                                                           | Type                                                                | Required                                                            | Description                                                         |
| ------------------------------------------------------------------- | ------------------------------------------------------------------- | ------------------------------------------------------------------- | ------------------------------------------------------------------- |
| `raster_id`                                                         | *str*                                                               | :heavy_check_mark:                                                  | N/A                                                                 |
| `retries`                                                           | [Optional[utils.RetryConfig]](../../models/utils/retryconfig.md)    | :heavy_minus_sign:                                                  | Configuration to override the default retry behavior of the client. |

### Response

**[models.GetVectorsForRasterResponse](../../models/getvectorsforrasterresponse.md)**

### Errors

| Error Type                | Status Code               | Content Type              |
| ------------------------- | ------------------------- | ------------------------- |
| errors.FlyPixDefaultError | 4XX, 5XX                  | \*/\*                     |

## get_vectors_by_ids

Returns the vector layers matching the given ids, in one call.

### Example Usage

<!-- UsageSnippet language="python" operationID="get-vectors-by-ids" method="post" path="/v2/vectors/get-by-ids" -->
```python
from flypix import Flypix, models


with Flypix(
    security=models.Security(
        api_key="<YOUR_API_KEY_HERE>",
    ),
) as f_client:

    res = f_client.vectors.get_vectors_by_ids(request=[
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

**[models.GetVectorsByIdsResponse](../../models/getvectorsbyidsresponse.md)**

### Errors

| Error Type                | Status Code               | Content Type              |
| ------------------------- | ------------------------- | ------------------------- |
| errors.FlyPixDefaultError | 4XX, 5XX                  | \*/\*                     |

## create_class_in_project

Creates a class in a project. Classes are shared among all vectors in a project.

### Example Usage

<!-- UsageSnippet language="python" operationID="create-class-in-project" method="post" path="/v2/vectors/{project_id}/class" -->
```python
from flypix import Flypix, models


with Flypix(
    security=models.Security(
        api_key="<YOUR_API_KEY_HERE>",
    ),
) as f_client:

    res = f_client.vectors.create_class_in_project(project_id="<id>", name="<value>")

    # Handle response
    print(res)

```

### Parameters

| Parameter                                                           | Type                                                                | Required                                                            | Description                                                         |
| ------------------------------------------------------------------- | ------------------------------------------------------------------- | ------------------------------------------------------------------- | ------------------------------------------------------------------- |
| `project_id`                                                        | *str*                                                               | :heavy_check_mark:                                                  | N/A                                                                 |
| `name`                                                              | *str*                                                               | :heavy_check_mark:                                                  | N/A                                                                 |
| `color`                                                             | *Optional[str]*                                                     | :heavy_minus_sign:                                                  | N/A                                                                 |
| `retries`                                                           | [Optional[utils.RetryConfig]](../../models/utils/retryconfig.md)    | :heavy_minus_sign:                                                  | Configuration to override the default retry behavior of the client. |

### Response

**[models.CreateClassInProjectResponse](../../models/createclassinprojectresponse.md)**

### Errors

| Error Type                | Status Code               | Content Type              |
| ------------------------- | ------------------------- | ------------------------- |
| errors.FlyPixDefaultError | 4XX, 5XX                  | \*/\*                     |

## delete_vector

Deletes a vector and its annotations. This cannot be undone.

### Example Usage

<!-- UsageSnippet language="python" operationID="delete-vector" method="delete" path="/v2/vectors/{vector_id}/" -->
```python
from flypix import Flypix, models


with Flypix(
    security=models.Security(
        api_key="<YOUR_API_KEY_HERE>",
    ),
) as f_client:

    res = f_client.vectors.delete_vector(vector_id="<id>")

    # Handle response
    print(res)

```

### Parameters

| Parameter                                                           | Type                                                                | Required                                                            | Description                                                         |
| ------------------------------------------------------------------- | ------------------------------------------------------------------- | ------------------------------------------------------------------- | ------------------------------------------------------------------- |
| `vector_id`                                                         | *str*                                                               | :heavy_check_mark:                                                  | N/A                                                                 |
| `retries`                                                           | [Optional[utils.RetryConfig]](../../models/utils/retryconfig.md)    | :heavy_minus_sign:                                                  | Configuration to override the default retry behavior of the client. |

### Response

**[models.DeleteVectorResponse](../../models/deletevectorresponse.md)**

### Errors

| Error Type                | Status Code               | Content Type              |
| ------------------------- | ------------------------- | ------------------------- |
| errors.FlyPixDefaultError | 4XX, 5XX                  | \*/\*                     |

## create_annotations_in_vector

Creates annotations in a vector from raw geometry payloads. Invalid geometry is rejected with a generic 400, not per-item validation errors.

### Example Usage

<!-- UsageSnippet language="python" operationID="create-annotations-in-vector" method="post" path="/v2/vectors/{vector_id}/annotations" -->
```python
from flypix import Flypix, models


with Flypix(
    security=models.Security(
        api_key="<YOUR_API_KEY_HERE>",
    ),
) as f_client:

    res = f_client.vectors.create_annotations_in_vector(vector_id="<id>", class_id="<id>", payload=[
        {
            "confidence": 5329.66,
            "polygon": "<value>",
        },
    ])

    # Handle response
    print(res)

```

### Parameters

| Parameter                                                                     | Type                                                                          | Required                                                                      | Description                                                                   |
| ----------------------------------------------------------------------------- | ----------------------------------------------------------------------------- | ----------------------------------------------------------------------------- | ----------------------------------------------------------------------------- |
| `vector_id`                                                                   | *str*                                                                         | :heavy_check_mark:                                                            | N/A                                                                           |
| `class_id`                                                                    | *str*                                                                         | :heavy_check_mark:                                                            | N/A                                                                           |
| `payload`                                                                     | List[[models.AnnotationPayloadInput](../../models/annotationpayloadinput.md)] | :heavy_check_mark:                                                            | N/A                                                                           |
| `retries`                                                                     | [Optional[utils.RetryConfig]](../../models/utils/retryconfig.md)              | :heavy_minus_sign:                                                            | Configuration to override the default retry behavior of the client.           |

### Response

**[models.CreateAnnotationsInVectorResponse](../../models/createannotationsinvectorresponse.md)**

### Errors

| Error Type                | Status Code               | Content Type              |
| ------------------------- | ------------------------- | ------------------------- |
| errors.FlyPixDefaultError | 4XX, 5XX                  | \*/\*                     |

## get_vector_features

Returns the vector features (annotations) of a vector.

### Example Usage

<!-- UsageSnippet language="python" operationID="get-vector-features" method="get" path="/v2/vectors/{vector_id}/features" -->
```python
from flypix import Flypix, models


with Flypix(
    security=models.Security(
        api_key="<YOUR_API_KEY_HERE>",
    ),
) as f_client:

    res = f_client.vectors.get_vector_features(vector_id="<id>")

    # Handle response
    print(res)

```

### Parameters

| Parameter                                                           | Type                                                                | Required                                                            | Description                                                         |
| ------------------------------------------------------------------- | ------------------------------------------------------------------- | ------------------------------------------------------------------- | ------------------------------------------------------------------- |
| `vector_id`                                                         | *str*                                                               | :heavy_check_mark:                                                  | N/A                                                                 |
| `retries`                                                           | [Optional[utils.RetryConfig]](../../models/utils/retryconfig.md)    | :heavy_minus_sign:                                                  | Configuration to override the default retry behavior of the client. |

### Response

**[models.GetVectorFeaturesResponse](../../models/getvectorfeaturesresponse.md)**

### Errors

| Error Type                | Status Code               | Content Type              |
| ------------------------- | ------------------------- | ------------------------- |
| errors.FlyPixDefaultError | 4XX, 5XX                  | \*/\*                     |

## upload_geojson

Creates annotations by uploading a GeoJSON file. Only Polygon features in EPSG:3857 are accepted; per-feature failures are collected into the response's `errored` list instead of failing the whole upload.

### Example Usage

<!-- UsageSnippet language="python" operationID="upload-geojson" method="post" path="/v2/vectors/{vector_id}/upload-geojson/" -->
```python
from flypix import Flypix, models


with Flypix(
    security=models.Security(
        api_key="<YOUR_API_KEY_HERE>",
    ),
) as f_client:

    res = f_client.vectors.upload_geojson(vector_id="<id>", file={
        "file_name": "example.file",
        "content": open("example.file", "rb"),
    })

    # Handle response
    print(res)

```

### Parameters

| Parameter                                                           | Type                                                                | Required                                                            | Description                                                         |
| ------------------------------------------------------------------- | ------------------------------------------------------------------- | ------------------------------------------------------------------- | ------------------------------------------------------------------- |
| `vector_id`                                                         | *str*                                                               | :heavy_check_mark:                                                  | N/A                                                                 |
| `file`                                                              | [models.UploadGeojsonFile](../../models/uploadgeojsonfile.md)       | :heavy_check_mark:                                                  | N/A                                                                 |
| `retries`                                                           | [Optional[utils.RetryConfig]](../../models/utils/retryconfig.md)    | :heavy_minus_sign:                                                  | Configuration to override the default retry behavior of the client. |

### Response

**[models.UploadGeojsonResponse](../../models/uploadgeojsonresponse.md)**

### Errors

| Error Type                | Status Code               | Content Type              |
| ------------------------- | ------------------------- | ------------------------- |
| errors.FlyPixDefaultError | 4XX, 5XX                  | \*/\*                     |

## upload_geopkg

Creates annotations by uploading a GeoPackage file. Same partial-failure behavior as the GeoJSON upload.

### Example Usage

<!-- UsageSnippet language="python" operationID="upload_geopkg" method="post" path="/v2/vectors/{vector_id}/upload-gpkg/" -->
```python
from flypix import Flypix, models


with Flypix(
    security=models.Security(
        api_key="<YOUR_API_KEY_HERE>",
    ),
) as f_client:

    res = f_client.vectors.upload_geopkg(vector_id="<id>", file={
        "file_name": "example.file",
        "content": open("example.file", "rb"),
    })

    # Handle response
    print(res)

```

### Parameters

| Parameter                                                           | Type                                                                | Required                                                            | Description                                                         |
| ------------------------------------------------------------------- | ------------------------------------------------------------------- | ------------------------------------------------------------------- | ------------------------------------------------------------------- |
| `vector_id`                                                         | *str*                                                               | :heavy_check_mark:                                                  | N/A                                                                 |
| `file`                                                              | [models.UploadGeopkgFile](../../models/uploadgeopkgfile.md)         | :heavy_check_mark:                                                  | N/A                                                                 |
| `retries`                                                           | [Optional[utils.RetryConfig]](../../models/utils/retryconfig.md)    | :heavy_minus_sign:                                                  | Configuration to override the default retry behavior of the client. |

### Response

**[models.UploadGeopkgResponse](../../models/uploadgeopkgresponse.md)**

### Errors

| Error Type                | Status Code               | Content Type              |
| ------------------------- | ------------------------- | ------------------------- |
| errors.FlyPixDefaultError | 4XX, 5XX                  | \*/\*                     |

## upload_shapefile

Creates annotations by uploading a zipped Shapefile. Same partial-failure behavior as the GeoJSON upload.

### Example Usage

<!-- UsageSnippet language="python" operationID="upload_shapefile" method="post" path="/v2/vectors/{vector_id}/upload-shp/" -->
```python
from flypix import Flypix, models


with Flypix(
    security=models.Security(
        api_key="<YOUR_API_KEY_HERE>",
    ),
) as f_client:

    res = f_client.vectors.upload_shapefile(vector_id="<id>", file={
        "file_name": "example.file",
        "content": open("example.file", "rb"),
    })

    # Handle response
    print(res)

```

### Parameters

| Parameter                                                           | Type                                                                | Required                                                            | Description                                                         |
| ------------------------------------------------------------------- | ------------------------------------------------------------------- | ------------------------------------------------------------------- | ------------------------------------------------------------------- |
| `vector_id`                                                         | *str*                                                               | :heavy_check_mark:                                                  | N/A                                                                 |
| `file`                                                              | [models.UploadShapefileFile](../../models/uploadshapefilefile.md)   | :heavy_check_mark:                                                  | N/A                                                                 |
| `retries`                                                           | [Optional[utils.RetryConfig]](../../models/utils/retryconfig.md)    | :heavy_minus_sign:                                                  | Configuration to override the default retry behavior of the client. |

### Response

**[models.UploadShapefileResponse](../../models/uploadshapefileresponse.md)**

### Errors

| Error Type                | Status Code               | Content Type              |
| ------------------------- | ------------------------- | ------------------------- |
| errors.FlyPixDefaultError | 4XX, 5XX                  | \*/\*                     |