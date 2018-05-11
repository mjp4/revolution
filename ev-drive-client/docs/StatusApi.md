# Revolution.StatusApi

All URIs are relative to *http://localhost/revolution/api*

Method | HTTP request | Description
------------- | ------------- | -------------
[**getChargePerc**](StatusApi.md#getChargePerc) | **GET** /charge_perc/nissan/{username}/{password} | Get the charge percentage


<a name="getChargePerc"></a>
# **getChargePerc**
> ChargePerc getChargePerc(username, password)

Get the charge percentage

### Example
```javascript
var Revolution = require('revolution');

var apiInstance = new Revolution.StatusApi();

var username = "username_example"; // String | Username for logging in 

var password = "password_example"; // String | Users password


var callback = function(error, data, response) {
  if (error) {
    console.error(error);
  } else {
    console.log('API called successfully. Returned data: ' + data);
  }
};
apiInstance.getChargePerc(username, password, callback);
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **username** | **String**| Username for logging in  | 
 **password** | **String**| Users password | 

### Return type

[**ChargePerc**](ChargePerc.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

