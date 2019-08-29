package dojo

import (
	"fmt"
	"strings"
)

func main() bool {
	return true
}

func subdominio(url string) string {
	afterHTTP := strings.Split(url, "://")
	splittedAfterHTTP := strings.Split(afterHTTP[1], ".")
	if splittedAfterHTTP[0] == dominio(url) {
		return nil
	} else {
		return splittedAfterHTTP[0]
	}
}

func subd2(url string) string {
	afterHTTP := strings.Split(url, "://")
	splittedAfterHTTP := strings.Split(afterHTTP[1], ".")
	if splittedAfterHTTP[0] == dominio(url) {
		return "g1.qa"
	} else {
		return splittedAfterHTTP[0]
	}
}

func protocolo(link string) string {
	prot := strings.Split(link, ":")
	return prot[0]

}
func dominio(link string) string {
	dom := strings.Split(link, ".")
	if dom[2] == "com" {
		return fmt.Sprintf("%s.%s", dom[1], dom[2])
	} else {
		return fmt.Sprintf("%s.%s", dom[2], dom[3])
	}
}
