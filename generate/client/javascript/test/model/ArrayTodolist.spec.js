/*
 * TodoList RESTful API
 * OpenAPI for TodoList RESTful API
 *
 * OpenAPI spec version: 1
 * Contact: yogadimaspambudi@gmail.com
 *
 * NOTE: This class is auto generated by the swagger code generator program.
 * https://github.com/swagger-api/swagger-codegen.git
 *
 * Swagger Codegen version: 3.0.47
 *
 * Do not edit the class manually.
 *
 */
(function(root, factory) {
  if (typeof define === 'function' && define.amd) {
    // AMD.
    define(['expect.js', '../../src/index'], factory);
  } else if (typeof module === 'object' && module.exports) {
    // CommonJS-like environments that support module.exports, like Node.
    factory(require('expect.js'), require('../../src/index'));
  } else {
    // Browser globals (root is window)
    factory(root.expect, root.TodoListResTfulApi);
  }
}(this, function(expect, TodoListResTfulApi) {
  'use strict';

  var instance;

  describe('(package)', function() {
    describe('ArrayTodolist', function() {
      beforeEach(function() {
        instance = new TodoListResTfulApi.ArrayTodolist();
      });

      it('should create an instance of ArrayTodolist', function() {
        // TODO: update the code to test ArrayTodolist
        expect(instance).to.be.a(TodoListResTfulApi.ArrayTodolist);
      });

    });
  });

}));
