# import sqlite3
#
# # Connect to the database
# connection = sqlite3.connect('posts.db')
# cursor = connection.cursor()
#
# # Query the expense table
# cursor.execute('SELECT * FROM expense')
# expenses = cursor.fetchall()
#
# # Print each expense
# for expense in expenses:
#     print(expense)
#
# # Close the connection
# connection.close()



import sqlite3

# Connect to the database
connection = sqlite3.connect('posts.db')  # Ensure 'posts.db' exists
cursor = connection.cursor()

# Query the expense table
try:
    cursor.execute('SELECT * FROM expense')
    expenses = cursor.fetchall()

    # Check if the table is empty
    if not expenses:
        print("No expenses found in the database.")
    else:
        # Print each expense
        for expense in expenses:
            print(expense)

except sqlite3.OperationalError as e:
    print(f"Error: {e}. The table might not exist.")

# Close the connection
connection.close()
