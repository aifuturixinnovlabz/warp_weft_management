# import mysql.connector
# from mysql.connector import Error
# import streamlit as st
#
#
# class Database:
#     def __init__(self):
#         self.host = "localhost"
#         self.user = "root"
#         self.password = "root"  # CHANGE THIS TO YOUR PASSWORD
#         self.database = "warp_weft_db"
#
#     def get_connection(self):
#         """Create database connection"""
#         try:
#             connection = mysql.connector.connect(
#                 host=self.host,
#                 user=self.user,
#                 password=self.password,
#                 database=self.database
#             )
#             return connection
#         except Error as e:
#             st.error(f"Database connection error: {e}")
#             return None
#
#     # ========================================
#     # COLOR METHODS
#     # ========================================
#     def get_all_colors(self):
#         """Fetch all colors"""
#         connection = self.get_connection()
#         if connection:
#             try:
#                 cursor = connection.cursor()
#                 cursor.execute("SELECT color_name FROM colors ORDER BY color_name")
#                 colors = [row[0] for row in cursor.fetchall()]
#                 cursor.close()
#                 connection.close()
#                 return colors
#             except Error as e:
#                 st.error(f"Fetch colors error: {e}")
#                 return []
#         return []
#
#     def add_color(self, color_name):
#         """Add new color"""
#         connection = self.get_connection()
#         if connection:
#             try:
#                 cursor = connection.cursor()
#                 cursor.execute("INSERT INTO colors (color_name) VALUES (%s)", (color_name,))
#                 connection.commit()
#                 cursor.close()
#                 connection.close()
#                 return True
#             except Error as e:
#                 st.error(f"Add color error: {e}")
#                 return False
#         return False
#
#     def update_color(self, old_color_name, new_color_name):
#         """Update color name"""
#         connection = self.get_connection()
#         if connection:
#             try:
#                 cursor = connection.cursor()
#                 cursor.execute("UPDATE colors SET color_name = %s WHERE color_name = %s",
#                                (new_color_name, old_color_name))
#                 connection.commit()
#                 cursor.close()
#                 connection.close()
#                 return True
#             except Error as e:
#                 st.error(f"Update color error: {e}")
#                 return False
#         return False
#
#     def delete_color(self, color_name):
#         """Delete color"""
#         connection = self.get_connection()
#         if connection:
#             try:
#                 cursor = connection.cursor()
#                 cursor.execute("DELETE FROM colors WHERE color_name = %s", (color_name,))
#                 connection.commit()
#                 cursor.close()
#                 connection.close()
#                 return True
#             except Error as e:
#                 st.error(f"Delete color error: {e}")
#                 return False
#         return False
#
#     # ========================================
#     # PRODUCT CATEGORY METHODS
#     # ========================================
#     def get_all_product_categories(self):
#         """Fetch all product categories"""
#         connection = self.get_connection()
#         if connection:
#             try:
#                 cursor = connection.cursor()
#                 cursor.execute("SELECT category_name FROM product_categories ORDER BY category_name")
#                 categories = [row[0] for row in cursor.fetchall()]
#                 cursor.close()
#                 connection.close()
#                 return categories
#             except Error as e:
#                 st.error(f"Fetch categories error: {e}")
#                 return []
#         return []
#
#     def add_product_category(self, category_name):
#         """Add new product category"""
#         connection = self.get_connection()
#         if connection:
#             try:
#                 cursor = connection.cursor()
#                 cursor.execute("INSERT INTO product_categories (category_name) VALUES (%s)", (category_name,))
#                 connection.commit()
#                 cursor.close()
#                 connection.close()
#                 return True
#             except Error as e:
#                 st.error(f"Add category error: {e}")
#                 return False
#         return False
#
#     def update_product_category(self, old_category_name, new_category_name):
#         """Update product category"""
#         connection = self.get_connection()
#         if connection:
#             try:
#                 cursor = connection.cursor()
#                 cursor.execute("UPDATE product_categories SET category_name = %s WHERE category_name = %s",
#                                (new_category_name, old_category_name))
#                 connection.commit()
#                 cursor.close()
#                 connection.close()
#                 return True
#             except Error as e:
#                 st.error(f"Update category error: {e}")
#                 return False
#         return False
#
#     def delete_product_category(self, category_name):
#         """Delete product category"""
#         connection = self.get_connection()
#         if connection:
#             try:
#                 cursor = connection.cursor()
#                 cursor.execute("DELETE FROM product_categories WHERE category_name = %s", (category_name,))
#                 connection.commit()
#                 cursor.close()
#                 connection.close()
#                 return True
#             except Error as e:
#                 st.error(f"Delete category error: {e}")
#                 return False
#         return False
#
#     # ========================================
#     # JOB WORKER METHODS
#     # ========================================
#     def get_all_job_workers(self):
#         """Fetch all job workers"""
#         connection = self.get_connection()
#         if connection:
#             try:
#                 cursor = connection.cursor()
#                 cursor.execute("SELECT worker_name FROM job_workers ORDER BY worker_name")
#                 workers = [row[0] for row in cursor.fetchall()]
#                 cursor.close()
#                 connection.close()
#                 return workers
#             except Error as e:
#                 st.error(f"Fetch workers error: {e}")
#                 return []
#         return []
#
#     def get_job_worker_details(self, worker_name):
#         """Get detailed information about a job worker"""
#         connection = self.get_connection()
#         if connection:
#             try:
#                 cursor = connection.cursor(dictionary=True)
#                 cursor.execute("""
#                     SELECT worker_name, contact_number, gst_number, aadhar_number
#                     FROM job_workers
#                     WHERE worker_name = %s
#                 """, (worker_name,))
#                 details = cursor.fetchone()
#                 cursor.close()
#                 connection.close()
#                 return details
#             except Error as e:
#                 st.error(f"Fetch worker details error: {e}")
#                 return None
#         return None
#
#     def add_job_worker(self, worker_name, contact_number="", gst_number="", aadhar_number=""):
#         """Add new job worker"""
#         connection = self.get_connection()
#         if connection:
#             try:
#                 cursor = connection.cursor()
#                 cursor.execute("""
#                     INSERT INTO job_workers (worker_name, contact_number, gst_number, aadhar_number)
#                     VALUES (%s, %s, %s, %s)
#                 """, (worker_name, contact_number, gst_number, aadhar_number))
#                 connection.commit()
#                 cursor.close()
#                 connection.close()
#                 return True
#             except Error as e:
#                 st.error(f"Add worker error: {e}")
#                 return False
#         return False
#
#     def update_job_worker(self, old_worker_name, worker_name, contact_number, gst_number, aadhar_number):
#         """Update job worker"""
#         connection = self.get_connection()
#         if connection:
#             try:
#                 cursor = connection.cursor()
#                 cursor.execute("""
#                     UPDATE job_workers
#                     SET worker_name = %s, contact_number = %s, gst_number = %s, aadhar_number = %s
#                     WHERE worker_name = %s
#                 """, (worker_name, contact_number, gst_number, aadhar_number, old_worker_name))
#                 connection.commit()
#                 cursor.close()
#                 connection.close()
#                 return True
#             except Error as e:
#                 st.error(f"Update worker error: {e}")
#                 return False
#         return False
#
#     def delete_job_worker(self, worker_name):
#         """Delete job worker"""
#         connection = self.get_connection()
#         if connection:
#             try:
#                 cursor = connection.cursor()
#                 cursor.execute("DELETE FROM job_workers WHERE worker_name = %s", (worker_name,))
#                 connection.commit()
#                 cursor.close()
#                 connection.close()
#                 return True
#             except Error as e:
#                 st.error(f"Delete worker error: {e}")
#                 return False
#         return False
#
#     # ========================================
#     # INVENTORY WARP METHODS
#     # ========================================
#     def get_available_inventory_warp(self):
#         """Get total available WARP in inventory (not yet distributed)"""
#         connection = self.get_connection()
#         if connection:
#             try:
#                 cursor = connection.cursor()
#                 # Total inventory WARP
#                 cursor.execute("SELECT COALESCE(SUM(beem_weight - paper_weight), 0) FROM inventory_warp")
#                 total_inventory = float(cursor.fetchone()[0])
#
#                 # Total distributed to job workers
#                 cursor.execute("SELECT COALESCE(SUM(beem_weight - paper_weight), 0) FROM job_worker_warp")
#                 total_distributed = float(cursor.fetchone()[0])
#
#                 cursor.close()
#                 connection.close()
#
#                 return max(0, total_inventory - total_distributed)
#             except Error as e:
#                 st.error(f"Get available inventory WARP error: {e}")
#                 return 0
#         return 0
#
#     def insert_inventory_warp(self, data):
#         """Insert WARP entry to inventory"""
#         connection = self.get_connection()
#         if connection:
#             try:
#                 cursor = connection.cursor()
#                 query = """INSERT INTO inventory_warp (date, yarn_name, design, paper_weight, beem_weight)
#                            VALUES (%s, %s, %s, %s, %s)"""
#                 cursor.execute(query, data)
#                 connection.commit()
#                 cursor.close()
#                 connection.close()
#                 return True
#             except Error as e:
#                 st.error(f"Insert inventory WARP error: {e}")
#                 return False
#         return False
#
#     def get_inventory_warp(self):
#         """Fetch all inventory WARP records"""
#         connection = self.get_connection()
#         if connection:
#             try:
#                 cursor = connection.cursor(dictionary=True)
#                 cursor.execute("""
#                     SELECT id, date, yarn_name, design, paper_weight, beem_weight,
#                            (beem_weight - paper_weight) as net_weight, created_at
#                     FROM inventory_warp
#                     ORDER BY date DESC
#                 """)
#                 records = cursor.fetchall()
#                 cursor.close()
#                 connection.close()
#                 return records
#             except Error as e:
#                 st.error(f"Fetch inventory WARP error: {e}")
#                 return []
#         return []
#
#     # ========================================
#     # INVENTORY WEFT METHODS
#     # ========================================
#     def get_available_inventory_weft(self):
#         """Get total available WEFT in inventory (not yet distributed)"""
#         connection = self.get_connection()
#         if connection:
#             try:
#                 cursor = connection.cursor()
#                 # Total inventory WEFT
#                 cursor.execute("SELECT COALESCE(SUM(no_of_cones * weight_per_cone), 0) FROM inventory_weft")
#                 total_inventory = float(cursor.fetchone()[0])
#
#                 # Total distributed to job workers
#                 cursor.execute("SELECT COALESCE(SUM(no_of_cones * weight_per_cone), 0) FROM job_worker_weft")
#                 total_distributed = float(cursor.fetchone()[0])
#
#                 cursor.close()
#                 connection.close()
#
#                 return max(0, total_inventory - total_distributed)
#             except Error as e:
#                 st.error(f"Get available inventory WEFT error: {e}")
#                 return 0
#         return 0
#
#     def insert_inventory_weft(self, data):
#         """Insert WEFT entry to inventory"""
#         connection = self.get_connection()
#         if connection:
#             try:
#                 cursor = connection.cursor()
#                 query = """INSERT INTO inventory_weft (date, colour, no_of_cones, weight_per_cone)
#                            VALUES (%s, %s, %s, %s)"""
#                 cursor.execute(query, data)
#                 connection.commit()
#                 cursor.close()
#                 connection.close()
#                 return True
#             except Error as e:
#                 st.error(f"Insert inventory WEFT error: {e}")
#                 return False
#         return False
#
#     def get_inventory_weft(self):
#         """Fetch all inventory WEFT records"""
#         connection = self.get_connection()
#         if connection:
#             try:
#                 cursor = connection.cursor(dictionary=True)
#                 cursor.execute("""
#                     SELECT id, date, colour, no_of_cones, weight_per_cone,
#                            (no_of_cones * weight_per_cone) as total_weight, created_at
#                     FROM inventory_weft
#                     ORDER BY date DESC
#                 """)
#                 records = cursor.fetchall()
#                 cursor.close()
#                 connection.close()
#                 return records
#             except Error as e:
#                 st.error(f"Fetch inventory WEFT error: {e}")
#                 return []
#         return []
#
#     # ========================================
#     # JOB WORKER WARP METHODS
#     # ========================================
#     def insert_job_worker_warp(self, data):
#         """Insert WARP entry for job worker"""
#         connection = self.get_connection()
#         if connection:
#             try:
#                 cursor = connection.cursor()
#                 query = """INSERT INTO job_worker_warp (date, yarn_name, design, paper_weight, beem_weight, job_worker)
#                            VALUES (%s, %s, %s, %s, %s, %s)"""
#                 cursor.execute(query, data)
#                 connection.commit()
#                 cursor.close()
#                 connection.close()
#                 return True
#             except Error as e:
#                 st.error(f"Insert job worker WARP error: {e}")
#                 return False
#         return False
#
#     def get_job_worker_warp(self):
#         """Fetch all job worker WARP records"""
#         connection = self.get_connection()
#         if connection:
#             try:
#                 cursor = connection.cursor(dictionary=True)
#                 cursor.execute("""
#                     SELECT id, date, yarn_name, design, paper_weight, beem_weight,
#                            (beem_weight - paper_weight) as net_weight, job_worker, created_at
#                     FROM job_worker_warp
#                     ORDER BY date DESC
#                 """)
#                 records = cursor.fetchall()
#                 cursor.close()
#                 connection.close()
#                 return records
#             except Error as e:
#                 st.error(f"Fetch job worker WARP error: {e}")
#                 return []
#         return []
#
#     def get_job_worker_warp_by_date(self, job_worker, from_date, to_date):
#         """Fetch job worker WARP records within date range"""
#         connection = self.get_connection()
#         if connection:
#             try:
#                 cursor = connection.cursor(dictionary=True)
#                 cursor.execute("""
#                     SELECT id, date, yarn_name, design, paper_weight, beem_weight,
#                            (beem_weight - paper_weight) as net_weight, job_worker, created_at
#                     FROM job_worker_warp
#                     WHERE job_worker = %s AND date BETWEEN %s AND %s
#                     ORDER BY date DESC
#                 """, (job_worker, from_date, to_date))
#                 records = cursor.fetchall()
#                 cursor.close()
#                 connection.close()
#                 return records
#             except Error as e:
#                 st.error(f"Fetch job worker WARP by date error: {e}")
#                 return []
#         return []
#
#     # ========================================
#     # JOB WORKER WEFT METHODS
#     # ========================================
#     def insert_job_worker_weft(self, data):
#         """Insert WEFT entry for job worker"""
#         connection = self.get_connection()
#         if connection:
#             try:
#                 cursor = connection.cursor()
#                 query = """INSERT INTO job_worker_weft (date, colour, no_of_cones, weight_per_cone, job_worker)
#                            VALUES (%s, %s, %s, %s, %s)"""
#                 cursor.execute(query, data)
#                 connection.commit()
#                 cursor.close()
#                 connection.close()
#                 return True
#             except Error as e:
#                 st.error(f"Insert job worker WEFT error: {e}")
#                 return False
#         return False
#
#     def get_job_worker_weft(self):
#         """Fetch all job worker WEFT records"""
#         connection = self.get_connection()
#         if connection:
#             try:
#                 cursor = connection.cursor(dictionary=True)
#                 cursor.execute("""
#                     SELECT id, date, colour, no_of_cones, weight_per_cone,
#                            (no_of_cones * weight_per_cone) as total_weight, job_worker, created_at
#                     FROM job_worker_weft
#                     ORDER BY date DESC
#                 """)
#                 records = cursor.fetchall()
#                 cursor.close()
#                 connection.close()
#                 return records
#             except Error as e:
#                 st.error(f"Fetch job worker WEFT error: {e}")
#                 return []
#         return []
#
#     def get_job_worker_weft_by_date(self, job_worker, from_date, to_date):
#         """Fetch job worker WEFT records within date range"""
#         connection = self.get_connection()
#         if connection:
#             try:
#                 cursor = connection.cursor(dictionary=True)
#                 cursor.execute("""
#                     SELECT id, date, colour, no_of_cones, weight_per_cone,
#                            (no_of_cones * weight_per_cone) as total_weight, job_worker, created_at
#                     FROM job_worker_weft
#                     WHERE job_worker = %s AND date BETWEEN %s AND %s
#                     ORDER BY date DESC
#                 """, (job_worker, from_date, to_date))
#                 records = cursor.fetchall()
#                 cursor.close()
#                 connection.close()
#                 return records
#             except Error as e:
#                 st.error(f"Fetch job worker WEFT by date error: {e}")
#                 return []
#         return []
#
#     # ========================================
#     # PRODUCT METHODS
#     # ========================================
#     def insert_product(self, data):
#         """Insert completed product with warp_used and weft_used"""
#         connection = self.get_connection()
#         if connection:
#             try:
#                 cursor = connection.cursor()
#                 query = """INSERT INTO products (job_worker, product_category, completion_date,
#                            total_pieces, total_meters, product_weight, warp_used, weft_used, notes)
#                            VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s)"""
#                 cursor.execute(query, data)
#                 connection.commit()
#                 cursor.close()
#                 connection.close()
#                 return True
#             except Error as e:
#                 st.error(f"Insert product error: {e}")
#                 return False
#         return False
#
#     def get_products(self):
#         """Fetch all products"""
#         connection = self.get_connection()
#         if connection:
#             try:
#                 cursor = connection.cursor(dictionary=True)
#                 cursor.execute("""
#                     SELECT * FROM products
#                     ORDER BY completion_date DESC
#                 """)
#                 records = cursor.fetchall()
#                 cursor.close()
#                 connection.close()
#                 return records
#             except Error as e:
#                 st.error(f"Fetch products error: {e}")
#                 return []
#         return []
#
#     def get_products_by_worker_and_date(self, job_worker, from_date, to_date):
#         """Fetch products by worker within date range"""
#         connection = self.get_connection()
#         if connection:
#             try:
#                 cursor = connection.cursor(dictionary=True)
#                 cursor.execute("""
#                     SELECT * FROM products
#                     WHERE job_worker = %s AND completion_date BETWEEN %s AND %s
#                     ORDER BY completion_date DESC
#                 """, (job_worker, from_date, to_date))
#                 records = cursor.fetchall()
#                 cursor.close()
#                 connection.close()
#                 return records
#             except Error as e:
#                 st.error(f"Fetch products by worker and date error: {e}")
#                 return []
#         return []
#
#     # ========================================
#     # BALANCE AND STATISTICS
#     # ========================================
#     def get_worker_balance(self, job_worker):
#         """Get current balance for a job worker"""
#         connection = self.get_connection()
#         if connection:
#             try:
#                 cursor = connection.cursor()
#
#                 # Get total WARP distributed
#                 cursor.execute("""
#                     SELECT COALESCE(SUM(beem_weight - paper_weight), 0)
#                     FROM job_worker_warp
#                     WHERE job_worker = %s
#                 """, (job_worker,))
#                 warp_total = float(cursor.fetchone()[0])
#
#                 # Get total WEFT distributed
#                 cursor.execute("""
#                     SELECT COALESCE(SUM(no_of_cones * weight_per_cone), 0)
#                     FROM job_worker_weft
#                     WHERE job_worker = %s
#                 """, (job_worker,))
#                 weft_total = float(cursor.fetchone()[0])
#
#                 # Get material used in products
#                 cursor.execute("""
#                     SELECT COALESCE(SUM(warp_used), 0), COALESCE(SUM(weft_used), 0)
#                     FROM products
#                     WHERE job_worker = %s
#                 """, (job_worker,))
#                 result = cursor.fetchone()
#                 warp_used = float(result[0])
#                 weft_used = float(result[1])
#
#                 cursor.close()
#                 connection.close()
#
#                 return {
#                     'warp_balance': max(0, warp_total - warp_used),
#                     'weft_balance': max(0, weft_total - weft_used)
#                 }
#             except Error as e:
#                 st.error(f"Get worker balance error: {e}")
#                 return {'warp_balance': 0, 'weft_balance': 0}
#         return {'warp_balance': 0, 'weft_balance': 0}
#
#     def get_dashboard_stats(self):
#         """Get statistics for dashboard"""
#         connection = self.get_connection()
#         if connection:
#             try:
#                 cursor = connection.cursor()
#
#                 # Total inventory WARP (procured)
#                 cursor.execute("SELECT COALESCE(SUM(beem_weight - paper_weight), 0) FROM inventory_warp")
#                 total_inventory_warp = float(cursor.fetchone()[0])
#
#                 # Total inventory WEFT (procured)
#                 cursor.execute("SELECT COALESCE(SUM(no_of_cones * weight_per_cone), 0) FROM inventory_weft")
#                 total_inventory_weft = float(cursor.fetchone()[0])
#
#                 # Job Worker WARP (total distributed)
#                 cursor.execute("SELECT COALESCE(SUM(beem_weight - paper_weight), 0) FROM job_worker_warp")
#                 job_worker_warp_distributed = float(cursor.fetchone()[0])
#
#                 # Job Worker WEFT (total distributed)
#                 cursor.execute("SELECT COALESCE(SUM(no_of_cones * weight_per_cone), 0) FROM job_worker_weft")
#                 job_worker_weft_distributed = float(cursor.fetchone()[0])
#
#                 # Available inventory (not distributed yet)
#                 available_inventory_warp = max(0, total_inventory_warp - job_worker_warp_distributed)
#                 available_inventory_weft = max(0, total_inventory_weft - job_worker_weft_distributed)
#
#                 # Material used in products
#                 cursor.execute("SELECT COALESCE(SUM(warp_used), 0), COALESCE(SUM(weft_used), 0) FROM products")
#                 result = cursor.fetchone()
#                 warp_used = float(result[0])
#                 weft_used = float(result[1])
#
#                 # Current job worker balances (distributed - used)
#                 job_worker_warp = max(0, job_worker_warp_distributed - warp_used)
#                 job_worker_weft = max(0, job_worker_weft_distributed - weft_used)
#
#                 # Finished products stats
#                 cursor.execute("""
#                     SELECT
#                         COUNT(*) as count,
#                         COALESCE(SUM(product_weight), 0) as total_weight,
#                         COALESCE(SUM(total_pieces), 0) as total_pieces,
#                         COALESCE(SUM(total_meters), 0) as total_meters
#                     FROM products
#                 """)
#                 product_stats = cursor.fetchone()
#
#                 cursor.close()
#                 connection.close()
#
#                 return {
#                     'inventory_warp': available_inventory_warp,
#                     'inventory_weft': available_inventory_weft,
#                     'job_worker_warp': job_worker_warp,
#                     'job_worker_weft': job_worker_weft,
#                     'finished_products_count': product_stats[0],
#                     'finished_products_weight': float(product_stats[1]),
#                     'total_pieces': int(product_stats[2]),
#                     'total_meters': float(product_stats[3])
#                 }
#             except Error as e:
#                 st.error(f"Get dashboard stats error: {e}")
#                 return {
#                     'inventory_warp': 0,
#                     'inventory_weft': 0,
#                     'job_worker_warp': 0,
#                     'job_worker_weft': 0,
#                     'finished_products_count': 0,
#                     'finished_products_weight': 0,
#                     'total_pieces': 0,
#                     'total_meters': 0
#                 }
#         return {
#             'inventory_warp': 0,
#             'inventory_weft': 0,
#             'job_worker_warp': 0,
#             'job_worker_weft': 0,
#             'finished_products_count': 0,
#             'finished_products_weight': 0,
#             'total_pieces': 0,
#             'total_meters': 0
#         }



