## object columns

`cat_df = airbnb_df.select_dtypes(include=['object']).copy()`

### transformed

| Column                           | Transformation                                                                        |
| -------------------------------- | ------------------------------------------------------------------------------------- |
| host_id                          | none                                                                                  |
| host_response_time               | drop_rows_occurs_less_than(1) ->fillna_with_lowest_occurance ->dic_host_response_time |
| host_is_superhost                | encode_boolean_to_float ->fillna False                                                |
| host_verifications               | extract_num_of_items_for_column                                                       |
| host_has_profile_pic             | encode_boolean_to_float ->fillna False                                                |
| host_identity_verified           | encode_boolean_to_float ->fillna False                                                |
| neighbourhood_group_cleansed     | drop_rows_occurs_less_than(1) ->encode_category_dic                                   |
| is_location_exact                | encode_boolean_to_float                                                               |
| property_type                    | encode_category_dic                                                                   |
| room_type                        | encode_category_dic                                                                   |
| bed_type                         | encode_category_dic                                                                   |
| amenities                        | extract_num_of_items_for_column                                                       |
| has_availability                 | encode_boolean_to_float                                                               |
| instant_bookable                 | encode_boolean_to_float                                                               |
| cancellation_policy              | drop_rows_occurs_less_than(2) -> encode_category_dic                                  |
| require_guest_profile_picture    | encode_boolean_to_float                                                               |
| require_guest_phone_verification | encode_boolean_to_float                                                               |

## float64 and int32

`numeric_df = airbnb_df.select_dtypes(include=['float64', 'int32']).copy()`

### transformed

| Column                                       | Transformation   |
| -------------------------------------------- | ---------------- |
| host_response_rate                           | fillna with mean |
| latitude                                     |
| longitude                                    |
| accommodates                                 |
| bathrooms                                    |
| bedrooms                                     |
| beds                                         |
| price                                        |
| security_deposit                             |
| cleaning_fee                                 |
| guests_included                              |
| extra_people                                 |
| availability_365                             |
| number_of_reviews                            |
| review_scores_rating                         |
| review_scores_accuracy                       |
| review_scores_cleanliness                    |
| review_scores_checkin                        |
| review_scores_communication                  |
| review_scores_location                       |
| review_scores_value                          |
| calculated_host_listings_count               |
| calculated_host_listings_count_entire_homes  |
| calculated_host_listings_count_private_rooms |
| calculated_host_listings_count_shared_rooms  |
| review_per_month                             |
