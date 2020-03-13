drop_columns = [
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