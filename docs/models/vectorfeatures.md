# VectorFeatures

This data structure contains the annotations.
The elements in each array map by index. i.e. the first annotation would correspond
with `(ids[0], areas[0], polygons[0], confidences[0], class_ids[0])`.

The polygon is indicated as a WKB string (Base64).
The class id is indicated as an integer that
maps to the `classes` property


## Fields

| Field                                                        | Type                                                         | Required                                                     | Description                                                  |
| ------------------------------------------------------------ | ------------------------------------------------------------ | ------------------------------------------------------------ | ------------------------------------------------------------ |
| `data`                                                       | [models.VectorFeaturesDict](../models/vectorfeaturesdict.md) | :heavy_check_mark:                                           | N/A                                                          |
| `classes`                                                    | Dict[str, *str*]                                             | :heavy_check_mark:                                           | N/A                                                          |