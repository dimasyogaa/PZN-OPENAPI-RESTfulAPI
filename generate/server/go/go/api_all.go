/*
 * TodoList RESTful API
 *
 * OpenAPI for TodoList RESTful API
 *
 * API version: 1
 * Contact: yogadimaspambudi@gmail.com
 * Generated by: Swagger Codegen (https://github.com/swagger-api/swagger-codegen.git)
 */
package swagger

import (
	"net/http"
)

func TodolistGet(w http.ResponseWriter, r *http.Request) {
	w.Header().Set("Content-Type", "application/json; charset=UTF-8")
	w.WriteHeader(http.StatusOK)
}
