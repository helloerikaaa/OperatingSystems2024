// paquete main
package main

// Librerías
import (
	"fmt"       // Imprimir
	"os"        // Interactuar con el OS
	"os/signal" // Señales del OS
	"syscall"   // Llamdas al OS
)

func main() {
	// Crear el canal para manejar la señal
	// (Interrupción con Ctrl + C)
	sigint := make(chan os.Signal, 1)
	// Notificacion para cuando se utilice
	// el Ctrl + C
	signal.Notify(sigint, syscall.SIGINT)

	// Rutina para manejar la interrupción
	go func() {
		<-sigint // Esperando a que llegue algo al canal
		fmt.Println("Interrupción del usuario recibida")
		os.Exit(1) // Salir del programa
	}()
	// Ejecución de la tarea
	fmt.Println("Esperando una interrupción")
	fmt.Println("Presiona Ctrl + C para interrumpir")

	// Simulación de tarea infinita
	for {
		fmt.Println("Estoy haciendo una tarea")
	}
}
