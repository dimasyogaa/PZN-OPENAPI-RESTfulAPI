# swagger.api.AllApi

## Load the API package
```dart
import 'package:swagger/api.dart';
```

All URIs are relative to *https://{environment}.yogadimaspambudi.com/api/v1*

Method | HTTP request | Description
------------- | ------------- | -------------
[**todolistGet**](AllApi.md#todolistGet) | **GET** /todolist | Get All Todolist

# **todolistGet**
> ArrayTodolist todolistGet(includeDone, name)

Get All Todolist

Get all active todolist by default

### Example
```dart
import 'package:swagger/api.dart';
// TODO Configure API key authorization: TodolistAuth
//swagger.api.Configuration.apiKey{'X-API-Key'} = 'YOUR_API_KEY';
// uncomment below to setup prefix (e.g. Bearer) for API key, if needed
//swagger.api.Configuration.apiKeyPrefix{'X-API-Key'} = "Bearer";

var api_instance = new AllApi();
var includeDone = true; // bool | Is include_done todolist
var name = name_example; // String | Filter todolist by name

try {
    var result = api_instance.todolistGet(includeDone, name);
    print(result);
} catch (e) {
    print("Exception when calling AllApi->todolistGet: $e\n");
}
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **includeDone** | **bool**| Is include_done todolist | [optional] [default to false]
 **name** | **String**| Filter todolist by name | [optional] 

### Return type

[**ArrayTodolist**](ArrayTodolist.md)

### Authorization

[TodolistAuth](../README.md#TodolistAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

