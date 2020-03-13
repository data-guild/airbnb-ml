drop_cat_columns = [
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
    'host_since',
]
drop_num_columns = [
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
