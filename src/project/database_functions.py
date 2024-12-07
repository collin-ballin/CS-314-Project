import psycopg2

# For Testing 
from datetime import datetime


#### FUNCTION PROTOTYPES ####


### CREATE ###

## CREATE MEMBER
# create_member(member id, name, street address, city, state, zip code, status, comments)

## CREATE PROVIDER
# create_provider(provider_id, name, street_address, city, state, zip_code)

## CREATE SERVICE
# create_service(service_code, service_name, fee)

## CREATE SERVICE RECORD
# create_service_record(provider_id, member_id, service_code, service_date, comments)


### RETRIEVE ###
# If no argument for anything with =None, then will search for ALL within that parameter

## RETRIEVE MEMBER
# retrieve_member(member_id=None, name=None)

## RETRIEVE PROVIDER
# retrieve_provider(provider_id=None, name=None)

## RETRIEVE SERVICE
# retrieve_service(service_code=None)

## RETRIEVE SERVICE RECORD
# retrieve_service_records(provider_id=None, member_id=None, service_date=None)


### DELETE ###

## DELETE MEMBER
# delete_member(member_id)

## DELETE PROVIDER
# delete_provider(provider_id)

## DELETE SERVICE 
# delete_service(service_code)

## DELETE SERVICE RECORD
# delete_service_record(record_id)


### MODIFY ####
# CANT CHANGE: Member ID, Provider ID, Service Code
# Search by ID/Code, then add argument you want to change. 
# Example: modify_member("111111111", name="New Name")

## MODIFY MEMBER
# modify_member(member_id, name=None, street_address=None, city=None, state=None, zip_code=None, status=None):

## MODIFY PROVIDER
# modify_provider(provider_id, name=None, street_address=None, city=None, state=None, zip_code=None):

## MODIFY SERVICE
# modify_service(service_code, service_name=None, fee=None)




##### Comment examples of how to call each function at bottom of this file. #####

# Create / Data Insertion Functions
def create_member(member_id, name, street_address, city, state, zip_code, status='active'):
    try:
        # Connect to database
        conn = psycopg2.connect(
                dbname="choco",
                user="dev",
                password="guest",
                host="localhost",
                port="5432"
                )
        cur = conn.cursor()

        # SQL insert statement
        insert_query = """
        INSERT INTO members (member_id, name, street_address, city, state, zip_code, status)
        VALUES (%s, %s, %s, %s, %s, %s, %s)
        """

        # Execute insert with values
        cur.execute(insert_query, (member_id, name, street_address, city, state, zip_code, status))

        # Commit the transaction
        conn.commit()
        print("Member created successfully!")

    except psycopg2.Error as e:
        print(f"Error creating member: {e}")
        conn.rollback()  # Roll back in case of error

    finally:
        # Close cursor and connection
        if cur:
            cur.close()
        if conn:
            conn.close()

def create_provider(provider_id, name, street_address, city, state, zip_code):
    try:
        conn = psycopg2.connect(
                dbname="choco",
                user="dev",
                password="guest",
                host="localhost",
                port="5432"
                )
        cur = conn.cursor()

        insert_query = """
        INSERT INTO providers (provider_id, name, street_address, city, state, zip_code)
        VALUES (%s, %s, %s, %s, %s, %s)
        """

        cur.execute(insert_query, (provider_id, name, street_address, city, state, zip_code))
        conn.commit()
        print("Provider created successfully!")

    except psycopg2.Error as e:
        print(f"Error creating provider: {e}")
        conn.rollback()

    finally:
        if cur:
            cur.close()
        if conn:
            conn.close()

def create_service(service_code, service_name, fee):
    try:
        conn = psycopg2.connect(
                dbname="choco",
                user="dev",
                password="guest",
                host="localhost",
                port="5432"
                )
        cur = conn.cursor()

        insert_query = """
        INSERT INTO services (service_code, service_name, fee)
        VALUES (%s, %s, %s)
        """

        cur.execute(insert_query, (service_code, service_name, fee))
        conn.commit()
        print("Service created successfully!")

    except psycopg2.Error as e:
        print(f"Error creating service: {e}")
        conn.rollback()

    finally:
        if cur:
            cur.close()
        if conn:
            conn.close()
def create_consultation(provider_id, member_id, consultation_date, comments):
    try:
        
        conn = psycopg2.connect(
                dbname="choco",
                user="dev",
                password="guest",
                host="localhost",
                port="5432"
                )
        cur = conn.cursor()

        # Insert a new record into consultation_records
        cur.execute("""
            INSERT INTO consultation_records (provider_id, member_id, consultation_date, comments)
            VALUES (?, ?, ?, ?);
        """, (provider_id, member_id, consultation_date, comments))

        # Commit the transaction
        conn.commit()

        print("Consultation record added successfully!")
        return True  # Return True to indicate success

    except psycopg2.Error as e:
        print(f"Error adding consultation record: {e}")
        return False  # Return False in case of an error

    finally:
        # Ensure the connection is closed
        if cur:
            cur.close()
        if conn:
            conn.close()

