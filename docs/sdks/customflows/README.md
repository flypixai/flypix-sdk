# CustomFlows

## Overview

### Available Operations

* [get_custom_flow_runs_for_project](#get_custom_flow_runs_for_project) - List project custom flow runs
* [get_custom_flow_runs_for_tenant](#get_custom_flow_runs_for_tenant) - List tenant custom flow runs
* [get_custom_flow_run](#get_custom_flow_run) - Get a custom flow run
* [get_custom_flow_run_outputs](#get_custom_flow_run_outputs) - Get a custom flow run's outputs
* [run_custom_flow](#run_custom_flow) - Run a custom flow

## get_custom_flow_runs_for_project

Lists the custom flow runs of a project with their live state.

### Example Usage

<!-- UsageSnippet language="python" operationID="get-custom-flow-runs-for-project" method="get" path="/v2/custom-flows/runs/for-project/{project_id}" -->
```python
from flypix import Flypix, models


with Flypix(
    security=models.Security(
        api_key="<YOUR_API_KEY_HERE>",
    ),
) as f_client:

    res = f_client.custom_flows.get_custom_flow_runs_for_project(project_id="<id>", offset=0, limit=200)

    # Handle response
    print(res)

```

### Parameters

| Parameter                                                                         | Type                                                                              | Required                                                                          | Description                                                                       |
| --------------------------------------------------------------------------------- | --------------------------------------------------------------------------------- | --------------------------------------------------------------------------------- | --------------------------------------------------------------------------------- |
| `project_id`                                                                      | *str*                                                                             | :heavy_check_mark:                                                                | N/A                                                                               |
| `filter_`                                                                         | *Optional[str]*                                                                   | :heavy_minus_sign:                                                                | Comma-separated field:operator:value clauses, e.g. flow_name:eq:custom_sennebogen |
| `sort`                                                                            | *Optional[str]*                                                                   | :heavy_minus_sign:                                                                | Comma-separated field:asc\|desc clauses, e.g. created_at:desc                     |
| `offset`                                                                          | *Optional[int]*                                                                   | :heavy_minus_sign:                                                                | N/A                                                                               |
| `limit`                                                                           | *Optional[int]*                                                                   | :heavy_minus_sign:                                                                | N/A                                                                               |
| `retries`                                                                         | [Optional[utils.RetryConfig]](../../models/utils/retryconfig.md)                  | :heavy_minus_sign:                                                                | Configuration to override the default retry behavior of the client.               |

### Response

**[models.GetCustomFlowRunsForProjectResponse](../../models/getcustomflowrunsforprojectresponse.md)**

### Errors

| Error Type                | Status Code               | Content Type              |
| ------------------------- | ------------------------- | ------------------------- |
| errors.FlyPixDefaultError | 4XX, 5XX                  | \*/\*                     |

## get_custom_flow_runs_for_tenant

Lists the custom flow runs of a tenant with their live state. Filter on flow_name to narrow down to a single flow.

### Example Usage

<!-- UsageSnippet language="python" operationID="get-custom-flow-runs-for-tenant" method="get" path="/v2/custom-flows/runs/for-tenant/{tenant_id}" -->
```python
from flypix import Flypix, models


with Flypix(
    security=models.Security(
        api_key="<YOUR_API_KEY_HERE>",
    ),
) as f_client:

    res = f_client.custom_flows.get_custom_flow_runs_for_tenant(tenant_id="<id>", offset=0, limit=200)

    # Handle response
    print(res)

```

### Parameters

| Parameter                                                                         | Type                                                                              | Required                                                                          | Description                                                                       |
| --------------------------------------------------------------------------------- | --------------------------------------------------------------------------------- | --------------------------------------------------------------------------------- | --------------------------------------------------------------------------------- |
| `tenant_id`                                                                       | *str*                                                                             | :heavy_check_mark:                                                                | N/A                                                                               |
| `filter_`                                                                         | *Optional[str]*                                                                   | :heavy_minus_sign:                                                                | Comma-separated field:operator:value clauses, e.g. flow_name:eq:custom_sennebogen |
| `sort`                                                                            | *Optional[str]*                                                                   | :heavy_minus_sign:                                                                | Comma-separated field:asc\|desc clauses, e.g. created_at:desc                     |
| `offset`                                                                          | *Optional[int]*                                                                   | :heavy_minus_sign:                                                                | N/A                                                                               |
| `limit`                                                                           | *Optional[int]*                                                                   | :heavy_minus_sign:                                                                | N/A                                                                               |
| `retries`                                                                         | [Optional[utils.RetryConfig]](../../models/utils/retryconfig.md)                  | :heavy_minus_sign:                                                                | Configuration to override the default retry behavior of the client.               |

### Response

**[models.GetCustomFlowRunsForTenantResponse](../../models/getcustomflowrunsfortenantresponse.md)**

### Errors

| Error Type                | Status Code               | Content Type              |
| ------------------------- | ------------------------- | ------------------------- |
| errors.FlyPixDefaultError | 4XX, 5XX                  | \*/\*                     |

## get_custom_flow_run

Returns a custom flow run with its live state: state, timings and elapsed seconds.

### Example Usage

<!-- UsageSnippet language="python" operationID="get-custom-flow-run" method="get" path="/v2/custom-flows/runs/{custom_flow_run_id}" -->
```python
from flypix import Flypix, models


with Flypix(
    security=models.Security(
        api_key="<YOUR_API_KEY_HERE>",
    ),
) as f_client:

    res = f_client.custom_flows.get_custom_flow_run(custom_flow_run_id="<id>")

    # Handle response
    print(res)

```

### Parameters

| Parameter                                                           | Type                                                                | Required                                                            | Description                                                         |
| ------------------------------------------------------------------- | ------------------------------------------------------------------- | ------------------------------------------------------------------- | ------------------------------------------------------------------- |
| `custom_flow_run_id`                                                | *str*                                                               | :heavy_check_mark:                                                  | N/A                                                                 |
| `retries`                                                           | [Optional[utils.RetryConfig]](../../models/utils/retryconfig.md)    | :heavy_minus_sign:                                                  | Configuration to override the default retry behavior of the client. |

### Response

**[models.GetCustomFlowRunResponse](../../models/getcustomflowrunresponse.md)**

### Errors

| Error Type                | Status Code               | Content Type              |
| ------------------------- | ------------------------- | ------------------------- |
| errors.FlyPixDefaultError | 4XX, 5XX                  | \*/\*                     |

## get_custom_flow_run_outputs

Returns the files a custom flow run wrote, as time-limited download links, with its live state.

### Example Usage

<!-- UsageSnippet language="python" operationID="get-custom-flow-run-outputs" method="get" path="/v2/custom-flows/runs/{custom_flow_run_id}/outputs" -->
```python
from flypix import Flypix, models


with Flypix(
    security=models.Security(
        api_key="<YOUR_API_KEY_HERE>",
    ),
) as f_client:

    res = f_client.custom_flows.get_custom_flow_run_outputs(custom_flow_run_id="<id>")

    # Handle response
    print(res)

```

### Parameters

| Parameter                                                           | Type                                                                | Required                                                            | Description                                                         |
| ------------------------------------------------------------------- | ------------------------------------------------------------------- | ------------------------------------------------------------------- | ------------------------------------------------------------------- |
| `custom_flow_run_id`                                                | *str*                                                               | :heavy_check_mark:                                                  | N/A                                                                 |
| `retries`                                                           | [Optional[utils.RetryConfig]](../../models/utils/retryconfig.md)    | :heavy_minus_sign:                                                  | Configuration to override the default retry behavior of the client. |

### Response

**[models.GetCustomFlowRunOutputsResponse](../../models/getcustomflowrunoutputsresponse.md)**

### Errors

| Error Type                | Status Code               | Content Type              |
| ------------------------- | ------------------------- | ------------------------- |
| errors.FlyPixDefaultError | 4XX, 5XX                  | \*/\*                     |

## run_custom_flow

Triggers a custom flow by name in a project of your tenant. The run is asynchronous: check its state with get-custom-flow-run, then fetch its files with get-custom-flow-run-outputs. Unknown flows 404.

### Example Usage

<!-- UsageSnippet language="python" operationID="run-custom-flow" method="post" path="/v2/custom-flows/{flow_name}/runs" -->
```python
from flypix import Flypix, models


with Flypix(
    security=models.Security(
        api_key="<YOUR_API_KEY_HERE>",
    ),
) as f_client:

    res = f_client.custom_flows.run_custom_flow(flow_name="<value>", project_id="<id>")

    # Handle response
    print(res)

```

### Parameters

| Parameter                                                                        | Type                                                                             | Required                                                                         | Description                                                                      |
| -------------------------------------------------------------------------------- | -------------------------------------------------------------------------------- | -------------------------------------------------------------------------------- | -------------------------------------------------------------------------------- |
| `flow_name`                                                                      | *str*                                                                            | :heavy_check_mark:                                                               | Name of the custom flow. Custom flows are named custom_*, e.g. custom_sennebogen |
| `project_id`                                                                     | *str*                                                                            | :heavy_check_mark:                                                               | N/A                                                                              |
| `input`                                                                          | Dict[str, *Any*]                                                                 | :heavy_minus_sign:                                                               | Parameters of the flow, passed to it as-is. Each flow defines its own.           |
| `retries`                                                                        | [Optional[utils.RetryConfig]](../../models/utils/retryconfig.md)                 | :heavy_minus_sign:                                                               | Configuration to override the default retry behavior of the client.              |

### Response

**[models.RunCustomFlowResponse](../../models/runcustomflowresponse.md)**

### Errors

| Error Type                | Status Code               | Content Type              |
| ------------------------- | ------------------------- | ------------------------- |
| errors.FlyPixDefaultError | 4XX, 5XX                  | \*/\*                     |