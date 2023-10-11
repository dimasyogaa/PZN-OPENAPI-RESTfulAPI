part of swagger.api;

class CreateOrUpdateTodolist {
  
  String name = null;

  double priority = null;

  List<String> tags = [];

  CreateOrUpdateTodolist();

  @override
  String toString() {
    return 'CreateOrUpdateTodolist[name=$name, priority=$priority, tags=$tags, ]';
  }

  CreateOrUpdateTodolist.fromJson(Map<String, dynamic> json) {
    if (json == null) return;
    name = json['name'];
    priority = json['priority'];
    tags = (json['tags'] as List).map((item) => item as String).toList();
  }

  Map<String, dynamic> toJson() {
    return {
      'name': name,
      'priority': priority,
      'tags': tags
     };
  }

  static List<CreateOrUpdateTodolist> listFromJson(List<dynamic> json) {
    return json == null ? new List<CreateOrUpdateTodolist>() : json.map((value) => new CreateOrUpdateTodolist.fromJson(value)).toList();
  }

  static Map<String, CreateOrUpdateTodolist> mapFromJson(Map<String, Map<String, dynamic>> json) {
    var map = new Map<String, CreateOrUpdateTodolist>();
    if (json != null && json.length > 0) {
      json.forEach((String key, Map<String, dynamic> value) => map[key] = new CreateOrUpdateTodolist.fromJson(value));
    }
    return map;
  }
}
