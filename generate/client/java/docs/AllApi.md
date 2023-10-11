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
```java
// Import classes:
//import io.swagger.client.ApiClient;
//import io.swagger.client.ApiException;
//import io.swagger.client.Configuration;
//import io.swagger.client.auth.*;
//import io.swagger.client.api.AllApi;

ApiClient defaultClient = Configuration.getDefaultApiClient();

// Configure API key authorization: TodolistAuth
ApiKeyAuth TodolistAuth = (ApiKeyAuth) defaultClient.getAuthentication("TodolistAuth");
TodolistAuth.setApiKey("YOUR API KEY");
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//TodolistAuth.setApiKeyPrefix("Token");

AllApi apiInstance = new AllApi();
Boolean includeDone = false; // Boolean | Is include_done todolist
String name = "name_example"; // String | Filter todolist by name
try {
    ArrayTodolist result = apiInstance.todolistGet(includeDone, name);
    System.out.println(result);
} catch (ApiException e) {
    System.err.println("Exception when calling AllApi#todolistGet");
    e.printStackTrace();
}
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

