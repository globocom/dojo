def get_tag(tag, body):
    arr = []
    tmp_body = body
    while True:
        idx = tmp_body.find("<"+tag)

        if -1 == idx:
            return arr
        
        id_end = tmp_body.find(">")
        arr.append(tmp_body[idx:id_end+1])
        tmp_body = tmp_body[id_end+1:]


    
    
    


