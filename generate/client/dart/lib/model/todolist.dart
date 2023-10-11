part of swagger.api;

class Todolist {
  
  String id = null;

  String name = null;

  double priority = null;

  List<String> tags = [];

  Todolist();

  @override
  String toString() {
    return 'Todolist[id=$id, name=$name, priority=$priority, tags=$tags, ]';
  }

  Todolist.fromJson(Map<String, dynamic> json) {
    if (json == null) return;
    id = json['id'];
    name = json['name'];
    priority = json['priority'];
    tags = (json['tags'] as List).map((item) => item as String).toList();
  }

  Map<String, dynamic> toJson() {
    return {
      'id': id,
      'name': name,
      'priority': priority,
      'tags': tags
     };
  }

  static List<Todolist> listFromJson(List<dynamic> json) {
    return json == null ? new List<Todolist>() : json.map((value) => new Todolist.fromJson(value)).toList();
  }

  static Map<String, Todolist> mapFromJson(Map<String, Map<String, dynamic>> json) {
    var map = new Map<String, Todolist>();
    if (json != null && json.length > 0) {
      json.forEach((String key, Map<String, dynamic> value) => map[key] = new Todolist.fromJson(value));
    }
    return map;
  }
}
