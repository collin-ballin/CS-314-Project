# ChocAn System

## Database Setup
1. Create PostgreSQL database:
CREATE DATABASE choco;


2. Create user:
CREATE USER dev WITH PASSWORD 'guest';

3. Load Schema:
psql -U dev -d choco -f database/schema/database_schema.sql

## Install Libraries:
psycopg2

## Install Database:
postgress

## Adding Members
1. Pass strings into the function create_member(member_id, name, street_address, city, state, zip_code, status):


## Adding Providers
1. Pass strings into the function create_provider(provider_id, name, street_address, city, state, zip_code):


## Adding Consulations
1. create_consultation(provider_id, member_id, consultation_date, comments):
2. consulation_date must be a date variable
3. week_start_date = datetime.strptime(start_date_str, "%Y-%m-%d").date()
4. week_end_date = datetime.strptime(end_date_str, "%Y-%m-%d").date()
5. this might be a way to convert string to time variables but i havent tested


## Adding Service Records (transcation history)
1. Verify the service code before entering by using verify_service(service_id):
2. once its verified add this into service records by using create_service_record(provider_id, member_id, service_code, service_date, comments=None):
3. service_date is another date variable

## Adding Consulation Records (making appointments)
1. pass strings into create_consultation(provider_id, member_id, consultation_date, comments):
2. comments is the reasoning of the meeting


## Adding Provider Report
1. pass id and two date variables into create_provider_report(provider_id, week_start_date, week_end_date):
2. once this is added use the print retrive provider report function to display : retrieve_provider_report(provider_id, week_start_date, week_end_date:


## Adding Services
1. pass strings into create_service and int for fee (service_code, service_name, fee):



## Printing Provider Reports
1. Add report into table using create_provider_report(provider_id, Week_end_date), this will automatically add their total consulations, fees, and pervices provided
2. Next use retrieve_provider_report(provider_id, week_start_date, week_end_date) to find all reports

## Printing Member Reports (No adding necessary)
1. pass two date variables into retrieve_member_report(week_start_date, week_end_date):
2. this will print each member report for the timeframe

## Printing Manager Reports (No adding necessary)
1. pass two date variables into retrieve_manager_report(weekstart_date, weekend_date):
2. this will print manager report for the timeframe

## Printing services
1. retrieve_service_codes():

## Printing Service records (transcation history)
1. pass string and a date variable retrieve_service_records(provider_id=None, member_id=None, service_date=None):
2. it will search for all services from provider first
3. To get all records for a specific provider_id:retrieve_service_records(provider_id=1)
4. To get all records for a specific service_date: retrieve_service_records(service_date="2024-12-07")
5. To get records filtered by both provider_id and service_date: retrieve_service_records(provider_id=1, service_date="2024-12-07")

## Printing Consulation Records ( Appointments )
1. display_consultations():

## Validate Member
1. pass ID into verify_member(member_id):

## Validate Service 
1. pass ID into verify_service(service_id):



## Deleteing conuslation table
1. clear_consultation_table():