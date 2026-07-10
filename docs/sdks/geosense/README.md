# Geosense

## Overview

GeoSense sessions, artifacts, and messages.

### Available Operations

* [create_session](#create_session) - Create Session In Project
* [create_artifact](#create_artifact) - Create Session Artifact
* [get_artifact](#get_artifact) - Get Session Artifact
* [send_message](#send_message) - Send Message

## create_session

Create a new empty session in a project ready to receive messages

### Example Usage

<!-- UsageSnippet language="python" operationID="geosense_create_session" method="post" path="/geosense/session/{project_id}/" -->
```python
from flypix import FlyPix
from uuid import UUID


with FlyPix(
    bearer_auth="<YOUR_BEARER_TOKEN_HERE>",
) as fly_pix:

    res = fly_pix.geosense.create_session(project_id=UUID("123e4567-e89b-12d3-a456-426614174000"))

    # Handle response
    print(res)

```

### Parameters

| Parameter                                                           | Type                                                                | Required                                                            | Description                                                         | Example                                                             |
| ------------------------------------------------------------------- | ------------------------------------------------------------------- | ------------------------------------------------------------------- | ------------------------------------------------------------------- | ------------------------------------------------------------------- |
| `project_id`                                                        | *UUID*                                                              | :heavy_check_mark:                                                  | N/A                                                                 | 123e4567-e89b-12d3-a456-426614174000                                |
| `retries`                                                           | [Optional[utils.RetryConfig]](../../models/utils/retryconfig.md)    | :heavy_minus_sign:                                                  | Configuration to override the default retry behavior of the client. |                                                                     |

### Response

**[UUID](../../models/responsecreatesessioninprojectgeosensesessionprojectidpost.md)**

### Errors

| Error Type                | Status Code               | Content Type              |
| ------------------------- | ------------------------- | ------------------------- |
| errors.FlyPixDefaultError | 4XX, 5XX                  | \*/\*                     |

## create_artifact

Create a data artifact to attach to a message.
Note: Not fully supported right now.

### Example Usage

<!-- UsageSnippet language="python" operationID="geosense_create_artifact" method="post" path="/geosense/session/{session_id}/artifact/" -->
```python
from flypix import FlyPix
from uuid import UUID


with FlyPix(
    bearer_auth="<YOUR_BEARER_TOKEN_HERE>",
) as fly_pix:

    res = fly_pix.geosense.create_artifact(session_id=UUID("123e4567-e89b-12d3-a456-426614174000"), artifact_data={
        "key": "<value>",
        "key1": "<value>",
        "key2": "<value>",
    }, type_="data")

    # Handle response
    print(res)

```

### Parameters

| Parameter                                                           | Type                                                                | Required                                                            | Description                                                         | Example                                                             |
| ------------------------------------------------------------------- | ------------------------------------------------------------------- | ------------------------------------------------------------------- | ------------------------------------------------------------------- | ------------------------------------------------------------------- |
| `session_id`                                                        | *UUID*                                                              | :heavy_check_mark:                                                  | N/A                                                                 | 123e4567-e89b-12d3-a456-426614174000                                |
| `artifact_data`                                                     | Dict[str, *Any*]                                                    | :heavy_check_mark:                                                  | N/A                                                                 |                                                                     |
| `type`                                                              | [models.ArtifactType](../../models/artifacttype.md)                 | :heavy_check_mark:                                                  | N/A                                                                 |                                                                     |
| `retries`                                                           | [Optional[utils.RetryConfig]](../../models/utils/retryconfig.md)    | :heavy_minus_sign:                                                  | Configuration to override the default retry behavior of the client. |                                                                     |

### Response

**[models.ArtifactResponse](../../models/artifactresponse.md)**

### Errors

| Error Type                | Status Code               | Content Type              |
| ------------------------- | ------------------------- | ------------------------- |
| errors.FlyPixDefaultError | 4XX, 5XX                  | \*/\*                     |

## get_artifact

Get a session artifact

### Example Usage

<!-- UsageSnippet language="python" operationID="geosense_get_artifact" method="get" path="/geosense/{session_id}/artifact/{artifact_id}" -->
```python
from flypix import FlyPix
from uuid import UUID


with FlyPix(
    bearer_auth="<YOUR_BEARER_TOKEN_HERE>",
) as fly_pix:

    res = fly_pix.geosense.get_artifact(session_id=UUID("123e4567-e89b-12d3-a456-426614174000"), artifact_id=UUID("123e4567-e89b-12d3-a456-426614174000"))

    # Handle response
    print(res)

```

### Parameters

| Parameter                                                           | Type                                                                | Required                                                            | Description                                                         | Example                                                             |
| ------------------------------------------------------------------- | ------------------------------------------------------------------- | ------------------------------------------------------------------- | ------------------------------------------------------------------- | ------------------------------------------------------------------- |
| `session_id`                                                        | *UUID*                                                              | :heavy_check_mark:                                                  | N/A                                                                 | 123e4567-e89b-12d3-a456-426614174000                                |
| `artifact_id`                                                       | *UUID*                                                              | :heavy_check_mark:                                                  | N/A                                                                 | 123e4567-e89b-12d3-a456-426614174000                                |
| `retries`                                                           | [Optional[utils.RetryConfig]](../../models/utils/retryconfig.md)    | :heavy_minus_sign:                                                  | Configuration to override the default retry behavior of the client. |                                                                     |

### Response

**[models.ArtifactResponse](../../models/artifactresponse.md)**

### Errors

| Error Type                | Status Code               | Content Type              |
| ------------------------- | ------------------------- | ------------------------- |
| errors.FlyPixDefaultError | 4XX, 5XX                  | \*/\*                     |

## send_message

Send a message to the LLM.
Check the official docs to understand the GeoSense message specification

### Example Usage

<!-- UsageSnippet language="python" operationID="geosense_send_message" method="post" path="/geosense/{session_id}/message/" -->
```python
from flypix import FlyPix
from uuid import UUID


with FlyPix(
    bearer_auth="<YOUR_BEARER_TOKEN_HERE>",
) as fly_pix:

    res = fly_pix.geosense.send_message(session_id=UUID("123e4567-e89b-12d3-a456-426614174000"), user_message="New String", vector_ids=[
        UUID("123e4567-e89b-12d3-a456-426614174000"),
    ], context=[
        {
            "artifact_id": UUID("123e4567-e89b-12d3-a456-426614174000"),
            "type": "data",
        },
    ])

    # Handle response
    print(res)

```

### Parameters

| Parameter                                                           | Type                                                                | Required                                                            | Description                                                         | Example                                                             |
| ------------------------------------------------------------------- | ------------------------------------------------------------------- | ------------------------------------------------------------------- | ------------------------------------------------------------------- | ------------------------------------------------------------------- |
| `session_id`                                                        | *UUID*                                                              | :heavy_check_mark:                                                  | N/A                                                                 | 123e4567-e89b-12d3-a456-426614174000                                |
| `user_message`                                                      | *str*                                                               | :heavy_check_mark:                                                  | A string based value object                                         | New String                                                          |
| `vector_ids`                                                        | List[*UUID*]                                                        | :heavy_check_mark:                                                  | N/A                                                                 |                                                                     |
| `context`                                                           | List[[models.AnyMessageContext](../../models/anymessagecontext.md)] | :heavy_minus_sign:                                                  | N/A                                                                 |                                                                     |
| `retries`                                                           | [Optional[utils.RetryConfig]](../../models/utils/retryconfig.md)    | :heavy_minus_sign:                                                  | Configuration to override the default retry behavior of the client. |                                                                     |

### Response

**[models.ChatMessageResponse](../../models/chatmessageresponse.md)**

### Errors

| Error Type                | Status Code               | Content Type              |
| ------------------------- | ------------------------- | ------------------------- |
| errors.FlyPixDefaultError | 4XX, 5XX                  | \*/\*                     |