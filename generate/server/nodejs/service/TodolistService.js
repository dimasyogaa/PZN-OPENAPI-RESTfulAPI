'use strict';


/**
 * Get All Todolist
 * Get all active todolist by default
 *
 * include_done Boolean Is include_done todolist (optional)
 * name String Filter todolist by name (optional)
 * returns ArrayTodolist
 **/
exports.todolistGET = function(include_done,name) {
  return new Promise(function(resolve, reject) {
    var examples = {};
    examples['application/json'] = [ {
  "name" : "name",
  "id" : "id",
  "priority" : 0.8008281904610115,
  "tags" : [ "tags", "tags" ]
}, {
  "name" : "name",
  "id" : "id",
  "priority" : 0.8008281904610115,
  "tags" : [ "tags", "tags" ]
} ];
    if (Object.keys(examples).length > 0) {
      resolve(examples[Object.keys(examples)[0]]);
    } else {
      resolve();
    }
  });
}


/**
 * Create new Todolist
 * Create new active todolist
 *
 * body CreateOrUpdateTodolist 
 * returns Todolist
 **/
exports.todolistPOST = function(body) {
  return new Promise(function(resolve, reject) {
    var examples = {};
    examples['application/json'] = {
  "name" : "name",
  "id" : "id",
  "priority" : 0.8008281904610115,
  "tags" : [ "tags", "tags" ]
};
    if (Object.keys(examples).length > 0) {
      resolve(examples[Object.keys(examples)[0]]);
    } else {
      resolve();
    }
  });
}


/**
 * Delete existing todolist
 * Delete existing todolist in database
 *
 * todolistId String TodoList id for updated
 * returns inline_response_200
 **/
exports.todolistTodolistIdDELETE = function(todolistId) {
  return new Promise(function(resolve, reject) {
    var examples = {};
    examples['application/json'] = {
  "success" : true
};
    if (Object.keys(examples).length > 0) {
      resolve(examples[Object.keys(examples)[0]]);
    } else {
      resolve();
    }
  });
}


/**
 * Update existing todolist
 * Update existing todolist in database
 *
 * body CreateOrUpdateTodolist 
 * todolistId String TodoList id for updated
 * returns Todolist
 **/
exports.todolistTodolistIdPUT = function(body,todolistId) {
  return new Promise(function(resolve, reject) {
    var examples = {};
    examples['application/json'] = {
  "name" : "name",
  "id" : "id",
  "priority" : 0.8008281904610115,
  "tags" : [ "tags", "tags" ]
};
    if (Object.keys(examples).length > 0) {
      resolve(examples[Object.keys(examples)[0]]);
    } else {
      resolve();
    }
  });
}

