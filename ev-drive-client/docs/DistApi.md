# Revolution.DistApi

All URIs are relative to *http://localhost/revolution/api*

Method | HTTP request | Description
------------- | ------------- | -------------
[**getDistToCharger**](DistApi.md#getDistToCharger) | **GET** /dist_to_charger/{lat_here}/{long_here}/{lat_there}/{long_there} | Get the distance to charger


<a name="getDistToCharger"></a>
# **getDistToCharger**
> DistToCharger getDistToCharger(latHere, longHere, latThere, longThere)

Get the distance to charger

### Example
```javascript
var Revolution = require('revolution');

var apiInstance = new Revolution.DistApi();

var latHere = "latHere_example"; // String | The latitude or longitude

var longHere = "longHere_example"; // String | The latitude or longitude

var latThere = "latThere_example"; // String | The latitude or longitude

var longThere = "longThere_example"; // String | The latitude or longitude


var callback = function(error, data, response) {
  if (error) {
    console.error(error);
  } else {
    console.log('API called successfully. Returned data: ' + data);
  }
};
apiInstance.getDistToCharger(latHere, longHere, latThere, longThere, callback);
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **latHere** | **String**| The latitude or longitude | 
 **longHere** | **String**| The latitude or longitude | 
 **latThere** | **String**| The latitude or longitude | 
 **longThere** | **String**| The latitude or longitude | 

### Return type

[**DistToCharger**](DistToCharger.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

