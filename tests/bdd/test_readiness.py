import pytest

from pytest_bdd import scenario


@pytest.mark.e2e
@pytest.mark.kubernetes
@pytest.mark.readiness
@pytest.mark.probe
@scenario('../../features/readiness.feature', 'Running')
def running():
    """
    This function represents the scenario 'Running'.

    :return:
    """
    raise NotImplementedError("The scenario 'Running' has not been implemented")


@pytest.mark.e2e
@pytest.mark.kubernetes
@pytest.mark.readiness
@pytest.mark.probe
@scenario('../../features/readiness.feature', 'Not Running')
def not_running():
    """
    This function represents the scenario 'Not Running'.

    :return:
    """
    raise NotImplementedError("The scenario 'Not Running' has not been implemented")


@pytest.mark.e2e
@pytest.mark.kubernetes
@pytest.mark.readiness
@pytest.mark.probe
@scenario('../../features/readiness.feature', 'Degraded State')
def degraded_state():
    """
    This function represents the scenario 'Degraded State'.

    :return:
    """
    raise NotImplementedError("The scenario 'Degraded State' has not been implemented")


@pytest.mark.e2e
@pytest.mark.kubernetes
@pytest.mark.readiness
@pytest.mark.probe
@scenario('../../features/readiness.feature', 'Heavy Load')
def heavy_load():
    """
    This function represents the scenario 'Heavy Load'.

    :return:
    """
    raise NotImplementedError("The scenario 'Heavy Load' has not been implemented")


@pytest.mark.e2e
@pytest.mark.kubernetes
@pytest.mark.readiness
@pytest.mark.probe
@scenario('../../features/readiness.feature', 'Database Available')
def database_available():
    """
    This function represents the scenario 'Database Available'.

    :return:
    """
    raise NotImplementedError("The scenario 'Database Available' has not been implemented")


@pytest.mark.e2e
@pytest.mark.kubernetes
@pytest.mark.readiness
@pytest.mark.probe
@scenario('../../features/readiness.feature', 'Database Not Available')
def database_not_available():
    """
    This function represents the scenario 'Database Not Available'.

    :return:
    """
    raise NotImplementedError("The scenario 'Database Not Available' has not been implemented")


@pytest.mark.e2e
@pytest.mark.kubernetes
@pytest.mark.readiness
@pytest.mark.probe
@scenario('../../features/readiness.feature', 'Database Degraded State')
def database_degraded_state():
    """
    This function represents the scenario 'Database Degraded State'.

    :return:
    """
    raise NotImplementedError("The scenario 'Database Degraded State' has not been implemented")
