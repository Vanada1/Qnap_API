import js2py

_js_file_path = "get_sid.js"


def utf16to8(value_string: str) -> str:
    eval_res, tempfile = js2py.run_file("get_sid.js")
    return tempfile.utf16to8(value_string)


def utf8to16(value_string: str) -> str:
    eval_res, tempfile = js2py.run_file("get_sid.js")
    return tempfile.utf8to16(value_string)


def ezEncode(value_string: str) -> str:
    eval_res, tempfile = js2py.run_file("get_sid.js")
    return tempfile.ezEncode(value_string)
