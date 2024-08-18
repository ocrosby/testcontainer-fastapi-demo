import pytest

from pytest_bdd import scenario


@pytest.mark.e2e
@pytest.mark.kubernetes
@pytest.mark.startup
@scenario('../../features/startup.feature', 'Check the startup of the application')
def running():
    """
    This function represents the scenario 'Running'.

    :return:
    """
    raise NotImplementedError("The scenario 'Running' has not been implemented")
