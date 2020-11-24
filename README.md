# bicingstationsbcn
An app to see the bicycles around you using geolocation in Barcelona
This app uses LeafLet to render bicycle stations within the range of 450 mts of the user.

The application works this way:

The user opens the app and it asks to use the geolocation on the browser, once the access is approved it generates two variables Latitude and Longitude.

These variables are then processed by two methods which loop through the API JSON and check out whether the coordinates are in a range within 450 meters, at the same time it loops through a real-time info service in JSON form to show the availability of each station any moment, this data is then arranged inside of an array and sent to the template.

Once in the template the array is then used to show every station within it using the LeafLet library, it shows every bicycle location using MapBox to render every position, additionally I've used a LeafLet functionality which allows to add an image of your choice to the info displayed.

To show the Station's real time information I've used a Popup to display the Station Number, Bicycles Available and docks available to park.
