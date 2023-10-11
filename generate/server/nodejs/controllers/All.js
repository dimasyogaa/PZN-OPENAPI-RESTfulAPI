'use strict';

var utils = require('../utils/writer.js');
var All = require('../service/AllService');

module.exports.todolistGET = function todolistGET (req, res, next, include_done, name) {
  All.todolistGET(include_done, name)
    .then(function (response) {
      utils.writeJson(res, response);
    })
    .catch(function (response) {
      utils.writeJson(res, response);
    });
};
