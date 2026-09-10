# Geosense

## Overview

### Available Operations

* [create_session_in_project](#create_session_in_project) - Start geosense session
* [create_session_artifact](#create_session_artifact) - Create session artifact
* [get_session_artifact](#get_session_artifact) - Get session artifact
* [send_message](#send_message) - Send geosense message

## create_session_in_project

Starts a new geosense chat session for a project.

### Example Usage

<!-- UsageSnippet language="python" operationID="create-session-in-project" method="post" path="/v2/geosense/session/{project_id}/" -->
```python
from flypix import Flypix, models


with Flypix(
    security=models.Security(
        api_key="<YOUR_API_KEY_HERE>",
    ),
) as f_client:

    res = f_client.geosense.create_session_in_project(project_id="<id>")

    # Handle response
    print(res)

```

### Parameters

| Parameter                                                           | Type                                                                | Required                                                            | Description                                                         |
| ------------------------------------------------------------------- | ------------------------------------------------------------------- | ------------------------------------------------------------------- | ------------------------------------------------------------------- |
| `project_id`                                                        | *str*                                                               | :heavy_check_mark:                                                  | N/A                                                                 |
| `retries`                                                           | [Optional[utils.RetryConfig]](../../models/utils/retryconfig.md)    | :heavy_minus_sign:                                                  | Configuration to override the default retry behavior of the client. |

### Response

**[models.CreateSessionInProjectResponse](../../models/createsessioninprojectresponse.md)**

### Errors

| Error Type                | Status Code               | Content Type              |
| ------------------------- | ------------------------- | ------------------------- |
| errors.FlyPixDefaultError | 4XX, 5XX                  | \*/\*                     |

## create_session_artifact

Creates an artifact in a geosense session.

### Example Usage

<!-- UsageSnippet language="python" operationID="create-session-artifact" method="post" path="/v2/geosense/{session_id}/artifact/" -->
```python
from flypix import Flypix, models


with Flypix(
    security=models.Security(
        api_key="<YOUR_API_KEY_HERE>",
    ),
) as f_client:

    res = f_client.geosense.create_session_artifact(session_id="<id>", artifact_data={
        "key": "<value>",
    }, type_="data")

    # Handle response
    print(res)

```

### Parameters

| Parameter                                                                                       | Type                                                                                            | Required                                                                                        | Description                                                                                     |
| ----------------------------------------------------------------------------------------------- | ----------------------------------------------------------------------------------------------- | ----------------------------------------------------------------------------------------------- | ----------------------------------------------------------------------------------------------- |
| `session_id`                                                                                    | *str*                                                                                           | :heavy_check_mark:                                                                              | N/A                                                                                             |
| `artifact_data`                                                                                 | Dict[str, *Any*]                                                                                | :heavy_check_mark:                                                                              | N/A                                                                                             |
| `type`                                                                                          | [models.CreateSessionArtifactInputBodyType](../../models/createsessionartifactinputbodytype.md) | :heavy_check_mark:                                                                              | N/A                                                                                             |
| `retries`                                                                                       | [Optional[utils.RetryConfig]](../../models/utils/retryconfig.md)                                | :heavy_minus_sign:                                                                              | Configuration to override the default retry behavior of the client.                             |

### Response

**[models.CreateSessionArtifactResponse](../../models/createsessionartifactresponse.md)**

### Errors

| Error Type                | Status Code               | Content Type              |
| ------------------------- | ------------------------- | ------------------------- |
| errors.FlyPixDefaultError | 4XX, 5XX                  | \*/\*                     |

## get_session_artifact

Returns an artifact from a geosense session.

### Example Usage

<!-- UsageSnippet language="python" operationID="get-session-artifact" method="get" path="/v2/geosense/{session_id}/artifact/{artifact_id}" -->
```python
from flypix import Flypix, models


with Flypix(
    security=models.Security(
        api_key="<YOUR_API_KEY_HERE>",
    ),
) as f_client:

    res = f_client.geosense.get_session_artifact(session_id="<id>", artifact_id="<id>")

    # Handle response
    print(res)

```

### Parameters

| Parameter                                                           | Type                                                                | Required                                                            | Description                                                         |
| ------------------------------------------------------------------- | ------------------------------------------------------------------- | ------------------------------------------------------------------- | ------------------------------------------------------------------- |
| `session_id`                                                        | *str*                                                               | :heavy_check_mark:                                                  | N/A                                                                 |
| `artifact_id`                                                       | *str*                                                               | :heavy_check_mark:                                                  | N/A                                                                 |
| `retries`                                                           | [Optional[utils.RetryConfig]](../../models/utils/retryconfig.md)    | :heavy_minus_sign:                                                  | Configuration to override the default retry behavior of the client. |

### Response

**[models.GetSessionArtifactResponse](../../models/getsessionartifactresponse.md)**

### Errors

| Error Type                | Status Code               | Content Type              |
| ------------------------- | ------------------------- | ------------------------- |
| errors.FlyPixDefaultError | 4XX, 5XX                  | \*/\*                     |

## send_message

Sends a chat message in a geosense session, optionally grounded in prior artifacts via `context`.

### Example Usage

<!-- UsageSnippet language="python" operationID="send-message" method="post" path="/v2/geosense/{session_id}/message/" -->
```python
from flypix import Flypix, models


with Flypix(
    security=models.Security(
        api_key="<YOUR_API_KEY_HERE>",
    ),
) as f_client:

    res = f_client.geosense.send_message(session_id="<id>", user_message="<value>", vector_ids=[
        "<value 1>",
    ])

    # Handle response
    print(res)

```

### Parameters

| Parameter                                                               | Type                                                                    | Required                                                                | Description                                                             |
| ----------------------------------------------------------------------- | ----------------------------------------------------------------------- | ----------------------------------------------------------------------- | ----------------------------------------------------------------------- |
| `session_id`                                                            | *str*                                                                   | :heavy_check_mark:                                                      | N/A                                                                     |
| `user_message`                                                          | *str*                                                                   | :heavy_check_mark:                                                      | N/A                                                                     |
| `vector_ids`                                                            | List[*str*]                                                             | :heavy_check_mark:                                                      | N/A                                                                     |
| `context`                                                               | List[[models.MessageContextInput](../../models/messagecontextinput.md)] | :heavy_minus_sign:                                                      | N/A                                                                     |
| `retries`                                                               | [Optional[utils.RetryConfig]](../../models/utils/retryconfig.md)        | :heavy_minus_sign:                                                      | Configuration to override the default retry behavior of the client.     |

### Response

**[models.SendMessageResponse](../../models/sendmessageresponse.md)**

### Errors

| Error Type                | Status Code               | Content Type              |
| ------------------------- | ------------------------- | ------------------------- |
| errors.FlyPixDefaultError | 4XX, 5XX                  | \*/\*                     |