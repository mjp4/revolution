# Revolution.AllApi

All URIs are relative to *http://localhost/revolution/api*

Method | HTTP request | Description
------------- | ------------- | -------------
[**allInfo**](AllApi.md#allInfo) | **GET** /all_info/{username}/{password}/{to} | Get all the info


<a name="allInfo"></a>
# **allInfo**
> AllInfo allInfo(username, passwordto)

Get all the info

### Example
```javascript
var Revolution = require('revolution');

var apiInstance = new Revolution.AllApi();

var username = "username_example"; // String | Username for logging in 

var password = "password_example"; // String | Users password

var to = "to_example"; // String | Start or end point


var callback = function(error, data, response) {
  if (error) {
    console.error(error);
  } else {
    console.log('API called successfully. Returned data: ' + data);
  }
};
apiInstance.allInfo(username, passwordto, callback);
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **username** | **String**| Username for logging in  | 
 **password** | **String**| Users password | 
 **to** | **String**| Start or end point | 

### Return type

[**AllInfo**](AllInfo.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

