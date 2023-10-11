# swagger-java-client

TodoList RESTful API
- API version: 1
  - Build date: 2023-10-11T18:42:59.438953605Z[GMT]

OpenAPI for TodoList RESTful API

  For more information, please visit [https://github.com/Yogadimas](https://github.com/Yogadimas)

*Automatically generated by the [Swagger Codegen](https://github.com/swagger-api/swagger-codegen)*


## Requirements

Building the API client library requires:
1. Java 1.7+
2. Maven/Gradle

## Installation

To install the API client library to your local Maven repository, simply execute:

```shell
mvn clean install
```

To deploy it to a remote Maven repository instead, configure the settings of the repository and execute:

```shell
mvn clean deploy
```

Refer to the [OSSRH Guide](http://central.sonatype.org/pages/ossrh-guide.html) for more information.

### Maven users

Add this dependency to your project's POM:

```xml
<dependency>
  <groupId>io.swagger</groupId>
  <artifactId>swagger-java-client</artifactId>
  <version>1.0.0</version>
  <scope>compile</scope>
</dependency>
```

### Gradle users

Add this dependency to your project's build file:

```groovy
compile "io.swagger:swagger-java-client:1.0.0"
```

### Others

At first generate the JAR by executing:

```shell
mvn clean package
```

Then manually install the following JARs:

* `target/swagger-java-client-1.0.0.jar`
* `target/lib/*.jar`

## Getting Started

Please follow the [installation](#installation) instruction and execute the following Java code:

```java
import io.swagger.client.*;
import io.swagger.client.auth.*;
import io.swagger.client.model.*;
import io.swagger.client.api.AllApi;

import java.io.File;
import java.util.*;

public class AllApiExample {

    public static void main(String[] args) {
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
    }
}
```

## Documentation for API Endpoints

All URIs are relative to *https://{environment}.yogadimaspambudi.com/api/v1*

Class | Method | HTTP request | Description
------------ | ------------- | ------------- | -------------
*AllApi* | [**todolistGet**](docs/AllApi.md#todolistGet) | **GET** /todolist | Get All Todolist
*TodolistApi* | [**todolistGet**](docs/TodolistApi.md#todolistGet) | **GET** /todolist | Get All Todolist
*TodolistApi* | [**todolistPost**](docs/TodolistApi.md#todolistPost) | **POST** /todolist | Create new Todolist
*TodolistApi* | [**todolistTodolistIdDelete**](docs/TodolistApi.md#todolistTodolistIdDelete) | **DELETE** /todolist/{todolistId} | Delete existing todolist
*TodolistApi* | [**todolistTodolistIdPut**](docs/TodolistApi.md#todolistTodolistIdPut) | **PUT** /todolist/{todolistId} | Update existing todolist

## Documentation for Models

 - [ArrayTodolist](docs/ArrayTodolist.md)
 - [CreateOrUpdateTodolist](docs/CreateOrUpdateTodolist.md)
 - [InlineResponse200](docs/InlineResponse200.md)
 - [Todolist](docs/Todolist.md)

## Documentation for Authorization

Authentication schemes defined for the API:
### TodolistAuth

- **Type**: API key
- **API key parameter name**: X-API-Key
- **Location**: HTTP header


## Recommendation

It's recommended to create an instance of `ApiClient` per thread in a multithreaded environment to avoid any potential issues.

## Author

yogadimaspambudi@gmail.com