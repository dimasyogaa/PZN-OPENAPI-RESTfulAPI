# TodoListResTfulApi.TodolistApi

All URIs are relative to *https://{environment}.yogadimaspambudi.com/api/v1*

Method | HTTP request | Description
------------- | ------------- | -------------
[**todolistGet**](TodolistApi.md#todolistGet) | **GET** /todolist | Get All Todolist
[**todolistPost**](TodolistApi.md#todolistPost) | **POST** /todolist | Create new Todolist
[**todolistTodolistIdDelete**](TodolistApi.md#todolistTodolistIdDelete) | **DELETE** /todolist/{todolistId} | Delete existing todolist
[**todolistTodolistIdPut**](TodolistApi.md#todolistTodolistIdPut) | **PUT** /todolist/{todolistId} | Update existing todolist

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

let apiInstance = new TodoListResTfulApi.TodolistApi();
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

<a name="todolistPost"></a>
# **todolistPost**
> Todolist todolistPost(body)

Create new Todolist

Create new active todolist

### Example
```javascript
import {TodoListResTfulApi} from 'todo_list_res_tful_api';
let defaultClient = TodoListResTfulApi.ApiClient.instance;

// Configure API key authorization: TodolistAuth
let TodolistAuth = defaultClient.authentications['TodolistAuth'];
TodolistAuth.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//TodolistAuth.apiKeyPrefix = 'Token';

let apiInstance = new TodoListResTfulApi.TodolistApi();
let body = new TodoListResTfulApi.CreateOrUpdateTodolist(); // CreateOrUpdateTodolist | 

apiInstance.todolistPost(body, (error, data, response) => {
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
 **body** | [**CreateOrUpdateTodolist**](CreateOrUpdateTodolist.md)|  | 

### Return type

[**Todolist**](Todolist.md)

### Authorization

[TodolistAuth](../README.md#TodolistAuth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

<a name="todolistTodolistIdDelete"></a>
# **todolistTodolistIdDelete**
> InlineResponse200 todolistTodolistIdDelete(todolistId)

Delete existing todolist

Delete existing todolist in database

### Example
```javascript
import {TodoListResTfulApi} from 'todo_list_res_tful_api';
let defaultClient = TodoListResTfulApi.ApiClient.instance;

// Configure API key authorization: TodolistAuth
let TodolistAuth = defaultClient.authentications['TodolistAuth'];
TodolistAuth.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//TodolistAuth.apiKeyPrefix = 'Token';

let apiInstance = new TodoListResTfulApi.TodolistApi();
let todolistId = "todolistId_example"; // String | TodoList id for updated

apiInstance.todolistTodolistIdDelete(todolistId, (error, data, response) => {
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
 **todolistId** | **String**| TodoList id for updated | 

### Return type

[**InlineResponse200**](InlineResponse200.md)

### Authorization

[TodolistAuth](../README.md#TodolistAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

<a name="todolistTodolistIdPut"></a>
# **todolistTodolistIdPut**
> Todolist todolistTodolistIdPut(body, todolistId)

Update existing todolist

Update existing todolist in database

### Example
```javascript
import {TodoListResTfulApi} from 'todo_list_res_tful_api';
let defaultClient = TodoListResTfulApi.ApiClient.instance;

// Configure API key authorization: TodolistAuth
let TodolistAuth = defaultClient.authentications['TodolistAuth'];
TodolistAuth.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//TodolistAuth.apiKeyPrefix = 'Token';

let apiInstance = new TodoListResTfulApi.TodolistApi();
let body = new TodoListResTfulApi.CreateOrUpdateTodolist(); // CreateOrUpdateTodolist | 
let todolistId = "todolistId_example"; // String | TodoList id for updated

apiInstance.todolistTodolistIdPut(body, todolistId, (error, data, response) => {
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
 **body** | [**CreateOrUpdateTodolist**](CreateOrUpdateTodolist.md)|  | 
 **todolistId** | **String**| TodoList id for updated | 

### Return type

[**Todolist**](Todolist.md)

### Authorization

[TodolistAuth](../README.md#TodolistAuth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

