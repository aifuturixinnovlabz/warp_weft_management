# from datetime import date
#
# class MaterialService:
#     def __init__(self, database):
#         self.db = database
#
#     # ========================================
#     # INVENTORY WARP VALIDATION & METHODS
#     # ========================================
#     def validate_inventory_warp_input(self, beem_weight, paper_weight):
#         """Validate inventory WARP inputs"""
#         errors = []
#         if beem_weight <= 0:
#             errors.append("Beem weight must be greater than 0")
#         if paper_weight < 0:
#             errors.append("Paper weight cannot be negative")
#         if beem_weight <= paper_weight:
#             errors.append("Beem weight must be greater than paper weight")
#         return errors
#
#     def calculate_warp_net_weight(self, beem_weight, paper_weight):
#         """Calculate WARP net weight"""
#         return round(beem_weight - paper_weight, 2)
#
#     def add_inventory_warp(self, entry_date, yarn_name, design, paper_weight, beem_weight):
#         """Add WARP to inventory"""
#         errors = self.validate_inventory_warp_input(beem_weight, paper_weight)
#         if errors:
#             return False, errors
#         data = (entry_date, yarn_name, design, paper_weight, beem_weight)
#         success = self.db.insert_inventory_warp(data)
#         if success:
#             net_weight = self.calculate_warp_net_weight(beem_weight, paper_weight)
#             return True, [f"✅ Inventory WARP added successfully! Net Weight: {net_weight:.2f} kg"]
#         else:
#             return False, ["❌ Failed to add inventory WARP"]
#
#     # ========================================
#     # INVENTORY WEFT VALIDATION & METHODS
#     # ========================================
#     def validate_inventory_weft_input(self, no_of_cones, weight_per_cone):
#         """Validate inventory WEFT inputs"""
#         errors = []
#         if no_of_cones <= 0:
#             errors.append("Number of cones must be greater than 0")
#         if weight_per_cone <= 0:
#             errors.append("Weight per cone must be greater than 0")
#         return errors
#
#     def calculate_weft_total_weight(self, no_of_cones, weight_per_cone):
#         """Calculate WEFT total weight"""
#         return round(no_of_cones * weight_per_cone, 2)
#
#     def add_inventory_weft(self, entry_date, colour, no_of_cones, weight_per_cone):
#         """Add WEFT to inventory"""
#         errors = self.validate_inventory_weft_input(no_of_cones, weight_per_cone)
#         if errors:
#             return False, errors
#         data = (entry_date, colour, no_of_cones, weight_per_cone)
#         success = self.db.insert_inventory_weft(data)
#         if success:
#             total_weight = self.calculate_weft_total_weight(no_of_cones, weight_per_cone)
#             return True, [f"✅ Inventory WEFT added successfully! Total Weight: {total_weight:.2f} kg"]
#         else:
#             return False, ["❌ Failed to add inventory WEFT"]
#
#     # ========================================
#     # JOB WORKER WARP VALIDATION & METHODS
#     # ========================================
#     def validate_job_worker_warp_input(self, beem_weight, paper_weight):
#         """Validate job worker WARP inputs"""
#         errors = []
#         if beem_weight <= 0:
#             errors.append("Beem weight must be greater than 0")
#         if paper_weight < 0:
#             errors.append("Paper weight cannot be negative")
#         if beem_weight <= paper_weight:
#             errors.append("Beem weight must be greater than paper weight")
#         return errors
#
#     def add_job_worker_warp(self, entry_date, yarn_name, design, paper_weight, beem_weight, job_worker):
#         """Distribute WARP to job worker with inventory validation"""
#         errors = self.validate_job_worker_warp_input(beem_weight, paper_weight)
#         if errors:
#             return False, errors
#         net_weight = self.calculate_warp_net_weight(beem_weight, paper_weight)
#         available_inventory = self.db.get_available_inventory_warp()
#         if net_weight > available_inventory:
#             return False, [
#                 f"❌ Insufficient WARP inventory!",
#                 f"Required: {net_weight:.2f} kg",
#                 f"Available: {available_inventory:.2f} kg",
#                 f"Shortage: {net_weight - available_inventory:.2f} kg"
#             ]
#         data = (entry_date, yarn_name, design, paper_weight, beem_weight, job_worker)
#         success = self.db.insert_job_worker_warp(data)
#         if success:
#             remaining_inventory = available_inventory - net_weight
#             return True, [
#                 f"✅ WARP distributed to {job_worker} successfully!",
#                 f"📊 Net Weight: {net_weight:.2f} kg",
#                 f"📦 Remaining Inventory: {remaining_inventory:.2f} kg"
#             ]
#         else:
#             return False, ["❌ Failed to distribute WARP to job worker"]
#
#     # ========================================
#     # JOB WORKER WEFT VALIDATION & METHODS
#     # ========================================
#     def validate_job_worker_weft_input(self, no_of_cones, weight_per_cone):
#         """Validate job worker WEFT inputs"""
#         errors = []
#         if no_of_cones <= 0:
#             errors.append("Number of cones must be greater than 0")
#         if weight_per_cone <= 0:
#             errors.append("Weight per cone must be greater than 0")
#         return errors
#
#     def add_job_worker_weft(self, entry_date, colour, no_of_cones, weight_per_cone, job_worker):
#         """Distribute WEFT to job worker with inventory validation"""
#         errors = self.validate_job_worker_weft_input(no_of_cones, weight_per_cone)
#         if errors:
#             return False, errors
#         total_weight = self.calculate_weft_total_weight(no_of_cones, weight_per_cone)
#         available_inventory = self.db.get_available_inventory_weft()
#         if total_weight > available_inventory:
#             return False, [
#                 f"❌ Insufficient WEFT inventory!",
#                 f"Required: {total_weight:.2f} kg",
#                 f"Available: {available_inventory:.2f} kg",
#                 f"Shortage: {total_weight - available_inventory:.2f} kg"
#             ]
#         data = (entry_date, colour, no_of_cones, weight_per_cone, job_worker)
#         success = self.db.insert_job_worker_weft(data)
#         if success:
#             remaining_inventory = available_inventory - total_weight
#             return True, [
#                 f"✅ WEFT distributed to {job_worker} successfully!",
#                 f"📊 Total Weight: {total_weight:.2f} kg",
#                 f"📦 Remaining Inventory: {remaining_inventory:.2f} kg"
#             ]
#         else:
#             return False, ["❌ Failed to distribute WEFT to job worker"]
#
#     # ========================================
#     # PRODUCT VALIDATION & METHODS
#     # ========================================
#     def validate_product_input(self, product_weight, total_pieces, total_meters, job_worker):
#         """Validate product completion inputs"""
#         errors = []
#         if product_weight <= 0:
#             errors.append("Product weight must be greater than 0")
#         if total_pieces <= 0:
#             errors.append("Total pieces must be greater than 0")
#         if total_meters <= 0:
#             errors.append("Total meters must be greater than 0")
#         warp_needed = product_weight / 2
#         weft_needed = product_weight / 2
#         balance = self.db.get_worker_balance(job_worker)
#         if balance:
#             warp_balance = balance['warp_balance']
#             weft_balance = balance['weft_balance']
#             if warp_needed > warp_balance:
#                 errors.append(
#                     f"❌ Insufficient WARP! Required: {warp_needed:.2f} kg, Available: {warp_balance:.2f} kg"
#                 )
#             if weft_needed > weft_balance:
#                 errors.append(
#                     f"❌ Insufficient WEFT! Required: {weft_needed:.2f} kg, Available: {weft_balance:.2f} kg"
#                 )
#         return errors
#
#     def complete_product(self, job_worker, product_category, completion_date, total_pieces,
#                          total_meters, product_weight, notes=""):
#         """Complete product - auto-divide material equally"""
#         errors = self.validate_product_input(product_weight, total_pieces, total_meters, job_worker)
#         if errors:
#             return False, errors
#         warp_used = product_weight / 2
#         weft_used = product_weight / 2
#         data = (job_worker, product_category, completion_date, total_pieces,
#                 total_meters, product_weight, warp_used, weft_used, notes)
#         success = self.db.insert_product(data)
#         if success:
#             balance = self.db.get_worker_balance(job_worker)
#             if balance:
#                 warp_balance = balance['warp_balance']
#                 weft_balance = balance['weft_balance']
#                 total_balance = warp_balance + weft_balance
#                 return True, [
#                     f"✅ Product completed successfully!",
#                     f"📦 Product: {product_category}",
#                     f"🏭 Pieces: {total_pieces} | Meters: {total_meters:.2f}m | Weight: {product_weight:.2f} kg",
#                     f"📊 Material Used (Auto-Divided Equally):",
#                     f"   • WARP: {warp_used:.2f} kg",
#                     f"   • WEFT: {weft_used:.2f} kg",
#                     f"💼 Remaining Balance:",
#                     f"   • WARP: {warp_balance:.2f} kg",
#                     f"   • WEFT: {weft_balance:.2f} kg",
#                     f"   • Total: {total_balance:.2f} kg"
#                 ]
#             else:
#                 return True, [f"✅ Product completed successfully!"]
#         else:
#             return False, ["❌ Failed to complete product"]
#
#     # ========================================
#     # COLOR MANAGEMENT
#     # ========================================
#     def validate_color_input(self, color_name):
#         """Validate color input"""
#         errors = []
#         if not color_name or not color_name.strip():
#             errors.append("Color name cannot be empty")
#         if len(color_name) > 50:
#             errors.append("Color name too long (max 50 characters)")
#         return errors
#
#     def add_color(self, color_name):
#         """Add new color"""
#         errors = self.validate_color_input(color_name)
#         if errors:
#             return False, errors
#         success = self.db.add_color(color_name.strip())
#         if success:
#             return True, [f"✅ Color '{color_name}' added successfully!"]
#         else:
#             return False, ["❌ Failed to add color (may already exist)"]
#
#     # ========================================
#     # YARN/MATERIAL MANAGEMENT (NEW)
#     # ========================================
#     def validate_yarn_material_input(self, material_name):
#         """Validate yarn/material input"""
#         errors = []
#         if not material_name or not material_name.strip():
#             errors.append("Material name cannot be empty")
#         if len(material_name) > 100:
#             errors.append("Material name too long (max 100 characters)")
#         return errors
#
#     def add_yarn_material(self, material_name):
#         """Add new yarn/material"""
#         errors = self.validate_yarn_material_input(material_name)
#         if errors:
#             return False, errors
#         success = self.db.add_yarn_material(material_name.strip())
#         if success:
#             return True, [f"✅ Yarn/Material '{material_name}' added successfully!"]
#         else:
#             return False, ["❌ Failed to add yarn/material (may already exist)"]
#
#     # ========================================
#     # DESIGN/WEAVE TYPE MANAGEMENT (NEW)
#     # ========================================
#     def validate_design_weave_type_input(self, design_name):
#         """Validate design/weave type input"""
#         errors = []
#         if not design_name or not design_name.strip():
#             errors.append("Design name cannot be empty")
#         if len(design_name) > 100:
#             errors.append("Design name too long (max 100 characters)")
#         return errors
#
#     def add_design_weave_type(self, design_name):
#         """Add new design/weave type"""
#         errors = self.validate_design_weave_type_input(design_name)
#         if errors:
#             return False, errors
#         success = self.db.add_design_weave_type(design_name.strip())
#         if success:
#             return True, [f"✅ Design/Weave Type '{design_name}' added successfully!"]
#         else:
#             return False, ["❌ Failed to add design/weave type (may already exist)"]
#
#     # ========================================
#     # PRODUCT CATEGORY MANAGEMENT
#     # ========================================
#     def validate_category_input(self, category_name):
#         """Validate product category input"""
#         errors = []
#         if not category_name or not category_name.strip():
#             errors.append("Category name cannot be empty")
#         if len(category_name) > 100:
#             errors.append("Category name too long (max 100 characters)")
#         return errors
#
#     def add_product_category(self, category_name):
#         """Add new product category"""
#         errors = self.validate_category_input(category_name)
#         if errors:
#             return False, errors
#         success = self.db.add_product_category(category_name.strip())
#         if success:
#             return True, [f"✅ Product category '{category_name}' added successfully!"]
#         else:
#             return False, ["❌ Failed to add category (may already exist)"]
#
#     # ========================================
#     # JOB WORKER MANAGEMENT
#     # ========================================
#     def validate_job_worker_input(self, worker_name, contact_number="", gst_number="", aadhar_number=""):
#         """Validate job worker input"""
#         errors = []
#         if not worker_name or not worker_name.strip():
#             errors.append("Worker name cannot be empty")
#         if len(worker_name) > 100:
#             errors.append("Worker name too long (max 100 characters)")
#         if contact_number and len(contact_number) > 0:
#             if len(contact_number) < 10:
#                 errors.append("Contact number must be at least 10 digits")
#             if not contact_number.replace("+", "").replace("-", "").replace(" ", "").isdigit():
#                 errors.append("Contact number must contain only digits, +, -, or spaces")
#         if gst_number and len(gst_number) > 0:
#             if len(gst_number) != 15:
#                 errors.append("GST number must be exactly 15 characters")
#         if aadhar_number and len(aadhar_number) > 0:
#             aadhar_clean = aadhar_number.replace("-", "").replace(" ", "")
#             if len(aadhar_clean) != 12:
#                 errors.append("Aadhar number must be 12 digits")
#             if not aadhar_clean.isdigit():
#                 errors.append("Aadhar number must contain only digits")
#         return errors
#
#     def add_job_worker(self, worker_name, contact_number="", gst_number="", aadhar_number=""):
#         """Add new job worker"""
#         errors = self.validate_job_worker_input(worker_name, contact_number, gst_number, aadhar_number)
#         if errors:
#             return False, errors
#         success = self.db.add_job_worker(
#             worker_name.strip(), contact_number.strip(), gst_number.strip(), aadhar_number.strip()
#         )
#         if success:
#             return True, [f"✅ Job worker '{worker_name}' added successfully!"]
#         else:
#             return False, ["❌ Failed to add job worker (may already exist)"]
#
#     def update_job_worker(self, old_worker_name, worker_name, contact_number, gst_number, aadhar_number):
#         """Update job worker"""
#         errors = self.validate_job_worker_input(worker_name, contact_number, gst_number, aadhar_number)
#         if errors:
#             return False, errors
#         success = self.db.update_job_worker(
#             old_worker_name, worker_name.strip(), contact_number.strip(), gst_number.strip(), aadhar_number.strip()
#         )
#         if success:
#             return True, [f"✅ Job worker '{worker_name}' updated successfully!"]
#         else:
#             return False, ["❌ Failed to update job worker"]



