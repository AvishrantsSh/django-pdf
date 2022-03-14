def test_decorator(function):
    def handler(*args, **kwargs):
        response = function(*args, **kwargs)
        response["Content-Type"] = "application/pdf"
        # response["Content-Disposition"] = "attachment; filename=test.pdf"
        return response

    return handler
