import psutil
import os

def endProcess(exename: str):
  """
  Function to close all processes of the name of an executable.

  Args:
    exename: The name of the executable of the process you want to close.

  Returns: The number of process finished or -1 if access denied.
  """
  # Fetch all process
  processes = psutil.process_iter()

  count = 0
  # Find processes with the matching executable name
  for process in processes:
    if process.name() == exename:
      # Kill the process
      try:
        process.kill()
        count += 1
        print(f"Process {count} finished.")
      except psutil.NoSuchProcess:
        # Did not find any process
        return 0
      except psutil.AccessDenied:
        # Process found but access denied to kill it, you need to run as admin.
        return -1

  return count

def main():
  
  com_fnshed_process = endProcess("dllhost.exe")
  
  if com_fnshed_process == 0:
    print("No COM Surrogate processes were found.")
    os.system("pause")
    
  elif com_fnshed_process == -1:
    print("Access denied to kill COM Surrogate processes, you need to run as admin.")
    os.system("pause")
    
if __name__ == "__main__":
  main()