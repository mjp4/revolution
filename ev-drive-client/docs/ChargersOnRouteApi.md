# Revolution.ChargersOnRouteApi

All URIs are relative to *http://localhost/revolution/api*

Method | HTTP request | Description
------------- | ------------- | -------------
[**chargersOnRoute**](ChargersOnRouteApi.md#chargersOnRoute) | **GET** /chargers_on_route/{from}/{to} | Get a list of the chargers on route


<a name="chargersOnRoute"></a>
# **chargersOnRoute**
> OnRoute chargersOnRoute(from, to)

Get a list of the chargers on route

### Example
```javascript
var Revolution = require('revolution');

var apiInstance = new Revolution.ChargersOnRouteApi();

var from = "from_example"; // String | Start or end point

var to = "to_example"; // String | Start or end point


var callback = function(error, data, response) {
  if (error) {
    console.error(error);
  } else {
    console.log('API called successfully. Returned data: ' + data);
  }
};
apiInstance.chargersOnRoute(from, to, callback);
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **from** | **String**| Start or end point | 
 **to** | **String**| Start or end point | 

### Return type

[**OnRoute**](OnRoute.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

