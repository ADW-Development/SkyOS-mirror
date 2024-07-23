import os
import subprocess
import sys
 
print("SkyOS v2.2 BIOS UPDATE")
print("This device is running SkyOS")
print("/kernel/bios")
print(" ^ BIOS is running here")

def main():
    while True:
        answer = input("exit? (yes/no): ").strip().lower()
        if answer == "no":
            print("SkyOS v2.2 BIOS UPDATE")
            print("This device is running SkyOS")
            print("/kernel/bios")
            print(" ^ BIOS is running here")
        elif answer == "yes":
            # Path to the kernel script in the KERNEL folder
            kernel_script = os.path.join(os.getcwd(), 'KERNEL', 'kernel.py')
            
            # Check if the kernel script exists before trying to run it
            if os.path.isfile(kernel_script):
                try:
                    # Run the kernel script as a subprocess
                    subprocess.run([sys.executable, kernel_script], check=True)
                except subprocess.CalledProcessError as e:
                    print(f"Error executing the kernel script: {e}")
                except Exception as e:
                    print(f"An unexpected error occurred: {e}")
            else:
                print("Kernel script not found. Make sure 'kernel.py' exists in the 'KERNEL' directory.")
            break  # Exit the loop after trying to run the kernel script
        else:
            print("Invalid input. Please type 'yes' or 'no'.")

if __name__ == "__main__":
    main()