def create_service_record(provider_id, member_id, service_code, service_date, comments=None):
    try:
        conn = psycopg2.connect(
                dbname="choco",
                user="dev",
                password="guest",
                host="localhost",
                port="5432"
                )
        cur = conn.cursor()

        insert_query = """
        INSERT INTO service_records (provider_id, member_id, service_code, service_date, comments)
        VALUES (%s, %s, %s, %s, %s)
        """

        cur.execute(insert_query, (provider_id, member_id, service_code, service_date, comments))
        conn.commit()
        print("Service record created successfully!")

    except psycopg2.Error as e:
        print(f"Error creating service record: {e}")
        conn.rollback()

    finally:
        if cur:
            cur.close()
        if conn:
            conn.close()

def create_provider_report(provider_id, week_start_date, week_end_date):
    try:
        # Connect to the psycopg2 database
        conn = psycopg2.connect(
                dbname="choco",
                user="dev",
                password="guest",
                host="localhost",
                port="5432"
                )
        cur = conn.cursor()

        # Calculate total consultations and total fees within the given week range
        total_consultations_query = """
        SELECT COUNT(*)
        FROM service_records
        WHERE provider_id = ? AND service_date BETWEEN ? AND ?;
        """

        total_fees_query = """
        SELECT SUM(services.fee)
        FROM service_records
        JOIN services ON service_records.service_code = services.service_code
        WHERE service_records.provider_id = ? AND service_records.service_date BETWEEN ? AND ?;
        """

        # Execute queries to fetch data
        cur.execute(total_consultations_query, (provider_id, week_start_date, week_end_date))
        total_consultations = cur.fetchone()[0] or 0  # Default to 0 if no records found

        cur.execute(total_fees_query, (provider_id, week_start_date, week_end_date))
        total_fees = cur.fetchone()[0] or 0.0  # Default to 0.0 if no fees found

        # Insert data into the weekly_provider_reports table
        insert_query = """
        INSERT INTO weekly_provider_reports (provider_id, week_end_date, total_consultations, total_fees)
        VALUES (?, ?, ?, ?);
        """
        cur.execute(insert_query, (provider_id, week_end_date, total_consultations, total_fees))

        # Commit the transaction
        conn.commit()
        print("Report inserted successfully.")

    except psycopg2.IntegrityError as e:
        print(f"Integrity error: {e}")
    except psycopg2.OperationalError as e:
        print(f"Operational error: {e}")
    except psycopg2.Error as e:
        print(f"psycopg2 error occurred: {e}")
    finally:
        # Ensure the connection is closed
        if cur:
            cur.close()
        if conn:
            conn.close()


# Retrieve / Printing Functions
def retrieve_members():
    try:
        # Connect to the database
        conn = psycopg2.connect(
                dbname="choco",
                user="dev",
                password="guest",
                host="localhost",
                port="5432"
                ) 
        cur = conn.cursor()

        # Query to fetch all service codes, names, and fees
        cur.execute("SELECT member_id, name, status, comments FROM members")

        # Fetch all the service details
        members = cur.fetchall()

        # Check if any services exist
        if members:
            print("\n\t\t=== Members ===")
            for member in members:
                member_id, name, status, comments = member
                print(f"Member Id: {member_id} | Name: {name} | Status : {status} | Comments: {comments}")
        else:
            print("No members found.")

    except psycopg2.Error as e:
        print(f"Error retrieving member details: {e}")
    
    finally:
        # Ensure the connection is closed
        if cur:
            cur.close()
        if conn:
            conn.close()    

def print_service_codes():
    try:
        # Connect to the database
        conn = psycopg2.connect(
                dbname="choco",
                user="dev",
                password="guest",
                host="localhost",
                port="5432"
                )  
        cur = conn.cursor()

        # Query to fetch all service codes, names, and fees
        cur.execute("SELECT service_code, service_name, fee FROM services")

        # Fetch all the service details
        services = cur.fetchall()

        # Check if any services exist
        if services:
            print("\n\t\t=== Service Codes ===")
            for service in services:
                service_code, service_name, fee = service
                print(f"Service Code: {service_code} | Name: {service_name} | Fee: ${fee:.2f}")
        else:
            print("No services found.")

    except psycopg2.Error as e:
        print(f"Error retrieving service details: {e}")
    
    finally:
        # Ensure the connection is closed
        if cur:
            cur.close()
        if conn:
            conn.close()

def retrieve_provider(provider_id=None, name=None):
    try:
        conn = psycopg2.connect(
                dbname="choco",
                user="dev",
                password="guest",
                host="localhost",
                port="5432"
                )
        cur = conn.cursor()

        if provider_id:
            cur.execute("SELECT * FROM providers WHERE provider_id = %s", (provider_id,))
        elif name:
            cur.execute("SELECT * FROM providers WHERE name LIKE %s", ('%' + name + '%',))
        else:
            cur.execute("SELECT * FROM providers")

        rows = cur.fetchall()
        for row in rows:
            print(f"Provider: {row}")
        return rows

    except psycopg2.Error as e:
        print(f"Error retrieving provider(s): {e}")
        return None

    finally:
        if cur:
            cur.close()
        if conn:
            conn.close()
