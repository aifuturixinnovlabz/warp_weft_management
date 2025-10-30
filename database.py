import mysql.connector
from mysql.connector import Error
import streamlit as st


class Database:
    def __init__(self):
        self.host = "localhost"
        self.user = "root"
        self.password = "root"  # CHANGE THIS TO YOUR PASSWORD
        self.database = "warp_weft_db"

        self.PAPER_DEPOSIT_RATE = 40  # ₹40 per kg
        self.BAG_DEPOSIT_RATE = 15  # ₹15 per bag

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
    # WARPER MANAGEMENT METHODS (Task #2)
    # ========================================
    def get_all_warpers(self):
        """Fetch all warpers"""
        connection = self.get_connection()
        if connection:
            try:
                cursor = connection.cursor()
                cursor.execute("SELECT warper_name FROM warpers ORDER BY warper_name")
                warpers = [row[0] for row in cursor.fetchall()]
                cursor.close()
                connection.close()
                return warpers
            except Error as e:
                st.error(f"Fetch warpers error: {e}")
                return []
        return []

    def add_warper(self, warper_name):
        """Add new warper"""
        connection = self.get_connection()
        if connection:
            try:
                cursor = connection.cursor()
                cursor.execute("INSERT INTO warpers (warper_name) VALUES (%s)", (warper_name,))
                connection.commit()
                cursor.close()
                connection.close()
                return True
            except Error as e:
                st.error(f"Add warper error: {e}")
                return False
        return False

    def update_warper(self, old_warper_name, new_warper_name):
        """Update warper name"""
        connection = self.get_connection()
        if connection:
            try:
                cursor = connection.cursor()
                cursor.execute("UPDATE warpers SET warper_name = %s WHERE warper_name = %s",
                               (new_warper_name, old_warper_name))
                connection.commit()
                cursor.close()
                connection.close()
                return True
            except Error as e:
                st.error(f"Update warper error: {e}")
                return False
        return False

    def delete_warper(self, warper_name):
        """Delete warper"""
        connection = self.get_connection()
        if connection:
            try:
                cursor = connection.cursor()
                cursor.execute("DELETE FROM warpers WHERE warper_name = %s", (warper_name,))
                connection.commit()
                cursor.close()
                connection.close()
                return True
            except Error as e:
                st.error(f"Delete warper error: {e}")
                return False
        return False

    def check_warper_usage(self, warper_name):
        """Check if warper is used in inventory or job worker tables"""
        connection = self.get_connection()
        if connection:
            try:
                cursor = connection.cursor()
                cursor.execute("SELECT COUNT(*) FROM inventory_warp WHERE warper_name = %s", (warper_name,))
                inventory_count = cursor.fetchone()[0]
                cursor.execute("SELECT COUNT(*) FROM job_worker_warp WHERE warper_name = %s", (warper_name,))
                jw_count = cursor.fetchone()[0]
                cursor.close()
                connection.close()
                return inventory_count + jw_count
            except Error as e:
                st.error(f"Check warper usage error: {e}")
                return 0
        return 0

    # ========================================
    # REED MANAGEMENT METHODS (Task #7)
    # ========================================
    def get_all_reed_types(self):
        """Fetch all reed types"""
        connection = self.get_connection()
        if connection:
            try:
                cursor = connection.cursor()
                cursor.execute("SELECT reed_name FROM reed_types ORDER BY reed_name")
                reeds = [row[0] for row in cursor.fetchall()]
                cursor.close()
                connection.close()
                return reeds
            except Error as e:
                st.error(f"Fetch reed types error: {e}")
                return []
        return []

    def add_reed_type(self, reed_name):
        """Add new reed type"""
        connection = self.get_connection()
        if connection:
            try:
                cursor = connection.cursor()
                cursor.execute("INSERT INTO reed_types (reed_name) VALUES (%s)", (reed_name,))
                connection.commit()
                cursor.close()
                connection.close()
                return True
            except Error as e:
                st.error(f"Add reed type error: {e}")
                return False
        return False

    def update_reed_type(self, old_reed_name, new_reed_name):
        """Update reed type name"""
        connection = self.get_connection()
        if connection:
            try:
                cursor = connection.cursor()
                cursor.execute("UPDATE reed_types SET reed_name = %s WHERE reed_name = %s",
                               (new_reed_name, old_reed_name))
                connection.commit()
                cursor.close()
                connection.close()
                return True
            except Error as e:
                st.error(f"Update reed type error: {e}")
                return False
        return False

    def delete_reed_type(self, reed_name):
        """Delete reed type"""
        connection = self.get_connection()
        if connection:
            try:
                cursor = connection.cursor()
                cursor.execute("DELETE FROM reed_types WHERE reed_name = %s", (reed_name,))
                connection.commit()
                cursor.close()
                connection.close()
                return True
            except Error as e:
                st.error(f"Delete reed type error: {e}")
                return False
        return False

    def check_reed_type_usage(self, reed_name):
        """Check if reed type is used in inventory or job worker tables"""
        connection = self.get_connection()
        if connection:
            try:
                cursor = connection.cursor()
                cursor.execute("SELECT COUNT(*) FROM inventory_warp WHERE reed = %s", (reed_name,))
                inventory_count = cursor.fetchone()[0]
                cursor.execute("SELECT COUNT(*) FROM job_worker_warp WHERE reed = %s", (reed_name,))
                jw_count = cursor.fetchone()[0]
                cursor.close()
                connection.close()
                return inventory_count + jw_count
            except Error as e:
                st.error(f"Check reed type usage error: {e}")
                return 0
        return 0

    # ========================================
    # WARP NUMBER GENERATION (Task #1)
    # ========================================
    def generate_warp_number(self):
        """Generate auto-incremented warp number based on financial year"""
        connection = self.get_connection()
        if connection:
            try:
                cursor = connection.cursor()
                # Call the MySQL function
                cursor.execute("SELECT generate_warp_number()")
                warp_number = cursor.fetchone()[0]
                cursor.close()
                connection.close()
                return warp_number
            except Error as e:
                st.error(f"Generate warp number error: {e}")
                return None
        return None

    # ========================================
    # CAUTION DEPOSIT CALCULATION METHODS
    # ========================================
    def calculate_paper_deposit(self, paper_weight):
        """Calculate paper caution deposit: ₹40/kg"""
        return round(paper_weight * self.PAPER_DEPOSIT_RATE, 2)

    def calculate_bag_deposit(self, no_of_bags):
        """Calculate bag caution deposit: ₹15/bag"""
        return no_of_bags * self.BAG_DEPOSIT_RATE



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
        """Get total available WARP using NEW FORMULA: gross_weight - (paper_weight + beam_weight)"""
        connection = self.get_connection()
        if connection:
            try:
                cursor = connection.cursor()
                # Total inventory WARP with NEW FORMULA
                cursor.execute("""
                    SELECT COALESCE(SUM(gross_weight - (paper_weight + beam_weight)), 0) 
                    FROM inventory_warp
                """)
                total_inventory = float(cursor.fetchone()[0])

                # Total distributed to job workers with NEW FORMULA
                cursor.execute("""
                    SELECT COALESCE(SUM(gross_weight - (paper_weight + beam_weight)), 0) 
                    FROM job_worker_warp
                """)
                total_distributed = float(cursor.fetchone()[0])

                cursor.close()
                connection.close()

                return max(0, total_inventory - total_distributed)
            except Error as e:
                st.error(f"Get available inventory WARP error: {e}")
                return 0
        return 0

    def insert_inventory_warp(self, data):
        """Insert WARP entry to inventory with all new fields"""
        connection = self.get_connection()
        if connection:
            try:
                cursor = connection.cursor()

                # Generate warp number
                warp_number = self.generate_warp_number()

                query = """INSERT INTO inventory_warp 
                           (warp_number, date, yarn_type, warper_name, design, gross_weight, 
                            paper_weight, beam_weight, no_of_bell, reed) 
                           VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s, %s)"""

                # data should be: (date, yarn_type, warper_name, design, gross_weight,
                #                  paper_weight, beam_weight, no_of_bell, reed)
                full_data = (warp_number,) + data

                cursor.execute(query, full_data)
                connection.commit()
                cursor.close()
                connection.close()
                return True, warp_number
            except Error as e:
                st.error(f"Insert inventory WARP error: {e}")
                return False, None
        return False, None

    def get_inventory_warp(self):
        """Fetch all inventory WARP records"""
        connection = self.get_connection()
        if connection:
            try:
                cursor = connection.cursor(dictionary=True)
                cursor.execute("""
                    SELECT id, warp_number, date, yarn_type, warper_name, design, 
                           gross_weight, paper_weight, beam_weight, no_of_bell, reed,
                           net_weight, created_at
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
        """Get total available WEFT using NEW FORMULA:
           gross_weight - (cone_weight × no_of_cones + bag_weight × no_of_bags)
           Note: bag_weight is constant 0.2 kg (200g)
        """
        connection = self.get_connection()
        if connection:
            try:
                cursor = connection.cursor()
                BAG_WEIGHT = 0.2  # 200g per bag

                # Total inventory WEFT with NEW FORMULA
                cursor.execute(f"""
                    SELECT COALESCE(
                        SUM(gross_weight - (cone_weight * no_of_cones + {BAG_WEIGHT} * no_of_bags)), 
                        0
                    ) 
                    FROM inventory_weft
                """)
                total_inventory = float(cursor.fetchone()[0])

                # Total distributed to job workers with NEW FORMULA
                cursor.execute(f"""
                    SELECT COALESCE(
                        SUM(gross_weight - (cone_weight * no_of_cones + {BAG_WEIGHT} * no_of_bags)), 
                        0
                    ) 
                    FROM job_worker_weft
                """)
                total_distributed = float(cursor.fetchone()[0])

                cursor.close()
                connection.close()

                return max(0, total_inventory - total_distributed)
            except Error as e:
                st.error(f"Get available inventory WEFT error: {e}")
                return 0
        return 0

    def insert_inventory_weft(self, data):
        """Insert WEFT entry to inventory with new fields (gross_weight, no_of_bags, cone_weight)"""
        connection = self.get_connection()
        if connection:
            try:
                cursor = connection.cursor()
                query = """INSERT INTO inventory_weft 
                           (date, colour, gross_weight, no_of_cones, cone_weight, no_of_bags) 
                           VALUES (%s, %s, %s, %s, %s, %s)"""
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
                    SELECT id, date, colour, gross_weight, no_of_cones, 
                           cone_weight, no_of_bags, net_weight, created_at
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
        """Insert WARP entry for job worker with caution deposit calculation"""
        connection = self.get_connection()
        if connection:
            try:
                cursor = connection.cursor()

                # Generate warp number for this distribution
                warp_number = self.generate_warp_number()

                # Calculate caution deposit for paper
                paper_weight = data[6]  # paper_weight is at index 6
                caution_deposit = self.calculate_paper_deposit(paper_weight)

                query = """INSERT INTO job_worker_warp 
                           (warp_number, date, yarn_type, warper_name, design, gross_weight,
                            paper_weight, beam_weight, no_of_bell, reed, job_worker, 
                            caution_deposit_paper) 
                           VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s)"""

                # data should be: (date, yarn_type, warper_name, design, gross_weight,
                #                  paper_weight, beam_weight, no_of_bell, reed, job_worker)
                full_data = (warp_number,) + data + (caution_deposit,)

                cursor.execute(query, full_data)
                connection.commit()
                cursor.close()
                connection.close()
                return True, warp_number, caution_deposit
            except Error as e:
                st.error(f"Insert job worker WARP error: {e}")
                return False, None, 0
        return False, None, 0

    def get_job_worker_warp(self):
        """Fetch all job worker WARP records"""
        connection = self.get_connection()
        if connection:
            try:
                cursor = connection.cursor(dictionary=True)
                cursor.execute("""
                    SELECT id, warp_number, date, yarn_type, warper_name, design,
                           gross_weight, paper_weight, beam_weight, no_of_bell, reed,
                           net_weight, job_worker, created_at
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
                    SELECT id, warp_number, date, yarn_type, warper_name, design,
                           gross_weight, paper_weight, beam_weight, no_of_bell, reed,
                           net_weight, job_worker, created_at
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
        """Insert WEFT entry for job worker with caution deposit calculation"""
        connection = self.get_connection()
        if connection:
            try:
                cursor = connection.cursor()

                # Calculate caution deposit for bags
                no_of_bags = data[5]  # no_of_bags is at index 5
                caution_deposit = self.calculate_bag_deposit(no_of_bags)

                query = """INSERT INTO job_worker_weft 
                           (date, colour, gross_weight, no_of_cones, cone_weight, no_of_bags, 
                            job_worker, caution_deposit_bags) 
                           VALUES (%s, %s, %s, %s, %s, %s, %s, %s)"""

                full_data = data + (caution_deposit,)

                cursor.execute(query, full_data)
                connection.commit()
                cursor.close()
                connection.close()
                return True, caution_deposit
            except Error as e:
                st.error(f"Insert job worker WEFT error: {e}")
                return False, 0
        return False, 0

        # ========================================
        # PAPER RETURN & REFUND METHODS (WARP)
        # ========================================
    def mark_paper_returned(self, warp_entry_id, return_date):
        """Mark paper as returned for a WARP entry"""
        connection = self.get_connection()
        if connection:
            try:
                cursor = connection.cursor()
                cursor.execute("""
                    UPDATE job_worker_warp 
                    SET paper_returned = TRUE, paper_return_date = %s
                    WHERE id = %s
                """, (return_date, warp_entry_id))
                connection.commit()
                cursor.close()
                connection.close()
                return True
            except Error as e:
                st.error(f"Mark paper returned error: {e}")
                return False
        return False

    def refund_paper_deposit(self, warp_entry_id, refund_date):
        """Mark paper deposit as refunded"""
        connection = self.get_connection()
        if connection:
            try:
                cursor = connection.cursor()
                cursor.execute("""
                    UPDATE job_worker_warp 
                    SET deposit_refunded = TRUE, deposit_refund_date = %s
                    WHERE id = %s AND paper_returned = TRUE
                """, (refund_date, warp_entry_id))
                connection.commit()

                if cursor.rowcount == 0:
                    cursor.close()
                    connection.close()
                    return False, "Paper must be returned before refund"

                cursor.close()
                connection.close()
                return True, "Deposit refunded successfully"
            except Error as e:
                st.error(f"Refund paper deposit error: {e}")
                return False, str(e)
        return False, "Database connection failed"

        # ========================================
        # BAG RETURN & REFUND METHODS (WEFT)
        # ========================================
        def mark_bags_returned(self, weft_entry_id, bags_returned, return_date):
            """Mark bags as returned for a WEFT entry (can be partial)"""
            connection = self.get_connection()
            if connection:
                try:
                    cursor = connection.cursor()

                    # Get total bags issued
                    cursor.execute("SELECT no_of_bags FROM job_worker_weft WHERE id = %s", (weft_entry_id,))
                    result = cursor.fetchone()

                    if not result:
                        cursor.close()
                        connection.close()
                        return False, "Entry not found"

                    total_bags = result[0]

                    if bags_returned > total_bags:
                        cursor.close()
                        connection.close()
                        return False, f"Cannot return more than {total_bags} bags"

                    cursor.execute("""
                        UPDATE job_worker_weft 
                        SET bags_returned = %s, bag_return_date = %s
                        WHERE id = %s
                    """, (bags_returned, return_date, weft_entry_id))
                    connection.commit()
                    cursor.close()
                    connection.close()
                    return True, "Bags return recorded successfully"
                except Error as e:
                    st.error(f"Mark bags returned error: {e}")
                    return False, str(e)
            return False, "Database connection failed"

        def refund_bag_deposit(self, weft_entry_id, refund_date):
            """Mark bag deposit as refunded (only if all bags returned)"""
            connection = self.get_connection()
            if connection:
                try:
                    cursor = connection.cursor()

                    # Check if all bags returned
                    cursor.execute("""
                        SELECT no_of_bags, bags_returned 
                        FROM job_worker_weft 
                        WHERE id = %s
                    """, (weft_entry_id,))
                    result = cursor.fetchone()

                    if not result:
                        cursor.close()
                        connection.close()
                        return False, "Entry not found"

                    total_bags, returned_bags = result

                    if returned_bags < total_bags:
                        cursor.close()
                        connection.close()
                        return False, f"Only {returned_bags}/{total_bags} bags returned. Cannot refund yet."

                    cursor.execute("""
                        UPDATE job_worker_weft 
                        SET deposit_refunded = TRUE, deposit_refund_date = %s
                        WHERE id = %s
                    """, (refund_date, weft_entry_id))
                    connection.commit()
                    cursor.close()
                    connection.close()
                    return True, "Deposit refunded successfully"
                except Error as e:
                    st.error(f"Refund bag deposit error: {e}")
                    return False, str(e)
            return False, "Database connection failed"


    # ========================================
    # CAUTION DEPOSIT TRACKING METHODS
    # ========================================
    def get_pending_paper_deposits(self, job_worker=None):
        """Get all pending paper deposits (not refunded)"""
        connection = self.get_connection()
        if connection:
            try:
                cursor = connection.cursor(dictionary=True)

                if job_worker:
                    cursor.execute("""
                        SELECT id, warp_number, job_worker, date, paper_weight, 
                               caution_deposit_paper, paper_returned, paper_return_date,
                               deposit_refunded, deposit_refund_date
                        FROM job_worker_warp 
                        WHERE job_worker = %s AND deposit_refunded = FALSE 
                              AND caution_deposit_paper > 0
                        ORDER BY date DESC
                    """, (job_worker,))
                else:
                    cursor.execute("""
                        SELECT id, warp_number, job_worker, date, paper_weight, 
                               caution_deposit_paper, paper_returned, paper_return_date,
                               deposit_refunded, deposit_refund_date
                        FROM job_worker_warp 
                        WHERE deposit_refunded = FALSE AND caution_deposit_paper > 0
                        ORDER BY date DESC
                    """)

                records = cursor.fetchall()
                cursor.close()
                connection.close()
                return records
            except Error as e:
                st.error(f"Get pending paper deposits error: {e}")
                return []
        return []

    def get_pending_bag_deposits(self, job_worker=None):
        """Get all pending bag deposits (not refunded)"""
        connection = self.get_connection()
        if connection:
            try:
                cursor = connection.cursor(dictionary=True)

                if job_worker:
                    cursor.execute("""
                        SELECT id, job_worker, date, colour, no_of_bags, bags_returned,
                               caution_deposit_bags, bag_return_date,
                               deposit_refunded, deposit_refund_date
                        FROM job_worker_weft 
                        WHERE job_worker = %s AND deposit_refunded = FALSE 
                              AND caution_deposit_bags > 0
                        ORDER BY date DESC
                    """, (job_worker,))
                else:
                    cursor.execute("""
                        SELECT id, job_worker, date, colour, no_of_bags, bags_returned,
                               caution_deposit_bags, bag_return_date,
                               deposit_refunded, deposit_refund_date
                        FROM job_worker_weft 
                        WHERE deposit_refunded = FALSE AND caution_deposit_bags > 0
                        ORDER BY date DESC
                    """)

                records = cursor.fetchall()
                cursor.close()
                connection.close()
                return records
            except Error as e:
                st.error(f"Get pending bag deposits error: {e}")
                return []
        return []

    def get_total_pending_deposits_by_worker(self, job_worker):
        """Get total pending deposits for a specific worker"""
        connection = self.get_connection()
        if connection:
            try:
                cursor = connection.cursor()

                # Pending paper deposits
                cursor.execute("""
                    SELECT COALESCE(SUM(caution_deposit_paper), 0)
                    FROM job_worker_warp
                    WHERE job_worker = %s AND deposit_refunded = FALSE
                """, (job_worker,))
                paper_pending = float(cursor.fetchone()[0])

                # Pending bag deposits
                cursor.execute("""
                    SELECT COALESCE(SUM(caution_deposit_bags), 0)
                    FROM job_worker_weft
                    WHERE job_worker = %s AND deposit_refunded = FALSE
                """, (job_worker,))
                bag_pending = float(cursor.fetchone()[0])

                cursor.close()
                connection.close()

                return {
                    'paper_deposits': paper_pending,
                    'bag_deposits': bag_pending,
                    'total_pending': paper_pending + bag_pending
                }
            except Error as e:
                st.error(f"Get total pending deposits error: {e}")
                return {'paper_deposits': 0, 'bag_deposits': 0, 'total_pending': 0}
        return {'paper_deposits': 0, 'bag_deposits': 0, 'total_pending': 0}



    def get_job_worker_weft(self):
        """Fetch all job worker WEFT records"""
        connection = self.get_connection()
        if connection:
            try:
                cursor = connection.cursor(dictionary=True)
                cursor.execute("""
                    SELECT id, date, colour, gross_weight, no_of_cones,
                           cone_weight, no_of_bags, net_weight, job_worker, created_at
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
                    SELECT id, date, colour, gross_weight, no_of_cones,
                           cone_weight, no_of_bags, net_weight, job_worker, created_at
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
                    SELECT COALESCE(SUM(gross_weight - (paper_weight + beam_weight)), 0) 
                    FROM job_worker_warp 
                    WHERE job_worker = %s
                """, (job_worker,))
                warp_total = float(cursor.fetchone()[0])

                # Get total WEFT distributed
                cursor.execute("""
                    SELECT COALESCE(SUM(gross_weight - (cone_weight * no_of_cones + 0.2 * no_of_bags)), 0) 
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
                # Total inventory WARP (procured) - NEW FORMULA
                cursor.execute("""
                                    SELECT COALESCE(SUM(gross_weight - (paper_weight + beam_weight)), 0) 
                                    FROM inventory_warp
                                """)
                total_inventory_warp = float(cursor.fetchone()[0])

                # Total inventory WEFT (procured) - NEW FORMULA
                cursor.execute("""
                                    SELECT COALESCE(SUM(gross_weight - (cone_weight * no_of_cones + 0.2 * no_of_bags)), 0) 
                                    FROM inventory_weft
                                """)
                total_inventory_weft = float(cursor.fetchone()[0])

                # Job Worker WARP (total distributed) - NEW FORMULA
                cursor.execute("""
                                    SELECT COALESCE(SUM(gross_weight - (paper_weight + beam_weight)), 0) 
                                    FROM job_worker_warp
                                """)
                job_worker_warp_distributed = float(cursor.fetchone()[0])

                # Job Worker WEFT (total distributed) - NEW FORMULA
                cursor.execute("""
                                    SELECT COALESCE(SUM(gross_weight - (cone_weight * no_of_cones + 0.2 * no_of_bags)), 0) 
                                    FROM job_worker_weft
                                """)
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

    # ========================================
    # CAUTION DEPOSIT TRACKING METHODS
    # ========================================
    def get_pending_paper_deposits(self, job_worker=None):
        """Get all pending paper deposits (not refunded)"""
        connection = self.get_connection()
        if connection:
            try:
                cursor = connection.cursor(dictionary=True)

                if job_worker:
                    cursor.execute("""
                        SELECT id, warp_number, job_worker, date, paper_weight, 
                               caution_deposit_paper, paper_returned, paper_return_date,
                               deposit_refunded, deposit_refund_date
                        FROM job_worker_warp 
                        WHERE job_worker = %s AND deposit_refunded = FALSE 
                              AND caution_deposit_paper > 0
                        ORDER BY date DESC
                    """, (job_worker,))
                else:
                    cursor.execute("""
                        SELECT id, warp_number, job_worker, date, paper_weight, 
                               caution_deposit_paper, paper_returned, paper_return_date,
                               deposit_refunded, deposit_refund_date
                        FROM job_worker_warp 
                        WHERE deposit_refunded = FALSE AND caution_deposit_paper > 0
                        ORDER BY date DESC
                    """)

                records = cursor.fetchall()
                cursor.close()
                connection.close()
                return records
            except Error as e:
                st.error(f"Get pending paper deposits error: {e}")
                return []
        return []

    def get_pending_bag_deposits(self, job_worker=None):
        """Get all pending bag deposits (not refunded)"""
        connection = self.get_connection()
        if connection:
            try:
                cursor = connection.cursor(dictionary=True)

                if job_worker:
                    cursor.execute("""
                        SELECT id, job_worker, date, colour, no_of_bags, bags_returned,
                               caution_deposit_bags, bag_return_date,
                               deposit_refunded, deposit_refund_date
                        FROM job_worker_weft 
                        WHERE job_worker = %s AND deposit_refunded = FALSE 
                              AND caution_deposit_bags > 0
                        ORDER BY date DESC
                    """, (job_worker,))
                else:
                    cursor.execute("""
                        SELECT id, job_worker, date, colour, no_of_bags, bags_returned,
                               caution_deposit_bags, bag_return_date,
                               deposit_refunded, deposit_refund_date
                        FROM job_worker_weft 
                        WHERE deposit_refunded = FALSE AND caution_deposit_bags > 0
                        ORDER BY date DESC
                    """)

                records = cursor.fetchall()
                cursor.close()
                connection.close()
                return records
            except Error as e:
                st.error(f"Get pending bag deposits error: {e}")
                return []
        return []

    def get_total_pending_deposits_by_worker(self, job_worker):
        """Get total pending deposits for a specific worker"""
        connection = self.get_connection()
        if connection:
            try:
                cursor = connection.cursor()

                # Pending paper deposits
                cursor.execute("""
                    SELECT COALESCE(SUM(caution_deposit_paper), 0)
                    FROM job_worker_warp
                    WHERE job_worker = %s AND deposit_refunded = FALSE
                """, (job_worker,))
                paper_pending = float(cursor.fetchone()[0])

                # Pending bag deposits
                cursor.execute("""
                    SELECT COALESCE(SUM(caution_deposit_bags), 0)
                    FROM job_worker_weft
                    WHERE job_worker = %s AND deposit_refunded = FALSE
                """, (job_worker,))
                bag_pending = float(cursor.fetchone()[0])

                cursor.close()
                connection.close()

                return {
                    'paper_deposits': paper_pending,
                    'bag_deposits': bag_pending,
                    'total_pending': paper_pending + bag_pending
                }
            except Error as e:
                st.error(f"Get total pending deposits error: {e}")
                return {'paper_deposits': 0, 'bag_deposits': 0, 'total_pending': 0}
        return {'paper_deposits': 0, 'bag_deposits': 0, 'total_pending': 0}

    def mark_paper_returned(self, warp_entry_id, return_date):
        """Mark paper as returned for a WARP entry"""
        connection = self.get_connection()
        if connection:
            try:
                cursor = connection.cursor()
                cursor.execute("""
                    UPDATE job_worker_warp 
                    SET paper_returned = TRUE, paper_return_date = %s
                    WHERE id = %s
                """, (return_date, warp_entry_id))
                connection.commit()
                cursor.close()
                connection.close()
                return True
            except Error as e:
                st.error(f"Mark paper returned error: {e}")
                return False
        return False

    def refund_paper_deposit(self, warp_entry_id, refund_date):
        """Mark paper deposit as refunded"""
        connection = self.get_connection()
        if connection:
            try:
                cursor = connection.cursor()
                cursor.execute("""
                    UPDATE job_worker_warp 
                    SET deposit_refunded = TRUE, deposit_refund_date = %s
                    WHERE id = %s AND paper_returned = TRUE
                """, (refund_date, warp_entry_id))
                connection.commit()

                if cursor.rowcount == 0:
                    cursor.close()
                    connection.close()
                    return False, "Paper must be returned before refund"

                cursor.close()
                connection.close()
                return True, "Deposit refunded successfully"
            except Error as e:
                st.error(f"Refund paper deposit error: {e}")
                return False, str(e)
        return False, "Database connection failed"

    def mark_bags_returned(self, weft_entry_id, bags_returned, return_date):
        """Mark bags as returned for a WEFT entry (can be partial)"""
        connection = self.get_connection()
        if connection:
            try:
                cursor = connection.cursor()

                # Get total bags issued
                cursor.execute("SELECT no_of_bags FROM job_worker_weft WHERE id = %s", (weft_entry_id,))
                result = cursor.fetchone()

                if not result:
                    cursor.close()
                    connection.close()
                    return False, "Entry not found"

                total_bags = result[0]

                if bags_returned > total_bags:
                    cursor.close()
                    connection.close()
                    return False, f"Cannot return more than {total_bags} bags"

                cursor.execute("""
                    UPDATE job_worker_weft 
                    SET bags_returned = %s, bag_return_date = %s
                    WHERE id = %s
                """, (bags_returned, return_date, weft_entry_id))
                connection.commit()
                cursor.close()
                connection.close()
                return True, "Bags return recorded successfully"
            except Error as e:
                st.error(f"Mark bags returned error: {e}")
                return False, str(e)
        return False, "Database connection failed"

    def refund_bag_deposit(self, weft_entry_id, refund_date):
        """Mark bag deposit as refunded (only if all bags returned)"""
        connection = self.get_connection()
        if connection:
            try:
                cursor = connection.cursor()

                # Check if all bags returned
                cursor.execute("""
                    SELECT no_of_bags, bags_returned 
                    FROM job_worker_weft 
                    WHERE id = %s
                """, (weft_entry_id,))
                result = cursor.fetchone()

                if not result:
                    cursor.close()
                    connection.close()
                    return False, "Entry not found"

                total_bags, returned_bags = result

                if returned_bags < total_bags:
                    cursor.close()
                    connection.close()
                    return False, f"Only {returned_bags}/{total_bags} bags returned. Cannot refund yet."

                cursor.execute("""
                    UPDATE job_worker_weft 
                    SET deposit_refunded = TRUE, deposit_refund_date = %s
                    WHERE id = %s
                """, (refund_date, weft_entry_id))
                connection.commit()
                cursor.close()
                connection.close()
                return True, "Deposit refunded successfully"
            except Error as e:
                st.error(f"Refund bag deposit error: {e}")
                return False, str(e)
        return False, "Database connection failed"

    # ==================== VIEW RECORDS METHODS ====================

    def get_inventory_warp_by_date(self, from_date, to_date):
        """Get all inventory WARP records within a date range"""
        connection = self.get_connection()
        if connection:
            try:
                cursor = connection.cursor(dictionary=True)
                cursor.execute("""
                    SELECT warp_number, date, yarn_type, warper_name, design,
                           gross_weight, paper_weight, beam_weight, no_of_bell,
                           reed, net_weight
                    FROM inventory_warp
                    WHERE date BETWEEN %s AND %s
                    ORDER BY date DESC, id DESC
                """, (from_date, to_date))
                records = cursor.fetchall()
                cursor.close()
                connection.close()
                return records
            except Error as e:
                st.error(f"Get inventory WARP by date error: {e}")
                return []
        return []

    def get_inventory_weft_by_date(self, from_date, to_date):
        """Get all inventory WEFT records within a date range"""
        connection = self.get_connection()
        if connection:
            try:
                cursor = connection.cursor(dictionary=True)
                cursor.execute("""
                    SELECT date, colour, gross_weight, no_of_cones,
                           cone_weight, no_of_bags, net_weight
                    FROM inventory_weft
                    WHERE date BETWEEN %s AND %s
                    ORDER BY date DESC, id DESC
                """, (from_date, to_date))
                records = cursor.fetchall()
                cursor.close()
                connection.close()
                return records
            except Error as e:
                st.error(f"Get inventory WEFT by date error: {e}")
                return []
        return []

    def get_all_job_worker_warp_by_date(self, from_date, to_date):
        """Get all job worker WARP records for all workers within a date range"""
        connection = self.get_connection()
        if connection:
            try:
                cursor = connection.cursor(dictionary=True)
                cursor.execute("""
                    SELECT warp_number, date, job_worker, yarn_type, warper_name, design,
                           gross_weight, paper_weight, beam_weight, no_of_bell,
                           reed, net_weight
                    FROM job_worker_warp
                    WHERE date BETWEEN %s AND %s
                    ORDER BY date DESC, id DESC
                """, (from_date, to_date))
                records = cursor.fetchall()
                cursor.close()
                connection.close()
                return records
            except Error as e:
                st.error(f"Get all job worker WARP by date error: {e}")
                return []
        return []

    def get_all_job_worker_weft_by_date(self, from_date, to_date):
        """Get all job worker WEFT records for all workers within a date range"""
        connection = self.get_connection()
        if connection:
            try:
                cursor = connection.cursor(dictionary=True)
                cursor.execute("""
                    SELECT date, job_worker, colour, gross_weight, no_of_cones,
                           cone_weight, no_of_bags, net_weight
                    FROM job_worker_weft
                    WHERE date BETWEEN %s AND %s
                    ORDER BY date DESC, id DESC
                """, (from_date, to_date))
                records = cursor.fetchall()
                cursor.close()
                connection.close()
                return records
            except Error as e:
                st.error(f"Get all job worker WEFT by date error: {e}")
                return []
        return []

    def get_all_products_by_date(self, from_date, to_date):
        """Get all finished products within a date range"""
        connection = self.get_connection()
        if connection:
            try:
                cursor = connection.cursor(dictionary=True)
                cursor.execute("""
                    SELECT completion_date, job_worker, product_category,
                           total_pieces, total_meters, product_weight,
                           warp_used, weft_used, notes
                    FROM products
                    WHERE completion_date BETWEEN %s AND %s
                    ORDER BY completion_date DESC, id DESC
                """, (from_date, to_date))
                records = cursor.fetchall()
                cursor.close()
                connection.close()
                return records
            except Error as e:
                st.error(f"Get all products by date error: {e}")
                return []
        return []

    # ==================== END OF VIEW RECORDS METHODS ====================

    # ============================================================
    # PART 1: ADD TO database.py
    # Location: After get_all_products_by_date method (around line 900)
    # ============================================================

    def get_job_worker_warp_with_balance(self, from_date, to_date):
        """Get all job worker WARP records with running balance"""
        connection = self.get_connection()
        if connection:
            try:
                cursor = connection.cursor(dictionary=True)

                # Get all WARP entries in date range
                cursor.execute("""
                    SELECT warp_number, date, job_worker, yarn_type, warper_name, design,
                           gross_weight, paper_weight, beam_weight, no_of_bell,
                           reed, net_weight, id
                    FROM job_worker_warp
                    WHERE date BETWEEN %s AND %s
                    ORDER BY date ASC, id ASC
                """, (from_date, to_date))
                records = cursor.fetchall()

                # Calculate balance for each record
                for record in records:
                    worker = record['job_worker']

                    # Get total material used in products UP TO this entry's date
                    cursor.execute("""
                        SELECT COALESCE(SUM(warp_used + weft_used), 0) as total_used
                        FROM products
                        WHERE job_worker = %s AND completion_date <= %s
                    """, (worker, record['date']))
                    total_used = float(cursor.fetchone()['total_used'])

                    # Get total WARP distributed UP TO this entry
                    cursor.execute("""
                        SELECT COALESCE(SUM(net_weight), 0) as total_distributed
                        FROM job_worker_warp
                        WHERE job_worker = %s AND date <= %s AND id <= %s
                    """, (worker, record['date'], record['id']))
                    warp_distributed = float(cursor.fetchone()['total_distributed'])

                    # Get total WEFT distributed UP TO this entry's date
                    cursor.execute("""
                        SELECT COALESCE(SUM(net_weight), 0) as total_distributed
                        FROM job_worker_weft
                        WHERE job_worker = %s AND date <= %s
                    """, (worker, record['date']))
                    weft_distributed = float(cursor.fetchone()['total_distributed'])

                    # Balance = (Total WARP + Total WEFT distributed - Used) / 2
                    total_distributed = warp_distributed + weft_distributed
                    balance = (total_distributed - total_used) / 2
                    record['balance'] = round(balance, 2)

                cursor.close()
                connection.close()
                return records
            except Error as e:
                st.error(f"Get job worker WARP with balance error: {e}")
                return []
        return []

    def get_job_worker_weft_with_balance(self, from_date, to_date):
        """Get all job worker WEFT records with running balance"""
        connection = self.get_connection()
        if connection:
            try:
                cursor = connection.cursor(dictionary=True)

                # Get all WEFT entries in date range
                cursor.execute("""
                    SELECT date, job_worker, colour, gross_weight, no_of_cones,
                           cone_weight, no_of_bags, net_weight, id
                    FROM job_worker_weft
                    WHERE date BETWEEN %s AND %s
                    ORDER BY date ASC, id ASC
                """, (from_date, to_date))
                records = cursor.fetchall()

                # Calculate balance for each record
                for record in records:
                    worker = record['job_worker']

                    # Get total material used in products UP TO this entry's date
                    cursor.execute("""
                        SELECT COALESCE(SUM(warp_used + weft_used), 0) as total_used
                        FROM products
                        WHERE job_worker = %s AND completion_date <= %s
                    """, (worker, record['date']))
                    total_used = float(cursor.fetchone()['total_used'])

                    # Get total WARP distributed UP TO this entry's date
                    cursor.execute("""
                        SELECT COALESCE(SUM(net_weight), 0) as total_distributed
                        FROM job_worker_warp
                        WHERE job_worker = %s AND date <= %s
                    """, (worker, record['date']))
                    warp_distributed = float(cursor.fetchone()['total_distributed'])

                    # Get total WEFT distributed UP TO this entry
                    cursor.execute("""
                        SELECT COALESCE(SUM(net_weight), 0) as total_distributed
                        FROM job_worker_weft
                        WHERE job_worker = %s AND date <= %s AND id <= %s
                    """, (worker, record['date'], record['id']))
                    weft_distributed = float(cursor.fetchone()['total_distributed'])

                    # Balance = (Total WARP + Total WEFT distributed - Used) / 2
                    total_distributed = warp_distributed + weft_distributed
                    balance = (total_distributed - total_used) / 2
                    record['balance'] = round(balance, 2)

                cursor.close()
                connection.close()
                return records
            except Error as e:
                st.error(f"Get job worker WEFT with balance error: {e}")
                return []
        return []

    def get_worker_summary_with_balance(self, job_worker, from_date, to_date):
        """Get worker summary with balance for specific date range"""
        connection = self.get_connection()
        if connection:
            try:
                cursor = connection.cursor(dictionary=True)

                # Total WARP distributed in period
                cursor.execute("""
                    SELECT COALESCE(SUM(net_weight), 0) as total_warp
                    FROM job_worker_warp
                    WHERE job_worker = %s AND date BETWEEN %s AND %s
                """, (job_worker, from_date, to_date))
                warp_in_period = float(cursor.fetchone()['total_warp'])

                # Total WEFT distributed in period
                cursor.execute("""
                    SELECT COALESCE(SUM(net_weight), 0) as total_weft
                    FROM job_worker_weft
                    WHERE job_worker = %s AND date BETWEEN %s AND %s
                """, (job_worker, from_date, to_date))
                weft_in_period = float(cursor.fetchone()['total_weft'])

                # Total used in products in period
                cursor.execute("""
                    SELECT COALESCE(SUM(warp_used + weft_used), 0) as total_used
                    FROM products
                    WHERE job_worker = %s AND completion_date BETWEEN %s AND %s
                """, (job_worker, from_date, to_date))
                material_used = float(cursor.fetchone()['total_used'])

                # Period balance = (WARP + WEFT distributed - Used) / 2
                total_distributed = warp_in_period + weft_in_period
                balance = (total_distributed - material_used) / 2

                cursor.close()
                connection.close()

                return {
                    'warp_distributed': warp_in_period,
                    'weft_distributed': weft_in_period,
                    'material_used': material_used,
                    'balance': round(balance, 2)
                }
            except Error as e:
                st.error(f"Get worker summary with balance error: {e}")
                return None
        return None

    # ==================== ADD THESE 3 METHODS TO database.py ====================
    # Location: After get_all_products_by_date method (around line 900)
    # Copy-paste ALL 3 methods below

    def get_job_worker_warp_with_balance(self, from_date, to_date):
        """Get all job worker WARP records with running balance"""
        connection = self.get_connection()
        if connection:
            try:
                cursor = connection.cursor(dictionary=True)

                # Get all WARP entries in date range
                cursor.execute("""
                    SELECT warp_number, date, job_worker, yarn_type, warper_name, design,
                           gross_weight, paper_weight, beam_weight, no_of_bell,
                           reed, net_weight, id
                    FROM job_worker_warp
                    WHERE date BETWEEN %s AND %s
                    ORDER BY date ASC, id ASC
                """, (from_date, to_date))
                records = cursor.fetchall()

                # Calculate balance for each record
                for record in records:
                    worker = record['job_worker']

                    # Get total material used in products UP TO this entry's date
                    cursor.execute("""
                        SELECT COALESCE(SUM(warp_used + weft_used), 0) as total_used
                        FROM products
                        WHERE job_worker = %s AND completion_date <= %s
                    """, (worker, record['date']))
                    total_used = float(cursor.fetchone()['total_used'])

                    # Get total WARP distributed UP TO this entry
                    cursor.execute("""
                        SELECT COALESCE(SUM(net_weight), 0) as total_distributed
                        FROM job_worker_warp
                        WHERE job_worker = %s AND date <= %s AND id <= %s
                    """, (worker, record['date'], record['id']))
                    warp_distributed = float(cursor.fetchone()['total_distributed'])

                    # Get total WEFT distributed UP TO this entry's date
                    cursor.execute("""
                        SELECT COALESCE(SUM(net_weight), 0) as total_distributed
                        FROM job_worker_weft
                        WHERE job_worker = %s AND date <= %s
                    """, (worker, record['date']))
                    weft_distributed = float(cursor.fetchone()['total_distributed'])

                    # Balance = (Total WARP + Total WEFT distributed - Used) / 2
                    total_distributed = warp_distributed + weft_distributed
                    balance = (total_distributed - total_used) / 2
                    record['balance'] = round(balance, 2)

                cursor.close()
                connection.close()
                return records
            except Error as e:
                st.error(f"Get job worker WARP with balance error: {e}")
                return []
        return []

    def get_job_worker_weft_with_balance(self, from_date, to_date):
        """Get all job worker WEFT records with running balance"""
        connection = self.get_connection()
        if connection:
            try:
                cursor = connection.cursor(dictionary=True)

                # Get all WEFT entries in date range
                cursor.execute("""
                    SELECT date, job_worker, colour, gross_weight, no_of_cones,
                           cone_weight, no_of_bags, net_weight, id
                    FROM job_worker_weft
                    WHERE date BETWEEN %s AND %s
                    ORDER BY date ASC, id ASC
                """, (from_date, to_date))
                records = cursor.fetchall()

                # Calculate balance for each record
                for record in records:
                    worker = record['job_worker']

                    # Get total material used in products UP TO this entry's date
                    cursor.execute("""
                        SELECT COALESCE(SUM(warp_used + weft_used), 0) as total_used
                        FROM products
                        WHERE job_worker = %s AND completion_date <= %s
                    """, (worker, record['date']))
                    total_used = float(cursor.fetchone()['total_used'])

                    # Get total WARP distributed UP TO this entry's date
                    cursor.execute("""
                        SELECT COALESCE(SUM(net_weight), 0) as total_distributed
                        FROM job_worker_warp
                        WHERE job_worker = %s AND date <= %s
                    """, (worker, record['date']))
                    warp_distributed = float(cursor.fetchone()['total_distributed'])

                    # Get total WEFT distributed UP TO this entry
                    cursor.execute("""
                        SELECT COALESCE(SUM(net_weight), 0) as total_distributed
                        FROM job_worker_weft
                        WHERE job_worker = %s AND date <= %s AND id <= %s
                    """, (worker, record['date'], record['id']))
                    weft_distributed = float(cursor.fetchone()['total_distributed'])

                    # Balance = (Total WARP + Total WEFT distributed - Used) / 2
                    total_distributed = warp_distributed + weft_distributed
                    balance = (total_distributed - total_used) / 2
                    record['balance'] = round(balance, 2)

                cursor.close()
                connection.close()
                return records
            except Error as e:
                st.error(f"Get job worker WEFT with balance error: {e}")
                return []
        return []

    def get_worker_summary_with_balance(self, job_worker, from_date, to_date):
        """Get worker summary with balance for specific date range"""
        connection = self.get_connection()
        if connection:
            try:
                cursor = connection.cursor(dictionary=True)

                # Total WARP distributed in period
                cursor.execute("""
                    SELECT COALESCE(SUM(net_weight), 0) as total_warp
                    FROM job_worker_warp
                    WHERE job_worker = %s AND date BETWEEN %s AND %s
                """, (job_worker, from_date, to_date))
                warp_in_period = float(cursor.fetchone()['total_warp'])

                # Total WEFT distributed in period
                cursor.execute("""
                    SELECT COALESCE(SUM(net_weight), 0) as total_weft
                    FROM job_worker_weft
                    WHERE job_worker = %s AND date BETWEEN %s AND %s
                """, (job_worker, from_date, to_date))
                weft_in_period = float(cursor.fetchone()['total_weft'])

                # Total used in products in period
                cursor.execute("""
                    SELECT COALESCE(SUM(warp_used + weft_used), 0) as total_used
                    FROM products
                    WHERE job_worker = %s AND completion_date BETWEEN %s AND %s
                """, (job_worker, from_date, to_date))
                material_used = float(cursor.fetchone()['total_used'])

                # Period balance = (WARP + WEFT distributed - Used) / 2
                total_distributed = warp_in_period + weft_in_period
                balance = (total_distributed - material_used) / 2

                cursor.close()
                connection.close()

                return {
                    'warp_distributed': warp_in_period,
                    'weft_distributed': weft_in_period,
                    'material_used': material_used,
                    'balance': round(balance, 2)
                }
            except Error as e:
                st.error(f"Get worker summary with balance error: {e}")
                return None
        return None

    # ==================== END OF NEW METHODS ====================
