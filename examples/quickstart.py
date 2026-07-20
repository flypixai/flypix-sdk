# /// script
# requires-python = ">=3.10"
# dependencies = ["flypix"]
# ///

"""
FlyPix SDK quickstart
=====================

A minimal, end-to-end example of using the FlyPix Python SDK:

    1. Log in with your username / password to get an access token
    2. Look up your tenant id
    3. Create a new project
    4. Upload a local GeoTIFF (.tiff) file into that project
    5. Wait for the upload to be processed
    6. Run inference on the uploaded file with a chosen model
    7. Poll until the inference finishes
    8. Fetch and summarise the detected features

This is intentionally a single, top-to-bottom script (not a CLI). Edit the
values in the CONFIGURATION section below and run it:

    pip install flypix
    python quickstart.py

or, with uv, run it directly (it declares its own dependencies above):

    uv run examples/quickstart.py

The interactive API docs (Swagger UI) are always available at:

    https://api.flypix.ai/docs
"""

import os
import sys
import time

from flypix import Flypix, models

# ---------------------------------------------------------------------------
# CONFIGURATION  --  edit these values
# ---------------------------------------------------------------------------

# Your FlyPix account ApiKey
API_KEY = os.getenv("API_KEY") or "your api key"
TENANT_ID = os.getenv("TENANT_ID") or "your tenant id"
TIFF_PATH = os.getenv("TIFF_PATH") or "your tiff path"

# Name of the project that will be created.
PROJECT_NAME = "Quickstart API"

# Path to the local GeoTIFF file you want to upload and run inference on.
# The model to run. This is a model id (UUID). You can list the official
# models available to your account with `client.models.list_official()`, or
# the models private to your tenant with
# `client.models.list_for_tenant(tenant_id=...)`.
# The default id is the official BUILDING detector model.
MODEL_ID = os.getenv("MODEL_ID") or "01736030-4011-4951-b9b7-1fecf5d00f80"

# only relevant for development, you can omit this parameter in normal SDK usage
BASE_URL = os.getenv("BASE_URL") or "https://api.flypix.ai"
# How long to keep polling (seconds) before giving up.
POLL_TIMEOUT = 900
# How long to wait between polls (seconds).
POLL_INTERVAL = 10


def upload_tiff(client: Flypix, tenant_id: str, project_id: str) -> str:
    """Upload the local TIFF file to the project root and return the file id.

    The file body is streamed as a raw binary body (application/octet-stream)
    and the metadata is passed as arguments. Passing the open file handle as
    ``body`` lets the SDK stream it without loading the whole file into memory.
    """
    filename = TIFF_PATH.rsplit("/", 1)[-1]
    print(f"Uploading '{filename}'...")
    with open(TIFF_PATH, "rb") as f:
        result = client.files.upload_v2(
            tenant_id=tenant_id,
            project_id=project_id,
            filename=filename,
            body=f,
        )
    # status here is "UPLOADED" -- the file still needs to be processed
    # asynchronously before it is ready for inference (see wait_until_ready).
    print(f"  -> uploaded file {result.file_id} (status: {result.status})")
    return result.file_id


def wait_until_ready(client: Flypix, file_id: str) -> None:
    """Poll until the file is READY and its raster has been PROCESSED.

    After an upload the file is processed into a raster asynchronously. Before
    a model can be applied we need two things:
      1. the file itself to reach status READY, and
      2. the raster for that file to reach status PROCESSED.
    """
    deadline = time.monotonic() + POLL_TIMEOUT

    print("Waiting for the file to be processed...")
    while time.monotonic() < deadline:
        try:
            client.files.get(file_id=file_id)
        except Exception as e:
            print(e)
        file_status = client.files.get(file_id=file_id).status
        print(f"  file status: {file_status}")
        if file_status == "READY":
            break
        if file_status == "FAILED":
            sys.exit("File processing failed.")
        time.sleep(POLL_INTERVAL)
    else:
        sys.exit("Timed out waiting for the file to become READY.")

    print("Waiting for the raster to be processed...")
    while time.monotonic() < deadline:
        raster_status = client.rasters.list_for_file(file_id=file_id).status
        print(f"  raster status: {raster_status}")
        if raster_status == "PROCESSED":
            return
        if raster_status == "FAILED":
            sys.exit("Raster processing failed.")
        time.sleep(POLL_INTERVAL)
    sys.exit("Timed out waiting for the raster to be PROCESSED.")


def wait_for_inference(client: Flypix, inference_id: str) -> None:
    """Poll the inference until it FINISHED or FAILED."""
    print("Waiting for inference to finish...")
    deadline = time.monotonic() + POLL_TIMEOUT
    while time.monotonic() < deadline:
        status = client.models.get_inference_status(inference_id=inference_id).status
        print(f"  inference status: {status}")
        if status == "FINISHED":
            return
        if status == "FAILED":
            sys.exit("Inference failed.")
        time.sleep(POLL_INTERVAL)
    sys.exit("Timed out waiting for the inference to finish.")


def fetch_features(client: Flypix, file_id: str) -> None:
    """Fetch and summarise the detected features (vectors) for the file.

    Inference produces one or more vector layers on the file. Each layer holds
    the detected features (polygons) and a map of class ids to class names.
    """
    print("Fetching detected features...")
    vectors = client.vectors.list_for_file(file_id=file_id)
    if not vectors:
        print("  no vector layers found for this file.")
        return

    for vector in vectors:
        print(f"\n  Vector layer '{vector.name}' ({vector.vector_id}):")

        features = client.vectors.get_features(vector_id=vector.vector_id)
        data = features.data
        # `classes` maps a class id (as a string) to its human-readable name.
        classes = features.classes
        # Each list maps by index: the i-th detection is described by
        # ids[i], areas[i], polygons[i] (WKB base64), confidences[i], class_ids[i].
        print(f"    {len(data.ids)} feature(s) detected")

        # Count detections per class for a quick summary.
        per_class: dict[str, int] = {}
        for class_id in data.class_ids:
            name = classes.get(str(class_id), f"class {class_id}")
            per_class[name] = per_class.get(name, 0) + 1
        for name, n in per_class.items():
            print(f"      - {name}: {n}")

        # `data.polygons` holds each geometry as a Base64-encoded WKB string,
        # which you can decode with a library such as `shapely` if you need the
        # actual geometries.


def main() -> None:
    with Flypix(security=models.security.Security(api_key=API_KEY), server_url=BASE_URL) as client:
        print(f"Creating project '{PROJECT_NAME}'...")
        project = client.projects.create(tenant_id=TENANT_ID, name=PROJECT_NAME)
        print(f"  -> created project {project.project_id}")

        file_id = upload_tiff(client, TENANT_ID, project.project_id)
        wait_until_ready(client, file_id)

        print(f"Applying model {MODEL_ID}...")
        inference = client.models.apply(model_id=MODEL_ID, file_id=file_id)
        print(f"  -> started inference {inference.inference_id}")

        wait_for_inference(client, inference.inference_id)
        fetch_features(client, file_id)

        print("\nDone!")
        print(f"  project id:   {project.project_id}")
        print(f"  file id:      {file_id}")
        print(f"  inference id: {inference.inference_id}")


if __name__ == "__main__":
    main()