def retrieve_manager_report(weekstart_date, weekend_date):
    try:
   
        conn = psycopg2.connect(
                dbname="choco",
                user="dev",
                password="guest",
                host="localhost",
                port="5432"
                )# Replace with your actual database path
        cur = conn.cursor()

        # Query to list every provider to be paid between the custom weekstart and weekend dates
        cur.execute('''
            SELECT 
                providers.provider_id, 
                providers.name AS provider_name,
                COUNT(service_records.record_id) AS num_consultations, 
                SUM(services.fee) AS total_fee
            FROM 
                service_records
            JOIN 
                providers ON service_records.provider_id = providers.provider_id
            JOIN 
                services ON service_records.service_code = services.service_code
            WHERE 
                service_records.service_date BETWEEN ? AND ?
            GROUP BY 
                providers.provider_id;
        ''', (weekstart_date, weekend_date))

        # Fetch and display the results for each provider
        provider_rows = cur.fetchall()
        print(f"Provider Report for week {weekstart_date} - {weekend_date}:")
        print("Provider ID | Provider Name | Consultations | Total Fee")
        print("-" * 60)
        for row in provider_rows:
            print(f"{row[0]:<12} | {row[1]:<15} | {row[2]:<15} | ${row[3]:<10.2f}")

        # Query to calculate total number of providers, consultations, and total fees
        cur.execute('''
            SELECT 
                COUNT(DISTINCT provider_id) AS total_providers,
                COUNT(record_id) AS total_consultations,
                SUM(services.fee) AS total_fee
            FROM 
                service_records
            JOIN 
                services ON service_records.service_code = services.service_code
            WHERE 
                service_date BETWEEN ? AND ?;
        ''', (weekstart_date, weekend_date))

        # Fetch and display total summary
        total_data = cur.fetchone()
        print("\nTotal Report for the Week:")
        print(f"Total Providers: {total_data[0]}")
        print(f"Total Consultations: {total_data[1]}")
        print(f"Total Fees: ${total_data[2]:.2f}")

    except psycopg2.Error as e:
        print(f"Error retrieving manager reports: {e}")

    finally:
        # Ensure the connection is closed
        if cur:
            cur.close()
        if conn:
            conn.close()
def display_consultations():
    try:
   
        conn = psycopg2.connect(
                dbname="choco",
                user="dev",
                password="guest",
                host="localhost",
                port="5432"
                )
        cur = conn.cursor()

        # Query to fetch records, joining with 'providers' and 'members' tables, and sorting by consultation_date
        cur.execute('''
            SELECT 
                consultation_records.consultation_id, 
                consultation_records.consultation_date, 
                providers.name AS provider_name, 
                members.name AS member_name, 
                consultation_records.comments
            FROM consultation_records
            JOIN providers ON consultation_records.provider_id = providers.provider_id
            JOIN members ON consultation_records.member_id = members.member_id
            ORDER BY consultation_records.consultation_date
        ''')

        # Fetch all rows
        rows = cur.fetchall()

        # Check if there are any records
        if rows:
            print("Consultation Records Sorted by Date:")
            print("ID | Provider Name | Member Name | Consultation Date | Reason")
            print("-" * 75)
            for row in rows:
                # Print each consultation record
                print(f"{row[0]:<3} | {row[2]:<15} | {row[3]:<12} | {row[1]} | {row[4]}")
        else:
            print("No consultation records found.")

    except psycopg2.Error as e:
        print(f"Error retrieving consultation records: {e}")

    finally:
        # Ensure the connection is closed
        if cur:
            cur.close()
        if conn:
            conn.close()

def retrieve_service_codes():
    try:
        
        conn = psycopg2.connect(
                dbname="choco",
                user="dev",
                password="guest",
                host="localhost",
                port="5432"
                )
        cur = conn.cursor()

        # Query to fetch all service codes, names, and fees
        cur.execute("SELECT service_code, service_name, fee FROM services")

        # Fetch all the service details
        services = cur.fetchall()

        # Check if any services exist
        if services:
            print("\n\t\t=== Service Codes ===")
            for service in services:
                service_code, service_name, fee = service
                print(f"Service Code: {service_code} | Name: {service_name} | Fee: ${fee:.2f}")
        else:
            print("No services found.")

    except psycopg2.Error as e:
        print(f"Error retrieving service details: {e}")
    
    finally:
        # Ensure the connection is closed
        if cur:
            cur.close()
        if conn:
            conn.close()


def retrieve_service_records(provider_id=None, member_id=None, service_date=None):
    try:
        conn = psycopg2.connect(
                dbname="choco",
                user="dev",
                password="guest",
                host="localhost",
                port="5432"
                )
        cur = conn.cursor()

        if provider_id:
            cur.execute("SELECT * FROM service_records WHERE provider_id = %s", (provider_id,))
        elif member_id:
            cur.execute("SELECT * FROM service_records WHERE member_id = %s", (member_id,))
        elif service_date:
            cur.execute("SELECT * FROM service_records WHERE service_date = %s", (service_date,))
        else:
            cur.execute("SELECT * FROM service_records")

        rows = cur.fetchall()
        for row in rows:
            print(f"Service Record: {row}")
        return rows

    except psycopg2.Error as e:
        print(f"Error retrieving service record(s): {e}")
        return None

    finally:
        if cur:
            cur.close()
        if conn:
            conn.close()

