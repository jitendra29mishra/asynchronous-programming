package main

import (
	"net/http"
	"time"
)

type HttpHandler struct{}

func (h HttpHandler) ServeHTTP(res http.ResponseWriter, req *http.Request) {
	data := []byte("Hello World!")
	time.Sleep(time.Second)
	res.Write(data)
}

func main() {
	handler := HttpHandler{}

	http.ListenAndServe(":8000", handler)
}
