# CreateRegionPayload


## Fields

| Field                                                                  | Type                                                                   | Required                                                               | Description                                                            |
| ---------------------------------------------------------------------- | ---------------------------------------------------------------------- | ---------------------------------------------------------------------- | ---------------------------------------------------------------------- |
| `polygon`                                                              | *str*                                                                  | :heavy_check_mark:                                                     | WKB Polygon encoded to Base64                                          |
| `metadata`                                                             | [models.RegionMetadata](../models/regionmetadata.md)                   | :heavy_check_mark:                                                     | N/A                                                                    |
| `training_behavior`                                                    | [models.RegionTrainingBehavior](../models/regiontrainingbehavior.md)   | :heavy_check_mark:                                                     | N/A                                                                    |
| `inference_behavior`                                                   | [models.RegionInferenceBehavior](../models/regioninferencebehavior.md) | :heavy_check_mark:                                                     | N/A                                                                    |