# GetAnnotationPreviewRequest


## Fields

| Field                                                                                | Type                                                                                 | Required                                                                             | Description                                                                          |
| ------------------------------------------------------------------------------------ | ------------------------------------------------------------------------------------ | ------------------------------------------------------------------------------------ | ------------------------------------------------------------------------------------ |
| `annotation_id`                                                                      | *str*                                                                                | :heavy_check_mark:                                                                   | N/A                                                                                  |
| `annotation_coverage`                                                                | *Optional[float]*                                                                    | :heavy_minus_sign:                                                                   | Share of the preview's area taken by the annotation's bounding box. Defaults to 0.7. |
| `preview_size_px`                                                                    | *Optional[int]*                                                                      | :heavy_minus_sign:                                                                   | Longest side of the preview, in pixels. Defaults to 512.                             |