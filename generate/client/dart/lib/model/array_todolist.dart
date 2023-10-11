part of swagger.api;

class ArrayTodolist {
  
  ArrayTodolist();

  @override
  String toString() {
    return 'ArrayTodolist[]';
  }

  ArrayTodolist.fromJson(Map<String, dynamic> json) {
    if (json == null) return;
  }

  Map<String, dynamic> toJson() {
    return {
     };
  }

  static List<ArrayTodolist> listFromJson(List<dynamic> json) {
    return json == null ? new List<ArrayTodolist>() : json.map((value) => new ArrayTodolist.fromJson(value)).toList();
  }

  static Map<String, ArrayTodolist> mapFromJson(Map<String, Map<String, dynamic>> json) {
    var map = new Map<String, ArrayTodolist>();
    if (json != null && json.length > 0) {
      json.forEach((String key, Map<String, dynamic> value) => map[key] = new ArrayTodolist.fromJson(value));
    }
    return map;
  }
}
