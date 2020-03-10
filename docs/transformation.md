# columns in valid parquet files

```
airbnb_df.dtypes.value_counts()
```

| type    | occurance |
| ------- | --------- |
| float64 | 42        |
| object  | 37        |
| int32   | 2         |

## objects

`cat_df = airbnb_df.select_dtypes(include=['object']).copy()`

### dropped

| Column | Reason   |
| ------ | -------- |
| rowId  | not used |

### transformed

| Column                           | Transformation |
| -------------------------------- | -------------- |
| rowId                            |
| id                               |
| experiences_offered              |
| host_since                       |
| host_location                    |
| host_response_time               |
| host_is_superhost                |
| host_neighbourhood               |
| host_verifications               |
| host_has_profile_pic             |
| host_identity_verified           |
| street                           |
| neighbourhood                    |
| neighbourhood_cleansed           |
| neighbourhood_group_cleansed     |
| city                             |
| state                            |
| zipcode                          |
| market                           |
| smart_location                   |
| is_location_exact                |
| property_type                    |
| room_type                        |
| bed_type                         |
| amenities                        |
| calendar_updated                 |
| has_availability                 |
| calendar_last_scraped            |
| first_review                     |
| last_review                      |
| requires_license                 |
| license                          |
| instant_bookable                 |
| is_business_travel_ready         |
| cancellation_policy              |
| require_guest_profile_picture    |
| require_guest_phone_verification |

## float64 and int32

`numeric_df = airbnb_df.select_dtypes(include=['float64', 'int32']).copy()`

### dropped

| Column               | Reason     |
| -------------------- | ---------- |
| host_acceptance_rate | mostly NaN |

### transformed

| Column                                       | Transformation |
| -------------------------------------------- | -------------- |
| host_response_rate                           |
| host_acceptance_rate                         |
| host_listings_count                          |
| host_total_listings_count                    |
| latitude                                     |
| longitude                                    |
| accommodates                                 |
| bathrooms                                    |
| bedrooms                                     |
| beds                                         |
| square_feet                                  |
| price                                        |
| weekly_price                                 |
| monthly_price                                |
| security_deposit                             |
| cleaning_fee                                 |
| guests_included                              |
| extra_people                                 |
| minimum_nights                               |
| maximum_nights                               |
| minimum_minimum_nights                       |
| maximum_minimum_nights                       |
| minimum_maximum_nights                       |
| maximum_maximum_nights                       |
| minimum_nights_avg_ntm                       |
| maximum_nights_avg_ntm                       |
| availability_30                              |
| availability_60                              |
| availability_90                              |
| availability_365                             |
| number_of_reviews                            |
| number_of_reviews_ltm                        |
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
| reviews_per_month                            |
