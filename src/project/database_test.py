import sqlite3



# Function to create a member in the database
def create_member(member_id, name, street_address, city, state, zip_code, status='active'):
    try:
        conn = sqlite3.connect('local_database.db')  # Use your SQLite file name here
        cur = conn.cursor()

        # SQL insert statement
        insert_query = """
        INSERT INTO members (member_id, name, street_address, city, state, zip_code, status)
        VALUES (?, ?, ?, ?, ?, ?, ?)
        """

        # Execute insert with values
        cur.execute(insert_query, (member_id, name, street_address, city, state, zip_code, status))

        # Commit the transaction
        conn.commit()
        print("Member created successfully!")
    
    except sqlite3.Error as e:
        print(f"Error creating member: {e}")
        conn.rollback()  # Rollback in case of error
    
    finally:
        if cur:
            cur.close()
        if conn:
            conn.close()

def create_provider_report(provider_id, week_start_date, week_end_date):
    try:
        # Connect to the SQLite database
        conn = sqlite3.connect("choco.db")
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

    except sqlite3.IntegrityError as e:
        print(f"Integrity error: {e}")
    except sqlite3.OperationalError as e:
        print(f"Operational error: {e}")
    except sqlite3.Error as e:
        print(f"SQLite error occurred: {e}")
    finally:
        # Ensure the connection is closed
        if cur:
            cur.close()
        if conn:
            conn.close()


# Function to retrieve member(s) by member_id or name
def retrieve_member(member_id=None, name=None):
    try:
        conn = sqlite3.connect('local_database.db')  # Use your SQLite file name here
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
    
    except sqlite3.Error as e:
        print(f"Error retrieving member(s): {e}")
        return None
    
    finally:
        if cur:
            cur.close()
        if conn:
            conn.close()

# Test function to create and retrieve a member
def test_create_and_retrieve_member():
    # Test data for the member
    test_member_id = 'M123456789'
    test_name = 'John Doe'
    test_street_address = '123 Main St'
    test_city = 'Springfield'
    test_state = 'IL'
    test_zip_code = '62701'

    # Step 1: Create the member
    create_member(test_member_id, test_name, test_street_address, test_city, test_state, test_zip_code)
    create_member("mark", "mark", "mark", "mark", "mark", "mark")
    # Step 2: Retrieve the member by member_id
    result = retrieve_member(member_id=test_member_id)

    # Check if the retrieved member is as expected
    if result:
        print("Test passed: Member retrieved successfully")
    else:
        print("Test failed: Member not found")

    # Optional: Clean up by deleting the member after test (if desired)
    try:
        conn = sqlite3.connect('local_database.db')  # Use your SQLite file name here
        cur = conn.cursor()
        # Delete the test member
        cur.execute("DELETE FROM members WHERE member_id = ?", (test_member_id,))
        conn.commit()
        print("Cleanup successful: Test member deleted.")
    except sqlite3.Error as e:
        print(f"Error deleting test member: {e}")
    finally:
        if cur:
            cur.close()
        if conn:
            conn.close()
from datetime import datetime

# Create Member Report
def retrieve_member_report(week_start_date, week_end_date):
    try:
        # Connect to the SQLite database
        conn = sqlite3.connect("choco.db")  # Use your SQLite database file
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

    except sqlite3.Error as e:
        print(f"Error retrieving member report: {e}")
    
    finally:
        if cur:
            cur.close()
        if conn:
            conn.close()
def print_service_codes():
    try:
        # Connect to the SQLite database
        conn = sqlite3.connect("choco.db")  # Replace with your actual database path
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

    except sqlite3.Error as e:
        print(f"Error retrieving service details: {e}")
    
    finally:
        # Ensure the connection is closed
        if cur:
            cur.close()
        if conn:
            conn.close()
