def get_cookies(scope):
    for header_name, header_value in scope["headers"]:
        if header_name == b'cookie':
            cookie_string = header_value.decode()
            cookies = {}
            for pair in cookie_string.split(";"):
                if "=" in pair:
                    key, value = pair.strip().split("=", 1)
                    cookies[key] = value
            return cookies
    return {}