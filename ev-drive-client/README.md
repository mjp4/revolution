# revolution

Revolution - JavaScript client for revolution
No description provided (generated by Swagger Codegen https://github.com/swagger-api/swagger-codegen)
This SDK is automatically generated by the [Swagger Codegen](https://github.com/swagger-api/swagger-codegen) project:

- API version: 0.0.1
- Package version: 0.0.1
- Build package: io.swagger.codegen.languages.JavascriptClientCodegen
For more information, please visit [https://www.metaswitch.com/](https://www.metaswitch.com/)

## Installation

### For [Node.js](https://nodejs.org/)

#### npm

To publish the library as a [npm](https://www.npmjs.com/),
please follow the procedure in ["Publishing npm packages"](https://docs.npmjs.com/getting-started/publishing-npm-packages).

Then install it via:

```shell
npm install revolution --save
```

##### Local development

To use the library locally without publishing to a remote npm registry, first install the dependencies by changing 
into the directory containing `package.json` (and this README). Let's call this `JAVASCRIPT_CLIENT_DIR`. Then run:

```shell
npm install
```

Next, [link](https://docs.npmjs.com/cli/link) it globally in npm with the following, also from `JAVASCRIPT_CLIENT_DIR`:

```shell
npm link
```

Finally, switch to the directory you want to use your revolution from, and run:

```shell
npm link /path/to/<JAVASCRIPT_CLIENT_DIR>
```

You should now be able to `require('revolution')` in javascript files from the directory you ran the last 
command above from.

#### git
#
If the library is hosted at a git repository, e.g.
https://github.com/GIT_USER_ID/GIT_REPO_ID
then install it via:

```shell
    npm install GIT_USER_ID/GIT_REPO_ID --save
```

### For browser

The library also works in the browser environment via npm and [browserify](http://browserify.org/). After following
the above steps with Node.js and installing browserify with `npm install -g browserify`,
perform the following (assuming *main.js* is your entry file, that's to say your javascript file where you actually 
use this library):

```shell
browserify main.js > bundle.js
```

Then include *bundle.js* in the HTML pages.

### Webpack Configuration

Using Webpack you may encounter the following error: "Module not found: Error:
Cannot resolve module", most certainly you should disable AMD loader. Add/merge
the following section to your webpack config:

```javascript
module: {
  rules: [
    {
      parser: {
        amd: false
      }
    }
  ]
}
```

## Getting Started

Please follow the [installation](#installation) instruction and execute the following JS code:

```javascript
var Revolution = require('revolution');

var api = new Revolution.AllApi()

var username = "username_example"; // {String} Username for logging in 

var password = "password_example"; // {String} Users password

var to = "to_example"; // {String} Start or end point


var callback = function(error, data, response) {
  if (error) {
    console.error(error);
  } else {
    console.log('API called successfully. Returned data: ' + data);
  }
};
api.allInfo(username, passwordto, callback);

```

## Documentation for API Endpoints

All URIs are relative to *http://localhost/revolution/api*

Class | Method | HTTP request | Description
------------ | ------------- | ------------- | -------------
*Revolution.AllApi* | [**allInfo**](docs/AllApi.md#allInfo) | **GET** /all_info/{username}/{password}/{to} | Get all the info
*Revolution.ChargersOnRouteApi* | [**chargersOnRoute**](docs/ChargersOnRouteApi.md#chargersOnRoute) | **GET** /chargers_on_route/{from}/{to} | Get a list of the chargers on route
*Revolution.DistApi* | [**getDistToCharger**](docs/DistApi.md#getDistToCharger) | **GET** /dist_to_charger/{lat_here}/{long_here}/{lat_there}/{long_there} | Get the distance to charger
*Revolution.StatusApi* | [**getChargePerc**](docs/StatusApi.md#getChargePerc) | **GET** /charge_perc/nissan/{username}/{password} | Get the charge percentage


## Documentation for Models

 - [Revolution.AllInfo](docs/AllInfo.md)
 - [Revolution.AllInfoCar](docs/AllInfoCar.md)
 - [Revolution.ChargePerc](docs/ChargePerc.md)
 - [Revolution.Charger](docs/Charger.md)
 - [Revolution.DistToCharger](docs/DistToCharger.md)
 - [Revolution.OnRoute](docs/OnRoute.md)


## Documentation for Authorization

 All endpoints do not require authorization.
