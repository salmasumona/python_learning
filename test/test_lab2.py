import pytest
# Import the function and the default configuration from your module
from lab2_ClusterAudit import calculate_capacity, cluster_config

# Test the function execution using the standard configuration
def test_calculate_capacity_output(capsys):
    # Execute the function with the default config dictionary
    calculate_capacity(cluster_config)
    
    # Capture everything printed to the console (stdout)
    captured = capsys.readouterr()
    
    # Verify that the correct cluster metadata is printed
    assert "Cluster name: dhaka-prod-east" in captured.out
    assert "Cluster max slots: 8" in captured.out
    assert "Total active nodes: 5" in captured.out
    
    # Verify that the mathematical calculation matches (5 / 8) * 100 = 62.5%
    assert "Cluster utilization percentage: 62.5%" in captured.out

# Test verification with a modified global configuration dictionary
def test_calculate_capacity_values(capsys):
    # Clear any previous console output buffer before starting
    capsys.readouterr()
    
    # Run the target function again to explicitly check values
    calculate_capacity(cluster_config)
    captured = capsys.readouterr()
    
    # Check if the specific text format exists in the printed output string
    assert "62.5%" in captured.out
