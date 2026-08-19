import logging
import sys
from unittest.mock import MagicMock, patch

from awsume.awsumepy import app, main
from awsume.awsumepy.lib.logger import logger


@patch.object(app.Awsume, "run")
def test_app_ran(run: MagicMock):
    main.main()
    run.assert_called()


@patch.object(sys, "argv", ["--debug"])
@patch.object(logger, "setLevel")
@patch.object(app.Awsume, "run")
def test_debug_flag(run: MagicMock, set_level: MagicMock):
    main.main()
    set_level.assert_called_with(logging.DEBUG)


@patch.object(sys, "argv", ["--info"])
@patch.object(logger, "setLevel")
@patch.object(app.Awsume, "run")
def test_info_flag(run: MagicMock, set_level: MagicMock):
    main.main()
    set_level.assert_called_with(logging.INFO)
    assert True
