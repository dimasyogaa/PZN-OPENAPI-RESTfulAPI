# TodoListResTfulApi.AllApi

All URIs are relative to *https://{environment}.yogadimaspambudi.com/api/v1*

Method | HTTP request | Description
------------- | ------------- | -------------
[**todolistGet**](AllApi.md#todolistGet) | **GET** /todolist | Get All Todolist

<a name="todolistGet"></a>
# **todolistGet**
> ArrayTodolist todolistGet(opts)

Get All Todolist

Get all active todolist by default

### Example
```javascript
import {TodoListResTfulApi} from 'todo_list_res_tful_api';
let defaultClient = TodoListResTfulApi.ApiClient.instance;

// Configure API key authorization: TodolistAuth
let TodolistAuth = defaultClient.authentications['TodolistAuth'];
TodolistAuth.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//TodolistAuth.apiKeyPrefix = 'Token';

let apiInstance = new TodoListResTfulApi.AllApi();
let opts = { 
  'includeDone': false, // Boolean | Is include_done todolist
  'name': "name_example" // String | Filter todolist by name
};
apiInstance.todolistGet(opts, (error, data, response) => {
  if (error) {
    console.error(error);
  } else {
    console.log('API called successfully. Returned data: ' + data);
  }
});
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **includeDone** | **Boolean**| Is include_done todolist | [optional] [default to false]
 **name** | **String**| Filter todolist by name | [optional] 

### Return type

[**ArrayTodolist**](ArrayTodolist.md)

### Authorization

[TodolistAuth](../README.md#TodolistAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

