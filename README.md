<p style="text-align: center">
  <a href="https://flypix.ai">
    <img src="https://flypix.ai/wp-content/uploads/2026/06/flypixLogoNew.webp" alt="FlyPix" width="240">
  </a>
</p>

# flypix

The official Python SDK for the [FlyPix](https://flypix.ai) API — programmatic
access to projects, files, models, inferences, vectors, and more.

> **Status:** released. The SDK is generated from the FlyPix OpenAPI spec with
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

### List tenants for the current user

```python
# Synchronous Example
from flypix import Flypix, models


with Flypix(
    security=models.Security(
        api_key="<YOUR_API_KEY_HERE>",
    ),
) as f_client:

    res = f_client.users.list_tenants()

    # Handle response
    print(res)
```

</br>

The same SDK client can also be used to make asynchronous requests by importing asyncio.

```python
# Asynchronous Example
import asyncio
from flypix import Flypix, models

async def main():

    async with Flypix(
        security=models.Security(
            api_key="<YOUR_API_KEY_HERE>",
        ),
    ) as f_client:

        res = await f_client.users.list_tenants_async()

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

    res = f_client.auth.login_with_password(username="Allie.Hartmann", password="9ne8TpFJLsebftr")

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
* [get_tenant_transactions_payments_balance_tenant_id_transactions_get](docs/sdks/payments/README.md#get_tenant_transactions_payments_balance_tenant_id_transactions_get) - Get Tenant Transactions

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
from flypix import Flypix, models


with Flypix(
    security=models.Security(
        api_key="<YOUR_API_KEY_HERE>",
    ),
) as f_client:

    res = f_client.vectors.upload_geojson(vector_id="123e4567-e89b-12d3-a456-426614174000", file={
        "file_name": "example.file",
        "content": open("example.file", "rb"),
    })

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

    res = f_client.auth.login_with_password(username="Allie.Hartmann", password="9ne8TpFJLsebftr",
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

    res = f_client.auth.login_with_password(username="Allie.Hartmann", password="9ne8TpFJLsebftr")

    # Handle response
    print(res)

```
<!-- End Retries [retries] -->

<!-- Start Error Handling [errors] -->
## Error Handling

[`FlyPixError`](./src/flypix/errors/flypixerror.py) is the base class for all HTTP error responses. It has the following properties:

| Property           | Type             | Description                                                                             |
| ------------------ | ---------------- | --------------------------------------------------------------------------------------- |
| `err.message`      | `str`            | Error message                                                                           |
| `err.status_code`  | `int`            | HTTP response status code eg `404`                                                      |
| `err.headers`      | `httpx.Headers`  | HTTP response headers                                                                   |
| `err.body`         | `str`            | HTTP body. Can be empty string if no body is returned.                                  |
| `err.raw_response` | `httpx.Response` | Raw HTTP response                                                                       |
| `err.data`         |                  | Optional. Some errors may contain structured data. [See Error Classes](#error-classes). |

### Example
```python
from flypix import Flypix, errors


with Flypix() as f_client:
    res = None
    try:

        res = f_client.auth.login_with_password(username="Allie.Hartmann", password="9ne8TpFJLsebftr")

        # Handle response
        print(res)


    except errors.FlyPixError as e:
        # The base class for HTTP error responses
        print(e.message)
        print(e.status_code)
        print(e.body)
        print(e.headers)
        print(e.raw_response)

        # Depending on the method different errors may be thrown
        if isinstance(e, errors.AuthLoginWithPasswordBadRequestErrorResponseSchema):
            print(e.data.error)  # str
            print(e.data.message)  # str
```

### Error Classes
**Primary error:**
* [`FlyPixError`](./src/flypix/errors/flypixerror.py): The base class for HTTP error responses.

<details><summary>Less common errors (209)</summary>

<br />

**Network errors:**
* [`httpx.RequestError`](https://www.python-httpx.org/exceptions/#httpx.RequestError): Base class for request errors.
    * [`httpx.ConnectError`](https://www.python-httpx.org/exceptions/#httpx.ConnectError): HTTP client was unable to make a request to a server.
    * [`httpx.TimeoutException`](https://www.python-httpx.org/exceptions/#httpx.TimeoutException): HTTP request timed out.


**Inherit from [`FlyPixError`](./src/flypix/errors/flypixerror.py)**:
* [`AuthLoginWithPasswordBadRequestErrorResponseSchema`](./src/flypix/errors/authloginwithpasswordbadrequesterrorresponseschema.py): Forbidden. Status code `400`. Applicable to 1 of 51 methods.*
* [`AuthRefreshTokenBadRequestErrorResponseSchema`](./src/flypix/errors/authrefreshtokenbadrequesterrorresponseschema.py): Forbidden. Status code `400`. Applicable to 1 of 51 methods.*
* [`PaymentsGetBalanceBadRequestErrorResponseSchema`](./src/flypix/errors/paymentsgetbalancebadrequesterrorresponseschema.py): Forbidden. Status code `400`. Applicable to 1 of 51 methods.*
* [`GetTenantTransactionsPaymentsBalanceTenantIDTransactionsGetBadRequestErrorResponseSchema`](./src/flypix/errors/gettenanttransactionspaymentsbalancetenantidtransactionsgetbadrequesterrorresponseschema.py): Forbidden. Status code `400`. Applicable to 1 of 51 methods.*
* [`UsersListTenantsBadRequestErrorResponseSchema`](./src/flypix/errors/userslisttenantsbadrequesterrorresponseschema.py): Forbidden. Status code `400`. Applicable to 1 of 51 methods.*
* [`ProjectsListForTenantBadRequestErrorResponseSchema`](./src/flypix/errors/projectslistfortenantbadrequesterrorresponseschema.py): Forbidden. Status code `400`. Applicable to 1 of 51 methods.*
* [`ProjectsDeleteBadRequestErrorResponseSchema`](./src/flypix/errors/projectsdeletebadrequesterrorresponseschema.py): Forbidden. Status code `400`. Applicable to 1 of 51 methods.*
* [`ProjectsCreateBadRequestErrorResponseSchema`](./src/flypix/errors/projectscreatebadrequesterrorresponseschema.py): Forbidden. Status code `400`. Applicable to 1 of 51 methods.*
* [`FoldersListForFolderBadRequestErrorResponseSchema`](./src/flypix/errors/folderslistforfolderbadrequesterrorresponseschema.py): Forbidden. Status code `400`. Applicable to 1 of 51 methods.*
* [`FoldersListForProjectBadRequestErrorResponseSchema`](./src/flypix/errors/folderslistforprojectbadrequesterrorresponseschema.py): Forbidden. Status code `400`. Applicable to 1 of 51 methods.*
* [`FoldersDeleteBadRequestErrorResponseSchema`](./src/flypix/errors/foldersdeletebadrequesterrorresponseschema.py): Forbidden. Status code `400`. Applicable to 1 of 51 methods.*
* [`FoldersCreateBadRequestErrorResponseSchema`](./src/flypix/errors/folderscreatebadrequesterrorresponseschema.py): Forbidden. Status code `400`. Applicable to 1 of 51 methods.*
* [`FilesListForProjectBadRequestErrorResponseSchema`](./src/flypix/errors/fileslistforprojectbadrequesterrorresponseschema.py): Forbidden. Status code `400`. Applicable to 1 of 51 methods.*
* [`FilesListForFolderBadRequestErrorResponseSchema`](./src/flypix/errors/fileslistforfolderbadrequesterrorresponseschema.py): Forbidden. Status code `400`. Applicable to 1 of 51 methods.*
* [`FilesGetBadRequestErrorResponseSchema`](./src/flypix/errors/filesgetbadrequesterrorresponseschema.py): Forbidden. Status code `400`. Applicable to 1 of 51 methods.*
* [`FilesDeleteBadRequestErrorResponseSchema`](./src/flypix/errors/filesdeletebadrequesterrorresponseschema.py): Forbidden. Status code `400`. Applicable to 1 of 51 methods.*
* [`FilesGetVisibleRasterBadRequestErrorResponseSchema`](./src/flypix/errors/filesgetvisiblerasterbadrequesterrorresponseschema.py): Forbidden. Status code `400`. Applicable to 1 of 51 methods.*
* [`FilesGetDownloadLinkBadRequestErrorResponseSchema`](./src/flypix/errors/filesgetdownloadlinkbadrequesterrorresponseschema.py): Forbidden. Status code `400`. Applicable to 1 of 51 methods.*
* [`FilesGetByIdsBadRequestErrorResponseSchema`](./src/flypix/errors/filesgetbyidsbadrequesterrorresponseschema.py): Forbidden. Status code `400`. Applicable to 1 of 51 methods.*
* [`FilesGetStorageUsageBadRequestErrorResponseSchema`](./src/flypix/errors/filesgetstorageusagebadrequesterrorresponseschema.py): Forbidden. Status code `400`. Applicable to 1 of 51 methods.*
* [`FilesUploadBadRequestErrorResponseSchema`](./src/flypix/errors/filesuploadbadrequesterrorresponseschema.py): Forbidden. Status code `400`. Applicable to 1 of 51 methods.*
* [`RastersListForTenantBadRequestErrorResponseSchema`](./src/flypix/errors/rasterslistfortenantbadrequesterrorresponseschema.py): Forbidden. Status code `400`. Applicable to 1 of 51 methods.*
* [`RastersListForProjectBadRequestErrorResponseSchema`](./src/flypix/errors/rasterslistforprojectbadrequesterrorresponseschema.py): Forbidden. Status code `400`. Applicable to 1 of 51 methods.*
* [`RastersListForFileBadRequestErrorResponseSchema`](./src/flypix/errors/rasterslistforfilebadrequesterrorresponseschema.py): Forbidden. Status code `400`. Applicable to 1 of 51 methods.*
* [`InferencesListForTenantBadRequestErrorResponseSchema`](./src/flypix/errors/inferenceslistfortenantbadrequesterrorresponseschema.py): Forbidden. Status code `400`. Applicable to 1 of 51 methods.*
* [`InferencesListForProjectBadRequestErrorResponseSchema`](./src/flypix/errors/inferenceslistforprojectbadrequesterrorresponseschema.py): Forbidden. Status code `400`. Applicable to 1 of 51 methods.*
* [`InferencesListForFileBadRequestErrorResponseSchema`](./src/flypix/errors/inferenceslistforfilebadrequesterrorresponseschema.py): Forbidden. Status code `400`. Applicable to 1 of 51 methods.*
* [`ModelsListForTenantBadRequestErrorResponseSchema`](./src/flypix/errors/modelslistfortenantbadrequesterrorresponseschema.py): Forbidden. Status code `400`. Applicable to 1 of 51 methods.*
* [`ModelsListForProjectBadRequestErrorResponseSchema`](./src/flypix/errors/modelslistforprojectbadrequesterrorresponseschema.py): Forbidden. Status code `400`. Applicable to 1 of 51 methods.*
* [`ModelsListOfficialBadRequestErrorResponseSchema`](./src/flypix/errors/modelslistofficialbadrequesterrorresponseschema.py): Forbidden. Status code `400`. Applicable to 1 of 51 methods.*
* [`ModelsApplyBadRequestErrorResponseSchema`](./src/flypix/errors/modelsapplybadrequesterrorresponseschema.py): Forbidden. Status code `400`. Applicable to 1 of 51 methods.*
* [`ModelsEstimateApplicationBadRequestErrorResponseSchema`](./src/flypix/errors/modelsestimateapplicationbadrequesterrorresponseschema.py): Forbidden. Status code `400`. Applicable to 1 of 51 methods.*
* [`ModelsGetInferenceStatusBadRequestErrorResponseSchema`](./src/flypix/errors/modelsgetinferencestatusbadrequesterrorresponseschema.py): Forbidden. Status code `400`. Applicable to 1 of 51 methods.*
* [`ModelsDeleteBadRequestErrorResponseSchema`](./src/flypix/errors/modelsdeletebadrequesterrorresponseschema.py): Forbidden. Status code `400`. Applicable to 1 of 51 methods.*
* [`VectorsListForFileBadRequestErrorResponseSchema`](./src/flypix/errors/vectorslistforfilebadrequesterrorresponseschema.py): Forbidden. Status code `400`. Applicable to 1 of 51 methods.*
* [`VectorsListClassesForProjectBadRequestErrorResponseSchema`](./src/flypix/errors/vectorslistclassesforprojectbadrequesterrorresponseschema.py): Forbidden. Status code `400`. Applicable to 1 of 51 methods.*
* [`VectorsCreateClassBadRequestErrorResponseSchema`](./src/flypix/errors/vectorscreateclassbadrequesterrorresponseschema.py): Forbidden. Status code `400`. Applicable to 1 of 51 methods.*
* [`VectorsGetFeaturesBadRequestErrorResponseSchema`](./src/flypix/errors/vectorsgetfeaturesbadrequesterrorresponseschema.py): Forbidden. Status code `400`. Applicable to 1 of 51 methods.*
* [`VectorsCreateBadRequestErrorResponseSchema`](./src/flypix/errors/vectorscreatebadrequesterrorresponseschema.py): Forbidden. Status code `400`. Applicable to 1 of 51 methods.*
* [`VectorsDeleteBadRequestErrorResponseSchema`](./src/flypix/errors/vectorsdeletebadrequesterrorresponseschema.py): Forbidden. Status code `400`. Applicable to 1 of 51 methods.*
* [`VectorsCreateAnnotationsBadRequestErrorResponseSchema`](./src/flypix/errors/vectorscreateannotationsbadrequesterrorresponseschema.py): Forbidden. Status code `400`. Applicable to 1 of 51 methods.*
* [`VectorsUploadGeojsonBadRequestErrorResponseSchema`](./src/flypix/errors/vectorsuploadgeojsonbadrequesterrorresponseschema.py): Forbidden. Status code `400`. Applicable to 1 of 51 methods.*
* [`VectorsUploadGpkgBadRequestErrorResponseSchema`](./src/flypix/errors/vectorsuploadgpkgbadrequesterrorresponseschema.py): Forbidden. Status code `400`. Applicable to 1 of 51 methods.*
* [`VectorsUploadShapefileBadRequestErrorResponseSchema`](./src/flypix/errors/vectorsuploadshapefilebadrequesterrorresponseschema.py): Forbidden. Status code `400`. Applicable to 1 of 51 methods.*
* [`RegionsListForFileBadRequestErrorResponseSchema`](./src/flypix/errors/regionslistforfilebadrequesterrorresponseschema.py): Forbidden. Status code `400`. Applicable to 1 of 51 methods.*
* [`RegionsCreateBadRequestErrorResponseSchema`](./src/flypix/errors/regionscreatebadrequesterrorresponseschema.py): Forbidden. Status code `400`. Applicable to 1 of 51 methods.*
* [`RegionsDeleteBadRequestErrorResponseSchema`](./src/flypix/errors/regionsdeletebadrequesterrorresponseschema.py): Forbidden. Status code `400`. Applicable to 1 of 51 methods.*
* [`GeosenseCreateSessionBadRequestErrorResponseSchema`](./src/flypix/errors/geosensecreatesessionbadrequesterrorresponseschema.py): Forbidden. Status code `400`. Applicable to 1 of 51 methods.*
* [`GeosenseCreateArtifactBadRequestErrorResponseSchema`](./src/flypix/errors/geosensecreateartifactbadrequesterrorresponseschema.py): Forbidden. Status code `400`. Applicable to 1 of 51 methods.*
* [`GeosenseGetArtifactBadRequestErrorResponseSchema`](./src/flypix/errors/geosensegetartifactbadrequesterrorresponseschema.py): Forbidden. Status code `400`. Applicable to 1 of 51 methods.*
* [`GeosenseSendMessageBadRequestErrorResponseSchema`](./src/flypix/errors/geosensesendmessagebadrequesterrorresponseschema.py): Forbidden. Status code `400`. Applicable to 1 of 51 methods.*
* [`AuthLoginWithPasswordForbiddenErrorResponseSchema`](./src/flypix/errors/authloginwithpasswordforbiddenerrorresponseschema.py): Not Found. Status code `403`. Applicable to 1 of 51 methods.*
* [`AuthRefreshTokenForbiddenErrorResponseSchema`](./src/flypix/errors/authrefreshtokenforbiddenerrorresponseschema.py): Not Found. Status code `403`. Applicable to 1 of 51 methods.*
* [`PaymentsGetBalanceForbiddenErrorResponseSchema`](./src/flypix/errors/paymentsgetbalanceforbiddenerrorresponseschema.py): Not Found. Status code `403`. Applicable to 1 of 51 methods.*
* [`GetTenantTransactionsPaymentsBalanceTenantIDTransactionsGetForbiddenErrorResponseSchema`](./src/flypix/errors/gettenanttransactionspaymentsbalancetenantidtransactionsgetforbiddenerrorresponseschema.py): Not Found. Status code `403`. Applicable to 1 of 51 methods.*
* [`UsersListTenantsForbiddenErrorResponseSchema`](./src/flypix/errors/userslisttenantsforbiddenerrorresponseschema.py): Not Found. Status code `403`. Applicable to 1 of 51 methods.*
* [`ProjectsListForTenantForbiddenErrorResponseSchema`](./src/flypix/errors/projectslistfortenantforbiddenerrorresponseschema.py): Not Found. Status code `403`. Applicable to 1 of 51 methods.*
* [`ProjectsDeleteForbiddenErrorResponseSchema`](./src/flypix/errors/projectsdeleteforbiddenerrorresponseschema.py): Not Found. Status code `403`. Applicable to 1 of 51 methods.*
* [`ProjectsCreateForbiddenErrorResponseSchema`](./src/flypix/errors/projectscreateforbiddenerrorresponseschema.py): Not Found. Status code `403`. Applicable to 1 of 51 methods.*
* [`FoldersListForFolderForbiddenErrorResponseSchema`](./src/flypix/errors/folderslistforfolderforbiddenerrorresponseschema.py): Not Found. Status code `403`. Applicable to 1 of 51 methods.*
* [`FoldersListForProjectForbiddenErrorResponseSchema`](./src/flypix/errors/folderslistforprojectforbiddenerrorresponseschema.py): Not Found. Status code `403`. Applicable to 1 of 51 methods.*
* [`FoldersDeleteForbiddenErrorResponseSchema`](./src/flypix/errors/foldersdeleteforbiddenerrorresponseschema.py): Not Found. Status code `403`. Applicable to 1 of 51 methods.*
* [`FoldersCreateForbiddenErrorResponseSchema`](./src/flypix/errors/folderscreateforbiddenerrorresponseschema.py): Not Found. Status code `403`. Applicable to 1 of 51 methods.*
* [`FilesListForProjectForbiddenErrorResponseSchema`](./src/flypix/errors/fileslistforprojectforbiddenerrorresponseschema.py): Not Found. Status code `403`. Applicable to 1 of 51 methods.*
* [`FilesListForFolderForbiddenErrorResponseSchema`](./src/flypix/errors/fileslistforfolderforbiddenerrorresponseschema.py): Not Found. Status code `403`. Applicable to 1 of 51 methods.*
* [`FilesGetForbiddenErrorResponseSchema`](./src/flypix/errors/filesgetforbiddenerrorresponseschema.py): Not Found. Status code `403`. Applicable to 1 of 51 methods.*
* [`FilesDeleteForbiddenErrorResponseSchema`](./src/flypix/errors/filesdeleteforbiddenerrorresponseschema.py): Not Found. Status code `403`. Applicable to 1 of 51 methods.*
* [`FilesGetVisibleRasterForbiddenErrorResponseSchema`](./src/flypix/errors/filesgetvisiblerasterforbiddenerrorresponseschema.py): Not Found. Status code `403`. Applicable to 1 of 51 methods.*
* [`FilesGetDownloadLinkForbiddenErrorResponseSchema`](./src/flypix/errors/filesgetdownloadlinkforbiddenerrorresponseschema.py): Not Found. Status code `403`. Applicable to 1 of 51 methods.*
* [`FilesGetByIdsForbiddenErrorResponseSchema`](./src/flypix/errors/filesgetbyidsforbiddenerrorresponseschema.py): Not Found. Status code `403`. Applicable to 1 of 51 methods.*
* [`FilesGetStorageUsageForbiddenErrorResponseSchema`](./src/flypix/errors/filesgetstorageusageforbiddenerrorresponseschema.py): Not Found. Status code `403`. Applicable to 1 of 51 methods.*
* [`FilesUploadForbiddenErrorResponseSchema`](./src/flypix/errors/filesuploadforbiddenerrorresponseschema.py): Not Found. Status code `403`. Applicable to 1 of 51 methods.*
* [`RastersListForTenantForbiddenErrorResponseSchema`](./src/flypix/errors/rasterslistfortenantforbiddenerrorresponseschema.py): Not Found. Status code `403`. Applicable to 1 of 51 methods.*
* [`RastersListForProjectForbiddenErrorResponseSchema`](./src/flypix/errors/rasterslistforprojectforbiddenerrorresponseschema.py): Not Found. Status code `403`. Applicable to 1 of 51 methods.*
* [`RastersListForFileForbiddenErrorResponseSchema`](./src/flypix/errors/rasterslistforfileforbiddenerrorresponseschema.py): Not Found. Status code `403`. Applicable to 1 of 51 methods.*
* [`InferencesListForTenantForbiddenErrorResponseSchema`](./src/flypix/errors/inferenceslistfortenantforbiddenerrorresponseschema.py): Not Found. Status code `403`. Applicable to 1 of 51 methods.*
* [`InferencesListForProjectForbiddenErrorResponseSchema`](./src/flypix/errors/inferenceslistforprojectforbiddenerrorresponseschema.py): Not Found. Status code `403`. Applicable to 1 of 51 methods.*
* [`InferencesListForFileForbiddenErrorResponseSchema`](./src/flypix/errors/inferenceslistforfileforbiddenerrorresponseschema.py): Not Found. Status code `403`. Applicable to 1 of 51 methods.*
* [`ModelsListForTenantForbiddenErrorResponseSchema`](./src/flypix/errors/modelslistfortenantforbiddenerrorresponseschema.py): Not Found. Status code `403`. Applicable to 1 of 51 methods.*
* [`ModelsListForProjectForbiddenErrorResponseSchema`](./src/flypix/errors/modelslistforprojectforbiddenerrorresponseschema.py): Not Found. Status code `403`. Applicable to 1 of 51 methods.*
* [`ModelsListOfficialForbiddenErrorResponseSchema`](./src/flypix/errors/modelslistofficialforbiddenerrorresponseschema.py): Not Found. Status code `403`. Applicable to 1 of 51 methods.*
* [`ModelsApplyForbiddenErrorResponseSchema`](./src/flypix/errors/modelsapplyforbiddenerrorresponseschema.py): Not Found. Status code `403`. Applicable to 1 of 51 methods.*
* [`ModelsEstimateApplicationForbiddenErrorResponseSchema`](./src/flypix/errors/modelsestimateapplicationforbiddenerrorresponseschema.py): Not Found. Status code `403`. Applicable to 1 of 51 methods.*
* [`ModelsGetInferenceStatusForbiddenErrorResponseSchema`](./src/flypix/errors/modelsgetinferencestatusforbiddenerrorresponseschema.py): Not Found. Status code `403`. Applicable to 1 of 51 methods.*
* [`ModelsDeleteForbiddenErrorResponseSchema`](./src/flypix/errors/modelsdeleteforbiddenerrorresponseschema.py): Not Found. Status code `403`. Applicable to 1 of 51 methods.*
* [`VectorsListForFileForbiddenErrorResponseSchema`](./src/flypix/errors/vectorslistforfileforbiddenerrorresponseschema.py): Not Found. Status code `403`. Applicable to 1 of 51 methods.*
* [`VectorsListClassesForProjectForbiddenErrorResponseSchema`](./src/flypix/errors/vectorslistclassesforprojectforbiddenerrorresponseschema.py): Not Found. Status code `403`. Applicable to 1 of 51 methods.*
* [`VectorsCreateClassForbiddenErrorResponseSchema`](./src/flypix/errors/vectorscreateclassforbiddenerrorresponseschema.py): Not Found. Status code `403`. Applicable to 1 of 51 methods.*
* [`VectorsGetFeaturesForbiddenErrorResponseSchema`](./src/flypix/errors/vectorsgetfeaturesforbiddenerrorresponseschema.py): Not Found. Status code `403`. Applicable to 1 of 51 methods.*
* [`VectorsCreateForbiddenErrorResponseSchema`](./src/flypix/errors/vectorscreateforbiddenerrorresponseschema.py): Not Found. Status code `403`. Applicable to 1 of 51 methods.*
* [`VectorsDeleteForbiddenErrorResponseSchema`](./src/flypix/errors/vectorsdeleteforbiddenerrorresponseschema.py): Not Found. Status code `403`. Applicable to 1 of 51 methods.*
* [`VectorsCreateAnnotationsForbiddenErrorResponseSchema`](./src/flypix/errors/vectorscreateannotationsforbiddenerrorresponseschema.py): Not Found. Status code `403`. Applicable to 1 of 51 methods.*
* [`VectorsUploadGeojsonForbiddenErrorResponseSchema`](./src/flypix/errors/vectorsuploadgeojsonforbiddenerrorresponseschema.py): Not Found. Status code `403`. Applicable to 1 of 51 methods.*
* [`VectorsUploadGpkgForbiddenErrorResponseSchema`](./src/flypix/errors/vectorsuploadgpkgforbiddenerrorresponseschema.py): Not Found. Status code `403`. Applicable to 1 of 51 methods.*
* [`VectorsUploadShapefileForbiddenErrorResponseSchema`](./src/flypix/errors/vectorsuploadshapefileforbiddenerrorresponseschema.py): Not Found. Status code `403`. Applicable to 1 of 51 methods.*
* [`RegionsListForFileForbiddenErrorResponseSchema`](./src/flypix/errors/regionslistforfileforbiddenerrorresponseschema.py): Not Found. Status code `403`. Applicable to 1 of 51 methods.*
* [`RegionsCreateForbiddenErrorResponseSchema`](./src/flypix/errors/regionscreateforbiddenerrorresponseschema.py): Not Found. Status code `403`. Applicable to 1 of 51 methods.*
* [`RegionsDeleteForbiddenErrorResponseSchema`](./src/flypix/errors/regionsdeleteforbiddenerrorresponseschema.py): Not Found. Status code `403`. Applicable to 1 of 51 methods.*
* [`GeosenseCreateSessionForbiddenErrorResponseSchema`](./src/flypix/errors/geosensecreatesessionforbiddenerrorresponseschema.py): Not Found. Status code `403`. Applicable to 1 of 51 methods.*
* [`GeosenseCreateArtifactForbiddenErrorResponseSchema`](./src/flypix/errors/geosensecreateartifactforbiddenerrorresponseschema.py): Not Found. Status code `403`. Applicable to 1 of 51 methods.*
* [`GeosenseGetArtifactForbiddenErrorResponseSchema`](./src/flypix/errors/geosensegetartifactforbiddenerrorresponseschema.py): Not Found. Status code `403`. Applicable to 1 of 51 methods.*
* [`GeosenseSendMessageForbiddenErrorResponseSchema`](./src/flypix/errors/geosensesendmessageforbiddenerrorresponseschema.py): Not Found. Status code `403`. Applicable to 1 of 51 methods.*
* [`AuthLoginWithPasswordNotFoundErrorResponseSchema`](./src/flypix/errors/authloginwithpasswordnotfounderrorresponseschema.py): Bad Request. Status code `404`. Applicable to 1 of 51 methods.*
* [`AuthRefreshTokenNotFoundErrorResponseSchema`](./src/flypix/errors/authrefreshtokennotfounderrorresponseschema.py): Bad Request. Status code `404`. Applicable to 1 of 51 methods.*
* [`PaymentsGetBalanceNotFoundErrorResponseSchema`](./src/flypix/errors/paymentsgetbalancenotfounderrorresponseschema.py): Bad Request. Status code `404`. Applicable to 1 of 51 methods.*
* [`GetTenantTransactionsPaymentsBalanceTenantIDTransactionsGetNotFoundErrorResponseSchema`](./src/flypix/errors/gettenanttransactionspaymentsbalancetenantidtransactionsgetnotfounderrorresponseschema.py): Bad Request. Status code `404`. Applicable to 1 of 51 methods.*
* [`UsersListTenantsNotFoundErrorResponseSchema`](./src/flypix/errors/userslisttenantsnotfounderrorresponseschema.py): Bad Request. Status code `404`. Applicable to 1 of 51 methods.*
* [`ProjectsListForTenantNotFoundErrorResponseSchema`](./src/flypix/errors/projectslistfortenantnotfounderrorresponseschema.py): Bad Request. Status code `404`. Applicable to 1 of 51 methods.*
* [`ProjectsDeleteNotFoundErrorResponseSchema`](./src/flypix/errors/projectsdeletenotfounderrorresponseschema.py): Bad Request. Status code `404`. Applicable to 1 of 51 methods.*
* [`ProjectsCreateNotFoundErrorResponseSchema`](./src/flypix/errors/projectscreatenotfounderrorresponseschema.py): Bad Request. Status code `404`. Applicable to 1 of 51 methods.*
* [`FoldersListForFolderNotFoundErrorResponseSchema`](./src/flypix/errors/folderslistforfoldernotfounderrorresponseschema.py): Bad Request. Status code `404`. Applicable to 1 of 51 methods.*
* [`FoldersListForProjectNotFoundErrorResponseSchema`](./src/flypix/errors/folderslistforprojectnotfounderrorresponseschema.py): Bad Request. Status code `404`. Applicable to 1 of 51 methods.*
* [`FoldersDeleteNotFoundErrorResponseSchema`](./src/flypix/errors/foldersdeletenotfounderrorresponseschema.py): Bad Request. Status code `404`. Applicable to 1 of 51 methods.*
* [`FoldersCreateNotFoundErrorResponseSchema`](./src/flypix/errors/folderscreatenotfounderrorresponseschema.py): Bad Request. Status code `404`. Applicable to 1 of 51 methods.*
* [`FilesListForProjectNotFoundErrorResponseSchema`](./src/flypix/errors/fileslistforprojectnotfounderrorresponseschema.py): Bad Request. Status code `404`. Applicable to 1 of 51 methods.*
* [`FilesListForFolderNotFoundErrorResponseSchema`](./src/flypix/errors/fileslistforfoldernotfounderrorresponseschema.py): Bad Request. Status code `404`. Applicable to 1 of 51 methods.*
* [`FilesGetNotFoundErrorResponseSchema`](./src/flypix/errors/filesgetnotfounderrorresponseschema.py): Bad Request. Status code `404`. Applicable to 1 of 51 methods.*
* [`FilesDeleteNotFoundErrorResponseSchema`](./src/flypix/errors/filesdeletenotfounderrorresponseschema.py): Bad Request. Status code `404`. Applicable to 1 of 51 methods.*
* [`FilesGetVisibleRasterNotFoundErrorResponseSchema`](./src/flypix/errors/filesgetvisiblerasternotfounderrorresponseschema.py): Bad Request. Status code `404`. Applicable to 1 of 51 methods.*
* [`FilesGetDownloadLinkNotFoundErrorResponseSchema`](./src/flypix/errors/filesgetdownloadlinknotfounderrorresponseschema.py): Bad Request. Status code `404`. Applicable to 1 of 51 methods.*
* [`FilesGetByIdsNotFoundErrorResponseSchema`](./src/flypix/errors/filesgetbyidsnotfounderrorresponseschema.py): Bad Request. Status code `404`. Applicable to 1 of 51 methods.*
* [`FilesGetStorageUsageNotFoundErrorResponseSchema`](./src/flypix/errors/filesgetstorageusagenotfounderrorresponseschema.py): Bad Request. Status code `404`. Applicable to 1 of 51 methods.*
* [`FilesUploadNotFoundErrorResponseSchema`](./src/flypix/errors/filesuploadnotfounderrorresponseschema.py): Bad Request. Status code `404`. Applicable to 1 of 51 methods.*
* [`RastersListForTenantNotFoundErrorResponseSchema`](./src/flypix/errors/rasterslistfortenantnotfounderrorresponseschema.py): Bad Request. Status code `404`. Applicable to 1 of 51 methods.*
* [`RastersListForProjectNotFoundErrorResponseSchema`](./src/flypix/errors/rasterslistforprojectnotfounderrorresponseschema.py): Bad Request. Status code `404`. Applicable to 1 of 51 methods.*
* [`RastersListForFileNotFoundErrorResponseSchema`](./src/flypix/errors/rasterslistforfilenotfounderrorresponseschema.py): Bad Request. Status code `404`. Applicable to 1 of 51 methods.*
* [`InferencesListForTenantNotFoundErrorResponseSchema`](./src/flypix/errors/inferenceslistfortenantnotfounderrorresponseschema.py): Bad Request. Status code `404`. Applicable to 1 of 51 methods.*
* [`InferencesListForProjectNotFoundErrorResponseSchema`](./src/flypix/errors/inferenceslistforprojectnotfounderrorresponseschema.py): Bad Request. Status code `404`. Applicable to 1 of 51 methods.*
* [`InferencesListForFileNotFoundErrorResponseSchema`](./src/flypix/errors/inferenceslistforfilenotfounderrorresponseschema.py): Bad Request. Status code `404`. Applicable to 1 of 51 methods.*
* [`ModelsListForTenantNotFoundErrorResponseSchema`](./src/flypix/errors/modelslistfortenantnotfounderrorresponseschema.py): Bad Request. Status code `404`. Applicable to 1 of 51 methods.*
* [`ModelsListForProjectNotFoundErrorResponseSchema`](./src/flypix/errors/modelslistforprojectnotfounderrorresponseschema.py): Bad Request. Status code `404`. Applicable to 1 of 51 methods.*
* [`ModelsListOfficialNotFoundErrorResponseSchema`](./src/flypix/errors/modelslistofficialnotfounderrorresponseschema.py): Bad Request. Status code `404`. Applicable to 1 of 51 methods.*
* [`ModelsApplyNotFoundErrorResponseSchema`](./src/flypix/errors/modelsapplynotfounderrorresponseschema.py): Bad Request. Status code `404`. Applicable to 1 of 51 methods.*
* [`ModelsEstimateApplicationNotFoundErrorResponseSchema`](./src/flypix/errors/modelsestimateapplicationnotfounderrorresponseschema.py): Bad Request. Status code `404`. Applicable to 1 of 51 methods.*
* [`ModelsGetInferenceStatusNotFoundErrorResponseSchema`](./src/flypix/errors/modelsgetinferencestatusnotfounderrorresponseschema.py): Bad Request. Status code `404`. Applicable to 1 of 51 methods.*
* [`ModelsDeleteNotFoundErrorResponseSchema`](./src/flypix/errors/modelsdeletenotfounderrorresponseschema.py): Bad Request. Status code `404`. Applicable to 1 of 51 methods.*
* [`VectorsListForFileNotFoundErrorResponseSchema`](./src/flypix/errors/vectorslistforfilenotfounderrorresponseschema.py): Bad Request. Status code `404`. Applicable to 1 of 51 methods.*
* [`VectorsListClassesForProjectNotFoundErrorResponseSchema`](./src/flypix/errors/vectorslistclassesforprojectnotfounderrorresponseschema.py): Bad Request. Status code `404`. Applicable to 1 of 51 methods.*
* [`VectorsCreateClassNotFoundErrorResponseSchema`](./src/flypix/errors/vectorscreateclassnotfounderrorresponseschema.py): Bad Request. Status code `404`. Applicable to 1 of 51 methods.*
* [`VectorsGetFeaturesNotFoundErrorResponseSchema`](./src/flypix/errors/vectorsgetfeaturesnotfounderrorresponseschema.py): Bad Request. Status code `404`. Applicable to 1 of 51 methods.*
* [`VectorsCreateNotFoundErrorResponseSchema`](./src/flypix/errors/vectorscreatenotfounderrorresponseschema.py): Bad Request. Status code `404`. Applicable to 1 of 51 methods.*
* [`VectorsDeleteNotFoundErrorResponseSchema`](./src/flypix/errors/vectorsdeletenotfounderrorresponseschema.py): Bad Request. Status code `404`. Applicable to 1 of 51 methods.*
* [`VectorsCreateAnnotationsNotFoundErrorResponseSchema`](./src/flypix/errors/vectorscreateannotationsnotfounderrorresponseschema.py): Bad Request. Status code `404`. Applicable to 1 of 51 methods.*
* [`VectorsUploadGeojsonNotFoundErrorResponseSchema`](./src/flypix/errors/vectorsuploadgeojsonnotfounderrorresponseschema.py): Bad Request. Status code `404`. Applicable to 1 of 51 methods.*
* [`VectorsUploadGpkgNotFoundErrorResponseSchema`](./src/flypix/errors/vectorsuploadgpkgnotfounderrorresponseschema.py): Bad Request. Status code `404`. Applicable to 1 of 51 methods.*
* [`VectorsUploadShapefileNotFoundErrorResponseSchema`](./src/flypix/errors/vectorsuploadshapefilenotfounderrorresponseschema.py): Bad Request. Status code `404`. Applicable to 1 of 51 methods.*
* [`RegionsListForFileNotFoundErrorResponseSchema`](./src/flypix/errors/regionslistforfilenotfounderrorresponseschema.py): Bad Request. Status code `404`. Applicable to 1 of 51 methods.*
* [`RegionsCreateNotFoundErrorResponseSchema`](./src/flypix/errors/regionscreatenotfounderrorresponseschema.py): Bad Request. Status code `404`. Applicable to 1 of 51 methods.*
* [`RegionsDeleteNotFoundErrorResponseSchema`](./src/flypix/errors/regionsdeletenotfounderrorresponseschema.py): Bad Request. Status code `404`. Applicable to 1 of 51 methods.*
* [`GeosenseCreateSessionNotFoundErrorResponseSchema`](./src/flypix/errors/geosensecreatesessionnotfounderrorresponseschema.py): Bad Request. Status code `404`. Applicable to 1 of 51 methods.*
* [`GeosenseCreateArtifactNotFoundErrorResponseSchema`](./src/flypix/errors/geosensecreateartifactnotfounderrorresponseschema.py): Bad Request. Status code `404`. Applicable to 1 of 51 methods.*
* [`GeosenseGetArtifactNotFoundErrorResponseSchema`](./src/flypix/errors/geosensegetartifactnotfounderrorresponseschema.py): Bad Request. Status code `404`. Applicable to 1 of 51 methods.*
* [`GeosenseSendMessageNotFoundErrorResponseSchema`](./src/flypix/errors/geosensesendmessagenotfounderrorresponseschema.py): Bad Request. Status code `404`. Applicable to 1 of 51 methods.*
* [`AuthLoginWithPasswordInternalServerErrorErrorResponseSchema`](./src/flypix/errors/authloginwithpasswordinternalservererrorerrorresponseschema.py): Internal server error. Status code `500`. Applicable to 1 of 51 methods.*
* [`AuthRefreshTokenInternalServerErrorErrorResponseSchema`](./src/flypix/errors/authrefreshtokeninternalservererrorerrorresponseschema.py): Internal server error. Status code `500`. Applicable to 1 of 51 methods.*
* [`PaymentsGetBalanceInternalServerErrorErrorResponseSchema`](./src/flypix/errors/paymentsgetbalanceinternalservererrorerrorresponseschema.py): Internal server error. Status code `500`. Applicable to 1 of 51 methods.*
* [`GetTenantTransactionsPaymentsBalanceTenantIDTransactionsGetInternalServerErrorErrorResponseSchema`](./src/flypix/errors/gettenanttransactionspaymentsbalancetenantidtransactionsgetinternalservererrorerrorresponseschema.py): Internal server error. Status code `500`. Applicable to 1 of 51 methods.*
* [`UsersListTenantsInternalServerErrorErrorResponseSchema`](./src/flypix/errors/userslisttenantsinternalservererrorerrorresponseschema.py): Internal server error. Status code `500`. Applicable to 1 of 51 methods.*
* [`ProjectsListForTenantInternalServerErrorErrorResponseSchema`](./src/flypix/errors/projectslistfortenantinternalservererrorerrorresponseschema.py): Internal server error. Status code `500`. Applicable to 1 of 51 methods.*
* [`ProjectsDeleteInternalServerErrorErrorResponseSchema`](./src/flypix/errors/projectsdeleteinternalservererrorerrorresponseschema.py): Internal server error. Status code `500`. Applicable to 1 of 51 methods.*
* [`ProjectsCreateInternalServerErrorErrorResponseSchema`](./src/flypix/errors/projectscreateinternalservererrorerrorresponseschema.py): Internal server error. Status code `500`. Applicable to 1 of 51 methods.*
* [`FoldersListForFolderInternalServerErrorErrorResponseSchema`](./src/flypix/errors/folderslistforfolderinternalservererrorerrorresponseschema.py): Internal server error. Status code `500`. Applicable to 1 of 51 methods.*
* [`FoldersListForProjectInternalServerErrorErrorResponseSchema`](./src/flypix/errors/folderslistforprojectinternalservererrorerrorresponseschema.py): Internal server error. Status code `500`. Applicable to 1 of 51 methods.*
* [`FoldersDeleteInternalServerErrorErrorResponseSchema`](./src/flypix/errors/foldersdeleteinternalservererrorerrorresponseschema.py): Internal server error. Status code `500`. Applicable to 1 of 51 methods.*
* [`FoldersCreateInternalServerErrorErrorResponseSchema`](./src/flypix/errors/folderscreateinternalservererrorerrorresponseschema.py): Internal server error. Status code `500`. Applicable to 1 of 51 methods.*
* [`FilesListForProjectInternalServerErrorErrorResponseSchema`](./src/flypix/errors/fileslistforprojectinternalservererrorerrorresponseschema.py): Internal server error. Status code `500`. Applicable to 1 of 51 methods.*
* [`FilesListForFolderInternalServerErrorErrorResponseSchema`](./src/flypix/errors/fileslistforfolderinternalservererrorerrorresponseschema.py): Internal server error. Status code `500`. Applicable to 1 of 51 methods.*
* [`FilesGetInternalServerErrorErrorResponseSchema`](./src/flypix/errors/filesgetinternalservererrorerrorresponseschema.py): Internal server error. Status code `500`. Applicable to 1 of 51 methods.*
* [`FilesDeleteInternalServerErrorErrorResponseSchema`](./src/flypix/errors/filesdeleteinternalservererrorerrorresponseschema.py): Internal server error. Status code `500`. Applicable to 1 of 51 methods.*
* [`FilesGetVisibleRasterInternalServerErrorErrorResponseSchema`](./src/flypix/errors/filesgetvisiblerasterinternalservererrorerrorresponseschema.py): Internal server error. Status code `500`. Applicable to 1 of 51 methods.*
* [`FilesGetDownloadLinkInternalServerErrorErrorResponseSchema`](./src/flypix/errors/filesgetdownloadlinkinternalservererrorerrorresponseschema.py): Internal server error. Status code `500`. Applicable to 1 of 51 methods.*
* [`FilesGetByIdsInternalServerErrorErrorResponseSchema`](./src/flypix/errors/filesgetbyidsinternalservererrorerrorresponseschema.py): Internal server error. Status code `500`. Applicable to 1 of 51 methods.*
* [`FilesGetStorageUsageInternalServerErrorErrorResponseSchema`](./src/flypix/errors/filesgetstorageusageinternalservererrorerrorresponseschema.py): Internal server error. Status code `500`. Applicable to 1 of 51 methods.*
* [`FilesUploadInternalServerErrorErrorResponseSchema`](./src/flypix/errors/filesuploadinternalservererrorerrorresponseschema.py): Internal server error. Status code `500`. Applicable to 1 of 51 methods.*
* [`RastersListForTenantInternalServerErrorErrorResponseSchema`](./src/flypix/errors/rasterslistfortenantinternalservererrorerrorresponseschema.py): Internal server error. Status code `500`. Applicable to 1 of 51 methods.*
* [`RastersListForProjectInternalServerErrorErrorResponseSchema`](./src/flypix/errors/rasterslistforprojectinternalservererrorerrorresponseschema.py): Internal server error. Status code `500`. Applicable to 1 of 51 methods.*
* [`RastersListForFileInternalServerErrorErrorResponseSchema`](./src/flypix/errors/rasterslistforfileinternalservererrorerrorresponseschema.py): Internal server error. Status code `500`. Applicable to 1 of 51 methods.*
* [`InferencesListForTenantInternalServerErrorErrorResponseSchema`](./src/flypix/errors/inferenceslistfortenantinternalservererrorerrorresponseschema.py): Internal server error. Status code `500`. Applicable to 1 of 51 methods.*
* [`InferencesListForProjectInternalServerErrorErrorResponseSchema`](./src/flypix/errors/inferenceslistforprojectinternalservererrorerrorresponseschema.py): Internal server error. Status code `500`. Applicable to 1 of 51 methods.*
* [`InferencesListForFileInternalServerErrorErrorResponseSchema`](./src/flypix/errors/inferenceslistforfileinternalservererrorerrorresponseschema.py): Internal server error. Status code `500`. Applicable to 1 of 51 methods.*
* [`ModelsListForTenantInternalServerErrorErrorResponseSchema`](./src/flypix/errors/modelslistfortenantinternalservererrorerrorresponseschema.py): Internal server error. Status code `500`. Applicable to 1 of 51 methods.*
* [`ModelsListForProjectInternalServerErrorErrorResponseSchema`](./src/flypix/errors/modelslistforprojectinternalservererrorerrorresponseschema.py): Internal server error. Status code `500`. Applicable to 1 of 51 methods.*
* [`ModelsListOfficialInternalServerErrorErrorResponseSchema`](./src/flypix/errors/modelslistofficialinternalservererrorerrorresponseschema.py): Internal server error. Status code `500`. Applicable to 1 of 51 methods.*
* [`ModelsApplyInternalServerErrorErrorResponseSchema`](./src/flypix/errors/modelsapplyinternalservererrorerrorresponseschema.py): Internal server error. Status code `500`. Applicable to 1 of 51 methods.*
* [`ModelsEstimateApplicationInternalServerErrorErrorResponseSchema`](./src/flypix/errors/modelsestimateapplicationinternalservererrorerrorresponseschema.py): Internal server error. Status code `500`. Applicable to 1 of 51 methods.*
* [`ModelsGetInferenceStatusInternalServerErrorErrorResponseSchema`](./src/flypix/errors/modelsgetinferencestatusinternalservererrorerrorresponseschema.py): Internal server error. Status code `500`. Applicable to 1 of 51 methods.*
* [`ModelsDeleteInternalServerErrorErrorResponseSchema`](./src/flypix/errors/modelsdeleteinternalservererrorerrorresponseschema.py): Internal server error. Status code `500`. Applicable to 1 of 51 methods.*
* [`VectorsListForFileInternalServerErrorErrorResponseSchema`](./src/flypix/errors/vectorslistforfileinternalservererrorerrorresponseschema.py): Internal server error. Status code `500`. Applicable to 1 of 51 methods.*
* [`VectorsListClassesForProjectInternalServerErrorErrorResponseSchema`](./src/flypix/errors/vectorslistclassesforprojectinternalservererrorerrorresponseschema.py): Internal server error. Status code `500`. Applicable to 1 of 51 methods.*
* [`VectorsCreateClassInternalServerErrorErrorResponseSchema`](./src/flypix/errors/vectorscreateclassinternalservererrorerrorresponseschema.py): Internal server error. Status code `500`. Applicable to 1 of 51 methods.*
* [`VectorsGetFeaturesInternalServerErrorErrorResponseSchema`](./src/flypix/errors/vectorsgetfeaturesinternalservererrorerrorresponseschema.py): Internal server error. Status code `500`. Applicable to 1 of 51 methods.*
* [`VectorsCreateInternalServerErrorErrorResponseSchema`](./src/flypix/errors/vectorscreateinternalservererrorerrorresponseschema.py): Internal server error. Status code `500`. Applicable to 1 of 51 methods.*
* [`VectorsDeleteInternalServerErrorErrorResponseSchema`](./src/flypix/errors/vectorsdeleteinternalservererrorerrorresponseschema.py): Internal server error. Status code `500`. Applicable to 1 of 51 methods.*
* [`VectorsCreateAnnotationsInternalServerErrorErrorResponseSchema`](./src/flypix/errors/vectorscreateannotationsinternalservererrorerrorresponseschema.py): Internal server error. Status code `500`. Applicable to 1 of 51 methods.*
* [`VectorsUploadGeojsonInternalServerErrorErrorResponseSchema`](./src/flypix/errors/vectorsuploadgeojsoninternalservererrorerrorresponseschema.py): Internal server error. Status code `500`. Applicable to 1 of 51 methods.*
* [`VectorsUploadGpkgInternalServerErrorErrorResponseSchema`](./src/flypix/errors/vectorsuploadgpkginternalservererrorerrorresponseschema.py): Internal server error. Status code `500`. Applicable to 1 of 51 methods.*
* [`VectorsUploadShapefileInternalServerErrorErrorResponseSchema`](./src/flypix/errors/vectorsuploadshapefileinternalservererrorerrorresponseschema.py): Internal server error. Status code `500`. Applicable to 1 of 51 methods.*
* [`RegionsListForFileInternalServerErrorErrorResponseSchema`](./src/flypix/errors/regionslistforfileinternalservererrorerrorresponseschema.py): Internal server error. Status code `500`. Applicable to 1 of 51 methods.*
* [`RegionsCreateInternalServerErrorErrorResponseSchema`](./src/flypix/errors/regionscreateinternalservererrorerrorresponseschema.py): Internal server error. Status code `500`. Applicable to 1 of 51 methods.*
* [`RegionsDeleteInternalServerErrorErrorResponseSchema`](./src/flypix/errors/regionsdeleteinternalservererrorerrorresponseschema.py): Internal server error. Status code `500`. Applicable to 1 of 51 methods.*
* [`GeosenseCreateSessionInternalServerErrorErrorResponseSchema`](./src/flypix/errors/geosensecreatesessioninternalservererrorerrorresponseschema.py): Internal server error. Status code `500`. Applicable to 1 of 51 methods.*
* [`GeosenseCreateArtifactInternalServerErrorErrorResponseSchema`](./src/flypix/errors/geosensecreateartifactinternalservererrorerrorresponseschema.py): Internal server error. Status code `500`. Applicable to 1 of 51 methods.*
* [`GeosenseGetArtifactInternalServerErrorErrorResponseSchema`](./src/flypix/errors/geosensegetartifactinternalservererrorerrorresponseschema.py): Internal server error. Status code `500`. Applicable to 1 of 51 methods.*
* [`GeosenseSendMessageInternalServerErrorErrorResponseSchema`](./src/flypix/errors/geosensesendmessageinternalservererrorerrorresponseschema.py): Internal server error. Status code `500`. Applicable to 1 of 51 methods.*
* [`ResponseValidationError`](./src/flypix/errors/responsevalidationerror.py): Type mismatch between the response data and the expected Pydantic model. Provides access to the Pydantic validation error via the `cause` attribute.

</details>

\* Check [the method documentation](#available-resources-and-operations) to see if the error is applicable.
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

    res = f_client.auth.login_with_password(username="Allie.Hartmann", password="9ne8TpFJLsebftr")

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
from flypix import Flypix, models
def main():

    with Flypix(
        security=models.Security(
            api_key="<YOUR_API_KEY_HERE>",
        ),
    ) as f_client:
        # Rest of application here...


# Or when using async:
async def amain():

    async with Flypix(
        security=models.Security(
            api_key="<YOUR_API_KEY_HERE>",
        ),
    ) as f_client:
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
