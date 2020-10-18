"""Acceptance tests of ballot status."""
import track_ma_ballot


def test_status_is_accepted(page):
    """Fail until the ballot has been accepted."""
    details = track_ma_ballot.get_details(page, track_ma_ballot.INPUTS)
    assert details.status == "Accepted", details
