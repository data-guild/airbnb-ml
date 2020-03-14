dropped_columns = [
    'rowId',
    'id',
    'host_location',
    'host_neighbourhood',
    'street',
    'neighbourhood',
    'neighbourhood_cleansed',
    'market',
    'license',
    'zipcode',
    'calendar_updated',
    'first_review',
    'last_review',
    'host_since',
    'host_listings_count',
    'host_total_listings_count',
    'minimum_nights',
    'maximum_nights',
    'minimum_nights_avg_ntm',
    'maximum_nights_avg_ntm',
    'availability_30',
    'availability_60',
    'availability_90',
    'number_of_reviews_ltm',
]

boolean_to_float_cols = [
    "host_is_superhost",
    "host_has_profile_pic",
    "host_identity_verified",
    "is_location_exact",
    "has_availability",
    "instant_bookable",
    "require_guest_profile_picture",
    "require_guest_phone_verification"]

category_columns = [
    "neighbourhood_group_cleansed",
    "property_type",
    "room_type",
    "bed_type",
    "cancellation_policy"
]

# used to extract columns in the correct order from post request json object
column_order = ['host_id', 'host_response_time', 'host_response_rate',
                'host_is_superhost', 'host_verifications', 'host_has_profile_pic',
                'host_identity_verified', 'neighbourhood_group_cleansed', 'latitude',
                'longitude', 'is_location_exact', 'property_type', 'room_type',
                'accommodates', 'bathrooms', 'bedrooms', 'beds', 'bed_type',
                'amenities', 'security_deposit', 'cleaning_fee',
                'guests_included', 'extra_people', 'has_availability',
                'availability_365', 'number_of_reviews', 'review_scores_rating',
                'review_scores_accuracy', 'review_scores_cleanliness',
                'review_scores_checkin', 'review_scores_communication',
                'review_scores_location', 'review_scores_value', 'instant_bookable',
                'cancellation_policy', 'require_guest_profile_picture',
                'require_guest_phone_verification', 'calculated_host_listings_count',
                'calculated_host_listings_count_entire_homes',
                'calculated_host_listings_count_private_rooms',
                'calculated_host_listings_count_shared_rooms', 'reviews_per_month']
