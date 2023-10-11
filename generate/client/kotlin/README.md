# io.swagger.client - Kotlin client library for TodoList RESTful API

## Requires

* Kotlin 1.4.30
* Gradle 5.3

## Build

First, create the gradle wrapper script:

```
gradle wrapper
```

Then, run:

```
./gradlew check assemble
```

This runs all tests and packages the library.

## Features/Implementation Notes

* Supports JSON inputs/outputs, File inputs, and Form inputs.
* Supports collection formats for query parameters: csv, tsv, ssv, pipes.
* Some Kotlin and Java types are fully qualified to avoid conflicts with types defined in Swagger definitions.
* Implementation of ApiClient is intended to reduce method counts, specifically to benefit Android targets.

<a name="documentation-for-api-endpoints"></a>
## Documentation for API Endpoints

All URIs are relative to *https://{environment}.yogadimaspambudi.com/api/v1*

Class | Method | HTTP request | Description
------------ | ------------- | ------------- | -------------
*AllApi* | [**todolistGet**](docs/AllApi.md#todolistget) | **GET** /todolist | Get All Todolist
*TodolistApi* | [**todolistGet**](docs/TodolistApi.md#todolistget) | **GET** /todolist | Get All Todolist
*TodolistApi* | [**todolistPost**](docs/TodolistApi.md#todolistpost) | **POST** /todolist | Create new Todolist
*TodolistApi* | [**todolistTodolistIdDelete**](docs/TodolistApi.md#todolisttodolistiddelete) | **DELETE** /todolist/{todolistId} | Delete existing todolist
*TodolistApi* | [**todolistTodolistIdPut**](docs/TodolistApi.md#todolisttodolistidput) | **PUT** /todolist/{todolistId} | Update existing todolist

<a name="documentation-for-models"></a>
## Documentation for Models

 - [io.swagger.client.models.ArrayTodolist](docs/ArrayTodolist.md)
 - [io.swagger.client.models.CreateOrUpdateTodolist](docs/CreateOrUpdateTodolist.md)
 - [io.swagger.client.models.InlineResponse200](docs/InlineResponse200.md)
 - [io.swagger.client.models.Todolist](docs/Todolist.md)

<a name="documentation-for-authorization"></a>
## Documentation for Authorization

<a name="TodolistAuth"></a>
### TodolistAuth


