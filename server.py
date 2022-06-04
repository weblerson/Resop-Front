def register(amb, start_response):
    with open("register.html", "rb") as file:
        body = file.read()
        status = "200 OK"
        response_headers = [("Content-type", "text/html")]
        start_response(status, response_headers)
        return [body]

def login(amb, start_response):
    with open("login.html", "rb") as file:
        body = file.read()
        status = "200 OK"
        response_headers = [("Content-type", "text/html")]
        start_response(status, response_headers)
        return [body]