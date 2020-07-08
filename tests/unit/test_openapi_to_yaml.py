import os

import pytest

from scanapi.errors import EmptyOpenAPIFileError, InvalidOpenAPIFileError
from scanapi.openapi_to_yaml import openapi_to_yaml


class TestOpenAPIToYAML:
    class TestOpenAPIToYAMLFunction:
        class TestWhenProvidedWithCorrectFile:
            def test_should_create_api_yaml_file(self):
                openapi_to_yaml('../data/openapi.json')

                assert os.path.exists('./api.yaml')

                os.remove('./api.yaml')

        class TestWhenProvidedWithEmptyFile:
            def test_should_raise_empty_openapi_file_error(self):
                with pytest.raises(EmptyOpenAPIFileError) as exc_info:
                    openapi_to_yaml('../data/empty_openapi.json')

                assert exc_info.type == EmptyOpenAPIFileError
                assert str(exc_info.value) == "File '../data/empty_openapi.json' is empty."

        class TestWhenProvidedWithEmptyJson:
            def test_should_raise_empty_openapi_file_error(self):
                with pytest.raises(EmptyOpenAPIFileError) as exc_info:
                    openapi_to_yaml('../data/empty_json_openapi.json')

                assert exc_info.type == EmptyOpenAPIFileError
                assert str(exc_info.value) == "File '../data/empty_json_openapi.json' is empty."

        class TestWhenProvidedWithInvalidOpenAPIFile:
            def test_should_raise_invalid_openapi_file_error(self):
                with pytest.raises(InvalidOpenAPIFileError) as exc_info:
                    openapi_to_yaml('../data/invalid_openapi.json')

                assert exc_info.type == InvalidOpenAPIFileError
                assert str(
                    exc_info.value) == "File '../data/invalid_openapi.json' is not a valid OpenAPI JSON spec file."
