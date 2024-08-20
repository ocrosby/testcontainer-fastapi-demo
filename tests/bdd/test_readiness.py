import pytest

from pytest_bdd import scenario

from tests.bdd.step_definitions.common_steps import *


@pytest.mark.e2e
@pytest.mark.kubernetes
@pytest.mark.readiness
@scenario('../../features/readiness.feature', 'Running')
def test_readiness(postgres_container):
    """
    This function represents the scenario 'Running'.

    :return:
    """
