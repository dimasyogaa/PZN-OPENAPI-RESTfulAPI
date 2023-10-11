# AllApi

All URIs are relative to *https://{environment}.yogadimaspambudi.com/api/v1*

Method | HTTP request | Description
------------- | ------------- | -------------
[**todolistGet**](AllApi.md#todolistGet) | **GET** /todolist | Get All Todolist

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

val apiInstance = AllApi()
val includeDone : kotlin.Boolean = true // kotlin.Boolean | Is include_done todolist
val name : kotlin.String = name_example // kotlin.String | Filter todolist by name
try {
    val result : ArrayTodolist = apiInstance.todolistGet(includeDone, name)
    println(result)
} catch (e: ClientException) {
    println("4xx response calling AllApi#todolistGet")
    e.printStackTrace()
} catch (e: ServerException) {
    println("5xx response calling AllApi#todolistGet")
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

