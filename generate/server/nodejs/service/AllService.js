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

