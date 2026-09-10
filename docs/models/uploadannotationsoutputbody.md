# UploadAnnotationsOutputBody


## Fields

| Field                                                            | Type                                                             | Required                                                         | Description                                                      | Example                                                          |
| ---------------------------------------------------------------- | ---------------------------------------------------------------- | ---------------------------------------------------------------- | ---------------------------------------------------------------- | ---------------------------------------------------------------- |
| `dollar_schema`                                                  | *Optional[str]*                                                  | :heavy_minus_sign:                                               | A URL to the JSON Schema for this object.                        | https://example.com/schemas/UploadAnnotationsOutputBody.json     |
| `annotation_ids`                                                 | List[*int*]                                                      | :heavy_check_mark:                                               | N/A                                                              |                                                                  |
| `errored`                                                        | List[[models.ErroredAnnotation](../models/erroredannotation.md)] | :heavy_check_mark:                                               | N/A                                                              |                                                                  |