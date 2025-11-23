#!/usr/bin/env python3
# test_reverse_shell.py - SAFE TEST SCRIPT (connects to localhost only)

import socket
import subprocess
import os
import sys

def safe_test():
    """Safe test that triggers detection without actual harm"""
    
    # Test 1: Create suspicious file
    test_code = '''
import socket
import subprocess
# This is a test reverse shell pattern
s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
# s.connect(("127.0.0.1", 4444))  # Commented for safety
'''
    
    with open('/tmp/test_shell.py', 'w') as f:
        f.write(test_code)
    
    # Test 2: Trigger socket creation (safe - no actual connection)
    try:
        test_sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        test_sock.close()
    except:
        pass
    
    # Test 3: Trigger subprocess (safe command)
    subprocess.run(['echo', 'Test reverse shell detection'], capture_output=True)
    
    print("Test completed - Check Wazuh alerts")
    
    # Clean up
    os.remove('/tmp/test_shell.py')

if __name__ == "__main__":
    print("Running safe reverse shell detection test...")
    safe_test()