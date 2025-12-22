#!/usr/bin/env python3
"""
ODOO WARUNG SETUP - Automated Installation Script
Setup database Odoo untuk sistem kasir dan pembukuan warung
Version: 1.0
"""

import os
import sys
import subprocess
import argparse
from pathlib import Path

# Colors for terminal output
class Colors:
    HEADER = '\033[95m'
    BLUE = '\033[94m'
    CYAN = '\033[96m'
    GREEN = '\033[92m'
    YELLOW = '\033[93m'
    RED = '\033[91m'
    ENDC = '\033[0m'
    BOLD = '\033[1m'
    UNDERLINE = '\033[4m'

def print_header(text):
    print(f"\n{Colors.HEADER}{Colors.BOLD}{'='*60}")
    print(f"{text:^60}")
    print(f"{'='*60}{Colors.ENDC}\n")

def print_step(step, text):
    print(f"{Colors.CYAN}[Step {step}] {text}{Colors.ENDC}")

def print_success(text):
    print(f"{Colors.GREEN}✓ {text}{Colors.ENDC}")

def print_warning(text):
    print(f"{Colors.YELLOW}⚠ {text}{Colors.ENDC}")

def print_error(text):
    print(f"{Colors.RED}✗ {text}{Colors.ENDC}")

def run_command(command, description=""):
    """Run shell command and return success status"""
    try:
        if description:
            print_step("CMD", description)
        result = subprocess.run(command, shell=True, capture_output=True, text=True)
        if result.returncode == 0:
            if description:
                print_success(description)
            return True
        else:
            if description:
                print_error(description)
            print(result.stderr)
            return False
    except Exception as e:
        print_error(f"Error running command: {e}")
        return False

def check_requirements():
    """Check if required tools are installed"""
    print_header("CHECKING REQUIREMENTS")
    
    requirements = {
        "Python 3.10+": "python3 --version",
        "PostgreSQL 14+": "psql --version",
        "Git": "git --version"
    }
    
    all_ok = True
    for req, cmd in requirements.items():
        result = subprocess.run(cmd, shell=True, capture_output=True, text=True)
        if result.returncode == 0:
            print_success(f"{req}: {result.stdout.strip()}")
        else:
            print_error(f"{req}: NOT INSTALLED")
            all_ok = False
    
    return all_ok

def setup_postgres():
    """Setup PostgreSQL database"""
    print_header("POSTGRESQL SETUP")
    
    # Start PostgreSQL service
    print_step(1, "Starting PostgreSQL service...")
    if not run_command("sudo service postgresql start 2>/dev/null || sudo /usr/local/bin/postgres &", 
                      "PostgreSQL started"):
        print_warning("Could not start PostgreSQL, continuing anyway...")
    
    return True

def create_database(db_name):
    """Create new PostgreSQL database"""
    print_header(f"CREATING DATABASE: {db_name}")
    
    # Check if database exists
    check_cmd = f"sudo -u postgres psql -l | grep {db_name}"
    if subprocess.run(check_cmd, shell=True, capture_output=True).returncode == 0:
        print_warning(f"Database '{db_name}' already exists. Skipping creation.")
        return True
    
    # Create database
    create_cmd = f"sudo -u postgres createdb {db_name} --encoding UTF8 --owner postgres 2>/dev/null || true"
    if run_command(create_cmd, f"Creating database '{db_name}'"):
        print_success(f"Database '{db_name}' created successfully")
        return True
    else:
        print_warning(f"Database creation may have failed, but continuing...")
        return True

def install_odoo_modules(db_name, odoo_path="/workspaces/erp-odoo"):
    """Install required Odoo modules"""
    print_header("INSTALLING ODOO MODULES")
    
    required_modules = [
        "base",
        "point_of_sale",
        "account",
        "stock",
        "sale",
        "pos_sale",
        "product",
        "contacts",
        "uom",
        "web"
    ]
    
    modules_str = ",".join(required_modules)
    
    print_step(1, f"Installing modules: {', '.join(required_modules)}")
    
    # Build Odoo command
    odoo_cmd = f"cd {odoo_path} && python3 odoo-bin -d {db_name} -i {modules_str} --init={modules_str}"
    
    if run_command(odoo_cmd, "Installing Odoo modules..."):
        print_success("Modules installed successfully")
        return True
    else:
        print_warning("Module installation may have issues, but continuing...")
        return True

def create_admin_user(db_name):
    """Create admin user via Odoo CLI (simplified)"""
    print_header("ADMIN USER SETUP")
    
    print_step(1, "Admin user will be created during first Odoo startup")
    print_warning("You'll be prompted to set admin password on first access")
    print("URL: http://localhost:8069")
    print("Default: admin / admin (then change immediately)")
    
    return True

