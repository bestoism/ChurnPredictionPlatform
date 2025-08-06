with source as (

    select * from {{ source('raw_telco', 'telco_customers') }}

),

renamed as (

    select
        -- Mengganti nama kolom agar snake_case dan lebih jelas
        customerID as customer_id,
        gender,
        SeniorCitizen as is_senior_citizen,
        Partner as has_partner,
        Dependents as has_dependents,
        tenure as tenure_months,
        PhoneService as has_phone_service,
        MultipleLines as has_multiple_lines,
        InternetService as internet_service_type,
        OnlineSecurity as has_online_security,
        OnlineBackup as has_online_backup,
        DeviceProtection as has_device_protection,
        TechSupport as has_tech_support,
        StreamingTV as has_streaming_tv,
        StreamingMovies as has_streaming_movies,
        Contract as contract_type,
        PaperlessBilling as has_paperless_billing,
        PaymentMethod as payment_method,
        
        ifnull(safe_cast(TotalCharges as numeric), 0) as total_charges,
        MonthlyCharges as monthly_charges,

        -- PERBAIKAN FINAL: Membandingkan langsung dengan nilai BOOLEAN, bukan string.
        case 
            when Churn = TRUE then 1
            else 0
        end as is_churn

    from source

)

select * from renamed