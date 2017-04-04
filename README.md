mysports-dl
========

Python script to mass download/export your activities from TomTom MySports website.

#### Usage

    python mysports-dl.py [-h] username password format [max-activity-id]

Parameters

* username: your account email 
* password: your password, enclose in double quotes if it has spaces
* format: format of download, one of the following: tcx, gpx, fit, or kml
* max-activity-id: optional argument to define an upper bound for activity download. In the activities list, it's the number sequence by the end of the url of the activity. The script will download all activities up to this argument.

Your activities will be downloaded to an activities folder, created in the same path as the script.

#### Requirements

 * requests

#### Useful notes

* TomTom automatic upload to Strava doesn't seem to carry laps information for interval training, but manual tcx file uploads do
* downloaded files has the following naming convention: <activity type>-<YYYYMMDD>T<HHMMSS>, which in my opinion is preferable than that from the watch, since it can nicely sorted by activity type and date

## License

This script is released under the [MIT License](https://github.com/vitorhirota/tcx-edit/blob/master/LICENSE).
