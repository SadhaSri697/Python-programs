# match It is a ladder like a switch fuc we use in C language we use match in python
def http_status(status):
    match status:
        case 200:
            return "OK"
        case 404:
            return "not found"
        case 500:
            return "Internet error"
        case _:
            return "Unknown Status"

print(http_status(200))     
        