from datetime import date

class MaterialService:
    def __init__(self, database):
        self.db = database

    # ========================================
    # INVENTORY WARP VALIDATION & METHODS
    # ========================================
    def validate_inventory_warp_input(self, beem_weight, paper_weight):
        """Validate inventory WARP inputs"""
        errors = []
        if beem_weight <= 0:
            errors.append("Beem weight must be greater than 0")
        if paper_weight < 0:
            errors.append("Paper weight cannot be negative")
        if beem_weight <= paper_weight:
            errors.append("Beem weight must be greater than paper weight")
        return errors

    def calculate_warp_net_weight(self, beem_weight, paper_weight):
        """Calculate WARP net weight"""
        return round(beem_weight - paper_weight, 2)

    def add_inventory_warp(self, entry_date, yarn_name, design, paper_weight, beem_weight):
        """Add WARP to inventory"""
        errors = self.validate_inventory_warp_input(beem_weight, paper_weight)
        if errors:
            return False, errors
        data = (entry_date, yarn_name, design, paper_weight, beem_weight)
        success = self.db.insert_inventory_warp(data)
        if success:
            net_weight = self.calculate_warp_net_weight(beem_weight, paper_weight)
            return True, [f"✅ Inventory WARP added successfully! Net Weight: {net_weight:.2f} kg"]
        else:
            return False, ["❌ Failed to add inventory WARP"]

    # ========================================
    # INVENTORY WEFT VALIDATION & METHODS
    # ========================================
    def validate_inventory_weft_input(self, no_of_cones, weight_per_cone):
        """Validate inventory WEFT inputs"""
        errors = []
        if no_of_cones <= 0:
            errors.append("Number of cones must be greater than 0")
        if weight_per_cone <= 0:
            errors.append("Weight per cone must be greater than 0")
        return errors

    def calculate_weft_total_weight(self, no_of_cones, weight_per_cone):
        """Calculate WEFT total weight"""
        return round(no_of_cones * weight_per_cone, 2)

    def add_inventory_weft(self, entry_date, colour, no_of_cones, weight_per_cone):
        """Add WEFT to inventory"""
        errors = self.validate_inventory_weft_input(no_of_cones, weight_per_cone)
        if errors:
            return False, errors
        data = (entry_date, colour, no_of_cones, weight_per_cone)
        success = self.db.insert_inventory_weft(data)
        if success:
            total_weight = self.calculate_weft_total_weight(no_of_cones, weight_per_cone)
            return True, [f"✅ Inventory WEFT added successfully! Total Weight: {total_weight:.2f} kg"]
        else:
            return False, ["❌ Failed to add inventory WEFT"]

    # ========================================
    # JOB WORKER WARP VALIDATION & METHODS
    # ========================================
    def validate_job_worker_warp_input(self, beem_weight, paper_weight):
        """Validate job worker WARP inputs"""
        errors = []
        if beem_weight <= 0:
            errors.append("Beem weight must be greater than 0")
        if paper_weight < 0:
            errors.append("Paper weight cannot be negative")
        if beem_weight <= paper_weight:
            errors.append("Beem weight must be greater than paper weight")
        return errors

    def add_job_worker_warp(self, entry_date, yarn_name, design, paper_weight, beem_weight, job_worker):
        """Distribute WARP to job worker with inventory validation"""
        errors = self.validate_job_worker_warp_input(beem_weight, paper_weight)
        if errors:
            return False, errors
        net_weight = self.calculate_warp_net_weight(beem_weight, paper_weight)
        available_inventory = self.db.get_available_inventory_warp()
        if net_weight > available_inventory:
            return False, [
                f"❌ Insufficient WARP inventory!",
                f"Required: {net_weight:.2f} kg",
                f"Available: {available_inventory:.2f} kg",
                f"Shortage: {net_weight - available_inventory:.2f} kg"
            ]
        data = (entry_date, yarn_name, design, paper_weight, beem_weight, job_worker)
        success = self.db.insert_job_worker_warp(data)
        if success:
            remaining_inventory = available_inventory - net_weight
            return True, [
                f"✅ WARP distributed to {job_worker} successfully!",
                f"📊 Net Weight: {net_weight:.2f} kg",
                f"📦 Remaining Inventory: {remaining_inventory:.2f} kg"
            ]
        else:
            return False, ["❌ Failed to distribute WARP to job worker"]

    # ========================================
    # JOB WORKER WEFT VALIDATION & METHODS
    # ========================================
    def validate_job_worker_weft_input(self, no_of_cones, weight_per_cone):
        """Validate job worker WEFT inputs"""
        errors = []
        if no_of_cones <= 0:
            errors.append("Number of cones must be greater than 0")
        if weight_per_cone <= 0:
            errors.append("Weight per cone must be greater than 0")
        return errors

    def add_job_worker_weft(self, entry_date, colour, no_of_cones, weight_per_cone, job_worker):
        """Distribute WEFT to job worker with inventory validation"""
        errors = self.validate_job_worker_weft_input(no_of_cones, weight_per_cone)
        if errors:
            return False, errors
        total_weight = self.calculate_weft_total_weight(no_of_cones, weight_per_cone)
        available_inventory = self.db.get_available_inventory_weft()
        if total_weight > available_inventory:
            return False, [
                f"❌ Insufficient WEFT inventory!",
                f"Required: {total_weight:.2f} kg",
                f"Available: {available_inventory:.2f} kg",
                f"Shortage: {total_weight - available_inventory:.2f} kg"
            ]
        data = (entry_date, colour, no_of_cones, weight_per_cone, job_worker)
        success = self.db.insert_job_worker_weft(data)
        if success:
            remaining_inventory = available_inventory - total_weight
            return True, [
                f"✅ WEFT distributed to {job_worker} successfully!",
                f"📊 Total Weight: {total_weight:.2f} kg",
                f"📦 Remaining Inventory: {remaining_inventory:.2f} kg"
            ]
        else:
            return False, ["❌ Failed to distribute WEFT to job worker"]

    # ========================================
    # PRODUCT VALIDATION & METHODS
    # ========================================
    def validate_product_input(self, product_weight, total_pieces, total_meters, job_worker):
        """Validate product completion inputs"""
        errors = []
        if product_weight <= 0:
            errors.append("Product weight must be greater than 0")
        if total_pieces <= 0:
            errors.append("Total pieces must be greater than 0")
        if total_meters <= 0:
            errors.append("Total meters must be greater than 0")
        warp_needed = product_weight / 2
        weft_needed = product_weight / 2
        balance = self.db.get_worker_balance(job_worker)
        if balance:
            warp_balance = balance['warp_balance']
            weft_balance = balance['weft_balance']
            if warp_needed > warp_balance:
                errors.append(
                    f"❌ Insufficient WARP! Required: {warp_needed:.2f} kg, Available: {warp_balance:.2f} kg"
                )
            if weft_needed > weft_balance:
                errors.append(
                    f"❌ Insufficient WEFT! Required: {weft_needed:.2f} kg, Available: {weft_balance:.2f} kg"
                )
        return errors

    def complete_product(self, job_worker, product_category, completion_date, total_pieces,
                         total_meters, product_weight, notes=""):
        """Complete product - auto-divide material equally"""
        errors = self.validate_product_input(product_weight, total_pieces, total_meters, job_worker)
        if errors:
            return False, errors
        warp_used = product_weight / 2
        weft_used = product_weight / 2
        data = (job_worker, product_category, completion_date, total_pieces,
                total_meters, product_weight, warp_used, weft_used, notes)
        success = self.db.insert_product(data)
        if success:
            balance = self.db.get_worker_balance(job_worker)
            if balance:
                warp_balance = balance['warp_balance']
                weft_balance = balance['weft_balance']
                total_balance = warp_balance + weft_balance
                return True, [
                    f"✅ Product completed successfully!",
                    f"📦 Product: {product_category}",
                    f"🏭 Pieces: {total_pieces} | Meters: {total_meters:.2f}m | Weight: {product_weight:.2f} kg",
                    f"📊 Material Used (Auto-Divided Equally):",
                    f"   • WARP: {warp_used:.2f} kg",
                    f"   • WEFT: {weft_used:.2f} kg",
                    f"💼 Remaining Balance:",
                    f"   • WARP: {warp_balance:.2f} kg",
                    f"   • WEFT: {weft_balance:.2f} kg",
                    f"   • Total: {total_balance:.2f} kg"
                ]
            else:
                return True, [f"✅ Product completed successfully!"]
        else:
            return False, ["❌ Failed to complete product"]

    # ========================================
    # COLOR MANAGEMENT
    # ========================================
    def validate_color_input(self, color_name):
        """Validate color input"""
        errors = []
        if not color_name or not color_name.strip():
            errors.append("Color name cannot be empty")
        if len(color_name) > 50:
            errors.append("Color name too long (max 50 characters)")
        return errors

    def add_color(self, color_name):
        """Add new color"""
        errors = self.validate_color_input(color_name)
        if errors:
            return False, errors
        success = self.db.add_color(color_name.strip())
        if success:
            return True, [f"✅ Color '{color_name}' added successfully!"]
        else:
            return False, ["❌ Failed to add color (may already exist)"]

    # ========================================
    # YARN/MATERIAL MANAGEMENT (NEW)
    # ========================================
    def validate_yarn_material_input(self, material_name):
        """Validate yarn/material input"""
        errors = []
        if not material_name or not material_name.strip():
            errors.append("Material name cannot be empty")
        if len(material_name) > 100:
            errors.append("Material name too long (max 100 characters)")
        return errors

    def add_yarn_material(self, material_name):
        """Add new yarn/material"""
        errors = self.validate_yarn_material_input(material_name)
        if errors:
            return False, errors
        success = self.db.add_yarn_material(material_name.strip())
        if success:
            return True, [f"✅ Yarn/Material '{material_name}' added successfully!"]
        else:
            return False, ["❌ Failed to add yarn/material (may already exist)"]

    # ========================================
    # DESIGN/WEAVE TYPE MANAGEMENT (NEW)
    # ========================================
    def validate_design_weave_type_input(self, design_name):
        """Validate design/weave type input"""
        errors = []
        if not design_name or not design_name.strip():
            errors.append("Design name cannot be empty")
        if len(design_name) > 100:
            errors.append("Design name too long (max 100 characters)")
        return errors

    def add_design_weave_type(self, design_name):
        """Add new design/weave type"""
        errors = self.validate_design_weave_type_input(design_name)
        if errors:
            return False, errors
        success = self.db.add_design_weave_type(design_name.strip())
        if success:
            return True, [f"✅ Design/Weave Type '{design_name}' added successfully!"]
        else:
            return False, ["❌ Failed to add design/weave type (may already exist)"]

    # ========================================
    # PRODUCT CATEGORY MANAGEMENT
    # ========================================
    def validate_category_input(self, category_name):
        """Validate product category input"""
        errors = []
        if not category_name or not category_name.strip():
            errors.append("Category name cannot be empty")
        if len(category_name) > 100:
            errors.append("Category name too long (max 100 characters)")
        return errors

    def add_product_category(self, category_name):
        """Add new product category"""
        errors = self.validate_category_input(category_name)
        if errors:
            return False, errors
        success = self.db.add_product_category(category_name.strip())
        if success:
            return True, [f"✅ Product category '{category_name}' added successfully!"]
        else:
            return False, ["❌ Failed to add category (may already exist)"]

    # ========================================
    # JOB WORKER MANAGEMENT
    # ========================================
    def validate_job_worker_input(self, worker_name, contact_number="", gst_number="", aadhar_number=""):
        """Validate job worker input"""
        errors = []
        if not worker_name or not worker_name.strip():
            errors.append("Worker name cannot be empty")
        if len(worker_name) > 100:
            errors.append("Worker name too long (max 100 characters)")
        if contact_number and len(contact_number) > 0:
            if len(contact_number) < 10:
                errors.append("Contact number must be at least 10 digits")
            if not contact_number.replace("+", "").replace("-", "").replace(" ", "").isdigit():
                errors.append("Contact number must contain only digits, +, -, or spaces")
        if gst_number and len(gst_number) > 0:
            if len(gst_number) != 15:
                errors.append("GST number must be exactly 15 characters")
        if aadhar_number and len(aadhar_number) > 0:
            aadhar_clean = aadhar_number.replace("-", "").replace(" ", "")
            if len(aadhar_clean) != 12:
                errors.append("Aadhar number must be 12 digits")
            if not aadhar_clean.isdigit():
                errors.append("Aadhar number must contain only digits")
        return errors

    def add_job_worker(self, worker_name, contact_number="", gst_number="", aadhar_number=""):
        """Add new job worker"""
        errors = self.validate_job_worker_input(worker_name, contact_number, gst_number, aadhar_number)
        if errors:
            return False, errors
        success = self.db.add_job_worker(
            worker_name.strip(), contact_number.strip(), gst_number.strip(), aadhar_number.strip()
        )
        if success:
            return True, [f"✅ Job worker '{worker_name}' added successfully!"]
        else:
            return False, ["❌ Failed to add job worker (may already exist)"]

    def update_job_worker(self, old_worker_name, worker_name, contact_number, gst_number, aadhar_number):
        """Update job worker"""
        errors = self.validate_job_worker_input(worker_name, contact_number, gst_number, aadhar_number)
        if errors:
            return False, errors
        success = self.db.update_job_worker(
            old_worker_name, worker_name.strip(), contact_number.strip(), gst_number.strip(), aadhar_number.strip()
        )
        if success:
            return True, [f"✅ Job worker '{worker_name}' updated successfully!"]
        else:
            return False, ["❌ Failed to update job worker"]