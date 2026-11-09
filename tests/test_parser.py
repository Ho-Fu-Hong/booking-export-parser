import json


def test_fixture_loads():
    with open("tests/fixtures/export_config.json") as handle:
        assert json.load(handle)["export_host"] == "localhost"
