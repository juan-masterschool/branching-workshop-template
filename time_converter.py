
def seconds_to_minutes(seconds):
    """Convert seconds to minutes and remaining seconds."""
    minutes = seconds // 60
    remaining_seconds = seconds % 60
    return minutes, remaining_seconds
