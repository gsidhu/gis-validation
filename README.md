# GIS Validation v0.1

**Author:** Gurjot Sidhu
**License:** MIT
**Acknowledgement:** James Halliday for [point-in-polygon](https://github.com/substack/point-in-polygon)

## Description
This script checks whether a geospatial coordinate (long, lat) falls within the boundaries defined by a (multi-shape) polygon. It uses the [PNPOLY - Point Inclusion in Polygon Test by W. Randolph Franklin (WRF)](https://wrf.ecse.rpi.edu/Research/Short_Notes/pnpoly.html).

This script contains wrapper functions to support purposes of geospatial shapes.

## To do
* Create a sister script where user can declare block / district to be validated against and the script automatically fetches the required polygon and runs the check for the point.
* Add more tests
* Add a `how to` section in README

## License
MIT