def retrieve_provider_report(provider_id=None, week_start_date=None, week_end_date=None):
    try:
        # Connect to the database
        conn = psycopg2.connect(
                dbname="choco",
                user="dev",
                password="guest",
                host="localhost",
                port="5432"
                )  
        cur = conn.cursor()

        if week_start_date and week_end_date:
            # Query to fetch reports for all providers within the specified week range
            query = """
                SELECT DISTINCT
                    p.provider_id,
                    p.name AS provider_name,
                    p.street_address,
                    p.city,
                    p.state,
                    p.zip_code,
                    r.total_consultations,
                    r.total_fees
                FROM 
                    providers p
                LEFT JOIN 
                    weekly_provider_reports r ON p.provider_id = r.provider_id
                WHERE 
                    r.week_end_date BETWEEN ? AND ?
            """
            if provider_id:
                query += " AND r.provider_id = ?"

            cur.execute(query, (week_start_date, week_end_date, provider_id) if provider_id else (week_start_date, week_end_date))

            provider_details = cur.fetchall()
            if not provider_details:
                print("No reports found for the specified week range.")
                return

            for provider in provider_details:
                print("\n=== Provider Report ===")
                print(f"Provider Name: {provider[1]}")
                print(f"Address: {provider[2]}, {provider[3]}, {provider[4]} {provider[5]}")

                total_consultations = provider[6] if provider[6] is not None else 0
                total_fees = provider[7] if provider[7] is not None else 0.0

                # If no report data, calculate the consultations and fees manually
                if total_consultations == 0 and total_fees == 0.0:
                    cur.execute("""
                        SELECT 
                            COUNT(s.record_id) AS total_consultations,
                            SUM(svc.fee) AS total_fees
                        FROM 
                            service_records s
                        INNER JOIN 
                            services svc ON s.service_code = svc.service_code
                        WHERE 
                            s.provider_id = ? AND s.service_date BETWEEN ? AND ?
                    """, (provider[0], week_start_date, week_end_date))

                    result = cur.fetchone()

                    total_consultations = result[0] if result[0] else 0
                    total_fees = result[1] if result[1] else 0.0

                print(f"Total Consultations: {total_consultations}")
                print(f"Total Fees: ${total_fees:.2f}")
                cur.execute("""
                    SELECT 
                        s.record_id,
                        s.service_date,
                        s.service_code,
                        m.name AS member_name,
                        svc.fee AS service_fee
                    FROM 
                        service_records s
                    INNER JOIN 
                        members m ON s.member_id = m.member_id
                    INNER JOIN
                        services svc ON s.service_code = svc.service_code
                    WHERE 
                        s.provider_id = ? AND s.service_date BETWEEN ? AND ?
                    ORDER BY 
                        s.service_date
                """, (provider[0], week_start_date, week_end_date))

                services = cur.fetchall()
                if services:
                    print("\n=== Services Provided ===")
                    for service in services:
                        print(f"Record ID: {service[0]}")
                        print(f"  Service Date: {datetime.strptime(service[1], '%Y-%m-%d').strftime('%m-%d-%Y')}")
                        print(f"  Service Code: {service[2]}")
                        print(f"  Member: {service[3]}")
                        print(f"  Service Fee: ${service[4]:.2f}")
                else:
                    print("\nNo services provided during this period.")

        else:
            print("Please provide week_start_date and week_end_date to retrieve the report.")

    except psycopg2.Error as e:
        print(f"Error retrieving report: {e}")
    
    finally:
        if cur:
            cur.close()
        if conn:
            conn.close()

from datetime import date
def retrieve_member(member_id=None, name=None):
    try:
        conn = psycopg2.connect(
                dbname="choco",
                user="dev",
                password="guest",
                host="localhost",
                port="5432"
                )  
        cur = conn.cursor()

        if member_id:
            cur.execute("SELECT * FROM members WHERE member_id = ?", (member_id,))
        elif name:
            cur.execute("SELECT * FROM members WHERE name LIKE ?", ('%' + name + '%',))
        else:
            cur.execute("SELECT * FROM members")

        rows = cur.fetchall()
        for row in rows:
            print(f"Member: {row}")
        return rows
    
    except psycopg2.Error as e:
        print(f"Error retrieving member(s): {e}")
        return None
    
    finally:
        if cur:
            cur.close()
        if conn:
            conn.close()
