from jwtfuzzer.decoder import decode_jwt
from jwtfuzzer.encoder import encode_jwt


def header_typ_empty(jwt_string):
    """
    If the header looks like:
        {
            "alg": "HS256",
            "typ": "JWT"
        }

    The result will look like:
        {
          "alg": "HS256",
          "typ": ""
        }

    :param jwt_string: The JWT as a string
    :return: The fuzzed JWT
    """
    header, payload, signature = decode_jwt(jwt_string)
    header['typ'] = ''
    return encode_jwt(header, payload, signature)


def header_typ_remove(jwt_string):
    """
    If the header looks like:
        {
            "alg": "HS256",
            "typ": "JWT"
        }

    The result will look like:
        {
          "alg": "HS256",
        }

    :param jwt_string: The JWT as a string
    :return: The fuzzed JWT
    """
    header, payload, signature = decode_jwt(jwt_string)
    del header['typ']
    return encode_jwt(header, payload, signature)


def header_typ_null(jwt_string):
    """
    If the header looks like:
        {
            "alg": "HS256",
            "typ": "JWT"
        }

    The result will look like:
        {
          "alg": "HS256",
          "typ": null
        }

    :param jwt_string: The JWT as a string
    :return: The fuzzed JWT
    """
    header, payload, signature = decode_jwt(jwt_string)
    header['typ'] = None
    return encode_jwt(header, payload, signature)


def header_typ_invalid(jwt_string):
    """
    If the header looks like:
        {
            "alg": "HS256",
            "typ": "JWT"
        }

    The result will look like:
        {
          "alg": "HS256",
          "typ": "invalid"
        }

    :param jwt_string: The JWT as a string
    :return: The fuzzed JWT
    """
    header, payload, signature = decode_jwt(jwt_string)
    header['typ'] = "invalid"
    return encode_jwt(header, payload, signature)


def header_typ_none(jwt_string):
    """
    If the header looks like:
        {
            "alg": "HS256",
            "typ": "JWT"
        }

    The result will look like:
        {
          "typ": "none"
          "alg": "HS256",
        }

    :param jwt_string: The JWT as a string
    :return: The fuzzed JWT
    """
    header, payload, signature = decode_jwt(jwt_string)
    header['typ'] = 'none'
    return encode_jwt(header, payload, signature)