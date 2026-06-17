cluster_config = {
    "cluster_name": "dhaka-prod-east",
    "total_max_slots": 8,
    "active_nodes": ["10.0.1.15", "10.0.1.16", "10.0.1.17", "10.0.1.18", "10.0.1.19"]
}

def calculate_capacity(config):

    # TODO: Calculate how many items are in the active_nodes list

    # Destructure values from dictionary 
    cluster_name,total_max_slots,active_nodes = cluster_config.values()

    # Initialize to count active nodes
    active_nodes_count = 0
    
    # Loop through each item and count them
    for count,node in enumerate(active_nodes):
        active_nodes_count = count + 1

    # TODO: Run the mathematical formula to find utilization percentage
    
    utilization =  (active_nodes_count/total_max_slots) * 100
    
    # TODO: Print the status statement

    print(f"""
    - Cluster name: {cluster_name}
    - Cluster max slots: {total_max_slots}
    - Total active nodes: {active_nodes_count}
    - Cluster utilization percentage: {utilization}%""")

    print("\n" * 1)

# Execute the audit tool
calculate_capacity(cluster_config)