def retrieve_member_report(week_start_date, week_end_date):
    try:
        # Connect to the database
        conn = psycopg2.connect(
                dbname="choco",
                user="dev",
                password="guest",
                host="localhost",
                port="5432"
                )  
        cur = conn.cursor()

        # Query to retrieve member details along with services provided during the week
        cur.execute("""
    SELECT DISTINCT
        m.name AS member_name,
        m.member_id,
        m.street_address,
        m.city,
        m.state,
        m.zip_code,
        s.service_date,
        p.name AS provider_name,
        svc.service_name
    FROM 
        members m
    INNER JOIN 
        service_records s ON m.member_id = s.member_id
    INNER JOIN 
        providers p ON s.provider_id = p.provider_id
    INNER JOIN 
        services svc ON s.service_code = svc.service_code
    WHERE 
        s.service_date BETWEEN ? AND ?
    ORDER BY 
        m.member_id, s.service_date
""", (week_start_date, week_end_date))
        member_services = cur.fetchall()

        if not member_services:
            print("No services provided to members during this week.")
            return

        # Group by members and print reports
        print("\n=== Weekly Member Reports ===")
        current_member_id = None
        for record in member_services:
            member_name, member_id, address, city, state, zip_code, service_date, provider_name, service_name = record

            # Start new report for each member
            if current_member_id != member_id:
                if current_member_id is not None:
                    print("\n" + "=" * 40)
                current_member_id = member_id
                print(f"\nMember Name: {member_name}")
                print(f"Member ID: {member_id}")
                print(f"Address: {address}, {city}, {state} {zip_code}")
                print("\nServices Provided:")

            # Use a set to track services to avoid printing duplicates
            printed_services = set()

            # Check if the service has already been printed for this member
            if service_name not in printed_services:
                printed_services.add(service_name)
                print(f"  - {datetime.strptime(service_date, '%Y-%m-%d').strftime('%m-%d-%Y')}: {provider_name} - {service_name}")

    except psycopg2.Error as e:
        print(f"Error retrieving member report: {e}")
    
    finally:
        if cur:
            cur.close()
        if conn:
            conn.close()

def retrieve_service_records(provider_id=None, member_id=None, service_date=None):
    try:
        conn = psycopg2.connect(
                dbname="choco",
                user="dev",
                password="guest",
                host="localhost",
                port="5432"
                )
        cur = conn.cursor()

        if provider_id:
            cur.execute("SELECT * FROM service_records WHERE provider_id = %s", (provider_id,))
        elif member_id:
            cur.execute("SELECT * FROM service_records WHERE member_id = %s", (member_id,))
        elif service_date:
            cur.execute("SELECT * FROM service_records WHERE service_date = %s", (service_date,))
        else:
            cur.execute("SELECT * FROM service_records")

        rows = cur.fetchall()
        for row in rows:
            print(f"Service Record: {row}")
        return rows

    except psycopg2.Error as e:
        print(f"Error retrieving service record(s): {e}")
        return None

    finally:
        if cur:
            cur.close()
        if conn:
            conn.close()
def retrieve_eft_records(transaction_id=None, provider_id=None, transfer_date=None):
    try:
        # Establish database connection
        conn = psycopg2.connect(
            dbname="choco",
            user="dev",
            password="guest",
            host="localhost",
            port="5432"
        )
        cur = conn.cursor()

        # Build query based on provided parameters
        if transaction_id:
            cur.execute("SELECT * FROM eft_records WHERE transaction_id = %s", (transaction_id,))
        elif provider_id:
            cur.execute("SELECT * FROM eft_records WHERE provider_id = %s", (provider_id,))
        elif transfer_date:
            cur.execute("SELECT * FROM eft_records WHERE transfer_date = %s", (transfer_date,))
        else:
            cur.execute("SELECT * FROM eft_records")  # Retrieve all records if no filter is applied

        # Fetch all results
        rows = cur.fetchall()
        for row in rows:
            print(f"EFT Record: {row}")
        return rows

    except psycopg2.Error as e:
        print(f"Error retrieving EFT record(s): {e}")
        return None

    finally:
        # Ensure resources are cleaned up
        if cur:
            cur.close()
        if conn:
            conn.close()
def retrieve_service_codes():
    try:
   
        conn = psycopg2.connect(
            dbname="choco",
            user="dev",
            password="guest",
            host="localhost",
            port="5432"
        )# Replace with your actual database path
        cur = conn.cursor()

        # Query to fetch all service codes, names, and fees
        cur.execute("SELECT service_code, service_name, fee FROM services")

        # Fetch all the service details
        services = cur.fetchall()

        # Check if any services exist
        if services:
            print("\n\t\t=== Service Codes ===")
            for service in services:
                service_code, service_name, fee = service
                print(f"Service Code: {service_code} | Name: {service_name} | Fee: ${fee:.2f}")
        else:
            print("No services found.")

    except psycopg2.Error as e:
        print(f"Error retrieving service details: {e}")
    
    finally:
        # Ensure the connection is closed
        if cur:
            cur.close()
        if conn:
            conn.close()
# Removal Functions
def delete_member(member_id):
   try:
       conn = psycopg2.connect(
           dbname="choco",
           user="dev", 
           password="guest",
           host="localhost",
           port="5432"
       )
       cur = conn.cursor()

       # Check if member exists
       cur.execute("SELECT member_id FROM members WHERE member_id = %s", (member_id,))
       if cur.fetchone() is None:
           print(f"Member with ID {member_id} does not exist!")
           return

       delete_query = "DELETE FROM members WHERE member_id = %s"
       cur.execute(delete_query, (member_id,))
       conn.commit()
       print("Member deleted successfully!")

   except psycopg2.Error as e:
       print(f"Error deleting member: {e}")
       conn.rollback()

   finally:
       if cur:
           cur.close()
       if conn:
           conn.close()

