"""
This module contains the end to end tests for the liveness feature.
"""
import pytest

from pytest_bdd import scenario

from tests.bdd.fixtures.testcontainers import api_container
from tests.bdd.step_definitions.common_steps import *


@pytest.mark.e2e
@pytest.mark.kubernetes
@pytest.mark.liveness
@scenario('../../features/liveness.feature', 'Running')
def test_liveness(api_container):
    """
    This function represents the scenario 'Running'.

    :return:
    """
