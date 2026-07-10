# Vectors

## Overview

Vector data — classes, features, and annotations.

### Available Operations

* [list_for_file](#list_for_file) - Get Vectors For File
* [list_classes_for_project](#list_classes_for_project) - Get Project Classes
* [create_class](#create_class) - Create Class In Project
* [get_features](#get_features) - Get Vector Features
* [create](#create) - Create Empty Vector
* [delete](#delete) - Delete Vector
* [create_annotations](#create_annotations) - Create Annotations In Vector
* [upload_geojson](#upload_geojson) - Upload Geojson
* [upload_gpkg](#upload_gpkg) - Upload Gpkg
* [upload_shapefile](#upload_shapefile) - Upload Shp

## list_for_file

Get the vector layers for a file.
This won't return the vector features but rather just the names and identifier of the vector layers

### Example Usage

<!-- UsageSnippet language="python" operationID="vectors_list_for_file" method="get" path="/vectors/for-file/{file_id}" -->
```python
from flypix import FlyPix
from uuid import UUID


with FlyPix(
    bearer_auth="<YOUR_BEARER_TOKEN_HERE>",
) as fly_pix:

    res = fly_pix.vectors.list_for_file(file_id=UUID("123e4567-e89b-12d3-a456-426614174000"))

    # Handle response
    print(res)

```

### Parameters

| Parameter                                                           | Type                                                                | Required                                                            | Description                                                         | Example                                                             |
| ------------------------------------------------------------------- | ------------------------------------------------------------------- | ------------------------------------------------------------------- | ------------------------------------------------------------------- | ------------------------------------------------------------------- |
| `file_id`                                                           | *UUID*                                                              | :heavy_check_mark:                                                  | N/A                                                                 | 123e4567-e89b-12d3-a456-426614174000                                |
| `retries`                                                           | [Optional[utils.RetryConfig]](../../models/utils/retryconfig.md)    | :heavy_minus_sign:                                                  | Configuration to override the default retry behavior of the client. |                                                                     |

### Response

**[List[models.VectorResponse]](../../models/.md)**

### Errors

| Error Type                | Status Code               | Content Type              |
| ------------------------- | ------------------------- | ------------------------- |
| errors.FlyPixDefaultError | 4XX, 5XX                  | \*/\*                     |

## list_classes_for_project

Get the classes for the specified project

### Example Usage

<!-- UsageSnippet language="python" operationID="vectors_list_classes_for_project" method="get" path="/vectors/classes/for-project/{project_id}" -->
```python
from flypix import FlyPix
from uuid import UUID


with FlyPix(
    bearer_auth="<YOUR_BEARER_TOKEN_HERE>",
) as fly_pix:

    res = fly_pix.vectors.list_classes_for_project(project_id=UUID("123e4567-e89b-12d3-a456-426614174000"))

    # Handle response
    print(res)

```

### Parameters

| Parameter                                                           | Type                                                                | Required                                                            | Description                                                         | Example                                                             |
| ------------------------------------------------------------------- | ------------------------------------------------------------------- | ------------------------------------------------------------------- | ------------------------------------------------------------------- | ------------------------------------------------------------------- |
| `project_id`                                                        | *UUID*                                                              | :heavy_check_mark:                                                  | N/A                                                                 | 123e4567-e89b-12d3-a456-426614174000                                |
| `retries`                                                           | [Optional[utils.RetryConfig]](../../models/utils/retryconfig.md)    | :heavy_minus_sign:                                                  | Configuration to override the default retry behavior of the client. |                                                                     |

### Response

**[List[models.ClassResponse]](../../models/.md)**

### Errors

| Error Type                | Status Code               | Content Type              |
| ------------------------- | ------------------------- | ------------------------- |
| errors.FlyPixDefaultError | 4XX, 5XX                  | \*/\*                     |

## create_class

Create Class in a project. Classes are shared among all vectors in a project

### Example Usage

<!-- UsageSnippet language="python" operationID="vectors_create_class" method="post" path="/vectors/{project_id}/class" -->
```python
from flypix import FlyPix
from uuid import UUID


with FlyPix(
    bearer_auth="<YOUR_BEARER_TOKEN_HERE>",
) as fly_pix:

    res = fly_pix.vectors.create_class(project_id=UUID("123e4567-e89b-12d3-a456-426614174000"), name="New String", color="FF0000")

    # Handle response
    print(res)

```

### Parameters

| Parameter                                                           | Type                                                                | Required                                                            | Description                                                         | Example                                                             |
| ------------------------------------------------------------------- | ------------------------------------------------------------------- | ------------------------------------------------------------------- | ------------------------------------------------------------------- | ------------------------------------------------------------------- |
| `project_id`                                                        | *UUID*                                                              | :heavy_check_mark:                                                  | N/A                                                                 | 123e4567-e89b-12d3-a456-426614174000                                |
| `name`                                                              | *str*                                                               | :heavy_check_mark:                                                  | A string based value object                                         | New String                                                          |
| `color`                                                             | *Optional[str]*                                                     | :heavy_minus_sign:                                                  | A string based value object                                         | FF0000                                                              |
| `retries`                                                           | [Optional[utils.RetryConfig]](../../models/utils/retryconfig.md)    | :heavy_minus_sign:                                                  | Configuration to override the default retry behavior of the client. |                                                                     |

### Response

**[models.ClassResponse](../../models/classresponse.md)**

### Errors

| Error Type                | Status Code               | Content Type              |
| ------------------------- | ------------------------- | ------------------------- |
| errors.FlyPixDefaultError | 4XX, 5XX                  | \*/\*                     |

## get_features

Get the vector features (annotations) of a vector

### Example Usage

<!-- UsageSnippet language="python" operationID="vectors_get_features" method="get" path="/vectors/{vector_id}/features" -->
```python
from flypix import FlyPix
from uuid import UUID


with FlyPix(
    bearer_auth="<YOUR_BEARER_TOKEN_HERE>",
) as fly_pix:

    res = fly_pix.vectors.get_features(vector_id=UUID("123e4567-e89b-12d3-a456-426614174000"))

    # Handle response
    print(res)

```

### Parameters

| Parameter                                                           | Type                                                                | Required                                                            | Description                                                         | Example                                                             |
| ------------------------------------------------------------------- | ------------------------------------------------------------------- | ------------------------------------------------------------------- | ------------------------------------------------------------------- | ------------------------------------------------------------------- |
| `vector_id`                                                         | *UUID*                                                              | :heavy_check_mark:                                                  | N/A                                                                 | 123e4567-e89b-12d3-a456-426614174000                                |
| `retries`                                                           | [Optional[utils.RetryConfig]](../../models/utils/retryconfig.md)    | :heavy_minus_sign:                                                  | Configuration to override the default retry behavior of the client. |                                                                     |

### Response

**[models.VectorFeatures](../../models/vectorfeatures.md)**

### Errors

| Error Type                | Status Code               | Content Type              |
| ------------------------- | ------------------------- | ------------------------- |
| errors.FlyPixDefaultError | 4XX, 5XX                  | \*/\*                     |

## create

Create a new empty vector layer in a file ready to receive annotations

### Example Usage

<!-- UsageSnippet language="python" operationID="vectors_create" method="post" path="/vectors/" -->
```python
from flypix import FlyPix
from uuid import UUID


with FlyPix(
    bearer_auth="<YOUR_BEARER_TOKEN_HERE>",
) as fly_pix:

    res = fly_pix.vectors.create(file_id=UUID("123e4567-e89b-12d3-a456-426614174000"), name="New String")

    # Handle response
    print(res)

```

### Parameters

| Parameter                                                           | Type                                                                | Required                                                            | Description                                                         | Example                                                             |
| ------------------------------------------------------------------- | ------------------------------------------------------------------- | ------------------------------------------------------------------- | ------------------------------------------------------------------- | ------------------------------------------------------------------- |
| `file_id`                                                           | *UUID*                                                              | :heavy_check_mark:                                                  | A string in UUID format                                             | 123e4567-e89b-12d3-a456-426614174000                                |
| `name`                                                              | *Optional[str]*                                                     | :heavy_minus_sign:                                                  | A string based value object                                         | New String                                                          |
| `retries`                                                           | [Optional[utils.RetryConfig]](../../models/utils/retryconfig.md)    | :heavy_minus_sign:                                                  | Configuration to override the default retry behavior of the client. |                                                                     |

### Response

**[models.VectorResponse](../../models/vectorresponse.md)**

### Errors

| Error Type                | Status Code               | Content Type              |
| ------------------------- | ------------------------- | ------------------------- |
| errors.FlyPixDefaultError | 4XX, 5XX                  | \*/\*                     |

## delete

Delete a vector and its annotations

### Example Usage

<!-- UsageSnippet language="python" operationID="vectors_delete" method="delete" path="/vectors/{vector_id}/" -->
```python
from flypix import FlyPix
from uuid import UUID


with FlyPix(
    bearer_auth="<YOUR_BEARER_TOKEN_HERE>",
) as fly_pix:

    res = fly_pix.vectors.delete(vector_id=UUID("123e4567-e89b-12d3-a456-426614174000"))

    # Handle response
    print(res)

```

### Parameters

| Parameter                                                           | Type                                                                | Required                                                            | Description                                                         | Example                                                             |
| ------------------------------------------------------------------- | ------------------------------------------------------------------- | ------------------------------------------------------------------- | ------------------------------------------------------------------- | ------------------------------------------------------------------- |
| `vector_id`                                                         | *UUID*                                                              | :heavy_check_mark:                                                  | N/A                                                                 | 123e4567-e89b-12d3-a456-426614174000                                |
| `retries`                                                           | [Optional[utils.RetryConfig]](../../models/utils/retryconfig.md)    | :heavy_minus_sign:                                                  | Configuration to override the default retry behavior of the client. |                                                                     |

### Response

**[Any](../../models/.md)**

### Errors

| Error Type                | Status Code               | Content Type              |
| ------------------------- | ------------------------- | ------------------------- |
| errors.FlyPixDefaultError | 4XX, 5XX                  | \*/\*                     |

## create_annotations

Create annotations in a vector

### Example Usage

<!-- UsageSnippet language="python" operationID="vectors_create_annotations" method="post" path="/vectors/{vector_id}/annotations" -->
```python
from flypix import FlyPix
from uuid import UUID


with FlyPix(
    bearer_auth="<YOUR_BEARER_TOKEN_HERE>",
) as fly_pix:

    res = fly_pix.vectors.create_annotations(vector_id=UUID("123e4567-e89b-12d3-a456-426614174000"), class_id="car-124b", payload=[])

    # Handle response
    print(res)

```

### Parameters

| Parameter                                                                           | Type                                                                                | Required                                                                            | Description                                                                         | Example                                                                             |
| ----------------------------------------------------------------------------------- | ----------------------------------------------------------------------------------- | ----------------------------------------------------------------------------------- | ----------------------------------------------------------------------------------- | ----------------------------------------------------------------------------------- |
| `vector_id`                                                                         | *UUID*                                                                              | :heavy_check_mark:                                                                  | N/A                                                                                 | 123e4567-e89b-12d3-a456-426614174000                                                |
| `class_id`                                                                          | *str*                                                                               | :heavy_check_mark:                                                                  | Class Id                                                                            | car-124b                                                                            |
| `payload`                                                                           | List[[models.AnnotationGeometryPayload](../../models/annotationgeometrypayload.md)] | :heavy_check_mark:                                                                  | N/A                                                                                 |                                                                                     |
| `retries`                                                                           | [Optional[utils.RetryConfig]](../../models/utils/retryconfig.md)                    | :heavy_minus_sign:                                                                  | Configuration to override the default retry behavior of the client.                 |                                                                                     |

### Response

**[List[int]](../../models/.md)**

### Errors

| Error Type                | Status Code               | Content Type              |
| ------------------------- | ------------------------- | ------------------------- |
| errors.FlyPixDefaultError | 4XX, 5XX                  | \*/\*                     |

## upload_geojson

Create annotations by uploading a GeoJSON file. The file must have a valid `.geojson` extension.
The only geometries supported are POLYGON. The only EPSG supported is EPSG3857.
The geojson MUST have either `class_id` or `class_name` property for every geometry.

### Example Usage

<!-- UsageSnippet language="python" operationID="vectors_upload_geojson" method="post" path="/vectors/{vector_id}/upload-geojson/" -->
```python
from flypix import FlyPix
from uuid import UUID


with FlyPix(
    bearer_auth="<YOUR_BEARER_TOKEN_HERE>",
) as fly_pix:

    res = fly_pix.vectors.upload_geojson(vector_id=UUID("123e4567-e89b-12d3-a456-426614174000"), file="<value>")

    # Handle response
    print(res)

```

### Parameters

| Parameter                                                           | Type                                                                | Required                                                            | Description                                                         | Example                                                             |
| ------------------------------------------------------------------- | ------------------------------------------------------------------- | ------------------------------------------------------------------- | ------------------------------------------------------------------- | ------------------------------------------------------------------- |
| `vector_id`                                                         | *UUID*                                                              | :heavy_check_mark:                                                  | N/A                                                                 | 123e4567-e89b-12d3-a456-426614174000                                |
| `file`                                                              | *str*                                                               | :heavy_check_mark:                                                  | N/A                                                                 |                                                                     |
| `retries`                                                           | [Optional[utils.RetryConfig]](../../models/utils/retryconfig.md)    | :heavy_minus_sign:                                                  | Configuration to override the default retry behavior of the client. |                                                                     |

### Response

**[models.UploadAnnotationsResponse](../../models/uploadannotationsresponse.md)**

### Errors

| Error Type                | Status Code               | Content Type              |
| ------------------------- | ------------------------- | ------------------------- |
| errors.FlyPixDefaultError | 4XX, 5XX                  | \*/\*                     |

## upload_gpkg

Create annotations by uploading a GeoPackage file. The file must have a valid `.gpkg` extension.
The only geometries supported are POLYGON. The only EPSG supported is EPSG3857
The GPKG MUST have either `class_id` or `class_name` column for every geometry.
The GPKG MUST have a `geometry` column

### Example Usage

<!-- UsageSnippet language="python" operationID="vectors_upload_gpkg" method="post" path="/vectors/{vector_id}/upload-gpkg/" -->
```python
from flypix import FlyPix
from uuid import UUID


with FlyPix(
    bearer_auth="<YOUR_BEARER_TOKEN_HERE>",
) as fly_pix:

    res = fly_pix.vectors.upload_gpkg(vector_id=UUID("123e4567-e89b-12d3-a456-426614174000"), file="<value>")

    # Handle response
    print(res)

```

### Parameters

| Parameter                                                           | Type                                                                | Required                                                            | Description                                                         | Example                                                             |
| ------------------------------------------------------------------- | ------------------------------------------------------------------- | ------------------------------------------------------------------- | ------------------------------------------------------------------- | ------------------------------------------------------------------- |
| `vector_id`                                                         | *UUID*                                                              | :heavy_check_mark:                                                  | N/A                                                                 | 123e4567-e89b-12d3-a456-426614174000                                |
| `file`                                                              | *str*                                                               | :heavy_check_mark:                                                  | N/A                                                                 |                                                                     |
| `retries`                                                           | [Optional[utils.RetryConfig]](../../models/utils/retryconfig.md)    | :heavy_minus_sign:                                                  | Configuration to override the default retry behavior of the client. |                                                                     |

### Response

**[models.UploadAnnotationsResponse](../../models/uploadannotationsresponse.md)**

### Errors

| Error Type                | Status Code               | Content Type              |
| ------------------------- | ------------------------- | ------------------------- |
| errors.FlyPixDefaultError | 4XX, 5XX                  | \*/\*                     |

## upload_shapefile

Create annotations by uploading a ZIPPED Shapefile (shp). The file must have a valid `.shp.zip` extension.
The zipped file must NOT contain any folders inside and only the shapefile
The only geometries supported are POLYGON. The only EPSG supported is EPSG3857
The SHP MUST have either `class_id` or `class_name` property for every geometry.

### Example Usage

<!-- UsageSnippet language="python" operationID="vectors_upload_shapefile" method="post" path="/vectors/{vector_id}/upload-shp/" -->
```python
from flypix import FlyPix
from uuid import UUID


with FlyPix(
    bearer_auth="<YOUR_BEARER_TOKEN_HERE>",
) as fly_pix:

    res = fly_pix.vectors.upload_shapefile(vector_id=UUID("123e4567-e89b-12d3-a456-426614174000"), file="<value>")

    # Handle response
    print(res)

```

### Parameters

| Parameter                                                           | Type                                                                | Required                                                            | Description                                                         | Example                                                             |
| ------------------------------------------------------------------- | ------------------------------------------------------------------- | ------------------------------------------------------------------- | ------------------------------------------------------------------- | ------------------------------------------------------------------- |
| `vector_id`                                                         | *UUID*                                                              | :heavy_check_mark:                                                  | N/A                                                                 | 123e4567-e89b-12d3-a456-426614174000                                |
| `file`                                                              | *str*                                                               | :heavy_check_mark:                                                  | N/A                                                                 |                                                                     |
| `retries`                                                           | [Optional[utils.RetryConfig]](../../models/utils/retryconfig.md)    | :heavy_minus_sign:                                                  | Configuration to override the default retry behavior of the client. |                                                                     |

### Response

**[models.UploadAnnotationsResponse](../../models/uploadannotationsresponse.md)**

### Errors

| Error Type                | Status Code               | Content Type              |
| ------------------------- | ------------------------- | ------------------------- |
| errors.FlyPixDefaultError | 4XX, 5XX                  | \*/\*                     |