# flypix

The official Python SDK for the [FlyPix](https://flypix.ai) API — programmatic
access to projects, files, models, inferences, vectors, and more.

> **Status:** pre-release. The SDK is generated from the FlyPix OpenAPI spec with
> [Speakeasy](https://www.speakeasy.com). See [`SETUP.md`](./SETUP.md) for how it
> is generated and maintained. Installation and usage are documented in the
> generated sections below.

## Contributing

This SDK is generated — the code under `src/flypix/` is **not** hand-edited.
Improvements to naming and ergonomics happen in `openapi/overlay.yaml`; see
[`SETUP.md`](./SETUP.md).

## License

See [LICENSE](./LICENSE).

<!-- Start Summary [summary] -->
## Summary

Public API: 
Public OpenAPI Schema

This API lets you interact directly with the application with HTTP requests.

You will need to set a valid authorization header for every request:

`Authorization: Bearer <token>`

Example use case: Find an existing file and its vector features:

```
POST /auth/login/password -> Fetch token and use it in subsequent requests
GET /users/tenant/for-user/ -> Get your tenant id for subsequent requests
GET /projects/for-tenant/{tenant_id} -> Find your project
GET /files/for-project/{project_id} -> Find your file
GET /files/{file_id}/visible -> Get a download link for the visible raster
GET /vectors/for-file/{file_id} -> Get the vector ids for the file
GET /vectors/{vector_id}/features -> Get the annotations
```
<!-- End Summary [summary] -->

<!-- Start Table of Contents [toc] -->
## Table of Contents
<!-- $toc-max-depth=2 -->
* [flypix](#flypix)
  * [Contributing](#contributing)
  * [License](#license)
  * [SDK Installation](#sdk-installation)
  * [IDE Support](#ide-support)
  * [SDK Example Usage](#sdk-example-usage)
  * [Authentication](#authentication)
  * [Available Resources and Operations](#available-resources-and-operations)
  * [File uploads](#file-uploads)
  * [Retries](#retries)
  * [Error Handling](#error-handling)
  * [Server Selection](#server-selection)
  * [Custom HTTP Client](#custom-http-client)
  * [Resource Management](#resource-management)
  * [Debugging](#debugging)

<!-- End Table of Contents [toc] -->

<!-- Start SDK Installation [installation] -->
## SDK Installation

> [!TIP]
> To finish publishing your SDK to PyPI you must [run your first generation action](https://www.speakeasy.com/docs/github-setup#step-by-step-guide).


> [!NOTE]
> **Python version upgrade policy**
>
> Once a Python version reaches its [official end of life date](https://devguide.python.org/versions/), a 3-month grace period is provided for users to upgrade. Following this grace period, the minimum python version supported in the SDK will be updated.

The SDK can be installed with *uv*, *pip*, or *poetry* package managers.

### uv

*uv* is a fast Python package installer and resolver, designed as a drop-in replacement for pip and pip-tools. It's recommended for its speed and modern Python tooling capabilities.

```bash
uv add git+https://github.com/flypix-ai/flypix-sdk.git
```

### PIP

*PIP* is the default package installer for Python, enabling easy installation and management of packages from PyPI via the command line.

```bash
pip install git+https://github.com/flypix-ai/flypix-sdk.git
```

### Poetry

*Poetry* is a modern tool that simplifies dependency management and package publishing by using a single `pyproject.toml` file to handle project metadata and dependencies.

```bash
poetry add git+https://github.com/flypix-ai/flypix-sdk.git
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

from flypix import FlyPix

sdk = FlyPix(
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
from flypix import FlyPix


with FlyPix() as fly_pix:

    res = fly_pix.auth.login_with_password(username="Allie.Hartmann", password="9ne8TpFJLsebftr")

    # Handle response
    print(res)
```

</br>

The same SDK client can also be used to make asynchronous requests by importing asyncio.

```python
# Asynchronous Example
import asyncio
from flypix import FlyPix

async def main():

    async with FlyPix() as fly_pix:

        res = await fly_pix.auth.login_with_password_async(username="Allie.Hartmann", password="9ne8TpFJLsebftr")

        # Handle response
        print(res)

asyncio.run(main())
```
<!-- End SDK Example Usage [usage] -->

<!-- Start Authentication [security] -->
## Authentication

### Per-Client Security Schemes

This SDK supports the following security scheme globally:

| Name          | Type | Scheme      |
| ------------- | ---- | ----------- |
| `bearer_auth` | http | HTTP Bearer |

To authenticate with the API the `bearer_auth` parameter must be set when initializing the SDK client instance. For example:
```python
from flypix import FlyPix


with FlyPix(
    bearer_auth="<YOUR_BEARER_TOKEN_HERE>",
) as fly_pix:

    res = fly_pix.auth.login_with_password(username="Allie.Hartmann", password="9ne8TpFJLsebftr")

    # Handle response
    print(res)

```
<!-- End Authentication [security] -->

<!-- Start Available Resources and Operations [operations] -->
## Available Resources and Operations

<details open>
<summary>Available methods</summary>

### [Auth](docs/sdks/auth/README.md)

* [login_with_password](docs/sdks/auth/README.md#login_with_password) - Login With Password
* [refresh_token](docs/sdks/auth/README.md#refresh_token) - Refresh Token

### [Files](docs/sdks/files/README.md)

* [list_for_project](docs/sdks/files/README.md#list_for_project) - Get Files For Project Root
* [list_for_folder](docs/sdks/files/README.md#list_for_folder) - Get For Folder
* [get](docs/sdks/files/README.md#get) - Get File
* [delete](docs/sdks/files/README.md#delete) - Delete File
* [get_visible_raster](docs/sdks/files/README.md#get_visible_raster) - Get Visible Raster Of File
* [get_download_link](docs/sdks/files/README.md#get_download_link) - Get File Download Link
* [get_by_ids](docs/sdks/files/README.md#get_by_ids) - Get Files By Ids
* [get_storage_usage](docs/sdks/files/README.md#get_storage_usage) - Get Storage Usage
* [~~upload~~](docs/sdks/files/README.md#upload) - Upload File :warning: **Deprecated**
* [upload_v2](docs/sdks/files/README.md#upload_v2) - Upload File
* [upload_from_url](docs/sdks/files/README.md#upload_from_url) - Upload File From Url

### [Folders](docs/sdks/folders/README.md)

* [list_for_folder](docs/sdks/folders/README.md#list_for_folder) - Get Folders For Folder
* [list_for_project](docs/sdks/folders/README.md#list_for_project) - Get Folders In Project Root
* [delete](docs/sdks/folders/README.md#delete) - Delete Folder
* [create](docs/sdks/folders/README.md#create) - Create Folder

### [Geosense](docs/sdks/geosense/README.md)

* [create_session](docs/sdks/geosense/README.md#create_session) - Create Session In Project
* [create_artifact](docs/sdks/geosense/README.md#create_artifact) - Create Session Artifact
* [get_artifact](docs/sdks/geosense/README.md#get_artifact) - Get Session Artifact
* [send_message](docs/sdks/geosense/README.md#send_message) - Send Message

### [Inferences](docs/sdks/inferences/README.md)

* [list_for_tenant](docs/sdks/inferences/README.md#list_for_tenant) - Get Inferences For Tenant
* [list_for_project](docs/sdks/inferences/README.md#list_for_project) - Get Inferences For Project
* [list_for_file](docs/sdks/inferences/README.md#list_for_file) - Get Inferences For File

### [Models](docs/sdks/models/README.md)

* [list_for_tenant](docs/sdks/models/README.md#list_for_tenant) - Get Models For Tenant
* [list_for_project](docs/sdks/models/README.md#list_for_project) - Get Models For Project
* [list_official](docs/sdks/models/README.md#list_official) - Get Official Models
* [apply](docs/sdks/models/README.md#apply) - Apply Model On File
* [estimate_application](docs/sdks/models/README.md#estimate_application) - Estimate Model Application On File
* [get_inference_status](docs/sdks/models/README.md#get_inference_status) - Get Inference Status
* [delete](docs/sdks/models/README.md#delete) - Delete Model

### [Payments](docs/sdks/payments/README.md)

* [get_balance](docs/sdks/payments/README.md#get_balance) - Get Tenant Balance

### [Projects](docs/sdks/projects/README.md)

* [list_for_tenant](docs/sdks/projects/README.md#list_for_tenant) - Get Projects For Tenant
* [delete](docs/sdks/projects/README.md#delete) - Delete Project
* [create](docs/sdks/projects/README.md#create) - Create Project

### [Rasters](docs/sdks/rasters/README.md)

* [list_for_tenant](docs/sdks/rasters/README.md#list_for_tenant) - Get Rasters For Tenant
* [list_for_project](docs/sdks/rasters/README.md#list_for_project) - Get Rasters For Project
* [list_for_file](docs/sdks/rasters/README.md#list_for_file) - Get Rasters For File

### [Regions](docs/sdks/regions/README.md)

* [list_for_file](docs/sdks/regions/README.md#list_for_file) - Get Regions For File
* [create](docs/sdks/regions/README.md#create) - Create Regions In File
* [delete](docs/sdks/regions/README.md#delete) - Delete Regions

### [Users](docs/sdks/users/README.md)

* [list_tenants](docs/sdks/users/README.md#list_tenants) - Get Tenants For User

### [Vectors](docs/sdks/vectors/README.md)

* [list_for_file](docs/sdks/vectors/README.md#list_for_file) - Get Vectors For File
* [list_classes_for_project](docs/sdks/vectors/README.md#list_classes_for_project) - Get Project Classes
* [create_class](docs/sdks/vectors/README.md#create_class) - Create Class In Project
* [get_features](docs/sdks/vectors/README.md#get_features) - Get Vector Features
* [create](docs/sdks/vectors/README.md#create) - Create Empty Vector
* [delete](docs/sdks/vectors/README.md#delete) - Delete Vector
* [create_annotations](docs/sdks/vectors/README.md#create_annotations) - Create Annotations In Vector
* [upload_geojson](docs/sdks/vectors/README.md#upload_geojson) - Upload Geojson
* [upload_gpkg](docs/sdks/vectors/README.md#upload_gpkg) - Upload Gpkg
* [upload_shapefile](docs/sdks/vectors/README.md#upload_shapefile) - Upload Shp

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
from flypix import FlyPix


with FlyPix(
    bearer_auth="<YOUR_BEARER_TOKEN_HERE>",
) as fly_pix:

    res = fly_pix.files.upload_v2(tenant_id="170b602d-192c-4e40-a031-f5892fa57f45", project_id="55299aef-34b1-4aaa-a1aa-cbeca6dd058b", filename="example.file", body=open("example.file", "rb"))

    # Handle response
    print(res)

```
<!-- End File uploads [file-upload] -->

<!-- Start Retries [retries] -->
## Retries

Some of the endpoints in this SDK support retries. If you use the SDK without any configuration, it will fall back to the default retry strategy provided by the API. However, the default retry strategy can be overridden on a per-operation basis, or across the entire SDK.

To change the default retry strategy for a single API call, simply provide a `RetryConfig` object to the call:
```python
from flypix import FlyPix
from flypix.utils import BackoffStrategy, RetryConfig


with FlyPix() as fly_pix:

    res = fly_pix.auth.login_with_password(username="Allie.Hartmann", password="9ne8TpFJLsebftr",
        RetryConfig("backoff", BackoffStrategy(1, 50, 1.1, 100), False))

    # Handle response
    print(res)

```

If you'd like to override the default retry strategy for all operations that support retries, you can use the `retry_config` optional parameter when initializing the SDK:
```python
from flypix import FlyPix
from flypix.utils import BackoffStrategy, RetryConfig


with FlyPix(
    retry_config=RetryConfig("backoff", BackoffStrategy(1, 50, 1.1, 100), False),
) as fly_pix:

    res = fly_pix.auth.login_with_password(username="Allie.Hartmann", password="9ne8TpFJLsebftr")

    # Handle response
    print(res)

```
<!-- End Retries [retries] -->

<!-- Start Error Handling [errors] -->
## Error Handling

[`FlyPixError`](./src/flypix/errors/flypixerror.py) is the base class for all HTTP error responses. It has the following properties:

| Property           | Type             | Description                                            |
| ------------------ | ---------------- | ------------------------------------------------------ |
| `err.message`      | `str`            | Error message                                          |
| `err.status_code`  | `int`            | HTTP response status code eg `404`                     |
| `err.headers`      | `httpx.Headers`  | HTTP response headers                                  |
| `err.body`         | `str`            | HTTP body. Can be empty string if no body is returned. |
| `err.raw_response` | `httpx.Response` | Raw HTTP response                                      |

### Example
```python
from flypix import FlyPix, errors


with FlyPix() as fly_pix:
    res = None
    try:

        res = fly_pix.auth.login_with_password(username="Allie.Hartmann", password="9ne8TpFJLsebftr")

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
* [`FlyPixError`](./src/flypix/errors/flypixerror.py): The base class for HTTP error responses.

<details><summary>Less common errors (5)</summary>

<br />

**Network errors:**
* [`httpx.RequestError`](https://www.python-httpx.org/exceptions/#httpx.RequestError): Base class for request errors.
    * [`httpx.ConnectError`](https://www.python-httpx.org/exceptions/#httpx.ConnectError): HTTP client was unable to make a request to a server.
    * [`httpx.TimeoutException`](https://www.python-httpx.org/exceptions/#httpx.TimeoutException): HTTP request timed out.


**Inherit from [`FlyPixError`](./src/flypix/errors/flypixerror.py)**:
* [`ResponseValidationError`](./src/flypix/errors/responsevalidationerror.py): Type mismatch between the response data and the expected Pydantic model. Provides access to the Pydantic validation error via the `cause` attribute.

</details>
<!-- End Error Handling [errors] -->

<!-- Start Server Selection [server] -->
## Server Selection

### Override Server URL Per-Client

The default server can be overridden globally by passing a URL to the `server_url: str` optional parameter when initializing the SDK client instance. For example:
```python
from flypix import FlyPix


with FlyPix(
    server_url="https://api.flypix.ai",
) as fly_pix:

    res = fly_pix.auth.login_with_password(username="Allie.Hartmann", password="9ne8TpFJLsebftr")

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
from flypix import FlyPix
import httpx

http_client = httpx.Client(headers={"x-custom-header": "someValue"})
s = FlyPix(client=http_client)
```

or you could wrap the client with your own custom logic:
```python
from flypix import FlyPix
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

s = FlyPix(async_client=CustomClient(httpx.AsyncClient()))
```
<!-- End Custom HTTP Client [http-client] -->

<!-- Start Resource Management [resource-management] -->
## Resource Management

The `FlyPix` class implements the context manager protocol and registers a finalizer function to close the underlying sync and async HTTPX clients it uses under the hood. This will close HTTP connections, release memory and free up other resources held by the SDK. In short-lived Python programs and notebooks that make a few SDK method calls, resource management may not be a concern. However, in longer-lived programs, it is beneficial to create a single SDK instance via a [context manager][context-manager] and reuse it across the application.

[context-manager]: https://docs.python.org/3/reference/datamodel.html#context-managers

```python
from flypix import FlyPix
def main():

    with FlyPix() as fly_pix:
        # Rest of application here...


# Or when using async:
async def amain():

    async with FlyPix() as fly_pix:
        # Rest of application here...
```
<!-- End Resource Management [resource-management] -->

<!-- Start Debugging [debug] -->
## Debugging

You can setup your SDK to emit debug logs for SDK requests and responses.

You can pass your own logger class directly into your SDK.
```python
from flypix import FlyPix
import logging

logging.basicConfig(level=logging.DEBUG)
s = FlyPix(debug_logger=logging.getLogger("flypix"))
```
<!-- End Debugging [debug] -->

<!-- Placeholder for Future Speakeasy SDK Sections -->
