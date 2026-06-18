
def estimate_deployment_cost(instance_count, hourly_rate, budget_cap):
    # TODO: Calculate total monthly cost (instances * hourly_rate * 720)

    total_monthly_cost = instance_count * hourly_rate * 720

    # TODO: Implement if/else conditional check against budget_cap

    if total_monthly_cost > budget_cap:
        cost_exceeds = total_monthly_cost - budget_cap
        # TODO: Return the appropriate message string
        return f"REJECTED: Budget Exceeded by ${cost_exceeds:.2f}!"
    else: 
        # TODO: Return the appropriate message string
        return f"APPROVED: Total Estimated Cost is ${total_monthly_cost:.2f}."  
        
# Test Cases to verify your execution:
print(estimate_deployment_cost(instance_count=5, hourly_rate=0.45, budget_cap=1500.00))
print(estimate_deployment_cost(instance_count=12, hourly_rate=0.85, budget_cap=5000.00))
