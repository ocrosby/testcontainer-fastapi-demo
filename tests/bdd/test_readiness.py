import pytest

from pytest_bdd import scenario


@pytest.mark.e2e
@pytest.mark.kubernetes
@pytest.mark.readiness
@scenario('../../features/readiness.feature', 'Running')
def running():
    """
    This function represents the scenario 'Running'.

    :return:
    """
    raise NotImplementedError("The scenario 'Running' has not been implemented")