# Create Table
def create_database():
    conn = sqlite3.connect("choco.db")
    cur = conn.cursor()

    # Drop the tables if they exist to avoid conflict
    cur.execute('DROP TABLE IF EXISTS weekly_provider_reports')
    cur.execute('DROP TABLE IF EXISTS service_records')
    cur.execute('DROP TABLE IF EXISTS services')
    cur.execute('DROP TABLE IF EXISTS providers')
    cur.execute('DROP TABLE IF EXISTS members')

    # Create the 'members' table
    cur.execute(''' 
        CREATE TABLE IF NOT EXISTS members (
            member_id INTEGER PRIMARY KEY AUTOINCREMENT,
            name TEXT NOT NULL,
            street_address TEXT NOT NULL,
            city TEXT NOT NULL,
            state TEXT NOT NULL,
            zip_code TEXT NOT NULL,
            status TEXT NOT NULL,
            comments TEXT DEFAULT NULL
        );
    ''')

    # Create the 'providers' table
    cur.execute('''
        CREATE TABLE IF NOT EXISTS providers (
            provider_id INTEGER PRIMARY KEY AUTOINCREMENT,
            name TEXT NOT NULL,
            street_address TEXT NOT NULL,
            city TEXT NOT NULL,
            state TEXT NOT NULL,
            zip_code TEXT NOT NULL
        );
    ''')

    # Create the 'services' table with the 'fee' column
    cur.execute('''
        CREATE TABLE IF NOT EXISTS services (
            service_code TEXT PRIMARY KEY,
            service_name TEXT NOT NULL,
            fee REAL NOT NULL CHECK(fee <= 999.99)
        );
    ''')

    # Create the 'service_records' table with foreign keys
    cur.execute('''
        CREATE TABLE IF NOT EXISTS service_records (
            record_id INTEGER PRIMARY KEY AUTOINCREMENT,
            member_id INTEGER,
            provider_id INTEGER,
            service_code TEXT,
            service_date TEXT,
            FOREIGN KEY (member_id) REFERENCES members (member_id),
            FOREIGN KEY (provider_id) REFERENCES providers (provider_id),
            FOREIGN KEY (service_code) REFERENCES services (service_code)
        );
    ''')

    # Create the 'weekly_provider_reports' table with foreign keys
    cur.execute('''
        CREATE TABLE IF NOT EXISTS weekly_provider_reports (
            report_id INTEGER PRIMARY KEY AUTOINCREMENT,
            provider_id INTEGER NOT NULL,
            week_end_date TEXT NOT NULL,
            total_consultations INTEGER CHECK(total_consultations <= 999),
            total_fees REAL CHECK(total_fees <= 99999.99),
            FOREIGN KEY (provider_id) REFERENCES providers(provider_id) ON DELETE CASCADE
        );
    ''')

    cur.execute('''
        CREATE TABLE IF NOT EXISTS consultation_records (
        consultation_id INTEGER PRIMARY KEY AUTOINCREMENT, 
        provider_id INTEGER NOT NULL,
        member_id INTEGER NOT NULL,  
        consultation_date DATE NOT NULL, 
        comments TEXT NOT NULL,  
        FOREIGN KEY (provider_id) REFERENCES providers(provider_id) ON DELETE CASCADE,  
        FOREIGN KEY (member_id) REFERENCES members(member_id) ON DELETE CASCADE    
        );
                
    ''')
   
    # Commit changes and close the connection
    conn.commit()
    conn.close()

# Call the function to 
# Call this function to create the database and tables
create_database()

# Insert Data Into member provider service and record table
def insert_test_data():
    conn = sqlite3.connect("choco.db")
    cur = conn.cursor()

    # Insert members without specifying member_id (auto-increment will handle it)
    cur.execute("INSERT INTO members (name, street_address, city, state, zip_code, status, comments) VALUES ('John Doe', '123 Main St', 'Springfield', 'IL', '62701', 'active', 'None')")
    cur.execute("INSERT INTO members (name, street_address, city, state, zip_code, status, comments) VALUES ('Jane Smith', '456 Oak St', 'Chicago', 'IL', '60601', 'suspended', 'Unpaid membership')")

    # Insert providers with unique provider_id
    cur.execute("INSERT INTO providers (name, street_address, city, state, zip_code) VALUES ('Provider A', '7110 sw queen ln', 'beaverton', 'oregon', '97008')")
    cur.execute("INSERT INTO providers (name, street_address, city, state, zip_code) VALUES ('Provider B', '15500 sw queen ln', 'beaverton', 'oregon', '97008')")

    # Insert services (ensure unique service_code values)
    cur.execute("INSERT INTO services (service_code, service_name, fee) VALUES ('SVC001', 'Service 1', 99.99)")
    cur.execute("INSERT INTO services (service_code, service_name, fee) VALUES ('SVC002', 'Service 2', 49.50)")

    # Insert service records using INSERT OR IGNORE to prevent duplicates
    cur.execute("""
        INSERT OR IGNORE INTO service_records (member_id, provider_id, service_code, service_date) 
        VALUES (1, 1, 'SVC001', '2024-12-01')
    """)
    cur.execute("""
        INSERT OR IGNORE INTO service_records (member_id, provider_id, service_code, service_date) 
        VALUES (1, 2, 'SVC002', '2024-12-02')
    """)
    cur.execute("""
        INSERT OR IGNORE INTO service_records (member_id, provider_id, service_code, service_date) 
        VALUES (2, 1, 'SVC001', '2024-12-03')
    """)


    conn.commit()
    conn.close()
    