def delete_provider(provider_id):
   try:
       conn = psycopg2.connect(
           dbname="choco",
           user="dev",
           password="guest", 
           host="localhost",
           port="5432"
       )
       cur = conn.cursor()

       # Check if provider exists
       cur.execute("SELECT provider_id FROM providers WHERE provider_id = %s", (provider_id,))
       if cur.fetchone() is None:
           print(f"Provider with ID {provider_id} does not exist!")
           return

       delete_query = "DELETE FROM providers WHERE provider_id = %s"
       cur.execute(delete_query, (provider_id,))
       conn.commit()
       print("Provider deleted successfully!")

   except psycopg2.Error as e:
       print(f"Error deleting provider: {e}")
       conn.rollback()

   finally:
       if cur:
           cur.close()
       if conn:
           conn.close()

def delete_service(service_code):
   try:
       conn = psycopg2.connect(
           dbname="choco",
           user="dev",
           password="guest",
           host="localhost",
           port="5432"
       )
       cur = conn.cursor()

       # Check if service exists
       cur.execute("SELECT service_code FROM services WHERE service_code = %s", (service_code,))
       if cur.fetchone() is None:
           print(f"Service with code {service_code} does not exist!")
           return

       delete_query = "DELETE FROM services WHERE service_code = %s"
       cur.execute(delete_query, (service_code,))
       conn.commit()
       print("Service deleted successfully!")

   except psycopg2.Error as e:
       print(f"Error deleting service: {e}")
       conn.rollback()

   finally:
       if cur:
           cur.close()
       if conn:
           conn.close()

def delete_service_record(record_id):
   try:
       conn = psycopg2.connect(
           dbname="choco",
           user="dev",
           password="guest",
           host="localhost",
           port="5432"
       )
       cur = conn.cursor()

       # Check if record exists
       cur.execute("SELECT record_id FROM service_records WHERE record_id = %s", (record_id,))
       if cur.fetchone() is None:
           print(f"Service record with ID {record_id} does not exist!")
           return

       delete_query = "DELETE FROM service_records WHERE record_id = %s"
       cur.execute(delete_query, (record_id,))
       conn.commit()
       print("Service record deleted successfully!")

   except psycopg2.Error as e:
       print(f"Error deleting service record: {e}")
       conn.rollback()

   finally:
       if cur:
           cur.close()
       if conn:
           conn.close()
def clear_consultation_table():
    try:
        conn = psycopg2.connect(
            dbname="choco",
            user="dev",
            password="guest",
            host="localhost",
            port="5432"
        )
        cur = conn.cursor()

        # Delete all records from the consultation_records table
        cur.execute("DELETE FROM consultation_records")

        # Reset the auto-increment counter for consultation_id
        cur.execute("SELECT setval(pg_get_serial_sequence('consultation_records', 'consultation_id'), 1, false);")

        # Commit the transaction
        conn.commit()

        print("All consultation records have been cleared and the ID counter has been reset.")

    except psycopg2.Error as e:
        print(f"Error clearing consultation records and resetting ID: {e}")

    finally:
        # Ensure the connection is closed
        if cur:
            cur.close()
        if conn:
            conn.close()


def delete_eft_record(transaction_id):
    try:
        # Establish database connection
        conn = psycopg2.connect(
            dbname="choco",
            user="dev",
            password="guest",
            host="localhost",
            port="5432"
        )
        cur = conn.cursor()

        # Check if the record exists
        cur.execute("SELECT transaction_id FROM eft_records WHERE transaction_id = %s", (transaction_id,))
        if cur.fetchone() is None:
            print(f"EFT record with transaction ID {transaction_id} does not exist!")
            return

        # Delete the record
        delete_query = "DELETE FROM eft_records WHERE transaction_id = %s"
        cur.execute(delete_query, (transaction_id,))
        conn.commit()
        print("EFT record deleted successfully!")

    except psycopg2.Error as e:
        print(f"Error deleting EFT record: {e}")
        conn.rollback()

    finally:
        if cur:
            cur.close()
        if conn:
            conn.close()

def delete_weekly_provider_report(report_id):
    try:
        # Establish database connection
        conn = psycopg2.connect(
            dbname="choco",
            user="dev",
            password="guest",
            host="localhost",
            port="5432"
        )
        cur = conn.cursor()

        # Check if the report exists
        cur.execute("SELECT report_id FROM weekly_provider_reports WHERE report_id = %s", (report_id,))
        if cur.fetchone() is None:
            print(f"Weekly provider report with report ID {report_id} does not exist!")
            return

        # Delete the report
        delete_query = "DELETE FROM weekly_provider_reports WHERE report_id = %s"
        cur.execute(delete_query, (report_id,))
        conn.commit()
        print("Weekly provider report deleted successfully!")

    except psycopg2.Error as e:
        print(f"Error deleting weekly provider report: {e}")
        conn.rollback()

    finally:
        if cur:
            cur.close()
        if conn:
            conn.close()

# Modification Functions
from datetime import date

