import pytest

def check_alert_status(is_active, cpu_percent, is_production):
    """Function wrapping the production logic for testability."""
    # The compound logical matching condition statement
    should_alert = (not is_active) or (cpu_percent > 90.0 and is_production is True)
    return should_alert

# Using parametrization to test multiple execution paths effectively
@pytest.mark.parametrize(
    "is_active, cpu_percent, is_production, expected_alert",
    [
        # Path 1: System is inactive -> Should alert regardless of CPU or Env
        (False, 50.0, True, True),
        (False, 95.0, False, True),
        
        # Path 2: Active, high CPU (>90), in production -> Should alert
        (True, 94.5, True, True),
        
        # Path 3: Active, high CPU (>90), but NOT in production -> Should NOT alert
        (True, 94.5, False, False),
        
        # Path 4: Active, safe CPU (<=90), in production -> Should NOT alert
        (True, 84.5, True, False),
        
        # Path 5: Boundary condition at exactly 90.0% CPU -> Should NOT alert
        (True, 90.0, True, False),
    ]
)
def test_check_alert_status(is_active, cpu_percent, is_production, expected_alert):
    # Act: Calculate the actual alert status based on inputs
    actual_alert = check_alert_status(is_active, cpu_percent, is_production)
    
    # Assert: Verify the result matches the expected execution path
    assert actual_alert == expected_alert
