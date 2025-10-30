from datetime import date

class MaterialService:
    def __init__(self, database):
        self.db = database

    # ========================================
    # INVENTORY WARP VALIDATION & METHODS
    # ========================================
    def validate_inventory_warp_input(self, gross_weight, paper_weight, beam_weight,
                                      yarn_type="", warper_name="", design="",
                                      no_of_bell=0, reed=""):
        """Validate inventory WARP inputs with NEW FORMULA and all new fields"""
        errors = []

        # Weight validations
        if gross_weight <= 0:
            errors.append("Gross weight must be greater than 0")
        if paper_weight < 0:
            errors.append("Paper weight cannot be negative")
        if beam_weight < 0:
            errors.append("Beam weight cannot be negative")

        # NEW FORMULA validation
        net_weight = gross_weight - (paper_weight + beam_weight)
        if net_weight <= 0:
            errors.append(f"Net weight must be positive. Current: {net_weight:.2f} kg")

        # Task #2: Warper Name validation
        if not warper_name or not warper_name.strip():
            errors.append("Warper name is required")

        # Task #6: No. of Bell validation
        if no_of_bell < 0:
            errors.append("No. of Bell cannot be negative")

        # Task #7: Reed validation (optional field - no validation needed)

        return errors

    def calculate_warp_net_weight(self, gross_weight, paper_weight, beam_weight):
        """Calculate WARP net weight using NEW FORMULA"""
        return round(gross_weight - (paper_weight + beam_weight), 2)

    def add_inventory_warp(self, entry_date, yarn_type, warper_name, design, gross_weight,
                           paper_weight, beam_weight, no_of_bell, reed):
        """Add WARP to inventory with all new fields"""
        errors = self.validate_inventory_warp_input(
            gross_weight, paper_weight, beam_weight,
            yarn_type, warper_name, design, no_of_bell, reed
        )
        if errors:
            return False, errors

        data = (entry_date, yarn_type, warper_name, design, gross_weight,
                paper_weight, beam_weight, no_of_bell, reed)

        success, warp_number = self.db.insert_inventory_warp(data)

        if success:
            net_weight = self.calculate_warp_net_weight(gross_weight, paper_weight, beam_weight)
            return True, [
                f"✅ Inventory WARP added successfully!",
                f"📝 Warp Number: {warp_number}",
                f"⚖️ Net Weight: {net_weight:.2f} kg",
                f"👷 Warper: {warper_name}",
                f"🔔 No. of Bell: {no_of_bell}",
                f"🧵 Reed: {reed if reed else 'Not specified'}"
            ]
        else:
            return False, ["❌ Failed to add inventory WARP"]

    # ========================================
    # INVENTORY WEFT VALIDATION & METHODS
    # ========================================
    def validate_inventory_weft_input(self, gross_weight, no_of_cones, cone_weight, no_of_bags, colour=""):
        """Validate inventory WEFT inputs with NEW FORMULA"""
        errors = []
        BAG_WEIGHT = 0.2  # 200g per bag

        if gross_weight <= 0:
            errors.append("Gross weight must be greater than 0")
        if no_of_cones <= 0:
            errors.append("Number of cones must be greater than 0")
        if cone_weight not in [0.03, 0.05, 0.09]:  # Task #9: Only 30g, 50g, 90g allowed
            errors.append("Cone weight must be 30g (0.03kg), 50g (0.05kg), or 90g (0.09kg)")
        if no_of_bags < 1:
            errors.append("Number of bags must be at least 1")

        # Colour validation (optional - just check if provided)
        if colour and not colour.strip():
            errors.append("Colour cannot be empty if provided")

        net_weight = gross_weight - (cone_weight * no_of_cones + BAG_WEIGHT * no_of_bags)
        if net_weight <= 0:
            errors.append(f"Net weight must be positive. Current: {net_weight:.2f} kg")

        return errors

    def calculate_weft_net_weight(self, gross_weight, no_of_cones, cone_weight, no_of_bags):
        """Calculate WEFT net weight using NEW FORMULA"""
        BAG_WEIGHT = 0.2  # 200g per bag
        return round(gross_weight - (cone_weight * no_of_cones + BAG_WEIGHT * no_of_bags), 2)

    def add_inventory_weft(self, entry_date, colour, gross_weight, no_of_cones, cone_weight, no_of_bags):
        """Add WEFT to inventory with new fields"""
        errors = self.validate_inventory_weft_input(gross_weight, no_of_cones, cone_weight, no_of_bags, colour)
        if errors:
            return False, errors

        data = (entry_date, colour, gross_weight, no_of_cones, cone_weight, no_of_bags)
        success = self.db.insert_inventory_weft(data)

        if success:
            net_weight = self.calculate_weft_net_weight(gross_weight, no_of_cones, cone_weight, no_of_bags)
            return True, [
                f"✅ Inventory WEFT added successfully!",
                f"⚖️ Net Weight: {net_weight:.2f} kg",
                f"🎨 Colour: {colour}",
                f"🔢 Cones: {no_of_cones} × {cone_weight}kg",
                f"📦 Bags: {no_of_bags}"
            ]
        else:
            return False, ["❌ Failed to add inventory WEFT"]

    # ========================================
    # JOB WORKER WARP VALIDATION & METHODS
    # ========================================
    def validate_job_worker_warp_input(self, gross_weight, paper_weight, beam_weight,
                                       yarn_type="", warper_name="", design="",
                                       no_of_bell=0, reed=""):
        """Validate job worker WARP inputs with NEW FORMULA and all new fields"""
        errors = []

        # Weight validations
        if gross_weight <= 0:
            errors.append("Gross weight must be greater than 0")
        if paper_weight < 0:
            errors.append("Paper weight cannot be negative")
        if beam_weight < 0:
            errors.append("Beam weight cannot be negative")

        # NEW FORMULA validation
        net_weight = gross_weight - (paper_weight + beam_weight)
        if net_weight <= 0:
            errors.append(f"Net weight must be positive. Current: {net_weight:.2f} kg")

        # Task #2: Warper Name validation
        if not warper_name or not warper_name.strip():
            errors.append("Warper name is required")

        # Task #6: No. of Bell validation
        if no_of_bell < 0:
            errors.append("No. of Bell cannot be negative")

        return errors

    def add_job_worker_warp(self, entry_date, yarn_type, warper_name, design, gross_weight,
                            paper_weight, beam_weight, no_of_bell, reed, job_worker):
        """Distribute WARP to job worker with inventory validation, caution deposit calculation, and all new fields"""
        errors = self.validate_job_worker_warp_input(
            gross_weight, paper_weight, beam_weight,
            yarn_type, warper_name, design, no_of_bell, reed
        )
        if errors:
            return False, errors

        net_weight = self.calculate_warp_net_weight(gross_weight, paper_weight, beam_weight)
        available_inventory = self.db.get_available_inventory_warp()

        if net_weight > available_inventory:
            return False, [
                f"❌ Insufficient WARP inventory!",
                f"Required: {net_weight:.2f} kg",
                f"Available: {available_inventory:.2f} kg",
                f"Shortage: {net_weight - available_inventory:.2f} kg"
            ]

        data = (entry_date, yarn_type, warper_name, design, gross_weight,
                paper_weight, beam_weight, no_of_bell, reed, job_worker)

        # NEW: Now receives 3 values (success, warp_number, caution_deposit)
        success, warp_number, caution_deposit = self.db.insert_job_worker_warp(data)

        if success:
            remaining_inventory = available_inventory - net_weight
            return True, [
                f"✅ WARP distributed to {job_worker} successfully!",
                f"📄 Warp Number: {warp_number}",
                f"📊 Net Weight: {net_weight:.2f} kg",
                f"👷 Warper: {warper_name}",
                f"🔔 No. of Bell: {no_of_bell}",
                f"🧵 Reed: {reed if reed else 'Not specified'}",
                f"💰 Paper Caution Deposit: ₹{caution_deposit:.2f} (@ ₹40/kg)",
                f"📝 Note: Deposit refundable upon paper return",
                f"📦 Remaining Inventory: {remaining_inventory:.2f} kg"
            ]
        else:
            return False, ["❌ Failed to distribute WARP to job worker"]

    # ========================================
    # JOB WORKER WEFT VALIDATION & METHODS
    # ========================================
    def validate_job_worker_weft_input(self, gross_weight, no_of_cones, cone_weight, no_of_bags, colour=""):
        """Validate job worker WEFT inputs with NEW FORMULA"""
        errors = []
        BAG_WEIGHT = 0.2  # 200g per bag

        if gross_weight <= 0:
            errors.append("Gross weight must be greater than 0")
        if no_of_cones <= 0:
            errors.append("Number of cones must be greater than 0")
        if cone_weight not in [0.03, 0.05, 0.09]:  # Task #9: Only 30g, 50g, 90g allowed
            errors.append("Cone weight must be 30g (0.03kg), 50g (0.05kg), or 90g (0.09kg)")
        if no_of_bags < 1:
            errors.append("Number of bags must be at least 1")

        # Colour validation (optional)
        if colour and not colour.strip():
            errors.append("Colour cannot be empty if provided")

        net_weight = gross_weight - (cone_weight * no_of_cones + BAG_WEIGHT * no_of_bags)
        if net_weight <= 0:
            errors.append(f"Net weight must be positive. Current: {net_weight:.2f} kg")

        return errors

    def add_job_worker_weft(self, entry_date, colour, gross_weight, no_of_cones, cone_weight, no_of_bags, job_worker):
        """Distribute WEFT to job worker with inventory validation and caution deposit calculation"""
        errors = self.validate_job_worker_weft_input(gross_weight, no_of_cones, cone_weight, no_of_bags, colour)
        if errors:
            return False, errors

        net_weight = self.calculate_weft_net_weight(gross_weight, no_of_cones, cone_weight, no_of_bags)
        available_inventory = self.db.get_available_inventory_weft()

        if net_weight > available_inventory:
            return False, [
                f"❌ Insufficient WEFT inventory!",
                f"Required: {net_weight:.2f} kg",
                f"Available: {available_inventory:.2f} kg",
                f"Shortage: {net_weight - available_inventory:.2f} kg"
            ]

        data = (entry_date, colour, gross_weight, no_of_cones, cone_weight, no_of_bags, job_worker)

        # NEW: Now receives 2 values (success, caution_deposit)
        success, caution_deposit = self.db.insert_job_worker_weft(data)

        if success:
            remaining_inventory = available_inventory - net_weight
            return True, [
                f"✅ WEFT distributed to {job_worker} successfully!",
                f"📊 Net Weight: {net_weight:.2f} kg",
                f"🎨 Colour: {colour}",
                f"🔢 Cones: {no_of_cones} × {cone_weight}kg",
                f"📦 Bags: {no_of_bags}",
                f"💰 Bag Caution Deposit: ₹{caution_deposit:.2f} (@ ₹15/bag)",
                f"📝 Note: Deposit refundable upon bag return",
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
    # WARPER MANAGEMENT (Task #2)
    # ========================================
    def validate_warper_input(self, warper_name):
        """Validate warper input"""
        errors = []
        if not warper_name or not warper_name.strip():
            errors.append("Warper name cannot be empty")
        if len(warper_name) > 100:
            errors.append("Warper name too long (max 100 characters)")
        return errors

    def add_warper(self, warper_name):
        """Add new warper"""
        errors = self.validate_warper_input(warper_name)
        if errors:
            return False, errors
        success = self.db.add_warper(warper_name.strip())
        if success:
            return True, [f"✅ Warper '{warper_name}' added successfully!"]
        else:
            return False, ["❌ Failed to add warper (may already exist)"]

    # ========================================
    # REED TYPE MANAGEMENT (Task #7)
    # ========================================
    def validate_reed_type_input(self, reed_name):
        """Validate reed type input"""
        errors = []
        if not reed_name or not reed_name.strip():
            errors.append("Reed type name cannot be empty")
        if len(reed_name) > 100:
            errors.append("Reed type name too long (max 100 characters)")
        return errors

    def add_reed_type(self, reed_name):
        """Add new reed type"""
        errors = self.validate_reed_type_input(reed_name)
        if errors:
            return False, errors
        success = self.db.add_reed_type(reed_name.strip())
        if success:
            return True, [f"✅ Reed type '{reed_name}' added successfully!"]
        else:
            return False, ["❌ Failed to add reed type (may already exist)"]

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


    # ========================================
    # CAUTION DEPOSIT MANAGEMENT METHODS
    # ========================================
    def mark_paper_return(self, warp_entry_id, return_date):
        """Mark paper as returned for a WARP entry"""
        success = self.db.mark_paper_returned(warp_entry_id, return_date)
        if success:
            return True, [f"✅ Paper return recorded successfully for entry #{warp_entry_id}"]
        else:
            return False, ["❌ Failed to record paper return"]

    def process_paper_deposit_refund(self, warp_entry_id, refund_date):
        """Process paper deposit refund"""
        success, message = self.db.refund_paper_deposit(warp_entry_id, refund_date)
        if success:
            return True, [f"✅ {message}"]
        else:
            return False, [f"❌ {message}"]

    def mark_bag_return(self, weft_entry_id, bags_returned, return_date):
        """Mark bags as returned for a WEFT entry"""
        if bags_returned <= 0:
            return False, ["❌ Number of bags returned must be greater than 0"]

        success, message = self.db.mark_bags_returned(weft_entry_id, bags_returned, return_date)
        if success:
            return True, [f"✅ {message}"]
        else:
            return False, [f"❌ {message}"]

    def process_bag_deposit_refund(self, weft_entry_id, refund_date):
        """Process bag deposit refund"""
        success, message = self.db.refund_bag_deposit(weft_entry_id, refund_date)
        if success:
            return True, [f"✅ {message}"]
        else:
            return False, [f"❌ {message}"]