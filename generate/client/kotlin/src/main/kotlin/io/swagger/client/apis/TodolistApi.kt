/**
 * TodoList RESTful API
 * OpenAPI for TodoList RESTful API
 *
 * OpenAPI spec version: 1
 * Contact: yogadimaspambudi@gmail.com
 *
 * NOTE: This class is auto generated by the swagger code generator program.
 * https://github.com/swagger-api/swagger-codegen.git
 * Do not edit the class manually.
 */
package io.swagger.client.apis

import io.swagger.client.models.ArrayTodolist
import io.swagger.client.models.CreateOrUpdateTodolist
import io.swagger.client.models.InlineResponse200
import io.swagger.client.models.Todolist

import io.swagger.client.infrastructure.*

class TodolistApi(basePath: kotlin.String = "https://{environment}.yogadimaspambudi.com/api/v1") : ApiClient(basePath) {

    /**
     * Get All Todolist
     * Get all active todolist by default
     * @param includeDone Is include_done todolist (optional, default to false)
     * @param name Filter todolist by name (optional)
     * @return ArrayTodolist
     */
    @Suppress("UNCHECKED_CAST")
    fun todolistGet(includeDone: kotlin.Boolean? = null, name: kotlin.String? = null): ArrayTodolist {
        val localVariableQuery: MultiValueMap = mutableMapOf<kotlin.String, kotlin.collections.List<kotlin.String>>().apply {
            if (includeDone != null) {
                put("include_done", listOf(includeDone.toString()))
            }
            if (name != null) {
                put("name", listOf(name.toString()))
            }
        }
        val localVariableConfig = RequestConfig(
                RequestMethod.GET,
                "/todolist", query = localVariableQuery
        )
        val response = request<ArrayTodolist>(
                localVariableConfig
        )

        return when (response.responseType) {
            ResponseType.Success -> (response as Success<*>).data as ArrayTodolist
            ResponseType.Informational -> TODO()
            ResponseType.Redirection -> TODO()
            ResponseType.ClientError -> throw ClientException((response as ClientError<*>).body as? String ?: "Client error")
            ResponseType.ServerError -> throw ServerException((response as ServerError<*>).message ?: "Server error")
        }
    }
    /**
     * Create new Todolist
     * Create new active todolist
     * @param body  
     * @return Todolist
     */
    @Suppress("UNCHECKED_CAST")
    fun todolistPost(body: CreateOrUpdateTodolist): Todolist {
        val localVariableBody: kotlin.Any? = body
        val localVariableConfig = RequestConfig(
                RequestMethod.POST,
                "/todolist"
        )
        val response = request<Todolist>(
                localVariableConfig, localVariableBody
        )

        return when (response.responseType) {
            ResponseType.Success -> (response as Success<*>).data as Todolist
            ResponseType.Informational -> TODO()
            ResponseType.Redirection -> TODO()
            ResponseType.ClientError -> throw ClientException((response as ClientError<*>).body as? String ?: "Client error")
            ResponseType.ServerError -> throw ServerException((response as ServerError<*>).message ?: "Server error")
        }
    }
    /**
     * Delete existing todolist
     * Delete existing todolist in database
     * @param todolistId TodoList id for updated 
     * @return InlineResponse200
     */
    @Suppress("UNCHECKED_CAST")
    fun todolistTodolistIdDelete(todolistId: kotlin.String): InlineResponse200 {
        val localVariableConfig = RequestConfig(
                RequestMethod.DELETE,
                "/todolist/{todolistId}".replace("{" + "todolistId" + "}", "$todolistId")
        )
        val response = request<InlineResponse200>(
                localVariableConfig
        )

        return when (response.responseType) {
            ResponseType.Success -> (response as Success<*>).data as InlineResponse200
            ResponseType.Informational -> TODO()
            ResponseType.Redirection -> TODO()
            ResponseType.ClientError -> throw ClientException((response as ClientError<*>).body as? String ?: "Client error")
            ResponseType.ServerError -> throw ServerException((response as ServerError<*>).message ?: "Server error")
        }
    }
    /**
     * Update existing todolist
     * Update existing todolist in database
     * @param body  
     * @param todolistId TodoList id for updated 
     * @return Todolist
     */
    @Suppress("UNCHECKED_CAST")
    fun todolistTodolistIdPut(body: CreateOrUpdateTodolist, todolistId: kotlin.String): Todolist {
        val localVariableBody: kotlin.Any? = body
        val localVariableConfig = RequestConfig(
                RequestMethod.PUT,
                "/todolist/{todolistId}".replace("{" + "todolistId" + "}", "$todolistId")
        )
        val response = request<Todolist>(
                localVariableConfig, localVariableBody
        )

        return when (response.responseType) {
            ResponseType.Success -> (response as Success<*>).data as Todolist
            ResponseType.Informational -> TODO()
            ResponseType.Redirection -> TODO()
            ResponseType.ClientError -> throw ClientException((response as ClientError<*>).body as? String ?: "Client error")
            ResponseType.ServerError -> throw ServerException((response as ServerError<*>).message ?: "Server error")
        }
    }
}
