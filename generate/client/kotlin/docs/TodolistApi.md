# TodolistApi

All URIs are relative to *https://{environment}.yogadimaspambudi.com/api/v1*

Method | HTTP request | Description
------------- | ------------- | -------------
[**todolistGet**](TodolistApi.md#todolistGet) | **GET** /todolist | Get All Todolist
[**todolistPost**](TodolistApi.md#todolistPost) | **POST** /todolist | Create new Todolist
[**todolistTodolistIdDelete**](TodolistApi.md#todolistTodolistIdDelete) | **DELETE** /todolist/{todolistId} | Delete existing todolist
[**todolistTodolistIdPut**](TodolistApi.md#todolistTodolistIdPut) | **PUT** /todolist/{todolistId} | Update existing todolist

<a name="todolistGet"></a>
# **todolistGet**
> ArrayTodolist todolistGet(includeDone, name)

Get All Todolist

Get all active todolist by default

### Example
```kotlin
// Import classes:
//import io.swagger.client.infrastructure.*
//import io.swagger.client.models.*;

val apiInstance = TodolistApi()
val includeDone : kotlin.Boolean = true // kotlin.Boolean | Is include_done todolist
val name : kotlin.String = name_example // kotlin.String | Filter todolist by name
try {
    val result : ArrayTodolist = apiInstance.todolistGet(includeDone, name)
    println(result)
} catch (e: ClientException) {
    println("4xx response calling TodolistApi#todolistGet")
    e.printStackTrace()
} catch (e: ServerException) {
    println("5xx response calling TodolistApi#todolistGet")
    e.printStackTrace()
}
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **includeDone** | **kotlin.Boolean**| Is include_done todolist | [optional] [default to false]
 **name** | **kotlin.String**| Filter todolist by name | [optional]

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
```kotlin
// Import classes:
//import io.swagger.client.infrastructure.*
//import io.swagger.client.models.*;

val apiInstance = TodolistApi()
val body : CreateOrUpdateTodolist = {
  "description" : "Example Create todolist Java",
  "value" : {
    "name" : "Java",
    "priority" : 3,
    "tags" : [ "Java", "Programming" ]
  }
} // CreateOrUpdateTodolist | 
try {
    val result : Todolist = apiInstance.todolistPost(body)
    println(result)
} catch (e: ClientException) {
    println("4xx response calling TodolistApi#todolistPost")
    e.printStackTrace()
} catch (e: ServerException) {
    println("5xx response calling TodolistApi#todolistPost")
    e.printStackTrace()
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

<a name="todolistTodolistIdDelete"></a>
# **todolistTodolistIdDelete**
> InlineResponse200 todolistTodolistIdDelete(todolistId)

Delete existing todolist

Delete existing todolist in database

### Example
```kotlin
// Import classes:
//import io.swagger.client.infrastructure.*
//import io.swagger.client.models.*;

val apiInstance = TodolistApi()
val todolistId : kotlin.String = todolistId_example // kotlin.String | TodoList id for updated
try {
    val result : InlineResponse200 = apiInstance.todolistTodolistIdDelete(todolistId)
    println(result)
} catch (e: ClientException) {
    println("4xx response calling TodolistApi#todolistTodolistIdDelete")
    e.printStackTrace()
} catch (e: ServerException) {
    println("5xx response calling TodolistApi#todolistTodolistIdDelete")
    e.printStackTrace()
}
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **todolistId** | **kotlin.String**| TodoList id for updated |

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
```kotlin
// Import classes:
//import io.swagger.client.infrastructure.*
//import io.swagger.client.models.*;

val apiInstance = TodolistApi()
val body : CreateOrUpdateTodolist = {
  "description" : "Example Create todolist Java",
  "value" : {
    "name" : "Java",
    "priority" : 3,
    "tags" : [ "Java", "Programming" ]
  }
} // CreateOrUpdateTodolist | 
val todolistId : kotlin.String = todolistId_example // kotlin.String | TodoList id for updated
try {
    val result : Todolist = apiInstance.todolistTodolistIdPut(body, todolistId)
    println(result)
} catch (e: ClientException) {
    println("4xx response calling TodolistApi#todolistTodolistIdPut")
    e.printStackTrace()
} catch (e: ServerException) {
    println("5xx response calling TodolistApi#todolistTodolistIdPut")
    e.printStackTrace()
}
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**CreateOrUpdateTodolist**](CreateOrUpdateTodolist.md)|  |
 **todolistId** | **kotlin.String**| TodoList id for updated |

### Return type

[**Todolist**](Todolist.md)

### Authorization

[TodolistAuth](../README.md#TodolistAuth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

