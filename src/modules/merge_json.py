def merge_rollouts(experiments, guild_rollouts, user_rollouts):
    merged_data = []
    
    for experiment in experiments:
        merged_entry = experiment.copy()
        matching_guild = next((item for item in guild_rollouts if item['id'] == experiment['id'] and item['kind'] == experiment['kind']), None)
        matching_user = next((item for item in user_rollouts if item['id'] == experiment['id'] and item['kind'] == experiment['kind']), None)
        
        if matching_guild:
            merged_entry.update(matching_guild)
        if matching_user:
            merged_entry.update(matching_user)
        
        merged_data.append(merged_entry)
    
    return merged_data
