import pytest
# Import the calculator function directly from the module
from lab3_BudgetOptimizer import estimate_deployment_cost

# Test case 1: Verify output when deployment cost exceeds the budget cap
def test_budget_exceeded():
    # 5 instances * 0.45 rate * 720 hours = $1620.00 (Exceeds $1500.00 cap by $120.00)
    result = estimate_deployment_cost(instance_count=5, hourly_rate=0.45, budget_cap=1500.00)
    assert result == "REJECTED: Budget Exceeded by $120.00!"

# Test case 2: Verify another budget rejection limit scenario from the lab readme
def test_budget_exceeded_large_scale():
    # 12 instances * 0.85 rate * 720 hours = $7344.00 (Exceeds $5000.00 cap by $2344.00)
    result = estimate_deployment_cost(instance_count=12, hourly_rate=0.85, budget_cap=5000.00)
    assert result == "REJECTED: Budget Exceeded by $2344.00!"

# Test case 3: Verify output when deployment cost is fully within safe budget boundaries
def test_budget_approved():
    # 2 instances * 0.10 rate * 720 hours = $144.00 (Within $200.00 budget)
    result = estimate_deployment_cost(instance_count=2, hourly_rate=0.10, budget_cap=200.00)
    assert result == "APPROVED: Total Estimated Cost is $144.00."
