<p style="text-align: center">
  <a href="https://flypix.ai">
    <img src="https://flypix.ai/wp-content/uploads/2026/06/flypixLogoNew.webp" alt="FlyPix" width="240">
  </a>
</p>

# flypix

The official Python SDK for the [FlyPix](https://flypix.ai) API — programmatic
access to projects, files, models, inferences, vectors, and more.

> **Status:** released. The SDK is generated from the FlyPix OpenAPI spec with
> [Speakeasy](https://www.speakeasy.com). See [`SETUP.md`](https://github.com/flypix-ai/flypix-sdk/blob/master/./SETUP.md) for how it
> is generated and maintained. Installation and usage are documented in the
> generated sections below.

## Contributing

This SDK is generated — the code under `src/flypix/` is **not** hand-edited.
Improvements to naming and ergonomics happen in `openapi/overlay.yaml`; see
[`SETUP.md`](https://github.com/flypix-ai/flypix-sdk/blob/master/./SETUP.md).

## License

See [LICENSE](https://github.com/flypix-ai/flypix-sdk/blob/master/./LICENSE).

<!-- Start Summary [summary] -->
## Summary

Public API: 
Public OpenAPI Schema

This API lets you interact directly with the application with HTTP requests.

You will need to set a valid authorization header for every request:

`Authorization: Bearer <token>`

Example use case: Find an existing raster and its vector features:

```
POST /auth/login/password -> Fetch token and use it in subsequent requests
GET /users/tenant/for-user/ -> Get your tenant id for subsequent requests
GET /projects/for-tenant/{tenant_id} -> Find your project
GET /rasters/for-project/{project_id}/tree -> Find your raster
GET /vectors/for-raster/{raster_id} -> Get the vector ids for the raster
GET /vectors/{vector_id}/features -> Get the annotations
```
<!-- End Summary [summary] -->

<!-- Start Table of Contents [toc] -->
## Table of Contents
<!-- $toc-max-depth=2 -->
* [flypix](https://github.com/flypix-ai/flypix-sdk/blob/master/#flypix)
  * [Contributing](https://github.com/flypix-ai/flypix-sdk/blob/master/#contributing)
  * [License](https://github.com/flypix-ai/flypix-sdk/blob/master/#license)
  * [SDK Installation](https://github.com/flypix-ai/flypix-sdk/blob/master/#sdk-installation)
  * [IDE Support](https://github.com/flypix-ai/flypix-sdk/blob/master/#ide-support)
  * [SDK Example Usage](https://github.com/flypix-ai/flypix-sdk/blob/master/#sdk-example-usage)
  * [Authentication](https://github.com/flypix-ai/flypix-sdk/blob/master/#authentication)
  * [Available Resources and Operations](https://github.com/flypix-ai/flypix-sdk/blob/master/#available-resources-and-operations)
  * [File uploads](https://github.com/flypix-ai/flypix-sdk/blob/master/#file-uploads)
  * [Retries](https://github.com/flypix-ai/flypix-sdk/blob/master/#retries)
  * [Error Handling](https://github.com/flypix-ai/flypix-sdk/blob/master/#error-handling)
  * [Server Selection](https://github.com/flypix-ai/flypix-sdk/blob/master/#server-selection)
  * [Custom HTTP Client](https://github.com/flypix-ai/flypix-sdk/blob/master/#custom-http-client)
  * [Resource Management](https://github.com/flypix-ai/flypix-sdk/blob/master/#resource-management)
  * [Debugging](https://github.com/flypix-ai/flypix-sdk/blob/master/#debugging)

<!-- End Table of Contents [toc] -->

<!-- Start SDK Installation [installation] -->
## SDK Installation

> [!NOTE]
> **Python version upgrade policy**
>
> Once a Python version reaches its [official end of life date](https://devguide.python.org/versions/), a 3-month grace period is provided for users to upgrade. Following this grace period, the minimum python version supported in the SDK will be updated.

The SDK can be installed with *uv*, *pip*, or *poetry* package managers.

### uv

*uv* is a fast Python package installer and resolver, designed as a drop-in replacement for pip and pip-tools. It's recommended for its speed and modern Python tooling capabilities.

```bash
uv add flypix
```

### PIP

*PIP* is the default package installer for Python, enabling easy installation and management of packages from PyPI via the command line.

```bash
pip install flypix
```

### Poetry

*Poetry* is a modern tool that simplifies dependency management and package publishing by using a single `pyproject.toml` file to handle project metadata and dependencies.

```bash
poetry add flypix
```

### Shell and script usage with `uv`

You can use this SDK in a Python shell with [uv](https://docs.astral.sh/uv/) and the `uvx` command that comes with it like so:

```shell
uvx --from flypix python
```

It's also possible to write a standalone Python script without needing to set up a whole project like so:

```python
#!/usr/bin/env -S uv run --script
# /// script
# requires-python = ">=3.10"
# dependencies = [
#     "flypix",
# ]
# ///

from flypix import Flypix

sdk = Flypix(
  # SDK arguments
)

# Rest of script here...
```

Once that is saved to a file, you can run it with `uv run script.py` where
`script.py` can be replaced with the actual file name.
<!-- End SDK Installation [installation] -->

<!-- Start IDE Support [idesupport] -->
## IDE Support

### PyCharm

Generally, the SDK will work well with most IDEs out of the box. However, when using PyCharm, you can enjoy much better integration with Pydantic by installing an additional plugin.

- [PyCharm Pydantic Plugin](https://docs.pydantic.dev/latest/integrations/pycharm/)
<!-- End IDE Support [idesupport] -->

<!-- Start SDK Example Usage [usage] -->
## SDK Example Usage

### Example

```python
# Synchronous Example
from flypix import Flypix


with Flypix() as f_client:

    res = f_client.system.health()

    # Handle response
    print(res)
```

</br>

The same SDK client can also be used to make asynchronous requests by importing asyncio.

```python
# Asynchronous Example
import asyncio
from flypix import Flypix

async def main():

    async with Flypix() as f_client:

        res = await f_client.system.health_async()

        # Handle response
        print(res)

asyncio.run(main())
```
<!-- End SDK Example Usage [usage] -->

<!-- Start Authentication [security] -->
## Authentication

### Per-Client Security Schemes

This SDK supports the following security schemes globally:

| Name          | Type   | Scheme      |
| ------------- | ------ | ----------- |
| `api_key`     | apiKey | API key     |
| `bearer_auth` | http   | HTTP Bearer |

You can set the security parameters through the `security` optional parameter when initializing the SDK client instance. The selected scheme will be used by default to authenticate with the API for all operations that support it. For example:
```python
from flypix import Flypix, models


with Flypix(
    security=models.Security(
        api_key="<YOUR_API_KEY_HERE>",
    ),
) as f_client:

    res = f_client.system.health()

    # Handle response
    print(res)

```
<!-- End Authentication [security] -->

<!-- Start Available Resources and Operations [operations] -->
## Available Resources and Operations

<details open>
<summary>Available methods</summary>

### [Auth](https://github.com/flypix-ai/flypix-sdk/blob/master/docs/sdks/auth/README.md)

* [login_with_password](https://github.com/flypix-ai/flypix-sdk/blob/master/docs/sdks/auth/README.md#login_with_password) - Login with password
* [refresh_token](https://github.com/flypix-ai/flypix-sdk/blob/master/docs/sdks/auth/README.md#refresh_token) - Refresh token

### [Files](https://github.com/flypix-ai/flypix-sdk/blob/master/docs/sdks/files/README.md)

* [upload_v2](https://github.com/flypix-ai/flypix-sdk/blob/master/docs/sdks/files/README.md#upload_v2) - Upload a file
* [upload_from_url](https://github.com/flypix-ai/flypix-sdk/blob/master/docs/sdks/files/README.md#upload_from_url) - Upload a file from a URL
* [get_storage_usage](https://github.com/flypix-ai/flypix-sdk/blob/master/docs/sdks/files/README.md#get_storage_usage) - Get storage usage
* [get_file_download_link](https://github.com/flypix-ai/flypix-sdk/blob/master/docs/sdks/files/README.md#get_file_download_link) - Get file download link

### [Folders](https://github.com/flypix-ai/flypix-sdk/blob/master/docs/sdks/folders/README.md)

* [create_folder](https://github.com/flypix-ai/flypix-sdk/blob/master/docs/sdks/folders/README.md#create_folder) - Create folder
* [get_folders_for_folder](https://github.com/flypix-ai/flypix-sdk/blob/master/docs/sdks/folders/README.md#get_folders_for_folder) - List subfolders
* [get_folders_in_project_root](https://github.com/flypix-ai/flypix-sdk/blob/master/docs/sdks/folders/README.md#get_folders_in_project_root) - List root folders
* [get_folders_by_ids](https://github.com/flypix-ai/flypix-sdk/blob/master/docs/sdks/folders/README.md#get_folders_by_ids) - Get folders by ids
* [delete_folder](https://github.com/flypix-ai/flypix-sdk/blob/master/docs/sdks/folders/README.md#delete_folder) - Delete folder

### [Geosense](https://github.com/flypix-ai/flypix-sdk/blob/master/docs/sdks/geosense/README.md)

* [create_session_in_project](https://github.com/flypix-ai/flypix-sdk/blob/master/docs/sdks/geosense/README.md#create_session_in_project) - Start geosense session
* [create_session_artifact](https://github.com/flypix-ai/flypix-sdk/blob/master/docs/sdks/geosense/README.md#create_session_artifact) - Create session artifact
* [get_session_artifact](https://github.com/flypix-ai/flypix-sdk/blob/master/docs/sdks/geosense/README.md#get_session_artifact) - Get session artifact
* [send_message](https://github.com/flypix-ai/flypix-sdk/blob/master/docs/sdks/geosense/README.md#send_message) - Send geosense message

### [Inferences](https://github.com/flypix-ai/flypix-sdk/blob/master/docs/sdks/inferences/README.md)

* [get_inferences_for_project](https://github.com/flypix-ai/flypix-sdk/blob/master/docs/sdks/inferences/README.md#get_inferences_for_project) - List project inferences
* [get_inferences_for_raster](https://github.com/flypix-ai/flypix-sdk/blob/master/docs/sdks/inferences/README.md#get_inferences_for_raster) - List raster inferences
* [get_inferences_for_tenant](https://github.com/flypix-ai/flypix-sdk/blob/master/docs/sdks/inferences/README.md#get_inferences_for_tenant) - List tenant inferences
* [get_inferences_by_ids](https://github.com/flypix-ai/flypix-sdk/blob/master/docs/sdks/inferences/README.md#get_inferences_by_ids) - Get inferences by ids

### [Models](https://github.com/flypix-ai/flypix-sdk/blob/master/docs/sdks/models/README.md)

* [apply_change_detection](https://github.com/flypix-ai/flypix-sdk/blob/master/docs/sdks/models/README.md#apply_change_detection) - Apply change detection
* [get_models_for_project](https://github.com/flypix-ai/flypix-sdk/blob/master/docs/sdks/models/README.md#get_models_for_project) - List project models
* [get_models_for_tenant](https://github.com/flypix-ai/flypix-sdk/blob/master/docs/sdks/models/README.md#get_models_for_tenant) - List tenant models
* [get_models_by_ids](https://github.com/flypix-ai/flypix-sdk/blob/master/docs/sdks/models/README.md#get_models_by_ids) - Get models by ids
* [get_inference_status](https://github.com/flypix-ai/flypix-sdk/blob/master/docs/sdks/models/README.md#get_inference_status) - Get inference status
* [get_official_models](https://github.com/flypix-ai/flypix-sdk/blob/master/docs/sdks/models/README.md#get_official_models) - List official models
* [delete_model](https://github.com/flypix-ai/flypix-sdk/blob/master/docs/sdks/models/README.md#delete_model) - Delete model
* [apply_model_on_raster](https://github.com/flypix-ai/flypix-sdk/blob/master/docs/sdks/models/README.md#apply_model_on_raster) - Apply model to raster
* [estimate_model_application_on_file](https://github.com/flypix-ai/flypix-sdk/blob/master/docs/sdks/models/README.md#estimate_model_application_on_file) - Estimate model application cost

### [Payments](https://github.com/flypix-ai/flypix-sdk/blob/master/docs/sdks/payments/README.md)

* [get_tenant_balance](https://github.com/flypix-ai/flypix-sdk/blob/master/docs/sdks/payments/README.md#get_tenant_balance) - Get tenant balance
* [get_tenant_transactions](https://github.com/flypix-ai/flypix-sdk/blob/master/docs/sdks/payments/README.md#get_tenant_transactions) - List tenant transactions

### [Projects](https://github.com/flypix-ai/flypix-sdk/blob/master/docs/sdks/projects/README.md)

* [create_project](https://github.com/flypix-ai/flypix-sdk/blob/master/docs/sdks/projects/README.md#create_project) - Create project
* [get_projects_for_tenant](https://github.com/flypix-ai/flypix-sdk/blob/master/docs/sdks/projects/README.md#get_projects_for_tenant) - List projects for tenant
* [delete_project](https://github.com/flypix-ai/flypix-sdk/blob/master/docs/sdks/projects/README.md#delete_project) - Delete project

### [Rasters](https://github.com/flypix-ai/flypix-sdk/blob/master/docs/sdks/rasters/README.md)

* [get_rasters_for_project](https://github.com/flypix-ai/flypix-sdk/blob/master/docs/sdks/rasters/README.md#get_rasters_for_project) - List project rasters
* [get_project_raster_tree](https://github.com/flypix-ai/flypix-sdk/blob/master/docs/sdks/rasters/README.md#get_project_raster_tree) - Get project raster tree
* [get_rasters_for_tenant](https://github.com/flypix-ai/flypix-sdk/blob/master/docs/sdks/rasters/README.md#get_rasters_for_tenant) - List tenant rasters
* [get_rasters_by_ids](https://github.com/flypix-ai/flypix-sdk/blob/master/docs/sdks/rasters/README.md#get_rasters_by_ids) - Get rasters by ids
* [delete_raster](https://github.com/flypix-ai/flypix-sdk/blob/master/docs/sdks/rasters/README.md#delete_raster) - Delete raster
* [get_raster](https://github.com/flypix-ai/flypix-sdk/blob/master/docs/sdks/rasters/README.md#get_raster) - Get raster details

### [Regions](https://github.com/flypix-ai/flypix-sdk/blob/master/docs/sdks/regions/README.md)

* [delete_regions](https://github.com/flypix-ai/flypix-sdk/blob/master/docs/sdks/regions/README.md#delete_regions) - Delete regions
* [get_regions_for_raster](https://github.com/flypix-ai/flypix-sdk/blob/master/docs/sdks/regions/README.md#get_regions_for_raster) - List raster regions
* [get_regions_by_ids](https://github.com/flypix-ai/flypix-sdk/blob/master/docs/sdks/regions/README.md#get_regions_by_ids) - Get regions by ids
* [create_regions_in_raster](https://github.com/flypix-ai/flypix-sdk/blob/master/docs/sdks/regions/README.md#create_regions_in_raster) - Create regions on a raster

### [System](https://github.com/flypix-ai/flypix-sdk/blob/master/docs/sdks/system/README.md)

* [health](https://github.com/flypix-ai/flypix-sdk/blob/master/docs/sdks/system/README.md#health) - Health check

### [Users](https://github.com/flypix-ai/flypix-sdk/blob/master/docs/sdks/users/README.md)

* [get_tenants_for_user](https://github.com/flypix-ai/flypix-sdk/blob/master/docs/sdks/users/README.md#get_tenants_for_user) - List tenants for user

### [Vectors](https://github.com/flypix-ai/flypix-sdk/blob/master/docs/sdks/vectors/README.md)

* [create_empty_vector](https://github.com/flypix-ai/flypix-sdk/blob/master/docs/sdks/vectors/README.md#create_empty_vector) - Create empty vector layer
* [get_classes_for_project](https://github.com/flypix-ai/flypix-sdk/blob/master/docs/sdks/vectors/README.md#get_classes_for_project) - List project classes
* [get_vectors_for_raster](https://github.com/flypix-ai/flypix-sdk/blob/master/docs/sdks/vectors/README.md#get_vectors_for_raster) - List raster vector layers
* [get_vectors_by_ids](https://github.com/flypix-ai/flypix-sdk/blob/master/docs/sdks/vectors/README.md#get_vectors_by_ids) - Get vector layers by ids
* [create_class_in_project](https://github.com/flypix-ai/flypix-sdk/blob/master/docs/sdks/vectors/README.md#create_class_in_project) - Create project class
* [delete_vector](https://github.com/flypix-ai/flypix-sdk/blob/master/docs/sdks/vectors/README.md#delete_vector) - Delete vector
* [create_annotations_in_vector](https://github.com/flypix-ai/flypix-sdk/blob/master/docs/sdks/vectors/README.md#create_annotations_in_vector) - Create annotations in a vector
* [get_vector_features](https://github.com/flypix-ai/flypix-sdk/blob/master/docs/sdks/vectors/README.md#get_vector_features) - List vector annotations
* [upload_geojson](https://github.com/flypix-ai/flypix-sdk/blob/master/docs/sdks/vectors/README.md#upload_geojson) - Upload GeoJSON annotations
* [upload_geopkg](https://github.com/flypix-ai/flypix-sdk/blob/master/docs/sdks/vectors/README.md#upload_geopkg) - Upload GeoPackage annotations
* [upload_shapefile](https://github.com/flypix-ai/flypix-sdk/blob/master/docs/sdks/vectors/README.md#upload_shapefile) - Upload Shapefile annotations

</details>
<!-- End Available Resources and Operations [operations] -->

<!-- Start File uploads [file-upload] -->
## File uploads

Certain SDK methods accept file objects as part of a request body or multi-part request. It is possible and typically recommended to upload files as a stream rather than reading the entire contents into memory. This avoids excessive memory consumption and potentially crashing with out-of-memory errors when working with very large files. The following example demonstrates how to attach a file stream to a request.

> [!TIP]
>
> For endpoints that handle file uploads bytes arrays can also be used. However, using streams is recommended for large files.
>

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
<!-- End File uploads [file-upload] -->

<!-- Start Retries [retries] -->
## Retries

Some of the endpoints in this SDK support retries. If you use the SDK without any configuration, it will fall back to the default retry strategy provided by the API. However, the default retry strategy can be overridden on a per-operation basis, or across the entire SDK.

To change the default retry strategy for a single API call, simply provide a `RetryConfig` object to the call:
```python
from flypix import Flypix
from flypix.utils import BackoffStrategy, RetryConfig


with Flypix() as f_client:

    res = f_client.system.health(,
        RetryConfig("backoff", BackoffStrategy(1, 50, 1.1, 100), False))

    # Handle response
    print(res)

```

If you'd like to override the default retry strategy for all operations that support retries, you can use the `retry_config` optional parameter when initializing the SDK:
```python
from flypix import Flypix
from flypix.utils import BackoffStrategy, RetryConfig


with Flypix(
    retry_config=RetryConfig("backoff", BackoffStrategy(1, 50, 1.1, 100), False),
) as f_client:

    res = f_client.system.health()

    # Handle response
    print(res)

```
<!-- End Retries [retries] -->

<!-- Start Error Handling [errors] -->
## Error Handling

[`FlyPixError`](https://github.com/flypix-ai/flypix-sdk/blob/master/./src/flypix/errors/flypixerror.py) is the base class for all HTTP error responses. It has the following properties:

| Property           | Type             | Description                                            |
| ------------------ | ---------------- | ------------------------------------------------------ |
| `err.message`      | `str`            | Error message                                          |
| `err.status_code`  | `int`            | HTTP response status code eg `404`                     |
| `err.headers`      | `httpx.Headers`  | HTTP response headers                                  |
| `err.body`         | `str`            | HTTP body. Can be empty string if no body is returned. |
| `err.raw_response` | `httpx.Response` | Raw HTTP response                                      |

### Example
```python
from flypix import Flypix, errors


with Flypix() as f_client:
    res = None
    try:

        res = f_client.system.health()

        # Handle response
        print(res)


    except errors.FlyPixError as e:
        # The base class for HTTP error responses
        print(e.message)
        print(e.status_code)
        print(e.body)
        print(e.headers)
        print(e.raw_response)

```

### Error Classes
**Primary error:**
* [`FlyPixError`](https://github.com/flypix-ai/flypix-sdk/blob/master/./src/flypix/errors/flypixerror.py): The base class for HTTP error responses.

<details><summary>Less common errors (5)</summary>

<br />

**Network errors:**
* [`httpx.RequestError`](https://www.python-httpx.org/exceptions/#httpx.RequestError): Base class for request errors.
    * [`httpx.ConnectError`](https://www.python-httpx.org/exceptions/#httpx.ConnectError): HTTP client was unable to make a request to a server.
    * [`httpx.TimeoutException`](https://www.python-httpx.org/exceptions/#httpx.TimeoutException): HTTP request timed out.


**Inherit from [`FlyPixError`](https://github.com/flypix-ai/flypix-sdk/blob/master/./src/flypix/errors/flypixerror.py)**:
* [`ResponseValidationError`](https://github.com/flypix-ai/flypix-sdk/blob/master/./src/flypix/errors/responsevalidationerror.py): Type mismatch between the response data and the expected Pydantic model. Provides access to the Pydantic validation error via the `cause` attribute.

</details>
<!-- End Error Handling [errors] -->

<!-- Start Server Selection [server] -->
## Server Selection

### Override Server URL Per-Client

The default server can be overridden globally by passing a URL to the `server_url: str` optional parameter when initializing the SDK client instance. For example:
```python
from flypix import Flypix


with Flypix(
    server_url="https://api.flypix.ai",
) as f_client:

    res = f_client.system.health()

    # Handle response
    print(res)

```
<!-- End Server Selection [server] -->

<!-- Start Custom HTTP Client [http-client] -->
## Custom HTTP Client

The Python SDK makes API calls using the [httpx](https://www.python-httpx.org/) HTTP library.  In order to provide a convenient way to configure timeouts, cookies, proxies, custom headers, and other low-level configuration, you can initialize the SDK client with your own HTTP client instance.
Depending on whether you are using the sync or async version of the SDK, you can pass an instance of `HttpClient` or `AsyncHttpClient` respectively, which are Protocol's ensuring that the client has the necessary methods to make API calls.
This allows you to wrap the client with your own custom logic, such as adding custom headers, logging, or error handling, or you can just pass an instance of `httpx.Client` or `httpx.AsyncClient` directly.

For example, you could specify a header for every request that this sdk makes as follows:
```python
from flypix import Flypix
import httpx

http_client = httpx.Client(headers={"x-custom-header": "someValue"})
s = Flypix(client=http_client)
```

or you could wrap the client with your own custom logic:
```python
from flypix import Flypix
from flypix.httpclient import AsyncHttpClient
import httpx

class CustomClient(AsyncHttpClient):
    client: AsyncHttpClient

    def __init__(self, client: AsyncHttpClient):
        self.client = client

    async def send(
        self,
        request: httpx.Request,
        *,
        stream: bool = False,
        auth: Union[
            httpx._types.AuthTypes, httpx._client.UseClientDefault, None
        ] = httpx.USE_CLIENT_DEFAULT,
        follow_redirects: Union[
            bool, httpx._client.UseClientDefault
        ] = httpx.USE_CLIENT_DEFAULT,
    ) -> httpx.Response:
        request.headers["Client-Level-Header"] = "added by client"

        return await self.client.send(
            request, stream=stream, auth=auth, follow_redirects=follow_redirects
        )

    def build_request(
        self,
        method: str,
        url: httpx._types.URLTypes,
        *,
        content: Optional[httpx._types.RequestContent] = None,
        data: Optional[httpx._types.RequestData] = None,
        files: Optional[httpx._types.RequestFiles] = None,
        json: Optional[Any] = None,
        params: Optional[httpx._types.QueryParamTypes] = None,
        headers: Optional[httpx._types.HeaderTypes] = None,
        cookies: Optional[httpx._types.CookieTypes] = None,
        timeout: Union[
            httpx._types.TimeoutTypes, httpx._client.UseClientDefault
        ] = httpx.USE_CLIENT_DEFAULT,
        extensions: Optional[httpx._types.RequestExtensions] = None,
    ) -> httpx.Request:
        return self.client.build_request(
            method,
            url,
            content=content,
            data=data,
            files=files,
            json=json,
            params=params,
            headers=headers,
            cookies=cookies,
            timeout=timeout,
            extensions=extensions,
        )

s = Flypix(async_client=CustomClient(httpx.AsyncClient()))
```
### httpx2 (Pydantic's httpx fork)

[httpx2](https://httpx2.pydantic.dev/) is Pydantic's maintained fork of `httpx`. To run this SDK on httpx2, call `alias_httpx()` at your program's entry point, before importing the SDK, so every `import httpx` — including the ones inside the SDK — resolves to `httpx2`:
```python
import httpx2

httpx2.alias_httpx()

from flypix import Flypix

s = Flypix()
```

An SDK can also be generated against httpx2 directly, so it depends on the fork instead of `httpx`, by setting `python.httpClientLibrary: httpx2` in `gen.yaml`.
<!-- End Custom HTTP Client [http-client] -->

<!-- Start Resource Management [resource-management] -->
## Resource Management

The `Flypix` class implements the context manager protocol and registers a finalizer function to close the underlying sync and async HTTPX clients it uses under the hood. This will close HTTP connections, release memory and free up other resources held by the SDK. In short-lived Python programs and notebooks that make a few SDK method calls, resource management may not be a concern. However, in longer-lived programs, it is beneficial to create a single SDK instance via a [context manager][context-manager] and reuse it across the application.

[context-manager]: https://docs.python.org/3/reference/datamodel.html#context-managers

```python
from flypix import Flypix
def main():

    with Flypix() as f_client:
        # Rest of application here...


# Or when using async:
async def amain():

    async with Flypix() as f_client:
        # Rest of application here...
```
<!-- End Resource Management [resource-management] -->

<!-- Start Debugging [debug] -->
## Debugging

You can setup your SDK to emit debug logs for SDK requests and responses.

You can pass your own logger class directly into your SDK.
```python
from flypix import Flypix
import logging

logging.basicConfig(level=logging.DEBUG)
s = Flypix(debug_logger=logging.getLogger("flypix"))
```
<!-- End Debugging [debug] -->

<!-- Placeholder for Future Speakeasy SDK Sections -->
