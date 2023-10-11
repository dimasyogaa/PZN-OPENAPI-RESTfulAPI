package io.swagger.server.api.service;

import io.swagger.server.api.model.ArrayTodolist;
import io.swagger.server.api.model.CreateOrUpdateTodolist;
import io.swagger.server.api.model.InlineResponse200;
import io.swagger.server.api.model.Todolist;

import io.vertx.core.Handler;
import io.vertx.core.AsyncResult;
import io.vertx.ext.web.validation.RequestParameter;
import io.vertx.ext.web.api.service.ServiceRequest;
import io.vertx.ext.web.api.service.ServiceResponse;
import io.vertx.ext.web.api.service.WebApiServiceGen;

import java.util.List;
import java.util.Map;

@WebApiServiceGen
public interface TodolistApi  {

    String WEBSERVICE_ADDRESS_TODOLISTAPI = "";
    String OPERATION_ID_TODOLISTGET = "todolistGet";
    String OPERATION_ID_TODOLISTPOST = "todolistPost";
    String OPERATION_ID_TODOLISTTODOLISTIDDELETE = "todolistTodolistIdDelete";
    String OPERATION_ID_TODOLISTTODOLISTIDPUT = "todolistTodolistIdPut";

    void GETTodolist(RequestParameter body, ServiceRequest request, Handler<AsyncResult<ServiceResponse>> resultHandler);
    void POSTTodolist(RequestParameter body, ServiceRequest request, Handler<AsyncResult<ServiceResponse>> resultHandler);
    void DELETETodolistTodolistId(RequestParameter body, ServiceRequest request, Handler<AsyncResult<ServiceResponse>> resultHandler);
    void PUTTodolistTodolistId(RequestParameter body, ServiceRequest request, Handler<AsyncResult<ServiceResponse>> resultHandler);
}
