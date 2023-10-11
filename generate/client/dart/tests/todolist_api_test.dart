import 'package:swagger/api.dart';
import 'package:test/test.dart';


/// tests for TodolistApi
void main() {
  var instance = new TodolistApi();

  group('tests for TodolistApi', () {
    // Get All Todolist
    //
    // Get all active todolist by default
    //
    //Future<ArrayTodolist> todolistGet({ bool includeDone, String name }) async
    test('test todolistGet', () async {
      // TODO
    });

    // Create new Todolist
    //
    // Create new active todolist
    //
    //Future<Todolist> todolistPost(CreateOrUpdateTodolist body) async
    test('test todolistPost', () async {
      // TODO
    });

    // Delete existing todolist
    //
    // Delete existing todolist in database
    //
    //Future<InlineResponse200> todolistTodolistIdDelete(String todolistId) async
    test('test todolistTodolistIdDelete', () async {
      // TODO
    });

    // Update existing todolist
    //
    // Update existing todolist in database
    //
    //Future<Todolist> todolistTodolistIdPut(CreateOrUpdateTodolist body, String todolistId) async
    test('test todolistTodolistIdPut', () async {
      // TODO
    });

  });
}