def add_consultation(provider_id, member_id, consultation_date, comments):
    try:
        # Connect to the SQLite database
        conn = sqlite3.connect("choco.db")  # Replace with your actual database path
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

    except sqlite3.Error as e:
        print(f"Error adding consultation record: {e}")
        return False  # Return False in case of an error

    finally:
        # Ensure the connection is closed
        if cur:
            cur.close()
        if conn:
            conn.close()
def clear_consultation_table():
    try:
        # Connect to the SQLite database
        conn = sqlite3.connect("choco.db")  # Replace with your actual database path
        cur = conn.cursor()

        # Delete all records from the consultation_records table
        cur.execute("DELETE FROM consultation_records")

        # Reset the auto-increment counter for consultation_id
        cur.execute("DELETE FROM sqlite_sequence WHERE name='consultation_records'")

        # Commit the transaction
        conn.commit()

        print("All consultation records have been cleared and the ID counter has been reset.")

    except sqlite3.Error as e:
        print(f"Error clearing consultation records and resetting ID: {e}")

    finally:
        # Ensure the connection is closed
        if cur:
            cur.close()
        if conn:
            conn.close()

# Call the function
clear_consultation_table()

def display_consultations():
    try:
        # Connect to the SQLite database
        conn = sqlite3.connect("choco.db")  # Replace with your actual database path
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

    except sqlite3.Error as e:
        print(f"Error retrieving consultation records: {e}")

    finally:
        # Ensure the connection is closed
        if cur:
            cur.close()
        if conn:
            conn.close()

def verify_service(service_id):
    try:
        # Connect to the SQLite database
        conn = sqlite3.connect("choco.db")  # Replace with your actual database path
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

    except sqlite3.Error as e:
        print(f"Error retrieving service details: {e}")
        return False  # Return False in case of an error

    finally:
        # Ensure the connection is closed
        if cur:
            cur.close()
        if conn:
            conn.close()

def manager_reports(weekstart_date, weekend_date):
    try:
        # Connect to the SQLite database
        conn = sqlite3.connect("choco.db")  # Replace with your actual database path
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

    except sqlite3.Error as e:
        print(f"Error retrieving manager reports: {e}")

    finally:
        # Ensure the connection is closed
        if cur:
            cur.close()
        if conn:
            conn.close()

def verify_member(member_id):
    try:
        # Connect to the SQLite database
        conn = sqlite3.connect("choco.db")  # Replace with your actual database path
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

    except sqlite3.Error as e:
        print(f"Error retrieving member details: {e}")
        return False  # Return False in case of an error
    
    finally:
        # Ensure the connection is closed
        if cur:
            cur.close()
        if conn:
            conn.close()
def test_retrieve_member_report():
    # Define the week range
    week_start_date = '2024-12-01'
    week_end_date = '2024-12-07'
    
    # Call the function to retrieve the report
    retrieve_member_report(week_start_date, week_end_date)

import sqlite3
from datetime import datetime

def printmembers():
    try:
        # Connect to the SQLite database
        conn = sqlite3.connect("choco.db")  # Replace with your actual database path
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

    except sqlite3.Error as e:
        print(f"Error retrieving member details: {e}")
    
    finally:
        # Ensure the connection is closed
        if cur:
            cur.close()
        if conn:
            conn.close()    
#Print Provider Report
def retrieve_provider_report(provider_id=None, week_start_date=None, week_end_date=None):
    try:
        # Connect to the SQLite database
        conn = sqlite3.connect("choco.db")  # Replace with your database path
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

    except sqlite3.Error as e:
        print(f"Error retrieving report: {e}")
    
    finally:
        if cur:
            cur.close()
        if conn:
            conn.close()



#Testing the provider report function
def test_retrieve_provider_report():
    # Define the provider ID and the week range for the test
    provider_id = 1  # Use an existing provider_id (e.g., Provider A)
    week_start_date = '2024-12-01'
    week_end_date = '2024-12-07'

    # Call the function to retrieve the provider report
    retrieve_provider_report(provider_id, week_start_date, week_end_date)


# Call the test function
if __name__ == "__main__":
 #   create_provider_report(1, "2024-12-01", "2024-12-07")
  #  create_provider_report(2, "2024-12-01", "2024-12-07")
    insert_test_data()
    #test_retrieve_member_report()
    #test_retrieve_provider_report()
   # print_service_codes()
  #  printmembers()
    verify_member(2)
    verify_service("SVC001")

    add_consultation(1, 1, "2024-12-07", "consulation")
    add_consultation(1, 1, "2024-12-07", "meeting")
    display_consultations()
    # Example usage of the function
    manager_reports('2024-12-01', '2024-12-07')
  
# Printing Provider Reports
# 1. Add report into table using  create_provider_report(provider_id, Week_end_date), this will automatically add their total consulations, fees, and pervices provided
# 2. Next use retrieve_provider_report(provider_id, week_start_date, week_end_date) to find all reports

# Printing Member Reports
# 1. 