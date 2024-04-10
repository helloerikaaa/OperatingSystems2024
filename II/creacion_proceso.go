package main

import (
	"fmt"
	"os/exec"
)

func main() {
	cmd := exec.Command("ls", "-l")
	err := cmd.Run()
	if err != nil {
		fmt.Println("Error al ejecutar el comando:", err)
	}
}
