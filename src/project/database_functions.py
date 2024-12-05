import psycopg2

# For Testing 
from datetime import datetime


#### FUNCTION PROTOTYPES ####


### CREATE ###

## CREATE MEMBER
# create_member(member id, name, street address, city, state, zip code, status)

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

def create_provider_report( provider_id, week_end_date, total_consultations, total_fees):
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
        INSERT INTO weekly_provider_reports (provider_id, week_end_date, total_consultations, total_fees)
        VALUES (%s, %s, %s, %s)
        """

        cur.execute(insert_query, (provider_id, week_end_date, total_consultations, total_fees))
        conn.commit()
        print("Provider record created successfully!")

    except psycopg2.Error as e:
        print(f"Error creating provider record: {e}")
        conn.rollback()

    finally:
        if cur:
            cur.close()
        if conn:
            conn.close()

def create_eft_report( provider_id, amount, transfer_date):
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
        INSERT INTO eft_records (provider_id, amount, transfer_date)
        VALUES (%s, %s, %s)
        """

        cur.execute(insert_query, (provider_id, amount, transfer_date))
        conn.commit()
        print("Eft record created successfully!")

    except psycopg2.Error as e:
        print(f"Error creating Eft record: {e}")
        conn.rollback()

    finally:
        if cur:
            cur.close()
        if conn:
            conn.close()

# Retrieve / Printing Functions
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
            cur.execute("SELECT * FROM members WHERE member_id = %s", (member_id,))
        elif name:
            cur.execute("SELECT * FROM members WHERE name LIKE %s", ('%' + name + '%',))
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

def retrieve_service(service_code=None):
    try:
        conn = psycopg2.connect(
                dbname="choco",
                user="dev",
                password="guest",
                host="localhost",
                port="5432"
                )
        cur = conn.cursor()

        if service_code:
            cur.execute("SELECT * FROM services WHERE service_code = %s", (service_code,))
        else:
            cur.execute("SELECT * FROM services")

        rows = cur.fetchall()
        for row in rows:
            print(f"Service: {row}")
        return rows

    except psycopg2.Error as e:
        print(f"Error retrieving service(s): {e}")
        return None

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

def retrieve_provider_report(provider_id=None, week_end_date=None):
    try:
        conn = psycopg2.connect(
            dbname="choco",
            user="dev",
            password="guest",
            host="localhost",
            port="5432"
        )
        cur = conn.cursor()

        if provider_id and week_end_date:
            # Query to fetch the report and provider details
            cur.execute("""
                SELECT DISTINCT
                    p.name AS provider_name,
                    p.street_address,
                    p.city,
                    p.state,
                    p.zip_code,
                    r.total_consultations,
                    r.total_fees
                FROM 
                    providers p
                INNER JOIN 
                    weekly_provider_reports r ON p.provider_id = r.provider_id
                WHERE 
                    r.provider_id = %s AND r.week_end_date = %s
            """, (provider_id, week_end_date))

            provider_details = cur.fetchone()
            if not provider_details:
                print("No report found for the specified provider and week.")
                return

            print("\n=== Provider Report ===")
            print(f"Name: {provider_details[0]}")
            print(f"Address: {provider_details[1]}, {provider_details[2]}, {provider_details[3]} {provider_details[4]}")
            print(f"Total Consultations: {provider_details[5]}")
            print(f"Total Fees: ${provider_details[6]:.2f}")

            # Query to fetch all services provided during the week along with member names
            cur.execute("""
                SELECT 
                    s.record_id,
                    s.service_date,
                    s.service_code,
                    m.name AS member_name,
                    s.comments
                FROM 
                    service_records s
                INNER JOIN 
                    members m ON s.member_id = m.member_id
                WHERE 
                    s.provider_id = %s AND s.service_date <= %s
                ORDER BY 
                    s.service_date
            """, (provider_id, week_end_date))

            services = cur.fetchall()
            if services:
                print("\n=== Services Provided ===")
                for service in services:
                    print(f"Record ID: {service[0]}")
                    print(f"  Date: {service[1]}")
                    print(f"  Service Code: {service[2]}")
                    print(f"  Member: {service[3]}")
                    print(f"  Comments: {service[4]}")
            else:
                print("\nNo services provided during this period.")

        else:
            print("Please provide both provider_id and week_end_date to retrieve the report.")

    except psycopg2.Error as e:
        print(f"Error retrieving report: {e}")
    
    finally:
        if cur:
            cur.close()
        if conn:
            conn.close()

def retrieve_member_report(week_start_date, week_end_date):
    try:
        # Connect to the PostgreSQL database
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
                s.service_date BETWEEN %s AND %s
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

from datetime import date
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
