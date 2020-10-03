def getProtocol(url):
    ret = url.split("://")
    return ret[0]


def getDomain(url):
    ret = url.split("://")
    ret2 = ret[1].split("/")
    full_domain = ret2[0]
    sub_domain = getSubD(url)
    if sub_domain is None:
        return full_domain
    else:
        return full_domain.replace(sub_domain + ".", "")


def getSubD(url):
    ret = url.split("://")
    ret2 = ret[1].split(".")

    if len(ret2) == 3 and ret2[-1] == "br/algumacoisa":
        return None
    elif len(ret2) > 2:
        return ret2[0]

    else:
        return None

    # ret = url.split("://")
    # ret2 = ret[1].split(".")
    # ret3 = ret2[1].split("/")
    # return ret3[0]


def parserUrl(url):
    return {"protocol": getProtocol(url), "domain": getDomain(url)}


def main():

    return True
