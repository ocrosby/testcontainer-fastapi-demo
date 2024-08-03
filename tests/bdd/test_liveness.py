"""
This module contains the end to end tests for the liveness feature.
"""

import pytest

from pytest_bdd import scenario


@pytest.mark.e2e
@pytest.mark.kubernetes
@pytest.mark.liveness
@pytest.mark.probe
@scenario('../../features/liveness.feature', 'Running')
def test_liveness():
    """
    This function represents the scenario 'Running'.

    :return:
    """


@pytest.mark.e2e
@pytest.mark.kubernetes
@pytest.mark.liveness
@pytest.mark.probe
@scenario('../../features/liveness.feature', 'Not Running')
def test_not_running():
    """
    This function represents the scenario 'Not Running'.

    :return:
    """


@pytest.mark.e2e
@pytest.mark.kubernetes
@pytest.mark.liveness
@pytest.mark.probe
@scenario('../../features/liveness.feature', 'Degraded State')
def test_degraded_state():
    """
    This function represents the scenario 'Degraded State'.

    :return:
    """


@pytest.mark.e2e
@pytest.mark.kubernetes
@pytest.mark.liveness
@pytest.mark.probe
@scenario('../../features/liveness.feature', 'Heavy Load')
def test_heavy_load():
    """
    This function represents the scenario 'Heavy Load'.

    :return:
    """