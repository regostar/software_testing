import pytest
from app import app, WEAPONS

# Add any shared fixtures here that might be used across multiple test files

@pytest.fixture
def sample_weapons():
    """
    Return a copy of the weapons catalog for testing.
    
    This fixture provides a copy of the WEAPONS list so tests can modify it
    without affecting the original data. This helps maintain test isolation.
    
    Returns:
        list: A copy of the weapons catalog
    """
    return WEAPONS.copy()


@pytest.fixture
def weapon_ids():
    """
    Return a list of all weapon IDs.
    
    This fixture extracts just the IDs from the weapons catalog for tests
    that only need to work with the IDs rather than full weapon objects.
    
    Returns:
        list: List of integers representing all weapon IDs in the catalog
    """
    return [weapon["id"] for weapon in WEAPONS] 