"""
This module contains the Pytest configuration.
"""

import os

from dotenv import load_dotenv

from app.core.logging import logger
from app.core.reporting import beautify_junit_xml
from app.utils.filesystem import find_root_dir

# Pytest Hooks


def pytest_configure(config):
    """
    Configure Pytest

    :param config: Pytest configuration
    """
    root_dir = find_root_dir(__file__)
    os.environ["ROOT_DIR"] = root_dir
    env_path = os.path.join(root_dir, ".env")

    load_dotenv(dotenv_path=env_path)  # Load environment variables from .env file


def pytest_sessionfinish(session, exitstatus):
    """
    Finish Pytest session

    :param session: Pytest session
    :param exitstatus: Exit status
    """
    logger.info("Test suite finished", extra={"event": "shutdown", "status": "success"})
    logger.info("Shutting down Pytest")

    junit_xml_path = session.config.option.xmlpath
    if junit_xml_path is None:
        logger.warning("Junit XML path not provided", extra={"event": "junit_xml", "status": "warning"})
        return

    if not os.path.exists(junit_xml_path):
        logger.warning(f"Junit XML not found '{junit_xml_path}'", extra={"event": "junit_xml", "status": "warning"})
        return

    logger.info(f"Beautifying Junit XML '{junit_xml_path}'", extra={"event": "junit_xml"})
    with open(junit_xml_path, "r", encoding="utf-8") as file:
        xml_content = file.read()

    beautified_xml = beautify_junit_xml(xml_content, indent=4)

    with open(junit_xml_path, "w", encoding="utf-8") as file:
        file.write(beautified_xml)


# Pytest-BDD Hooks


def pytest_bdd_before_scenario(request, feature, scenario):
    """
    Before scenario hook

    :param request: Pytest request
    :param feature: Feature
    :param scenario: Scenario
    """
    logger.info(
        "Scenario started",
        extra={
            "event": "scenario_started",
            "feature": feature.name,
            "scenario": scenario.name,
        },
    )


def pytest_bdd_after_scenario(request, feature, scenario):
    """
    After scenario hook

    :param request: Pytest request
    :param feature: Feature
    :param scenario: Scenario
    """
    logger.info(
        "Scenario finished",
        extra={
            "event": "scenario_finished",
            "feature": feature.name,
            "scenario": scenario.name,
        },
    )


def pytest_bdd_step_error(
        request,
        feature,
        scenario,
        step,
        step_func,
        step_func_args,
        exception
):
    """
    Handle step error

    :param request: Pytest request
    :param feature: Feature
    :param scenario: Scenario
    :param step: Step
    :param step_func: Step function
    :param step_func_args: Step function arguments
    :param exception: Exception
    """
    logger.error(
        "Step error",
        extra={
            "event": "step_error",
            "feature": feature.name,
            "scenario": scenario.name,
            "step": step.name,
            "exception": exception,
        },
    )


def pytest_bdd_before_step(request, feature, scenario, step, step_func):
    """
    Before step hook

    :param request: Pytest request
    :param feature: Feature
    :param scenario: Scenario
    :param step: Step
    :param step_func: Step function
    """
    # logger.info(
    #     "Step started",
    #     extra={
    #         "event": "step_started",
    #         "feature": feature.name,
    #         "scenario": scenario.name,
    #         "step": step.name,
    #     },
    # )


def pytest_bdd_after_step(request, feature, scenario, step, step_func):
    """
    After step hook

    :param request: Pytest request
    :param feature: Feature
    :param scenario: Scenario
    :param step: Step
    :param step_func: Step function
    """
    # logger.info(
    #     "Step finished",
    #     extra={
    #         "event": "step_finished",
    #         "feature": feature.name,
    #         "scenario": scenario.name,
    #         "step": step.name,
    #     },
    # )


def pytest_bdd_step_func_lookup_error(request, feature, scenario, step, exception):
    """
    Handle step function lookup error

    :param request: Pytest request
    :param feature: Feature
    :param scenario: Scenario
    :param step: Step
    :param exception: Exception
    """
    logger.error(
        "Step function lookup error",
        extra={
            "event": "step_func_lookup_error",
            "feature": feature.name,
            "scenario": scenario.name,
            "step": step.name,
            "exception": exception,
        },
    )
