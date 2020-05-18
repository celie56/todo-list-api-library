"""Ensure that we can call the service via CLI."""
from click.testing import CliRunner
import cli


def test_list_service() -> None:
    """Test list service."""
    runner = CliRunner()
    result = runner.invoke(cli.create_list, ['groceries'])
    assert result.exit_code == 0

    result = runner.invoke(cli.get_lists, [])
    assert result.exit_code == 0
    assert 'groceries' in result.output
