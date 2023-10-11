# swagger.api.TodolistApi

## Load the API package
```dart
import 'package:swagger/api.dart';
```

All URIs are relative to *https://{environment}.yogadimaspambudi.com/api/v1*

Method | HTTP request | Description
------------- | ------------- | -------------
[**todolistGet**](TodolistApi.md#todolistGet) | **GET** /todolist | Get All Todolist
[**todolistPost**](TodolistApi.md#todolistPost) | **POST** /todolist | Create new Todolist
[**todolistTodolistIdDelete**](TodolistApi.md#todolistTodolistIdDelete) | **DELETE** /todolist/{todolistId} | Delete existing todolist
[**todolistTodolistIdPut**](TodolistApi.md#todolistTodolistIdPut) | **PUT** /todolist/{todolistId} | Update existing todolist

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

var api_instance = new TodolistApi();
var includeDone = true; // bool | Is include_done todolist
var name = name_example; // String | Filter todolist by name

try {
    var result = api_instance.todolistGet(includeDone, name);
    print(result);
} catch (e) {
    print("Exception when calling TodolistApi->todolistGet: $e\n");
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

# **todolistPost**
> Todolist todolistPost(body)

Create new Todolist

Create new active todolist

### Example
```dart
import 'package:swagger/api.dart';
// TODO Configure API key authorization: TodolistAuth
//swagger.api.Configuration.apiKey{'X-API-Key'} = 'YOUR_API_KEY';
// uncomment below to setup prefix (e.g. Bearer) for API key, if needed
//swagger.api.Configuration.apiKeyPrefix{'X-API-Key'} = "Bearer";

var api_instance = new TodolistApi();
var body = new CreateOrUpdateTodolist(); // CreateOrUpdateTodolist | 

try {
    var result = api_instance.todolistPost(body);
    print(result);
} catch (e) {
    print("Exception when calling TodolistApi->todolistPost: $e\n");
}
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**CreateOrUpdateTodolist**](CreateOrUpdateTodolist.md)|  | 

### Return type

[**Todolist**](Todolist.md)

### Authorization

[TodolistAuth](../README.md#TodolistAuth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **todolistTodolistIdDelete**
> InlineResponse200 todolistTodolistIdDelete(todolistId)

Delete existing todolist

Delete existing todolist in database

### Example
```dart
import 'package:swagger/api.dart';
// TODO Configure API key authorization: TodolistAuth
//swagger.api.Configuration.apiKey{'X-API-Key'} = 'YOUR_API_KEY';
// uncomment below to setup prefix (e.g. Bearer) for API key, if needed
//swagger.api.Configuration.apiKeyPrefix{'X-API-Key'} = "Bearer";

var api_instance = new TodolistApi();
var todolistId = todolistId_example; // String | TodoList id for updated

try {
    var result = api_instance.todolistTodolistIdDelete(todolistId);
    print(result);
} catch (e) {
    print("Exception when calling TodolistApi->todolistTodolistIdDelete: $e\n");
}
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **todolistId** | **String**| TodoList id for updated | 

### Return type

[**InlineResponse200**](InlineResponse200.md)

### Authorization

[TodolistAuth](../README.md#TodolistAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **todolistTodolistIdPut**
> Todolist todolistTodolistIdPut(body, todolistId)

Update existing todolist

Update existing todolist in database

### Example
```dart
import 'package:swagger/api.dart';
// TODO Configure API key authorization: TodolistAuth
//swagger.api.Configuration.apiKey{'X-API-Key'} = 'YOUR_API_KEY';
// uncomment below to setup prefix (e.g. Bearer) for API key, if needed
//swagger.api.Configuration.apiKeyPrefix{'X-API-Key'} = "Bearer";

var api_instance = new TodolistApi();
var body = new CreateOrUpdateTodolist(); // CreateOrUpdateTodolist | 
var todolistId = todolistId_example; // String | TodoList id for updated

try {
    var result = api_instance.todolistTodolistIdPut(body, todolistId);
    print(result);
} catch (e) {
    print("Exception when calling TodolistApi->todolistTodolistIdPut: $e\n");
}
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**CreateOrUpdateTodolist**](CreateOrUpdateTodolist.md)|  | 
 **todolistId** | **String**| TodoList id for updated | 

### Return type

[**Todolist**](Todolist.md)

### Authorization

[TodolistAuth](../README.md#TodolistAuth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