def modify_member(member_id, name=None, street_address=None, city=None, state=None, zip_code=None, status=None):
   try:
       conn = psycopg2.connect(
           dbname="choco",
           user="dev",
           password="guest",
           host="localhost",
           port="5432"
       )
       cur = conn.cursor()

       # Check if member exists
       cur.execute("SELECT member_id FROM members WHERE member_id = %s", (member_id,))
       if cur.fetchone() is None:
           print(f"Member with ID {member_id} does not exist!")
           return

       # Build update query dynamically based on provided fields
       update_parts = []
       values = []
       if name is not None:
           update_parts.append("name = %s")
           values.append(name)
       if street_address is not None:
           update_parts.append("street_address = %s")
           values.append(street_address)
       if city is not None:
           update_parts.append("city = %s")
           values.append(city)
       if state is not None:
           update_parts.append("state = %s")
           values.append(state)
       if zip_code is not None:
           update_parts.append("zip_code = %s")
           values.append(zip_code)
       if status is not None:
           update_parts.append("status = %s")
           values.append(status)

       if not update_parts:
           print("No fields to update!")
           return

       # Add member_id to values list
       values.append(member_id)

       update_query = f"""
           UPDATE members 
           SET {', '.join(update_parts)}
           WHERE member_id = %s
       """
       
       cur.execute(update_query, values)
       conn.commit()
       print("Member updated successfully!")

   except psycopg2.Error as e:
       print(f"Error updating member: {e}")
       conn.rollback()

   finally:
       if cur:
           cur.close()
       if conn:
           conn.close()

def modify_provider(provider_id, name=None, street_address=None, city=None, state=None, zip_code=None):
   try:
       conn = psycopg2.connect(
           dbname="choco",
           user="dev",
           password="guest",
           host="localhost",
           port="5432"
       )
       cur = conn.cursor()

       # Check if provider exists
       cur.execute("SELECT provider_id FROM providers WHERE provider_id = %s", (provider_id,))
       if cur.fetchone() is None:
           print(f"Provider with ID {provider_id} does not exist!")
           return

       update_parts = []
       values = []
       if name is not None:
           update_parts.append("name = %s")
           values.append(name)
       if street_address is not None:
           update_parts.append("street_address = %s")
           values.append(street_address)
       if city is not None:
           update_parts.append("city = %s")
           values.append(city)
       if state is not None:
           update_parts.append("state = %s")
           values.append(state)
       if zip_code is not None:
           update_parts.append("zip_code = %s")
           values.append(zip_code)

       if not update_parts:
           print("No fields to update!")
           return

       values.append(provider_id)

       update_query = f"""
           UPDATE providers 
           SET {', '.join(update_parts)}
           WHERE provider_id = %s
       """
       
       cur.execute(update_query, values)
       conn.commit()
       print("Provider updated successfully!")

   except psycopg2.Error as e:
       print(f"Error updating provider: {e}")
       conn.rollback()

   finally:
       if cur:
           cur.close()
       if conn:
           conn.close()

def modify_service(service_code, service_name=None, fee=None):
   try:
       conn = psycopg2.connect(
           dbname="choco",
           user="dev",
           password="guest",
           host="localhost",
           port="5432"
       )
       cur = conn.cursor()

       # Check if service exists
       cur.execute("SELECT service_code FROM services WHERE service_code = %s", (service_code,))
       if cur.fetchone() is None:
           print(f"Service with code {service_code} does not exist!")
           return

       update_parts = []
       values = []
       if service_name is not None:
           update_parts.append("service_name = %s")
           values.append(service_name)
       if fee is not None:
           update_parts.append("fee = %s")
           values.append(fee)

       if not update_parts:
           print("No fields to update!")
           return

       values.append(service_code)

       update_query = f"""
           UPDATE services 
           SET {', '.join(update_parts)}
           WHERE service_code = %s
       """
       
       cur.execute(update_query, values)
       conn.commit()
       print("Service updated successfully!")

   except psycopg2.Error as e:
       print(f"Error updating service: {e}")
       conn.rollback()

   finally:
       if cur:
           cur.close()
       if conn:
           conn.close()
def modify_eft_record(transaction_id, provider_id=None, amount=None, transfer_date=None):
    try:
        conn = psycopg2.connect(
            dbname="choco",
            user="dev",
            password="guest",
            host="localhost",
            port="5432"
        )
        cur = conn.cursor()

        # Check if the EFT record exists
        cur.execute("SELECT transaction_id FROM eft_records WHERE transaction_id = %s", (transaction_id,))
        if cur.fetchone() is None:
            print(f"EFT record with transaction ID {transaction_id} does not exist!")
            return

        # Build update query dynamically
        update_parts = []
        values = []
        if provider_id is not None:
            update_parts.append("provider_id = %s")
            values.append(provider_id)
        if amount is not None:
            update_parts.append("amount = %s")
            values.append(amount)
        if transfer_date is not None:
            update_parts.append("transfer_date = %s")
            values.append(transfer_date)

        if not update_parts:
            print("No fields to update!")
            return

        values.append(transaction_id)

        update_query = f"""
            UPDATE eft_records
            SET {', '.join(update_parts)}
            WHERE transaction_id = %s
        """

        cur.execute(update_query, values)
        conn.commit()
        print("EFT record updated successfully!")

    except psycopg2.Error as e:
        print(f"Error updating EFT record: {e}")
        conn.rollback()

    finally:
        if cur:
            cur.close()
        if conn:
            conn.close()
