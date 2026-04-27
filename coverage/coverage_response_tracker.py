from django.utils.timezone import now

def calculate_average_response_time(existing_avg, existing_count, new_time):
    """
    Incremental average calculation.
    """
    total_time = existing_avg * existing_count
    updated_count = existing_count + 1
    updated_avg = (total_time + new_time) / updated_count

    return round(updated_avg, 4)