def main():
    N = input()
    sizeInShop = input().split(" ")
    M = input()
    sizeReq = input().split(" ")
    temp = list(sizeReq)
    if M > N:
        return "No"
    
    for req in sizeReq:
        if req not in sizeInShop:
            if "S" in req:
                for item in sizeInShop: 
                    if item.count('X') > req.count('X'):
                        temp.remove(req)
                        break
            elif "L" in req:
                 for item in sizeInShop: 
                    if item.count('X') > req.count('X'):
                        temp.remove(req)
                        break
        else:
            temp.remove(req)
    if len(temp) != 0:
        return "No"
    
    return "Yes"

print(main())