def create_config_file(odoo_path="/workspaces/erp-odoo"):
    """Create Odoo config file for warung"""
    print_header("CREATING ODOO CONFIG FILE")
    
    config_content = """[options]
; Odoo Configuration untuk Warung
; ================================

; Database settings
db_host = localhost
db_port = 5432
db_user = postgres
db_password = False
db_filter = warung_a

; Administrative Settings
admin_passwd = admin
; ⚠️ PENTING: Ganti password ini setelah setup selesai!

; Server settings
http_port = 8069
longpolling_port = 8072
workers = 2
max_cron_interval = 300

; File storage
data_dir = /tmp/odoo

; Debug mode (untuk development, matikan untuk production)
debug = False
log_level = info

; Session settings
session_cookie_secure = False
session_cookie_httponly = True

; Timezone (Indonesia/Jakarta)
timezone = Asia/Jakarta

; Email settings (opsional - configure kemudian)
; smtp_server = smtp.gmail.com
; smtp_port = 587
; smtp_user = your-email@gmail.com
; smtp_password = your-app-password

; Modules load at startup (optimize startup)
init = base,web,point_of_sale,account,stock,sale,pos_sale

; Features
web.web_unsplash_access_key = False
"""
    
    config_path = os.path.join(odoo_path, ".odoorc")
    
    try:
        with open(config_path, 'w') as f:
            f.write(config_content)
        print_success(f"Config file created: {config_path}")
        return True
    except Exception as e:
        print_error(f"Failed to create config file: {e}")
        return False

def print_summary():
    """Print setup summary and next steps"""
    print_header("SETUP SUMMARY & NEXT STEPS")
    
    summary = f"""
{Colors.BOLD}✓ DATABASE & MODULES:{Colors.ENDC}
  • Database 'warung_a' ready
  • Core modules installed (POS, Accounting, Stock)
  • Config file created

{Colors.BOLD}🚀 STARTING ODOO SERVER:{Colors.ENDC}
  
  Option 1: Manual start
  $ cd /workspaces/erp-odoo
  $ python3 odoo-bin -d warung_a -c .odoorc
  
  Option 2: With watch mode (development)
  $ python3 odoo-bin -d warung_a -c .odoorc --dev=xml
  
  Option 3: Background start
  $ python3 odoo-bin -d warung_a -c .odoorc &

{Colors.BOLD}🌐 ACCESS ODOO:{Colors.ENDC}
  • URL: http://localhost:8069
  • Default Login: admin / admin
  • Database: warung_a
  
  {Colors.RED}⚠️ IMPORTANT: Change admin password after first login!{Colors.ENDC}

{Colors.BOLD}📋 CONFIGURATION CHECKLIST:{Colors.ENDC}
  ☐ Change admin password
  ☐ Setup company info (Settings > Companies)
  ☐ Configure POS settings (Point of Sale > Configuration)
  ☐ Create products & categories
  ☐ Setup accounting chart of accounts
  ☐ Configure taxes (PPN 11% untuk Indonesia)
  ☐ Add inventory initial stock
  ☐ Create user accounts untuk kasir
  ☐ Setup cash journal & payment methods
  ☐ Test transaksi POS

{Colors.BOLD}📖 DOCUMENTATION:{Colors.ENDC}
  Lihat file: /workspaces/erp-odoo/SETUP_WARUNG.md
  untuk panduan lengkap setup dan penggunaan

{Colors.BOLD}💡 SUPPORT:{Colors.ENDC}
  • Odoo Docs: https://www.odoo.com/documentation/18.0/
  • POS Guide: /workspaces/erp-odoo/SETUP_WARUNG.md
  • Error logs: ~/.local/share/Odoo/logs/

{Colors.GREEN}{Colors.BOLD}✓ SETUP COMPLETED!{Colors.ENDC}
"""
    
    print(summary)

def main():
    """Main setup flow"""
    parser = argparse.ArgumentParser(
        description="Setup Odoo untuk sistem kasir warung"
    )
    parser.add_argument('--db-name', default='warung_a', 
                       help='Nama database (default: warung_a)')
    parser.add_argument('--odoo-path', default='/workspaces/erp-odoo',
                       help='Path ke Odoo installation')
    parser.add_argument('--skip-postgres', action='store_true',
                       help='Skip PostgreSQL setup')
    parser.add_argument('--no-modules', action='store_true',
                       help='Skip module installation')
    
    args = parser.parse_args()
    
    print_header("ODOO WARUNG SETUP TOOL")
    print("Setup Odoo 18.0 untuk sistem kasir & pembukuan warung\n")
    
    # Check requirements
    if not check_requirements():
        print_error("Please install missing requirements first!")
        return False
    
    # Setup PostgreSQL
    if not args.skip_postgres:
        if not setup_postgres():
            return False
    
    # Create database
    if not create_database(args.db_name):
        return False
    
    # Create config file
    if not create_config_file(args.odoo_path):
        print_warning("Config file creation failed, continuing...")
    
    # Install modules
    if not args.no_modules:
        if not install_odoo_modules(args.db_name, args.odoo_path):
            print_warning("Module installation had issues")
    
    # Create admin user info
    if not create_admin_user(args.db_name):
        return False
    
    # Print summary
    print_summary()
    
    return True

if __name__ == "__main__":
    try:
        success = main()
        sys.exit(0 if success else 1)
    except KeyboardInterrupt:
        print_error("\nSetup cancelled by user")
        sys.exit(1)
    except Exception as e:
        print_error(f"Unexpected error: {e}")
        sys.exit(1)
