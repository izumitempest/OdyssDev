def validate_trip_dates(start_date, end_date):
    if start_date > end_date:
        raise ValueError("Start date must be before end date")