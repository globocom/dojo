package dojo

import "strings"

var knownDomains = []string{".com.br", ".net.br", ".com", ".br", ".net"}

func extractProtocol(input string) string {
	protocol := strings.Split(input, "://")
	return protocol[0]
}

func stripDomain(input string) string {
	for _, knownDomain := range knownDomains {
		if strings.HasSuffix(input, knownDomain) {
			return strings.Replace(input, knownDomain, "", 1)
		}
	}
	return input
}

func extractHost(input string) string {
	host := strings.Split(input, "://")
	host = strings.Split(host[1], ".")
	return host[0]
}