def modify_weekly_provider_report(report_id, provider_id=None, week_end_date=None, total_consultations=None, total_fees=None):
    try:
        conn = psycopg2.connect(
            dbname="choco",
            user="dev",
            password="guest",
            host="localhost",
            port="5432"
        )
        cur = conn.cursor()

        # Check if the report exists
        cur.execute("SELECT report_id FROM weekly_provider_reports WHERE report_id = %s", (report_id,))
        if cur.fetchone() is None:
            print(f"Weekly provider report with report ID {report_id} does not exist!")
            return

        # Build update query dynamically
        update_parts = []
        values = []
        if provider_id is not None:
            update_parts.append("provider_id = %s")
            values.append(provider_id)
        if week_end_date is not None:
            update_parts.append("week_end_date = %s")
            values.append(week_end_date)
        if total_consultations is not None:
            update_parts.append("total_consultations = %s")
            values.append(total_consultations)
        if total_fees is not None:
            update_parts.append("total_fees = %s")
            values.append(total_fees)

        if not update_parts:
            print("No fields to update!")
            return

        values.append(report_id)

        update_query = f"""
            UPDATE weekly_provider_reports
            SET {', '.join(update_parts)}
            WHERE report_id = %s
        """

        cur.execute(update_query, values)
        conn.commit()
        print("Weekly provider report updated successfully!")

    except psycopg2.Error as e:
        print(f"Error updating weekly provider report: {e}")
        conn.rollback()

    finally:
        if cur:
            cur.close()
        if conn:
            conn.close()

# Validate Functions
def verify_member(member_id):
    try:
  
        conn = psycopg2.connect(
                    dbname="choco",
                    user="dev",
                    password="guest",
                    host="localhost",
                    port="5432"
                )  
        cur = conn.cursor()

        # Query to check if the member_id exists and retrieve the status and comments
        cur.execute("SELECT member_id, name, status, comments FROM members WHERE member_id = ?", (member_id,))

        # Fetch the member details
        member = cur.fetchone()  # Fetch a single row

        # Check if the member exists
        if member:
            member_id, name, status, comments = member  # Unpack the result
            
            # Check if the member is active
            if status.lower() == "active":
                print("Active Member Found!")
            else:
                print(f"Account Owner: {name}, Member Status: Inactive -> Comments: {comments}")       
        else:
            print("No Member Exists.")  # Print this if no member is found
            return False  # Return False if no matching member_id is found

        return True  # Return True if the member exists and has the required status

    except psycopg2.Error as e:
        print(f"Error retrieving member details: {e}")
        return False  # Return False in case of an error
    
    finally:
        # Ensure the connection is closed
        if cur:
            cur.close()
        if conn:
            conn.close()

def verify_service(service_id):
    try:
    
        conn = psycopg2.connect(
                    dbname="choco",
                    user="dev",
                    password="guest",
                    host="localhost",
                    port="5432"
                )  
        cur = conn.cursor()

        # Query to check if the service_id exists and retrieve the name and fee
        cur.execute("SELECT service_name, fee FROM services WHERE service_code = ?", (service_id,))

        # Fetch the service details
        service = cur.fetchone()  # Fetch a single row

        # Check if the service exists
        if service:
            service_name, fee = service  # Unpack the result
            print(f"Service Found: Name: {service_name}, Fee: ${fee:.2f}")
        else:
            print("No Service Exists with the provided service code.")  # Print if no service is found
            return False  # Return False if no matching service_code is found

        return True  # Return True if the service exists

    except psycopg2.Error as e:
        print(f"Error retrieving service details: {e}")
        return False  # Return False in case of an error

    finally:
        # Ensure the connection is closed
        if cur:
            cur.close()
        if conn:
            conn.close()
"""
# Test CREATE Functions

    create_member(
        "999888777",
        "Test Member",
        "123 Test St",
        "Portland",
        "OR",
        "97201"
    )

    create_provider(
        "888777666",
        "Test Provider",
        "456 Test Ave",
        "Portland",
        "OR",
        "97202"
    )

    create_service(
        "123456",
        "Test Service",
        199.99
    )

    create_service_record(
        "888777666",  # provider_id from above
        "999888777",  # member_id from above
        "123456",     # service_code from above
        datetime.now().date(),
        "Test service record"
    )

# Test RETRIEVE Functions

    print("\nRetrieving all members:")
    retrieve_member()

    print("\nRetrieving specific member:")
    retrieve_member(member_id="111111111")

    print("\nRetrieving all providers:")
    retrieve_provider()

    print("\nRetrieving specific provider:")
    retrieve_provider(provider_id="222222222")

    print("\nRetrieving all services:")
    retrieve_service()

    print("\nRetrieving specific service:")
    retrieve_service(service_code="555555")

    print("\nRetrieving all service records:")
    retrieve_service_records()

    print("\nRetrieving service records for specific provider:")
    retrieve_service_records(provider_id="222222222")

# Test DELETE Functions 

    delete_member("111111111")

    delete_provider("222222222")

    delete_service("555555")

    delete_service_record(1) 


# Test MODIFY Functions

    modify_member(
       "111111111",
       name="Updated Member",
       street_address="456 New St",
       status="suspended"
   )
   
   modify_provider(
       "222222222",
       name="Updated Provider",
       city="Salem"
   )
   
   modify_service(
       "555555",
       service_name="Updated Service",
       fee=299.99
   )

"""
