# -*- coding: utf-8 -*-
"""
Pytest sequencer tests conftest
"""
import pytest


@pytest.fixture(scope="session")
def executed_tests(request, test_config_parser, logger):
    """
    Analyze executed tests
    """
    executed_tests = []

    def analyze_result():
        """
        Analyze list
        """
        required_list = []
        required_list = [int(x) for x in test_config_parser.get(
            "Result", "executed_tests").split(",")]
        test_name = test_config_parser.get("Result", "test_name")
        fail_message = test_name + " failed"
        logger.info(test_name)
        logger.info("Executed tests = " + str(executed_tests))
        logger.info("Required test = " + str(required_list))
        assert executed_tests == required_list, fail_message

    request.addfinalizer(analyze_result)
    return executed_tests


@pytest.fixture(scope="function")
def test_result(test_info):
    """
    Test result
    """
    if "result" not in test_info.keys():
        return True
    elif test_info["result"].lower() == "pass":
        return True
    elif test_info["result"].lower() == "fail":
        return False
    else:
        error = "Bad parameter in test config file"
        pytest.fail(error)