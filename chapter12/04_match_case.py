def htttp_status(status):
    match status:
        case 200:
            return "ok"
        case 404:
            return "None"
        case 500:
            return "Internal Server Error"
        case _:
            return "Unknown status"

print(htttp_status(500))