import mysql.connector
from mysql.connector import Error
import streamlit as st


class Database:
    def __init__(self):
        self.host = "localhost"
        self.user = "root"
        self.password = "root"  # CHANGE THIS TO YOUR PASSWORD
        self.database = "warp_weft_db"

    def get_connection(self):
        """Create database connection"""
        try:
            connection = mysql.connector.connect(
                host=self.host,
                user=self.user,
                password=self.password,
                database=self.database
            )
            return connection
        except Error as e:
            st.error(f"Database connection error: {e}")
            return None

    # ========================================
    # COLOR METHODS
    # ========================================
    def get_all_colors(self):
        """Fetch all colors"""
        connection = self.get_connection()
        if connection:
            try:
                cursor = connection.cursor()
                cursor.execute("SELECT color_name FROM colors ORDER BY color_name")
                colors = [row[0] for row in cursor.fetchall()]
                cursor.close()
                connection.close()
                return colors
            except Error as e:
                st.error(f"Fetch colors error: {e}")
                return []
        return []

    def add_color(self, color_name):
        """Add new color"""
        connection = self.get_connection()
        if connection:
            try:
                cursor = connection.cursor()
                cursor.execute("INSERT INTO colors (color_name) VALUES (%s)", (color_name,))
                connection.commit()
                cursor.close()
                connection.close()
                return True
            except Error as e:
                st.error(f"Add color error: {e}")
                return False
        return False

    def update_color(self, old_color_name, new_color_name):
        """Update color name"""
        connection = self.get_connection()
        if connection:
            try:
                cursor = connection.cursor()
                cursor.execute("UPDATE colors SET color_name = %s WHERE color_name = %s",
                               (new_color_name, old_color_name))
                connection.commit()
                cursor.close()
                connection.close()
                return True
            except Error as e:
                st.error(f"Update color error: {e}")
                return False
        return False

    def delete_color(self, color_name):
        """Delete color"""
        connection = self.get_connection()
        if connection:
            try:
                cursor = connection.cursor()
                cursor.execute("DELETE FROM colors WHERE color_name = %s", (color_name,))
                connection.commit()
                cursor.close()
                connection.close()
                return True
            except Error as e:
                st.error(f"Delete color error: {e}")
                return False
        return False

    def check_color_usage(self, color_name):
        """Check if color is used in inventory or job worker tables"""
        connection = self.get_connection()
        if connection:
            try:
                cursor = connection.cursor()
                cursor.execute("SELECT COUNT(*) FROM inventory_weft WHERE colour = %s", (color_name,))
                inventory_count = cursor.fetchone()[0]
                cursor.execute("SELECT COUNT(*) FROM job_worker_weft WHERE colour = %s", (color_name,))
                jw_count = cursor.fetchone()[0]
                cursor.close()
                connection.close()
                return inventory_count + jw_count
            except Error as e:
                st.error(f"Check color usage error: {e}")
                return 0
        return 0

    # ========================================
    # YARN/MATERIAL METHODS (NEW)
    # ========================================
    def get_all_yarn_materials(self):
        """Fetch all yarn/materials"""
        connection = self.get_connection()
        if connection:
            try:
                cursor = connection.cursor()
                cursor.execute("SELECT material_name FROM yarn_materials ORDER BY material_name")
                materials = [row[0] for row in cursor.fetchall()]
                cursor.close()
                connection.close()
                return materials
            except Error as e:
                st.error(f"Fetch yarn materials error: {e}")
                return []
        return []

    def add_yarn_material(self, material_name):
        """Add new yarn/material"""
        connection = self.get_connection()
        if connection:
            try:
                cursor = connection.cursor()
                cursor.execute("INSERT INTO yarn_materials (material_name) VALUES (%s)", (material_name,))
                connection.commit()
                cursor.close()
                connection.close()
                return True
            except Error as e:
                st.error(f"Add yarn material error: {e}")
                return False
        return False

    def update_yarn_material(self, old_material_name, new_material_name):
        """Update yarn/material name"""
        connection = self.get_connection()
        if connection:
            try:
                cursor = connection.cursor()
                cursor.execute("UPDATE yarn_materials SET material_name = %s WHERE material_name = %s",
                               (new_material_name, old_material_name))
                connection.commit()
                cursor.close()
                connection.close()
                return True
            except Error as e:
                st.error(f"Update yarn material error: {e}")
                return False
        return False

    def delete_yarn_material(self, material_name):
        """Delete yarn/material"""
        connection = self.get_connection()
        if connection:
            try:
                cursor = connection.cursor()
                cursor.execute("DELETE FROM yarn_materials WHERE material_name = %s", (material_name,))
                connection.commit()
                cursor.close()
                connection.close()
                return True
            except Error as e:
                st.error(f"Delete yarn material error: {e}")
                return False
        return False

    def check_yarn_material_usage(self, material_name):
        """Check if yarn/material is used in inventory or job worker tables"""
        connection = self.get_connection()
        if connection:
            try:
                cursor = connection.cursor()
                cursor.execute("SELECT COUNT(*) FROM inventory_warp WHERE yarn_name = %s", (material_name,))
                inventory_count = cursor.fetchone()[0]
                cursor.execute("SELECT COUNT(*) FROM job_worker_warp WHERE yarn_name = %s", (material_name,))
                jw_count = cursor.fetchone()[0]
                cursor.close()
                connection.close()
                return inventory_count + jw_count
            except Error as e:
                st.error(f"Check yarn material usage error: {e}")
                return 0
        return 0

    # ========================================
    # DESIGN/WEAVE TYPE METHODS (NEW)
    # ========================================
    def get_all_design_weave_types(self):
        """Fetch all design/weave types"""
        connection = self.get_connection()
        if connection:
            try:
                cursor = connection.cursor()
                cursor.execute("SELECT design_name FROM design_weave_types ORDER BY design_name")
                designs = [row[0] for row in cursor.fetchall()]
                cursor.close()
                connection.close()
                return designs
            except Error as e:
                st.error(f"Fetch design weave types error: {e}")
                return []
        return []

    def add_design_weave_type(self, design_name):
        """Add new design/weave type"""
        connection = self.get_connection()
        if connection:
            try:
                cursor = connection.cursor()
                cursor.execute("INSERT INTO design_weave_types (design_name) VALUES (%s)", (design_name,))
                connection.commit()
                cursor.close()
                connection.close()
                return True
            except Error as e:
                st.error(f"Add design weave type error: {e}")
                return False
        return False

    def update_design_weave_type(self, old_design_name, new_design_name):
        """Update design/weave type name"""
        connection = self.get_connection()
        if connection:
            try:
                cursor = connection.cursor()
                cursor.execute("UPDATE design_weave_types SET design_name = %s WHERE design_name = %s",
                               (new_design_name, old_design_name))
                connection.commit()
                cursor.close()
                connection.close()
                return True
            except Error as e:
                st.error(f"Update design weave type error: {e}")
                return False
        return False

    def delete_design_weave_type(self, design_name):
        """Delete design/weave type"""
        connection = self.get_connection()
        if connection:
            try:
                cursor = connection.cursor()
                cursor.execute("DELETE FROM design_weave_types WHERE design_name = %s", (design_name,))
                connection.commit()
                cursor.close()
                connection.close()
                return True
            except Error as e:
                st.error(f"Delete design weave type error: {e}")
                return False
        return False

    def check_design_weave_type_usage(self, design_name):
        """Check if design/weave type is used in inventory or job worker tables"""
        connection = self.get_connection()
        if connection:
            try:
                cursor = connection.cursor()
                cursor.execute("SELECT COUNT(*) FROM inventory_warp WHERE design = %s", (design_name,))
                inventory_count = cursor.fetchone()[0]
                cursor.execute("SELECT COUNT(*) FROM job_worker_warp WHERE design = %s", (design_name,))
                jw_count = cursor.fetchone()[0]
                cursor.close()
                connection.close()
                return inventory_count + jw_count
            except Error as e:
                st.error(f"Check design weave type usage error: {e}")
                return 0
        return 0


    def check_job_worker_usage(self, worker_name):
        """Check if job worker is used in job worker tables or products"""
        connection = self.get_connection()
        if connection:
            try:
                cursor = connection.cursor()
                # Check job_worker_warp
                cursor.execute("SELECT COUNT(*) FROM job_worker_warp WHERE job_worker = %s", (worker_name,))
                warp_count = cursor.fetchone()[0]
                # Check job_worker_weft
                cursor.execute("SELECT COUNT(*) FROM job_worker_weft WHERE job_worker = %s", (worker_name,))
                weft_count = cursor.fetchone()[0]
                # Check products
                cursor.execute("SELECT COUNT(*) FROM products WHERE job_worker = %s", (worker_name,))
                product_count = cursor.fetchone()[0]
                cursor.close()
                connection.close()
                return warp_count + weft_count + product_count
            except Error as e:
                st.error(f"Check job worker usage error: {e}")
                return 0
        return 0

    def check_product_category_usage(self, category_name):
        """Check if product category is used in products table"""
        connection = self.get_connection()
        if connection:
            try:
                cursor = connection.cursor()
                cursor.execute("SELECT COUNT(*) FROM products WHERE product_category = %s", (category_name,))
                count = cursor.fetchone()[0]
                cursor.close()
                connection.close()
                return count
            except Error as e:
                st.error(f"Check product category usage error: {e}")
                return 0
        return 0

    # ========================================
    # PRODUCT CATEGORY METHODS
    # ========================================
    def get_all_product_categories(self):
        """Fetch all product categories"""
        connection = self.get_connection()
        if connection:
            try:
                cursor = connection.cursor()
                cursor.execute("SELECT category_name FROM product_categories ORDER BY category_name")
                categories = [row[0] for row in cursor.fetchall()]
                cursor.close()
                connection.close()
                return categories
            except Error as e:
                st.error(f"Fetch categories error: {e}")
                return []
        return []

    def add_product_category(self, category_name):
        """Add new product category"""
        connection = self.get_connection()
        if connection:
            try:
                cursor = connection.cursor()
                cursor.execute("INSERT INTO product_categories (category_name) VALUES (%s)", (category_name,))
                connection.commit()
                cursor.close()
                connection.close()
                return True
            except Error as e:
                st.error(f"Add category error: {e}")
                return False
        return False

    def update_product_category(self, old_category_name, new_category_name):
        """Update product category"""
        connection = self.get_connection()
        if connection:
            try:
                cursor = connection.cursor()
                cursor.execute("UPDATE product_categories SET category_name = %s WHERE category_name = %s",
                               (new_category_name, old_category_name))
                connection.commit()
                cursor.close()
                connection.close()
                return True
            except Error as e:
                st.error(f"Update category error: {e}")
                return False
        return False

    def delete_product_category(self, category_name):
        """Delete product category"""
        connection = self.get_connection()
        if connection:
            try:
                cursor = connection.cursor()
                cursor.execute("DELETE FROM product_categories WHERE category_name = %s", (category_name,))
                connection.commit()
                cursor.close()
                connection.close()
                return True
            except Error as e:
                st.error(f"Delete category error: {e}")
                return False
        return False

    # ========================================
    # JOB WORKER METHODS
    # ========================================
    def get_all_job_workers(self):
        """Fetch all job workers"""
        connection = self.get_connection()
        if connection:
            try:
                cursor = connection.cursor()
                cursor.execute("SELECT worker_name FROM job_workers ORDER BY worker_name")
                workers = [row[0] for row in cursor.fetchall()]
                cursor.close()
                connection.close()
                return workers
            except Error as e:
                st.error(f"Fetch workers error: {e}")
                return []
        return []

    def get_job_worker_details(self, worker_name):
        """Get detailed information about a job worker"""
        connection = self.get_connection()
        if connection:
            try:
                cursor = connection.cursor(dictionary=True)
                cursor.execute("""
                    SELECT worker_name, contact_number, gst_number, aadhar_number 
                    FROM job_workers 
                    WHERE worker_name = %s
                """, (worker_name,))
                details = cursor.fetchone()
                cursor.close()
                connection.close()
                return details
            except Error as e:
                st.error(f"Fetch worker details error: {e}")
                return None
        return None

    def add_job_worker(self, worker_name, contact_number="", gst_number="", aadhar_number=""):
        """Add new job worker"""
        connection = self.get_connection()
        if connection:
            try:
                cursor = connection.cursor()
                cursor.execute("""
                    INSERT INTO job_workers (worker_name, contact_number, gst_number, aadhar_number) 
                    VALUES (%s, %s, %s, %s)
                """, (worker_name, contact_number, gst_number, aadhar_number))
                connection.commit()
                cursor.close()
                connection.close()
                return True
            except Error as e:
                st.error(f"Add worker error: {e}")
                return False
        return False

    def update_job_worker(self, old_worker_name, worker_name, contact_number, gst_number, aadhar_number):
        """Update job worker"""
        connection = self.get_connection()
        if connection:
            try:
                cursor = connection.cursor()
                cursor.execute("""
                    UPDATE job_workers 
                    SET worker_name = %s, contact_number = %s, gst_number = %s, aadhar_number = %s
                    WHERE worker_name = %s
                """, (worker_name, contact_number, gst_number, aadhar_number, old_worker_name))
                connection.commit()
                cursor.close()
                connection.close()
                return True
            except Error as e:
                st.error(f"Update worker error: {e}")
                return False
        return False

    def delete_job_worker(self, worker_name):
        """Delete job worker"""
        connection = self.get_connection()
        if connection:
            try:
                cursor = connection.cursor()
                cursor.execute("DELETE FROM job_workers WHERE worker_name = %s", (worker_name,))
                connection.commit()
                cursor.close()
                connection.close()
                return True
            except Error as e:
                st.error(f"Delete worker error: {e}")
                return False
        return False

    # ========================================
    # INVENTORY WARP METHODS
    # ========================================
    def get_available_inventory_warp(self):
        """Get total available WARP in inventory (not yet distributed)"""
        connection = self.get_connection()
        if connection:
            try:
                cursor = connection.cursor()
                # Total inventory WARP
                cursor.execute("SELECT COALESCE(SUM(beem_weight - paper_weight), 0) FROM inventory_warp")
                total_inventory = float(cursor.fetchone()[0])

                # Total distributed to job workers
                cursor.execute("SELECT COALESCE(SUM(beem_weight - paper_weight), 0) FROM job_worker_warp")
                total_distributed = float(cursor.fetchone()[0])

                cursor.close()
                connection.close()

                return max(0, total_inventory - total_distributed)
            except Error as e:
                st.error(f"Get available inventory WARP error: {e}")
                return 0
        return 0

    def insert_inventory_warp(self, data):
        """Insert WARP entry to inventory"""
        connection = self.get_connection()
        if connection:
            try:
                cursor = connection.cursor()
                query = """INSERT INTO inventory_warp (date, yarn_name, design, paper_weight, beem_weight) 
                           VALUES (%s, %s, %s, %s, %s)"""
                cursor.execute(query, data)
                connection.commit()
                cursor.close()
                connection.close()
                return True
            except Error as e:
                st.error(f"Insert inventory WARP error: {e}")
                return False
        return False

    def get_inventory_warp(self):
        """Fetch all inventory WARP records"""
        connection = self.get_connection()
        if connection:
            try:
                cursor = connection.cursor(dictionary=True)
                cursor.execute("""
                    SELECT id, date, yarn_name, design, paper_weight, beem_weight,
                           (beem_weight - paper_weight) as net_weight, created_at
                    FROM inventory_warp 
                    ORDER BY date DESC
                """)
                records = cursor.fetchall()
                cursor.close()
                connection.close()
                return records
            except Error as e:
                st.error(f"Fetch inventory WARP error: {e}")
                return []
        return []

    # ========================================
    # INVENTORY WEFT METHODS
    # ========================================
    def get_available_inventory_weft(self):
        """Get total available WEFT in inventory (not yet distributed)"""
        connection = self.get_connection()
        if connection:
            try:
                cursor = connection.cursor()
                # Total inventory WEFT
                cursor.execute("SELECT COALESCE(SUM(no_of_cones * weight_per_cone), 0) FROM inventory_weft")
                total_inventory = float(cursor.fetchone()[0])

                # Total distributed to job workers
                cursor.execute("SELECT COALESCE(SUM(no_of_cones * weight_per_cone), 0) FROM job_worker_weft")
                total_distributed = float(cursor.fetchone()[0])

                cursor.close()
                connection.close()

                return max(0, total_inventory - total_distributed)
            except Error as e:
                st.error(f"Get available inventory WEFT error: {e}")
                return 0
        return 0

    def insert_inventory_weft(self, data):
        """Insert WEFT entry to inventory"""
        connection = self.get_connection()
        if connection:
            try:
                cursor = connection.cursor()
                query = """INSERT INTO inventory_weft (date, colour, no_of_cones, weight_per_cone) 
                           VALUES (%s, %s, %s, %s)"""
                cursor.execute(query, data)
                connection.commit()
                cursor.close()
                connection.close()
                return True
            except Error as e:
                st.error(f"Insert inventory WEFT error: {e}")
                return False
        return False

    def get_inventory_weft(self):
        """Fetch all inventory WEFT records"""
        connection = self.get_connection()
        if connection:
            try:
                cursor = connection.cursor(dictionary=True)
                cursor.execute("""
                    SELECT id, date, colour, no_of_cones, weight_per_cone,
                           (no_of_cones * weight_per_cone) as total_weight, created_at
                    FROM inventory_weft 
                    ORDER BY date DESC
                """)
                records = cursor.fetchall()
                cursor.close()
                connection.close()
                return records
            except Error as e:
                st.error(f"Fetch inventory WEFT error: {e}")
                return []
        return []

    # ========================================
    # JOB WORKER WARP METHODS
    # ========================================
    def insert_job_worker_warp(self, data):
        """Insert WARP entry for job worker"""
        connection = self.get_connection()
        if connection:
            try:
                cursor = connection.cursor()
                query = """INSERT INTO job_worker_warp (date, yarn_name, design, paper_weight, beem_weight, job_worker) 
                           VALUES (%s, %s, %s, %s, %s, %s)"""
                cursor.execute(query, data)
                connection.commit()
                cursor.close()
                connection.close()
                return True
            except Error as e:
                st.error(f"Insert job worker WARP error: {e}")
                return False
        return False

    def get_job_worker_warp(self):
        """Fetch all job worker WARP records"""
        connection = self.get_connection()
        if connection:
            try:
                cursor = connection.cursor(dictionary=True)
                cursor.execute("""
                    SELECT id, date, yarn_name, design, paper_weight, beem_weight,
                           (beem_weight - paper_weight) as net_weight, job_worker, created_at
                    FROM job_worker_warp 
                    ORDER BY date DESC
                """)
                records = cursor.fetchall()
                cursor.close()
                connection.close()
                return records
            except Error as e:
                st.error(f"Fetch job worker WARP error: {e}")
                return []
        return []

    def get_job_worker_warp_by_date(self, job_worker, from_date, to_date):
        """Fetch job worker WARP records within date range"""
        connection = self.get_connection()
        if connection:
            try:
                cursor = connection.cursor(dictionary=True)
                cursor.execute("""
                    SELECT id, date, yarn_name, design, paper_weight, beem_weight,
                           (beem_weight - paper_weight) as net_weight, job_worker, created_at
                    FROM job_worker_warp 
                    WHERE job_worker = %s AND date BETWEEN %s AND %s 
                    ORDER BY date DESC
                """, (job_worker, from_date, to_date))
                records = cursor.fetchall()
                cursor.close()
                connection.close()
                return records
            except Error as e:
                st.error(f"Fetch job worker WARP by date error: {e}")
                return []
        return []

    # ========================================
    # JOB WORKER WEFT METHODS
    # ========================================
    def insert_job_worker_weft(self, data):
        """Insert WEFT entry for job worker"""
        connection = self.get_connection()
        if connection:
            try:
                cursor = connection.cursor()
                query = """INSERT INTO job_worker_weft (date, colour, no_of_cones, weight_per_cone, job_worker) 
                           VALUES (%s, %s, %s, %s, %s)"""
                cursor.execute(query, data)
                connection.commit()
                cursor.close()
                connection.close()
                return True
            except Error as e:
                st.error(f"Insert job worker WEFT error: {e}")
                return False
        return False

    def get_job_worker_weft(self):
        """Fetch all job worker WEFT records"""
        connection = self.get_connection()
        if connection:
            try:
                cursor = connection.cursor(dictionary=True)
                cursor.execute("""
                    SELECT id, date, colour, no_of_cones, weight_per_cone,
                           (no_of_cones * weight_per_cone) as total_weight, job_worker, created_at
                    FROM job_worker_weft 
                    ORDER BY date DESC
                """)
                records = cursor.fetchall()
                cursor.close()
                connection.close()
                return records
            except Error as e:
                st.error(f"Fetch job worker WEFT error: {e}")
                return []
        return []

    def get_job_worker_weft_by_date(self, job_worker, from_date, to_date):
        """Fetch job worker WEFT records within date range"""
        connection = self.get_connection()
        if connection:
            try:
                cursor = connection.cursor(dictionary=True)
                cursor.execute("""
                    SELECT id, date, colour, no_of_cones, weight_per_cone,
                           (no_of_cones * weight_per_cone) as total_weight, job_worker, created_at
                    FROM job_worker_weft 
                    WHERE job_worker = %s AND date BETWEEN %s AND %s 
                    ORDER BY date DESC
                """, (job_worker, from_date, to_date))
                records = cursor.fetchall()
                cursor.close()
                connection.close()
                return records
            except Error as e:
                st.error(f"Fetch job worker WEFT by date error: {e}")
                return []
        return []

    # ========================================
    # PRODUCT METHODS
    # ========================================
    def insert_product(self, data):
        """Insert completed product with warp_used and weft_used"""
        connection = self.get_connection()
        if connection:
            try:
                cursor = connection.cursor()
                query = """INSERT INTO products (job_worker, product_category, completion_date, 
                           total_pieces, total_meters, product_weight, warp_used, weft_used, notes) 
                           VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s)"""
                cursor.execute(query, data)
                connection.commit()
                cursor.close()
                connection.close()
                return True
            except Error as e:
                st.error(f"Insert product error: {e}")
                return False
        return False

    def get_products(self):
        """Fetch all products"""
        connection = self.get_connection()
        if connection:
            try:
                cursor = connection.cursor(dictionary=True)
                cursor.execute("""
                    SELECT * FROM products 
                    ORDER BY completion_date DESC
                """)
                records = cursor.fetchall()
                cursor.close()
                connection.close()
                return records
            except Error as e:
                st.error(f"Fetch products error: {e}")
                return []
        return []

    def get_products_by_worker_and_date(self, job_worker, from_date, to_date):
        """Fetch products by worker within date range"""
        connection = self.get_connection()
        if connection:
            try:
                cursor = connection.cursor(dictionary=True)
                cursor.execute("""
                    SELECT * FROM products 
                    WHERE job_worker = %s AND completion_date BETWEEN %s AND %s 
                    ORDER BY completion_date DESC
                """, (job_worker, from_date, to_date))
                records = cursor.fetchall()
                cursor.close()
                connection.close()
                return records
            except Error as e:
                st.error(f"Fetch products by worker and date error: {e}")
                return []
        return []

    # ========================================
    # BALANCE AND STATISTICS
    # ========================================
    def get_worker_balance(self, job_worker):
        """Get current balance for a job worker"""
        connection = self.get_connection()
        if connection:
            try:
                cursor = connection.cursor()

                # Get total WARP distributed
                cursor.execute("""
                    SELECT COALESCE(SUM(beem_weight - paper_weight), 0) 
                    FROM job_worker_warp 
                    WHERE job_worker = %s
                """, (job_worker,))
                warp_total = float(cursor.fetchone()[0])

                # Get total WEFT distributed
                cursor.execute("""
                    SELECT COALESCE(SUM(no_of_cones * weight_per_cone), 0) 
                    FROM job_worker_weft 
                    WHERE job_worker = %s
                """, (job_worker,))
                weft_total = float(cursor.fetchone()[0])

                # Get material used in products
                cursor.execute("""
                    SELECT COALESCE(SUM(warp_used), 0), COALESCE(SUM(weft_used), 0)
                    FROM products 
                    WHERE job_worker = %s
                """, (job_worker,))
                result = cursor.fetchone()
                warp_used = float(result[0])
                weft_used = float(result[1])

                cursor.close()
                connection.close()

                return {
                    'warp_balance': max(0, warp_total - warp_used),
                    'weft_balance': max(0, weft_total - weft_used)
                }
            except Error as e:
                st.error(f"Get worker balance error: {e}")
                return {'warp_balance': 0, 'weft_balance': 0}
        return {'warp_balance': 0, 'weft_balance': 0}

    def get_dashboard_stats(self):
        """Get statistics for dashboard"""
        connection = self.get_connection()
        if connection:
            try:
                cursor = connection.cursor()

                # Total inventory WARP (procured)
                cursor.execute("SELECT COALESCE(SUM(beem_weight - paper_weight), 0) FROM inventory_warp")
                total_inventory_warp = float(cursor.fetchone()[0])

                # Total inventory WEFT (procured)
                cursor.execute("SELECT COALESCE(SUM(no_of_cones * weight_per_cone), 0) FROM inventory_weft")
                total_inventory_weft = float(cursor.fetchone()[0])

                # Job Worker WARP (total distributed)
                cursor.execute("SELECT COALESCE(SUM(beem_weight - paper_weight), 0) FROM job_worker_warp")
                job_worker_warp_distributed = float(cursor.fetchone()[0])

                # Job Worker WEFT (total distributed)
                cursor.execute("SELECT COALESCE(SUM(no_of_cones * weight_per_cone), 0) FROM job_worker_weft")
                job_worker_weft_distributed = float(cursor.fetchone()[0])

                # Available inventory (not distributed yet)
                available_inventory_warp = max(0, total_inventory_warp - job_worker_warp_distributed)
                available_inventory_weft = max(0, total_inventory_weft - job_worker_weft_distributed)

                # Material used in products
                cursor.execute("SELECT COALESCE(SUM(warp_used), 0), COALESCE(SUM(weft_used), 0) FROM products")
                result = cursor.fetchone()
                warp_used = float(result[0])
                weft_used = float(result[1])

                # Current job worker balances (distributed - used)
                job_worker_warp = max(0, job_worker_warp_distributed - warp_used)
                job_worker_weft = max(0, job_worker_weft_distributed - weft_used)

                # Finished products stats
                cursor.execute("""
                    SELECT 
                        COUNT(*) as count,
                        COALESCE(SUM(product_weight), 0) as total_weight,
                        COALESCE(SUM(total_pieces), 0) as total_pieces,
                        COALESCE(SUM(total_meters), 0) as total_meters
                    FROM products
                """)
                product_stats = cursor.fetchone()

                cursor.close()
                connection.close()

                return {
                    'inventory_warp': available_inventory_warp,
                    'inventory_weft': available_inventory_weft,
                    'job_worker_warp': job_worker_warp,
                    'job_worker_weft': job_worker_weft,
                    'finished_products_count': product_stats[0],
                    'finished_products_weight': float(product_stats[1]),
                    'total_pieces': int(product_stats[2]),
                    'total_meters': float(product_stats[3])
                }
            except Error as e:
                st.error(f"Get dashboard stats error: {e}")
                return {
                    'inventory_warp': 0,
                    'inventory_weft': 0,
                    'job_worker_warp': 0,
                    'job_worker_weft': 0,
                    'finished_products_count': 0,
                    'finished_products_weight': 0,
                    'total_pieces': 0,
                    'total_meters': 0
                }
        return {
            'inventory_warp': 0,
            'inventory_weft': 0,
            'job_worker_warp': 0,
            'job_worker_weft': 0,
            'finished_products_count': 0,
            'finished_products_weight': 0,
            'total_pieces': 0,
            'total_meters': 0
        }