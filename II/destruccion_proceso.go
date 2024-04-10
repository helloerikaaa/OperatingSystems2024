package main

import (
	"fmt"
	"time"
)

func main() {
	fmt.Println("Iniciando tarea...")
	time.Sleep(5 * time.Second) // Suspender el proceso durante 5 segundos
	fmt.Println("Tarea completada.")
}
