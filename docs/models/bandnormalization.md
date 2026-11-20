# BandNormalization


## Fields

| Field                                                                        | Type                                                                         | Required                                                                     | Description                                                                  |
| ---------------------------------------------------------------------------- | ---------------------------------------------------------------------------- | ---------------------------------------------------------------------------- | ---------------------------------------------------------------------------- |
| `band`                                                                       | *int*                                                                        | :heavy_check_mark:                                                           | 1-based raster band                                                          |
| `max`                                                                        | *Optional[float]*                                                            | :heavy_minus_sign:                                                           | Value mapped to 255. Measured over both rasters (98th percentile) when unset |
| `min`                                                                        | *Optional[float]*                                                            | :heavy_minus_sign:                                                           | Value mapped to 0. Measured over both rasters (2nd percentile) when unset    |