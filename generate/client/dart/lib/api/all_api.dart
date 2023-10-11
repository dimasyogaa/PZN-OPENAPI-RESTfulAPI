part of swagger.api;



class AllApi {
  final ApiClient apiClient;

  AllApi([ApiClient apiClient]) : apiClient = apiClient ?? defaultApiClient;

  /// Get All Todolist
  ///
  /// Get all active todolist by default
  Future<ArrayTodolist> todolistGet({ bool includeDone, String name }) async {
    Object postBody = null;

    // verify required params are set

    // create path and map variables
    String path = "/todolist".replaceAll("{format}","json");

    // query params
    List<QueryParam> queryParams = [];
    Map<String, String> headerParams = {};
    Map<String, String> formParams = {};
    if(includeDone != null) {
      queryParams.addAll(_convertParametersForCollectionFormat("", "include_done", includeDone));
    }
    if(name != null) {
      queryParams.addAll(_convertParametersForCollectionFormat("", "name", name));
    }
    
    List<String> contentTypes = [];

    String contentType = contentTypes.length > 0 ? contentTypes[0] : "application/json";
    List<String> authNames = ["TodolistAuth"];

    if(contentType.startsWith("multipart/form-data")) {
      bool hasFields = false;
      MultipartRequest mp = new MultipartRequest(null, null);
      if(hasFields)
        postBody = mp;
    }
    else {
          }

    var response = await apiClient.invokeAPI(path,
                                             'GET',
                                             queryParams,
                                             postBody,
                                             headerParams,
                                             formParams,
                                             contentType,
                                             authNames);

    if(response.statusCode >= 400) {
      throw new ApiException(response.statusCode, response.body);
    } else if(response.body != null) {
      return
          apiClient.deserialize(response.body, 'ArrayTodolist') as ArrayTodolist ;
    } else {
      return null;
    }
  }
}
